===========================
Erstellen eigener Formulare
===========================

Um ein eigenes Formular zu erstellen, erzeugen wir zunächst ein Page Template ``registrationreport`` in ``src/vs.registration/vs/registration/browser/`` mit folgendem Inhalt::

 <form method="get"
       tal:attributes="action string:${context/absolute_url}/${view/__name__}">

     <div i18n:translate="registration_report_days_searched">
         Show changes in the the last
         <input type="text" size="2" name="days"
             tal:attributes="value view/days"
             i18n:name="num_days" />
         days.
         <input type="submit" class="context" name="form.button.UpdateDays"
             value="Refresh"
             i18n:name="submit_button"
             i18n:attributes="value" />
     </div>

 </form>

Dabei wird das ``action``-Attribut dynamisch generiert um zu gewährleisten, dass immer dasselbe Formular im selben Kontext aufgerufen wird.

**Anmerkung 1:** Würde ein Skin-Template verwendet, müsste statt der Variablen ``${view/__name__}`` die Variable ``${template/getId}`` verwendet werden.

Das Formular wird verarbeitet, wenn der View in ``registrationreport.py`` mit der ``__call__()``-Methode aufgerufen wird::

 template = ViewPageTemplateFile('registrationreport.pt')

 def __call__(self):
     # Hide the editable-border
     self.request.set('disable_border', True)

     # The number for days with a silent fallback on the default
     # if the input is invalid.
     try:
         self.days = int(self.request.get('days', 7))
     except ValueError:
         self.days = 7

     return self.template()

**Anmerkung 2:** Falls eine Anfrage nicht nur auf den View selbst zugreifen muss, ist ``self.request`` nicht mehr ausreichend; stattdessen ist dann die Anfrage zu akquirieren mit ``request = context.REQUEST``.

**Anmerkung 3:** Für ``HTTP POST``-Anfragen sollte statt ``self.request`` ``self.request.form`` angegeben werden, da dies versehentlich akzeptierte Variablen verhindert.

Die anderen Methoden des Views untersuchen ``self.days`` zum Erstellen der Such-Parameter::

 def recently_modified_registrants(self):
     context = aq_inner(self.context)
     catalog = getToolByName(context, 'portal_catalog')
     results = []
     for r in catalog(object_provides=IRegistrant.__identifier__,
                      modified=dict(query=self.modified_after(), range='min'),
                      sort_on='modified',
                      sort_order='reverse',):
         results.append(dict(url=r.getURL(),
                             title=r.Title,
                             description=r.Description,
                             modified=self.localize(r.modified)))
     return results

 def localize(self, time):
     return self._time_localizer()(time, None, aq_inner(self.context), domain='plonelocales')

 def modified_after(self):
     return DateTime() - self.days

 @memoize
 def _time_localizer(self):
     context = aq_inner(self.context)
     translation_service = getToolByName(context, 'translation_service')

Mehrere ``submit``-Tasten
=========================

Sind für ein Formular mehrere Tasten verfügbar, muss überprüft werden, welche der Tasten gedrückt wurde und welche Aktion hierfür auszuführen ist. Wie dies geschieht, können Sie sich z.B. in ``plone.app.workflow.browser.sharing`` anschauen::

 <input class="context" type="submit" name="form.button.Save" value="Save" i18n:attributes="value label_save" />
 <input class="standalone" type="submit" name="form.button.Cancel" value="Cancel" i18n:attributes="value label_cancel"/>

In ``sharing.py`` wird dann zunächst überprüft, welche Taste gedrückt wurde. Dabei ist zu beachten, dass Web-Browser immer nur den Wert für ``name`` derjenigen Taste senden, auf die geklickt wurde. Anschließend wird die entsprechende Aktion zuzuweisen::

 class SharingView(BrowserView):

     # Actions

     template = ViewPageTemplateFile('sharing.pt')

     def __call__(self):
         """Perform the update and redirect if necessary, or render the page
         """

         postback = True

         form = self.request.form
         submitted = form.get('form.submitted', False)

         save_button = form.get('form.button.Save', None) is not None
         cancel_button = form.get('form.button.Cancel', None) is not None

         if submitted and not cancel_button:

             if not self.request.get('REQUEST_METHOD','GET') == 'POST':
                 raise Forbidden

             # Update the acquire-roles setting
             inherit = bool(form.get('inherit', False))
             self.update_inherit(inherit)

             # Update settings for users and groups
             entries = form.get('entries', [])
             roles = [r['id'] for r in self.roles()]
             settings = []
             for entry in entries:
                 settings.append(
                     dict(id = entry['id'],
                          type = entry['type'],
                          roles = [r for r in roles if entry.get('role_%s' % r, False)]))
             if settings:
                 self.update_role_settings(settings)

         # Other buttons return to the sharing page
         if cancel_button:
             postback = False

         if postback:
             return self.template()
         else:
             context_state = self.context.restrictedTraverse("@@plone_context_state")
             url = context_state.view_url()
             self.request.response.redirect(url)

Eingabekonverter
================

Aus dem ``sharing.pt``-*Page Template* lässt sich auch ablesen, wie Formularfelder berechnet werden können::

 <input
     type="hidden"
     name="entries.id:records"
     tal:attributes="value entry/id"
     />
 <input
     type="hidden"
     name="entries.type:records"
     tal:attributes="value entry/type"
     />

Dies wird dargestellt in einer ``tal:repeat``-Schleife. Wird das Formular abgeschickt, wird die Variable ``entries`` mit einer Liste von Wörterbüchern aus den Schlüsselwörtern ``"id"`` und ``"type"`` übertragen. Ein Überblick über alle verfügbaren Konverter erhalten Sie hier:

+------------------------+------------------------------------------------+--------------------------------+
| Konverter              | Beispiel                                       | Anmerkung                      |
+========================+================================================+================================+
| ``boolean``,           | ::                                             | Wandelt die Variable in den    |
|                        |                                                | zugehörigen Python-Typ um,     |
| ``int``,               |  <input type="hidden"                          | ``date`` führt so zu           |
|                        |         name="limit:int"                       | ``DateTime``.                  |
| ``long``,              |         value="8 />"                           |                                |
|                        |                                                | Solche Umwandlungen sind       |
| ``float``,             |                                                | normalerweise nur in           |
|                        |                                                | ``hidden``-Feldern sinnvoll;   |
| ``string``,            |                                                | werden unzulässige Werte       |
|                        |                                                | eingegeben, ist die            |
| ``date``,              |                                                | resultierende Fehlermeldung    |
|                        |                                                | für die meisten Nutzer wenig   |
| ``boolean``            |                                                | aussagekräftig.                |
+------------------------+------------------------------------------------+--------------------------------+
| ``text``               | ::                                             | Konvertiert eine Zeichenkette  |
|                        |                                                | mit normalisierten             |
|                        |  <textarea name="description:text" />          | Zeilenumbrüchen entsprechend   |
|                        |                                                | der Server-Plattform           |
+------------------------+------------------------------------------------+--------------------------------+
| ``list``,              | ::                                             | Erstellt eine Liste oder ein   |
|                        |                                                | Tuple aus mehreren Feldern     |
| ``tuple``              |  <input type="checkbox"                        | mit demselben Namen oder aus   |
|                        |         name="status:list"                     | einer mehrwertigen             |
|                        |         value="1"                              | Listenauswahl.                 |
|                        |                                                |                                |
|                        |                                                | Dieser Konverter kann mit      |
|                        |                                                | anderen kombiniert werden,     |
|                        |                                                | z.B. ``int:list`` um eine      |
|                        |                                                | Liste ganzer Zahlen zu         |
|                        |                                                | erhalten                       |
+------------------------+------------------------------------------------+--------------------------------+
| ``tokens``,            | ::                                             | Wandelt eine durch Leerzeichen |
|                        |                                                | (tokens) oder neue Zeilen      |
| ``lines``              |  <input type="text"                            | (lines) getrennte Zeichenkette |
|                        |         name="keywords:tokens" />              | in eine Liste um               |
+------------------------+------------------------------------------------+--------------------------------+
| ``record``,            | ::                                             | Erstellt ein Wörterbuch        |
|                        |                                                | (``record``) oder eine Liste   |
| ``records``            |  <input type="text"                            | von Wörterbüchern              |
|                        |         name="data.id:record" />               | (``records``). Der Name vor    |
|                        |                                                | ``.`` ist der Variablenname,   |
|                        |                                                | der Name danach der            |
|                        |                                                | Schlüssel.                     |
+------------------------+------------------------------------------------+--------------------------------+
| ``required``           | ::                                             | Gibt eine Fehlermeldung aus    |
|                        |                                                | wenn das Feld nicht ausgefüllt |
|                        |  <input type="text"                            | wurde.                         |
|                        |         name="title:required" />               |                                |
|                        |                                                |                                |
+------------------------+------------------------------------------------+--------------------------------+
| ``ignore_empty``       | ::                                             | Die Variable wird bei einem    |
|                        |                                                | Request nicht angegeben wenn   |
|                        |  <input type="text"                            | sie leer ist.                  |
|                        |         name="id:ignore_empty" />              |                                |
|                        |                                                | Dieser Konverter kann mit      |
|                        |                                                | anderen kombiniert werden.     |
+------------------------+------------------------------------------------+--------------------------------+
| ``default``            | ::                                             | Standardwert, falls in keinem  |
|                        |                                                | Feld mit demselben Namen ein   |
|                        |  <input type="hidden"                          | Wert übermittelt wurde.        |
|                        |         name="accept:boolean:default"          |                                |
|                        |         value="True" />                        | Dies ist vor allem für         |
|                        |  <input type="checkbox"                        | Checkboxen sinnvoll, die nicht |
|                        |         name="accept:boolean:default"          | übertragen werden wenn für sie |
|                        |         value="False" />                       | keine Angabe gemacht wurde.    |
|                        |                                                |                                |
|                        |                                                | Dieser Konverter kann mit      |
|                        |                                                | anderen kombiniert werden.     |
+------------------------+------------------------------------------------+--------------------------------+

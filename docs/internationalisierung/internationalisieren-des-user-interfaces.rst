========================================
Internationalisieren des User-Interfaces
========================================

Plone nutzt den  `Placeless Translation Service`_ um das User-Interface zu übersetzen. Ist das Produkt installiert, werden alle verfügbaren Übersetzungsdateien in ``/Control_Panel/TranslationService/manage_main`` angezeigt. Dabei schaut der Placeless Translation Service nach Übersetzungsdateien in ``i18n``- und ``locales``-Ordnern innerhalb von ``INSTANCE_HOME`` und ``INSTANCE_HOME/Products``.

Internationalisieren von Page Templates
=======================================

Domäne
------

Für jedes Page Template kann im HTML-Header die Standard-Übersetzungsdomäne angegeben werden, z.B.::

 <html xmlns:tal="http://xml.zope.org/namespaces/tal"
       xmlns:metal="http://xml.zope.org/namespaces/metal"
       i18n:domain="vs.registration">

Existiert jedoch für eine Zeichenkette bereits eine Übersetzung in einer anderen Domain, verweisen Sie auf diese, z.B.::

 <a href=""
    tal:attributes="href python:test(item_type in use_view_action, item_url+'/view', item_url);"
    i18n:translate="read_more">
     Read More&hellip;
 </a>

Inhalte
-------

Text wird mit einer bestimmten *message id*, hier ``read_more``, verknüpft um übersetzt werden zu können. Würde die *message id* leer sein, also ``i18n:translate=""``, dann wird stattdessen der zu übersetzende  Text selbst, hier ``Read More``, verwendet. Dabei sind für die Präfixe der *message ids* in Plone bestimmte, unten genannte Regeln festgelegt worden.

Attribute
---------

Um Attribute zu übersetzen wird nicht ``i18n:translate`` sondern ``i18n:attributes`` verwendet. Auch können mehrere Attribute gleichzeitig adressiert werden, wie z.B. in::

 <img src="plone.gif"
      alt="Plone Icon"
      title="Plone Icon Title"
      i18n:attributes="alt vs_registration_plone_icon;
                       title vs_registration_plone_icon_title">

Dynamische Inhalte
------------------

Mit ``i18n:name`` lassen sich auch dynamische Inhalte übersetzen, z.B.::

 <p i18n:translate="text_download">There have been
     <span tal:content="here/download_count"
           i18n:name="count">100.000</span>
     downloads of Plone. </p>

Der Eintrag in die Übersetzungsdatei sieht dann folgendermaßen aus::

 msgid "text_download"
 msgstr "There have been ${count} downloads of Plone."

Für Datum und Zeit wird die ``localized_time``-Methode mit den zwei message ids ``date_format_long`` und ``date_format_short`` verwendet. Gibt es keine Übersetzungen für eine Sprache wird das Standardformat ``strftime``, wie in den ``portal_properties`` angegeben, verwendet. Siehe auch `Übersetzen des User-Interfaces: Datum und Urzeit`_.

Verschachtelungen
-----------------

Message ids lassen sich auch verschachteln, z.B.::

 <p i18n:translate="contentrules_controlpanel_link">
     Use the
     <a i18n:name="controlpanel_link"
        i18n:translate="contentrules_control_panel"
        tal:attributes="href string:${portal/absolute_url}/@@rules-controlpanel">
         content rules control panel
     </a>
     to create new rules or delete or modify existing ones.
 </p>

In der Übersetzungsdatei findet die Übersetzung in verschiedenen Abschnitten statt::

 msgid "contentrules_controlpanel_link"
 msgstr "Benutzen Sie ${controlpanel_link} um neue Regeln zu erstellen, zu löschen oder zu modifizieren."

 msgid "contentrules_control_panel"
 msgstr "die Regeleinstellungen"

Internationalisieren von Pythonskripten
=======================================

In Pythonskripten sollten eigentlich keine Angaben zum User Interface stehen. Meist sind jedoch zumindest ``label`` und ``description`` von Widgets in den Pythonskripten selbst enthalten. Um diese lokalisieren zu können, werden gegebenenfalls ``label_msgid`` und ``description_msgid`` eingefügt, z.B.::

 StringField('event_type', vocabulary='EventTypes',
     widget=SelectionWidget(
         label='Event Type',
         label_msgid='label_event_type',
         description='The type of the event',
         description_msgid='help_event_type',
         i18n_domain='vs.registration'),),

Seit Plone 2.5 kann die *Zope Message Factory* in Pythonskripten verwendet werden. Hierzu wird zunächst in der ``__init__.py``-Datei des Pakets die *Message Factory* registriert::

 from zope.i18nmessageid import MessageFactory
 RegistrationMessageFactory = MessageFactory('vs.registration')

Anschließend lässt sich diese *Message Factory* in ein Pythonskript importiert mit::

 from vs.registration import RegistrationMessageFactory as _

Und nun lassen sich folgende Angaben einfach übersetzen::

 label=_(u"Body Text"),
 description=_(u"Text for front page of registration")

Mit dem ``u``-Präfix wird Unicode als Kodierung für die Zeichenketten festgelegt.  Dieses Beispiel wird in einem Page Template weiterverwendet werden (z.B. in ``tal:replace`` oder ``tal:content``).

Falls das Pythonskript nicht in einem Page Template verarbeitet wird, muss ``translation_service`` direkt aufgerufen werden::

 from Products.CMFCore.utils import getToolByName
 ...
 translation_service = getToolByName(self, 'translation_service')
 value = u'John Doo'
 return translation_service.utranslate('plone',
                                        u'My name is ${fullname}',
                                        mapping={u'fullname' : value})


Schließlich können auf diese Weise die Titel und Aktionen von Inhaltstypen in einer eigenen Produktdomäne verwaltet werden – es wird keine zusätzliche ``.pot``-Datei für die Plone-Domäne benötigt.

Siehe auch `Translating text in code`_.

Internationalisieren von GenericSetup-Profilen
==============================================

Verschiedene Angaben in den ``.xml``-Dateien des ``profiles``-Ordner können ebenfalls lokalisert werden, z.B. ``src/vs.registration/vs/registration/profiles/default/types/Registration.xml``::

 <object name="Registration"
         meta_type="Factory-based Type Information with dynamic views"
         i18n:domain="vs.registration"
         xmlns:i18n="http://xml.zope.org/namespaces/i18n">
     <property name="title"
               i18n:translate="">Registration</property>

Standardisierte Präfixe
=======================

In Plone werden bestimmte Präfixe für *message ids* verwendet. Da die IDs später alphabetisch sortiert werden, lassen sich semantische Differenzen leichter erkennen.

``heading_``
 für ``<h>``-Elemente.
``description_``
 erläuternder Text direkt unterhalb von ``<h1>``.
``legend_``
 verwendet für ``<legend>``-Elemente.
``label_``
 Für ``label`` von ``input``- und ``textarea``-Felder sowie ``<a>``-Elemente.
``help_``
 für Hilfetexte von ``input``-Fledern.
``box_``
 für die Inhalte von Portlets.
``listingheader_``
 für ``header``-Angaben in Tabellen (üblicherweisse in der Klasse``listing``).
``date_``
 für datumsspezifische Angaben, wie z.B. *Gestern*, *letzte Woche*.
``text_``
 Nachrichten, die keiner anderen Kategorie zugeordnet werden konnten, üblicherweise innerhalb von ``<p>``.
``batch_``
 für Stapeldarstellungen wie *X bis Y von Z*.
``summary_``
 für Zusammenfassungen in Tabellen.
``title_``
 für Titel aller Elemente.
``message_``
 für Text in ``portal_status_message``

Den Präfixen folgt nach dem Unterstrich eine kurze Beschreibung der Nachricht, wie z.B. *label_address*.

Siehe auch: `Guide to Prefixes`_.

Tipps & Tricks
==============

Vermeiden sie aufwändige Differenzierungen
------------------------------------------

Es ist möglich, z.B. zwischen Singular und Plural zu unterscheiden::

 <p i18n:translate="">
   Cart has <tal:block replace="number">#</tal:block>
   book<tal:block condition=
       "python: number <> 1">s</tal:block>.</p>

Dies macht jedoch die Arbeit der Übersetzer sehr schwierig, da in manchen Sprachen der Plural nicht einfach durch ein bis zwei angehängte Buchstaben gebildet wird.

.. Trennen sie ``i18n:name``- und ``i18n:translate``-Attribute
.. -----------------------------------------------------------

.. Damit die Übersetzungen wiederverwendbar bleiben, sollten beide Attribute **nicht** zusammen verwendet werden. Es sollte also statt::

 <p i18n:translate="">Please visit
     <a href="about"
        i18n:name="about-plone"
        i18n:translate="">
         About Plone</a>
     for more information.
 </p>

.. so gegliedert werden::

 <p i18n:translate="">Please visit
     <span i18n:name="about-plone">
         <a href="about" i18n:translate="">
             About Plone</a>
     </span>
     for more information.
 </p>

Schließen sie die gesamte Phrase ein
------------------------------------

Schließen sie die gesamte Phrase einschließlich der Satzzeichen in die zu übersetzende *message id* ein.

Teilen sie Sätze nicht in zwei verschiedene *message id* auf
------------------------------------------------------------

Verwenden sie für den gesamten Satz den ``i18n:translate``-Tag (s.o.) und verwenden ``i18n:name`` für den eingeschlossenen Teil.

.. _`Placeless Translation Service`: http://pypi.python.org/pypi/Products.PlacelessTranslationService
.. _`Übersetzen des User-Interfaces: Datum und Urzeit`: http://www.veit-schiele.de/dienstleistungen/technische-dokumentation/plone-entwicklerhandbuch/internationalisierung/ubersetzen-des-user-interfaces.html
.. _`Translating text in code`: http://plone.org/documentation/manual/developer-manual/internationalization-i18n-and-localization-l10n/translating-text-in-code/referencemanual-all-pages
.. _`Guide to Prefixes`: http://dev.plone.org/plone/wiki/TranslationGuidelines#GuidetoPrefixes
.. _`Plone Translations`: http://plone.org/products/plonetranslations/

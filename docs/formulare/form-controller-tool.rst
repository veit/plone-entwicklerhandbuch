====================
Form Controller Tool
====================

Plone kommt mit dem `CMF Form Controller`_-Produkt, mit dem die Abläufe zwischen Formularen und Skripten geregelt werden können. Gerade für komplexe Abläufe ist es sehr hilfreich, unterstützt jedoch keine Zope3-Views und kann daher nur in Skin-Layern definiert werden.

Schauen wir uns nun als Beispiel Plone’s *Send this page to someone*-Formular an, das in ``CMFPlone/skins/plone_forms/sendto_form.cpt`` definiert ist. Dabei steht der ``cpt``-Suffix für *Controller Page Template*::

 <div metal:fill-slot="main"
      tal:define="errors options/state/getErrors;">
   ...
   <form name="sendto_form"
         class="enableAutoFocus"
         action="sendto_form"
         method="post"
         enctype="multipart/form-data"
         tal:attributes="action string:$here_url/$template_id">
     ...
     <div class="field"
          tal:define="error errors/send_to_address|nothing;"
          tal:attributes="class python:test(error, ``field error``, ``field``)">
       ...
       <div class="formControls">
         <input class="context"
                type="submit"
                name="form.button.Send"
                value="Send"
                i18n:attributes="value label_send;"
                />
     </div>
     ...
   </form>

- Zunächst fällt auf, dass eine Variable ``errors`` definiert wird, die das Auffinden von Validierungsfehlern erlaubt.
- Dann sehen wir, dass das Formular – wie bei CMFFormController üblich – wieder auf sich selbst verweist.
- Schließlich erkennen wir die versteckte Variable ``form.submitted``, wobei das *Controller Page Template* überprüft, ob das Formular einfach aufgerufen oder bereits abgeschickt wurde.

CMFFormController benötigt zur Auswertung des Formulars eine korrespondierende Datei ``sendto.cpy.metadata`` im selben Verzeichnis::

 [default]
 title=Send this page to somebody

 [validators]
 validators=validate_sendto

 [actions]
 action.success=traverse_to:string:sendto
 action.failure=traverse_to:string:sendto_form

Schauen wir uns nun die Validatoren und Aktionen genauer an.

Validatoren angeben
===================

Allgemein lassen sich für Für *Controller Page Templates* folgendermaßen Validatoren angeben::

 [validators]
 validators = validate_script1, validate_script2

Diese Angabe startet zwei Prüfskripte: zunächst *validate_script1* , dann ``validate_script2`` . Ein Prüfskript untersucht die Formulardaten wobei Fehler dem Form Controller Status hinzugefügt werden.

Objekttyp-spezifische Validierung
---------------------------------

Soll die Validierung vom Objekttyp *Document* verschieden sein von der des Objekttyps *Image* sieht die Metaangabe so aus::

 validators.Document = validate_script1
 validators.Image = validate_script2

Button-spezifische Validierung
------------------------------

Kommen im Formular mehrere Buttons (Tasten) vor, z.B.::

 <input type="submit" name="form.button.button1" value="Value1" />
 <input type="submit" name="form.button.button2" value="Value2" />

können für diese auch unterschiedliche Validierungen angegeben werden::

 validators.button1 = validate_script1
 validators.button2 = validate_script2

Aktionen angeben
================

Für *Controller Page Templates* lassen sich auch Aktionen angeben, z.B.::

 [actions]
 action.success = traverse_to:string:script1

Haben die Prüfskripte den Status ``success`` ausgegeben,  wird die Aktion ``traverse_to`` mit dem Argument ``string:script1`` aufgerufen.

Schlägt ein Prüfskript fehl, wird gemäß den Standardeinstellungen das Formular erneut geladen.

Wie bei Validatoren kann auch bei Aktionen zwischen Dokumenttypen und Buttons unterschieden werden::

 action.success.Document = traverse_to:string:document_script
 action.success.Image = traverse_to:string:image_script

::

 action.success.button1 = traverse_to:string:script1
 action.success.button2 = traverse_to:string:script2

Folgende Aktionen sind möglich:

- ``redirect_to``
- ``redirect_to_action``
- ``traverse_to``
- ``traverse_to_action``.

Dabei rufen die ``traverse_to``-Aktionen direkt ein Template oder Skript auf dem Server auf, wohingegen die ``redirect_to``-Aktionen eine Weiterleitung des Browsers bewirken. Normalerweise werden die Zwischenschritte mit ``traverse_to``-Aktionen und nur der letzte Schritt mit einer
``redirect_to``-Aktion angegeben, sodass die Angabe der URL im Browser die aktuelle Seite wiedergibt. So ist z.B. in unserem Beispiel in ``sendto.cpy.metadata`` folgendes angegeben::

 [validators]
 validators=validate_sendto

 [actions]
 action.success = redirect_to_action:string:view
 action.failure = redirect_to_action:string:view

Validator-Skripte schreiben
===========================

Schauen wir uns nun das Validator-Skript ``validate_sendto.vpy`` genauer an, auf das in ``sendto.cpy.metadata`` verwiesen wurde::

 ## Controller Script Python "validate_sendto"
 ##bind container=container
 ##bind context=context
 ##bind namespace=
 ##bind script=script
 ##bind state=state
 ##bind subpath=traverse_subpath
 ##parameters=send_to_address='',send_from_address=''
 ##title=validates the email adresses

 from Products.CMFPlone import PloneMessageFactory as _
 plone_utils=context.plone_utils

 if not send_to_address:
     state.setError('send_to_address', _(u'Please submit an email address.'), 'email_required')
 ...
 if state.getErrors():
     context.plone_utils.addPortalMessage(_(u'Please correct the indicated errors.'), 'error')
     return state.set(status='failure')
 else:
     return state

Aktionen schreiben
==================

Ist die Validierung erfolgreich, fährt der CMFFormController, wie in ``sendto_form.cpt.metadata`` angegeben mit dem Skript ``sendto.cpy`` fort. Dieses Skript gibt schließlich den Wert für ``state`` aus::

 ## Controller Python Script "sendto"
 ##bind container=container
 ##bind context=context
 ##bind namespace=
 ##bind script=script
 ##bind state=state
 ##bind subpath=traverse_subpath
 ##parameters=
 ##title=Send an URL to a friend
 ##
 REQUEST=context.REQUEST

 ...

 if not mtool.checkPermission(AllowSendto, context):
     context.plone_utils.addPortalMessage(_(u'You are not allowed to send this link.'), 'error')
     return state.set(status='failure')

 ...

 context.plone_utils.addPortalMessage(_(u'Mail sent.'))
 return state

.. _`CMF Form Controller`: http://plone.org/products/cmfformcontroller

=============================================
Zusätzliche Änderungen der Site-Konfiguration
=============================================

Leider lässt sich bisher nicht die gesamte Site durch Profile konfigurieren. Es lassen sich jedoch Methoden hinzufügen, die eine solche umfassende Konfiguration erlauben.

#. Hierzu wird zunächst in ``vs.policy/vs/policy/configure.zcml`` folgendes angegeben::

     <genericsetup:importStep
         name="vs.policy.various"
         title="vs.policy: miscellaneous import steps"
         description="Various import steps that are not handled by GS import/export handlers."
         handler="vs.policy.setuphandlers.setupVarious">
     </genericsetup:importStep>

#. Anschließend wird die Datei ``setuphandlers.py`` angelegt in ``vs.policy/vs/policy/``.

#. Diese Datei enthält zumindest die Methode ``setupVarious``, die nur ausgeführt wird, sofern in im Kontext eine Datei ``vs.policy_various.txt`` vorhanden ist::

    def setupVarious(context):
        if context.readDataFile('vs.policy_various.txt') is None:
            return

#. Schließlich wird noch die Datei ``vs.policy_various.txt`` in ``vs.policy/vs/policy/profiles/default`` angelegt.

Konfigurieren der HTML-Filter
=============================

Die HTML-Filterregeln lassen sich aktuell nicht mit Generic Setup-Profilen konfigurieren. Soll dies mit der ``setuphandlers.py``-Datei geschehen, kann diese z.B. so aussehen::

 import logging
 from plone.app.controlpanel.filter import IFilterSchema

 logger = logging.getLogger('vs.policy')

 def allowTags(site):
     """
     Allows embed, object, param and iframe tags
     """

     adapter = IFilterSchema(site)
     nasty_tags = adapter.nasty_tags
     if 'object' in nasty_tags:
         nasty_tags.remove('object')
     if 'embed' in nasty_tags:
         nasty_tags.remove('embed')

     stripped_tags = adapter.stripped_tags
     if 'object' in stripped_tags:
         stripped_tags.remove('object')
     if 'param' in stripped_tags:
         stripped_tags.remove('param')

     custom_tags = adapter.custom_tags
     if not 'embed' in custom_tags:
         custom_tags.append('embed')
     if not 'iframe' in custom_tags:
         custom_tags.append('iframe')

     adapter.nasty_tags = nasty_tags
     adapter.stripped_tags = stripped_tags
     adapter.custom_tags = custom_tags
     logger.info("Allowing embed, object, param and iframe tags.")

 def setupVarious(context):

     if context.readDataFile('vs.policy_various.txt') is None:
         return

     site = context.getSite()
     allowIframeTags(site)

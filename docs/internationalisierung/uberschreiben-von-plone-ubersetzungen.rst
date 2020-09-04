=================================
Übersetzungen in der Plone-Domäne
=================================

Die folgenden Konfigurationsdateien des *GenericSetup Tools* müssen in der Plone-Domäne übersetzt werden:

- ``portal_atct.xml``
- ``portlets.xml``
- ``workflows/MYWORKFLOW/definition.xml``

Erweitern der Übersetzungen
===========================

In **Plone 3** können Übersetzungen der Übersetzungsdomäne ``plone`` nicht im ``locales``-Ordner angepasst werden. Sollten Sie dies dennoch gemacht haben, werden Sie feststellen, dass nur noch Ihre eigenen Übersetzungen angezeigt werden. Damit Ihre Übersetzungen zusätzlich verwendet werden, müssen die Übersetzungsdateien im ``i18n``-Ordner erstellt werden.

Schemata
--------

Zur Lokalisierung von Schemata wird die ``message_id`` generiert. Dabei wird der
ID des Schemata ``label_schema_`` vorangestellt. Im Folgenden ein Beispiel aus
``plone/app/locales/locales/de/LC_MESSAGES/plone.po``::

    #. Default: "Categorization"
    #: ./ATContentTypes/content/schemata.py
    msgid "label_schema_categorization"
    msgstr "Kategorisierung"

Überschreiben von Plone-Übersetzungen
=====================================

Hierzu erstellen wir zunächst in unserem Buildout-Projekt einen Ordner namens ``i18n`` und darin ``plone-vs-de.po``. Anschließend fügen wir in der ``buildout.cfg``-Datei einen neuen Abschnitt hinzu::

 [buildout]
 ...
 instance
 i18n-overwrites
 ...

 [i18n-overwrites]
 recipe = plone.recipe.command
 command =
     ln -sf ${buildout:directory}/i18n ${instance:location}/
 update-command =
     ${i18n-overwrites:command}

.. `collective.recipe.i18noverrides`_

.. _`collective.recipe.i18noverrides`: http://pypi.python.org/pypi/collective.recipe.i18noverrides/


Plone 4
=======

In **Plone 4** hingegen wird das ``i18n``-Verzeichnis in der Instanz ignoriert. Um Übersetzungen der Domäne Plone zu überschreiben, müssen Sie ein eigenes ``locales``-Verzeichnis anlegen und die Plone-Übersetzungsdatei ``plone.app.locales-4.0.2-py2.6.egg/plone/app/locales/locales/de/LC_MESSAGES/plone.po`` dahin kopieren, also z.B. nach ``vs.theme/vs/theme/locales/de/LC_MESSAGES/plone.po``. Anschließend können Sie aus dieser Datei die Übersetzungen löschen, die Sie nicht ändern wollen und Ihre Übersetzungen hinzufügen.

Nun müssen wir in unserer Buildout-Konfiguration nur noch beachten, dass die ``zcml``-Datei von ``vs.theme`` vor allen anderen Paketen geladen wird. Dies kann gewährleistet werden indem ``vs.theme`` als erstes in der Liste der ``zcml``-Optionen gelistet wird, z.B.::

 [instance]
 ...
 eggs =
     Zope2
     Plone
     ${buildout:eggs}

 zcml =
     vs.theme
     ...

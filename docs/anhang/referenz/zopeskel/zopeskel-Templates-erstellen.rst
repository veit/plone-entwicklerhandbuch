============================
ZopeSkel Templates erstellen
============================

Erstellen eigener ZopeSkel- und local commands-Templates.

Erstellen eines *local command*-Templates
=========================================

Die Python-Skripte zum Erstellen eines *local commands*-Templates entsprechen weitgehend denen eines normalen ZopeSkel-Templates. Wenn wir uns die ``Portlet``-Klasse in ``zopeskel/localcommands/archetype.py`` genauer anschauen, stellen wir fest, dass sie von ``ArchetypeSubTemplate`` abgeleitet wird und diese wiederum von ``ZopeSkelLocalTemplate``::

 import os
 from templer.core.vars import var
 from templer.localcommands import TemplerLocalTemplate

 from Cheetah.Template import Template as cheetah_template

 class ArchetypeSubTemplate(TemplerLocalTemplate):
     use_cheetah = True
     parent_templates = ['archetype']

 class ContentType(ArchetypeSubTemplate):
     _template_dir = 'templates/archetype/contenttype'
     summary = "A content type skeleton"
 ...

``use_cheetah``
 Für *local commands* muss der Wert auf ``True`` gesetzt werden.
``parent_templates``
 Liste der ZopeSkel-Templates, die dieses *local command*-Template aufrufen können.
``_template_dir``
 Verzeichnis mit den Template-Dateien.
``summary``
 Zusammenfassende Beschreibung des Templates.

Die anschließend folgende ``pre``-Methode ermittelt die Variablen ``contenttype_classname``, ``contenttype_classname``, ``contenttype_classname``, ``contenttype_name`` und ``add_permission_name`` des übergeordneten Pakets.

Auch die Template-Struktur entspricht weitgehend der von normalen ZopeSkel-Templates mit dem Unterschied, dass alle Dateien mit ``_insert`` enden. Betrachten wir uns z.B. das ``portlet``-Template genauer, entdecken wir folgende Struktur::

 $ tree ~/.buildout/eggs/templer.plone.localcommands-1.0b1-py2.7.egg/templer/plone/localcommands/templates/archetype/contenttype/
 /home/veit/.buildout/eggs/templer.plone.localcommands-1.0b1-py2.7.egg/templer/plone/localcommands/templates/archetype/contenttype/
 ├── config.py_insert
 ├── content
 │   ├── configure.zcml_insert
 │   └── +content_class_filename+.py_tmpl
 ├── interfaces
 │   ├── +content_class_filename+.py_tmpl
 │   └── __init__.py_insert
 ├── profiles
 │   └── default
 │       ├── factorytool.xml_insert
 │       ├── rolemap.xml_insert
 │       ├── types
 │       │   └── +types_xml_filename+.xml_tmpl
 │       └── types.xml_insert
 └── README.txt_insert

 5 directories, 10 files

Die mit ``_tmpl`` endenden Dateien werden wie normale ZopeSkel-Templates behandelt. Speziell für **local command**-Templates sind die auf ``_insert`` endenden Dateien. Der Inhalt dieser Dateien wird in die korrespondierenden Dateien des bereits bestehenden Projekts eingefügt. Schauen wir uns nun z.B. ``profiles/default/rolemap.xml_insert`` genauer an::

 #<?xml version="1.0"?>
 #<rolemap>
 #  <permissions>
 #    <!-- -*- extra stuff goes here -*- -->
     <permission name="$add_permission_name" acquire="False">
       <role name="Manager" />
       <role name="Contributor" />
     </permission>
 #  </permissions>
 #</rolemap>

- Existiert in dem Projekt bereits eine Datei ``profiles/default/rolemap.xml``, dann werden nur die Zeilen hinzugefügt, die nicht mit ``#`` beginnen.
- Existiert noch keine ``profiles/default/rolemap.xml``-Datei, wird die Datei aus dem Template ohne die mit ``#`` beginnenden Zeilen geschrieben.

Zum Weiterlesen
===============

- `Creating your own Paster templates <http://developer.plone.org/misc/paster_templates.html>`_

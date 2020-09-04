ZopeSkel – Einleitung und Installation
======================================

ZopeSkel ist eine Sammlung von Vorlagen, mit denen sich schnell Buildout-Projekte und Plone-Erweiterungen erstellen lassen.

Einleitung
----------

.. note::

   In der Vergangenheit war `ZopeSkel
   <http://pypi.python.org/pypi/ZopeSkel>`_ ein einziges großes
   Paket, das nun ab Version 3.0 in mehrere kleine Pakete
   aufgeteilt wurde, die unter dem ``templer``-Namespace erschienen.

   Falls Sie ältere Vorlagen benötigen, sollten Sie eine Version
   von ``ZopeSkel < 3.0`` verwenden.

Im ``templer``-Namespace sind u.a. folgende Pakete zu finden:

`templer.core <http://pypi.python.org/pypi/templer.core>`_
 stellt Ihnen ``basic_namespace`` und ``nested_namespace`` zum Erstellen von Python-Namespace- und verschachtelten Python-Namespace-Paketen zur Verfügung.
`templer.buildout <http://pypi.python.org/pypi/templer.buildout>`_
 stellt Ihnen ``basic_buildout`` und ``recipe`` zum Erstellen von Buildout-Projekten und Rezepten zum Erweitern des Buildout-Systems zur Verfügung.
`templer.zope <http://pypi.python.org/pypi/templer.zope>`_
 stellt Ihnen ``zope2_basic`` und ``zope2_nested`` zum Erstellen von Zope-Namespace- und verschachtelten Zope-Namespace-Paketen zur Verfügung.
`templer.plone <http://pypi.python.org/pypi/templer.plone>`_
 stellt Ihnen ``archetype``, ``plone_basic`` und ``plone_nested`` zum Erstellen von Paketen für Plone.
`templer.plone.localcommands <http://pypi.python.org/pypi/templer.plone.localcommands>`_
 stellt Ihnen sog. *local commands* zur Verfügung und zwar für die folgenden Vorlagen:

 - ``archetype``

   ``contenttype``
    Ein Gerüst für einen Archetypes-Artikeltyp
   ``schema_field``
    Ein iterativer Generator für Archetypes-Felder.

 - ``plone_basic``

   ``browserview``
    Eine Zope-``BrowserView``-Klasse mit Interface und Template
   ``browserlayer``
    Ein Zope-``BrowserLayer``-Interface und dessen GenericSetup-Registrierung

Installation
------------

ZopeSkel kann einfach mit buildout installiert werden::

 parts =
     ...
     zopeskel

 [zopeskel]
 recipe = zc.recipe.egg
 unzip = true
 eggs =
     Paste
     ZopeSkel
     templer.plone
     templer.plone.localcommands

Beim Erstellen des buildout-Projekts werden im ``bin/``-Verzeichnis die Skripte ``zopeskel`` und ``paster`` erstellt.

``bin/zopeskel --list``
 gibt eine Liste der verfügbaren Vorlagen aus.
``bin/zopeskel --help``
 stellt Ihnen eine vollständige Hilfe für ZopeSkel zur Verfügung.

Weitere Informationen
=====================

- `Templer System Manual <http://templer-manual.readthedocs.org/en/latest/index.html>`_

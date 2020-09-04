=========================
ZopeSkel – Local Commands
=========================

Neben den Vorlagen für Projekte liefert ZopeSkel auch Vorlagen, die nur in bestimmten Kontexten zur Verfügung stehen, sog. local commands. Mit diesen können Sie bestehende ZopeSkel-Projekte erweitern.

.. note::

   *Local commands* können aktuell nur mit dem ``paster``-Skript aufgerufen werden.

Installation
============

Die Installation erfolgt in Buildout mit::

 [buildout]
 parts =
     ...
     paster
     zopeskel
 ...
 [paster]
 recipe = zc.recipe.egg
 eggs =
    ZopeSkel
    PasteScript
    PasteDeploy

Verwendung
==========

Wenn Sie z.B. ein Archetypes-Paket erstellt haben mit::

 $ cd src
 $ ../bin/zopeskel archetype vs.registration

dann können Sie als nächstes die *local commands* hierfür installieren mit::

 $ cd vs.registration/
 $ python setup.py egg_info

Schließlich können Sie in das ``src/``-Verzechnis dieses Pakets wechseln und dort
einen Artikeltyp erstellen::

 $ cd src/
 $ ../../../bin/paster add contenttype Registrant

Einen Überblick über alle im Kontext verfügbaren *local commands* erhalten Sie mit::

 $ ../../../bin/paster add --list
 Available templates:
     browserlayer:  A Plone browserlayer
     browserview:   A browser view skeleton
     contenttype:   A content type skeleton
     schema_field:  A handy AT schema builder

.. seealso::
    * `ZopeSkel with local commands <https://github.com/collective/ZopeSkel#local-commands>`_

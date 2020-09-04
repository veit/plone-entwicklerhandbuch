=================
Ressourcen teilen
=================

Verzeichnisse teilen
====================

Da wir mehrere Projekte mit verschiedenen Buildout-Konfigurationen betreuen,
wollen wir die Sourcen zwischen den Projekten teilen.

So ist es möglich, Eggs verschiedener Versionen in einem Verzeichnis
bereitzustellen. Ein solches Verzeichnis kann in der
Buildout-Konfigurationsdatei ``buildout.cfg`` im Abschnitt ``[buildout]``
eingetragen werden, z.B.::

    [buildout]
    eggs-directory = /home/veit/.buildout/eggs

Analog teilen wir das ``downloads``-Verzeichnis zwischen verschiedenen
Buildout-Projekten::

    download-cache = /home/veit/.buildout/downloads

Ab Version 1.4.1 von ``zc.buildout`` lässt sich auch ein geteiltes Verzeichnis
für die heruntergeladenen Dateien angeben::

    extends-cache = /home/veit/.buildout/cache

Um Fehlermeldungen zu vermeiden sollten die zu verwendenden Verzeichnisse vor
dem ersten Durchlauf von Buildout erstellt werden, z.B. mit ``mkdir -p
/home/veit/.buildout/{eggs,downloads,cache}``.

Distributionen finden
=====================

Indizes
-------

Üblicherweise sucht Buildout im Python Package Index nach Distributionen. Es
können jedoch auch auch weitere Indizes angegeben werden mit::

    [buildout]
    …
    index = https://pypi.org/simple/

Dieser Index oder falls kein Index angegeben ist
``https://pypi.python.org/simple/`` wird zur Suche nach der passenden
Distribution verwendet. Dabei wird immer die letzte passende Version einer
angeforderten Distribution heruntergeladen.

Links
-----

Neben Indizes kann auch die ``find-links``-Option angegeben werden um
Distributionen zu finden.

Dabei können sowohl URLs als auch Pfadangaben verwendet werden::

    [buildout]
    …
    find-links =
        http://download.zope.org/distribution/
        /some/path
        /other/path/someegg-1.0.0-py2.4.egg

Globale Variablen für alle Buildout-Projekte
============================================

Um diese Konfiguration nicht für jedes Buildout-Projekt erneut angeben zu
müssen, kann eine ``default.cfg``-Datei im Verzeichnis ``~/.buildout`` angelegt
werden::

    [buildout]
    eggs-directory = /home/veit/.buildout/eggs
    download-cache = /home/veit/.buildout/downloads
    extends-cache = /home/veit/.buildout/cache
    index = https://pypi.python.org/simple
    socket-timeout = 3

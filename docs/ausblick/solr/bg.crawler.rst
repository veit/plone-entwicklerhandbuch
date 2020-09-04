==========
bg.crawler
==========

bg.crawler ermöglicht die Indexierung von Dateien und Dateibäumen im Dateisystem durch Solr.

`bg.crawler`_ erlaubt auf der Komandozeile (Command line interface, CLI), einzelne Dateien oder Dateibäume von Solr indizieren zu lassen.

.. _`bg.crawler`: http://pypi.python.org/pypi/bg.crawler

Voraussetzungen
===============

- Python 2.6 oder 2.7
- `curl`_

.. _`curl`: http://curl.haxx.se/

Installation
============

In einer ``virtualenv``-Umgebung lässt sich ``bg.crawler`` einfach installieren mit::

 $ easy_install bg.crawler

Optionen
========

Innerhalb dieser virtuellen Umgebung lässt sich ``bg.crawler`` einfach aufrufen mit::

 $ ./bin/solr-crawler --help

Folgende Parameter stehen Ihnen zur Verfügung:

``--solr-url``
 definiert die URL des Solr-Servers.
``--render-base-url``
 Basis-URL, die den ersten Teil von Solrs ``renderurl`` bildet.
``--max-depth``
 begrenzt die Tiefe der Ordnerhierarchie bis zu der Dateien indiziert werden sollen.
``--commit-after``
 Die Anzahl der Dokumente, die mit einem *commit* an Solr übergeben werden.
``--tag``
 Die importierten Dokumente werden mit einer bestimmten Zeichenkette getagt.

 So lassen sich unterschiedliche Datenquellen auch bei einer späteren Suchanfrage in Solr noch durch unterschiedliche Tags unterscheiden.

``--clear-all``
 leert den Solr-Index vollständig bevor die Daten neu importiert werden.
``--clear-tag``
 entfernt alle Dokumente aus dem Solr-Index, die einen bestimmten Tag enthalten, bevor die Daten neu importiert werden.
``--verbose``
 ermöglicht ein besseres Logging.
``--no-type-check``
 Falls diese Option gewählt wird, wird nicht nach bestimmten Dateitypen gefiltert.

Weitere Informationen zu ``bg.crawler`` erhalten sie unter `bg.crawler documentation`_.

.. _`bg.crawler documentation`: http://packages.python.org/bg.crawler/

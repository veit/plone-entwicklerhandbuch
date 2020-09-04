=========
SolrIndex
=========

`SolrIndex`_ ist ein ZCatalog Multi-Index, der Solr verwendet. Er ersetzt den Standard Volltext-Index von Plone und ermöglicht damit u.a.

- die unterschiedliche Gewichtung von Feldern
- die Verwendung von Stopwords
- die Einbeziehung von Synonymen

.. _`SolrIndex`: http://pypi.python.org/pypi/alm.solrindex

SolrIndex lässt sich so erweitern um

Facettierte Suche
 Dies erlaubt die zunehmende Verfeinerung der Suche
Autovervollständigung (suggestions)
 Anhand der von Ihnen gemachten Eingaben werden Ihnen die am häufigsten gesuchten Phrasen vorgeschlagen
Rechtschreibkorrektur
 Falls Sie sich vertippt haben sollten, schlägt Solr Ihnen eine korrekte Schreibweise vor.

Installation
============

SolrIndex kann einfach mit Buildout installiert werden::

 [instance]
 …
 eggs =
     …
     …alm.solrindex

Anschließend sollte SolrIndex ein SolrIndex auf der Plone-Site hinzugefügt werden. Ein solcher SolrIndex kann dann mehrere ZCatalog-Indexe enthalten.

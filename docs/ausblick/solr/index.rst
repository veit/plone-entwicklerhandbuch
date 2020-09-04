====
Solr
====

Apache Solr ist eine OpenSource Suchmaschine, die auf Sites wie Twitter Apple- and iTunes-Stores, Wikipedia und vielen anderen eingesetzt wird.

.. figure:: solr.jpg
    :width: 169px
    :alt: Solr Logo

`Apache Solr`_ erlaubt nicht nur, die Inhalte verschiedener Systeme zu durchsuchen, es bietet auch weitere umfangreiche Suchfunktionen:

Facettierte Suche
 erlaubt die zunehmende Verfeinerung der Suche
Räumliche Suche (*Geospatial search*)
 anhand von Geodaten
Autovervollständigung (*suggestions*)
 Anhand der von Ihnen gemachten Eingaben werden Ihnen die am häufigsten gesuchten Phrasen vorgeschlagen
Rechtschreibkorrektur
 Falls Sie sich vertippt haben sollten, schlägt Solr Ihnen eine korrekte Schreibweise vor.
Indizierung von binären Dateien
 Hierzu gehören z.B. auch PDFs und MS-Office-Dokumente.

.. _`Apache Solr`: http://lucene.apache.org/solr/

Darüberhinaus kann ein Cluster für Solr erstellt werden, wodurch sich die Last deutlich verteilen lässt.

.. toctree::
    :titlesonly:
    :maxdepth: 1

    solr-installation-und-konfiguration
    solrindex
    bg.solr
    bg.crawler

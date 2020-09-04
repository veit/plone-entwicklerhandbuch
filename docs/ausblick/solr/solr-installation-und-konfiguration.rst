====================================
Solr: Installation und Konfiguration
====================================

Solr lässt sich einfach mit Buildout installieren. Hierzu kann das Paket `collective.recipe.solrinstance`_ verwendet werden.

.. _`collective.recipe.solrinstance`: http://pypi.python.org/pypi/collective.recipe.solrinstance

Hierzu erstellen wir die Datei ``solr.cfg``, die z.B. so aussehen kann::

 [buildout]
 parts =
     solr-download
     solr-instance

 [versions]
 collective.recipe.solrinstance = 3.5
 gocept.download = 0.9.5

 [solr-download]
 recipe = hexagonit.recipe.download
 download-directory = parts/solr-download
 strip-top-level-dir = true
 url = http://ftp-stud.hs-esslingen.de/pub/Mirrors/ftp.apache.org/dist//lucene/solr/3.4.0/apache-solr-3.4.0.tgz
 ignore-existing = true

 solr-instance]
 recipe = collective.recipe.solrinstance
 solr-location = ${solr-download:location}
 host = 83.223.91.163
 port = 8983
 basepath = search

``solr-location``
 Pfad zur Installation von Solr. In unserem Fall ist dies

 ::

  ${solr-download:location}

``host``
 Name oder IP-Adresse des Solr-Servers.

 Der Standardwert ist ``localhost``:

``port``
 Der Port, an dem Solr auf Anfragen lauscht.

 Der Standardwert ist ``8983``.

``basepath``
 Pfad zum Solr-Service auf dem Server. Hieruas wird die endgülitge URL für den Solr-Service generiert::

  $host:$port/$basepath

 Der Standardwert ist ``solr``.

Der Solr-Server kann nun einfach gestartet werden mit::

 $ ./bin/solr-instance fg

oder::

 $ ./bin/solr-instance start

Logging
=======

::

 logdir = ${buildout:directory}/var/solr
 logging-template = ${buildout:directory}/templates/logging.properties.tmpl

``logdir``
 ::

  ${buildout:directory}/var/solr

``logging-template``
 ::

  ${buildout:directory}/templates/logging.properties.tmpl

 Das ``logging.properties.tmpl`` kann dann z.B. so aussehen::

  # Default global logging level:
  .level= INFO

Konfiguration der Suche
=======================

::

 max-num-results = 500
 section-name = SOLR
 unique-key = id
 default-search-field = text
 filter =
     text solr.StopFilterFactory ignoreCase="true" words="stopwords.txt"
     text solr.WordDelimiterFilterFactory generateWordParts="1" generateNumberParts="1" catenateWords="0" catencatenateAll="0"
     text solr.LowerCaseFilterFactory
     text solr.RemoveDuplicatesTokenFilterFactory

 index =
     name:text             type:text    stored:true
     name:title            type:text    stored:true
     name:created          type:date    stored:true required:true
     name:modified         type:date    stored:true
     name:filesize         type:integer stored:true
     name:mimetype         type:string  stored:true
     name:id               type:string  stored:true required:true
     name:relpath          type:string  stored:true
     name:fullpath         type:string  stored:true
     name:renderurl        type:string  stored:true
     name:tag              type:string  stored:true

``max-num-results``
 Die maximale Anzahl von Ergebnissen, die der Solr-Server ausliefern soll.

 Der Standardwert ist ``500``.

``section-name``
 Name des Abschnitts für die Produktkonfiguration, die für die ``zope.conf`` generiert wird.

 Der Standardwert ist ``solr``.

``unique-key``
 beschreibt ein Feld als eindeutig für alle Dokumente. Weitere Informationen hierzu erhalten Sie unter `SchemaXml`_.

 Der Standardwert ist ``uid``.

``default-search-field``
 konfiguriert das Standardsuchfeld sofern kein Feld explizit angegeben wurde.
``filter``
 konfiguriert zusätzliche Filter für den Standard-Feldtyp. Jeder Filter wird in einer neuen Zeile aus einem Index und Parametern definiert. Dabei kann einer der verfügbaren Indextypen angegeben werden und als Parameter Schlüssel-Wert-Paare. Einen Überblick über die verfügbaren Filter erhalten Sie in `TokenFilterFactories`_.

.. _`SchemaXml`: http://wiki.apache.org/solr/SchemaXml
.. _`TokenFilterFactories`: http://wiki.apache.org/solr/AnalyzersTokenizersTokenFilters#TokenFilterFactories

Weitere Konfigurationsmöglichkeiten von ``collective.recipe.solrinstance`` erhalten Sie in `Supported options`_.

.. _`Supported options`: http://pypi.python.org/pypi/collective.recipe.solrinstance#supported-options

======================
unimr.catalogqueryplan
======================

Üblicherweise iteriert die Suchmethode des ZCatalog über alle beteiligten Indizes und bildet anschließend jedesmal die Schnittmenge. Dabei bleibt die Reihenfolge der Indizes, an die die Anfrage gestellt wird, unbestimmt. Dieses Vorgehen lässt sich nun optimieren wenn die Anfrage zunächst an Indizes gestellt wird, dessen Trefferwahrscheinlichkeiten am geringsten sind.

.. note::
    Ab Zope 2.13, das mit Plone 4.1 kommt, unterstützt der ZCatalog Query Plans, s.a. `ZCatalog`_.

.. _`ZCatalog`: http://docs.zope.org/zope2/releases/2.13/WHATSNEW.html#zcatalog

Der Monkey Patch des
`unimr.catalogqueryplan`_ berechnet die durchschnittliche Trefferwahrscheinlichkeit und Verarbeitungsdauer jedes Index. Darauf aufbauend werden die Indizes so sortiert, dass zunächst die effektivsten Anfragen abgearbeitet werden. Hierdurch kann die durchschnittliche Dauer von Anfragen auf die Hälfte reduziert werden.

.. _`unimr.catalogqueryplan`: https://svn.plone.org/svn/collective/unimr.catalogqueryplan/trunk/

Installation
------------

Um ``unimr.catalogqueryplan`` zu installieren, wird ein Abschnitt ``[eggcheckouts]`` im ``[buildout``-Abschnitt eingetragen,  anschließend dieser Abschnitt definiert und schließlich die Eggs dem ZEO-Client zur Verfügung gestellt::

 [buildout]
 parts =
     ...
     eggcheckouts
 ...
 [eggcheckouts]
 recipe = infrae.subversion
 urls =
     https://svn.plone.org/svn/collective/unimr.catalogqueryplan/trunk unimr.catalogqueryplan
 location = src
 as_eggs = true

 [instance]
 ...
 eggs =
     ...
    ${eggcheckouts:eggs}


Logging langsamer Kataloganfragen
---------------------------------

Darüberhinaus kann ``unimr.catalogqueryplan`` langsame Anfragen in das *Event-Log* schreiben. Hierzu werden die Umgebungsvariablen im Abschnitt für den oder die Zope-Server in die Buildout-Konfigurationsdatei eingetragen::

 [instance]
 ...
 zope-conf-additional =
     <environment>
         LOG_SLOW_QUERIES True
         LONG_QUERY_TIME  0.05
     </environment>

``LOG_SLOW_QUERIES``
 Wird der Wert auf ``True`` gesetzt, werden langsame Anfragen in das *Event-Log* geschrieben.
``LONG_QUERY_TIME``
 Nur diejenigen Anfragen, die länger als die hier angegebene Zeit in Sekunden dauern, werden in das *Event-Log* geschrieben.

 Der Standardwert ist ``0.0``.

Die Ausgabe im *Event-Log* kann dann z.B. so aussehen::

 2009-04-17T16:56:47 INFO unimr.catalogqueryplan portal_catalog, query: 0.11ms (hits: 0), mean 128.41ms (key hits: 11),  priority: ('path', 'review_state', 'is_default_page', 'allowedRolesAndUsers', 'portal_type')

Aktualisierungsfrequenz
-----------------------

Wie oft der *Query-Plan* aktualisiert wird, lässt sich ebenfalls über Umgebungsvariablen in der Buildout-Konfigurationsdatei angeben::

 [instance]
 ...
 zope-conf-additional =
     ...
     <environment>
         REFRESH_RATE 500
     </environment>

``REFRESH_RATE``
 Die Zeitspanne, nach der ein neuer *Query Plan* berechnet wird.

 Der Standardwert ist ``100``.

Bogus-Index
-----------

Um unterschiedliche *Query-Plans* für ähnliche Anfragen zu erhalten, können zusätzliche *Bogus-Iindizes* bereitgestellt werden. Diese werden zwar im Katalog ignoriert, können aber dennoch zur Erstellung eines *Query-Plan* verwendet werden.

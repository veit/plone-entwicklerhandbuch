==========
Query-Plan
==========

Üblicherweise iteriert die Suchmethode des ZCatalog über alle beteiligten Indizes und bildet anschließend jedesmal die Schnittmenge. Dabei bleibt die Reihenfolge der Indizes, an die die Anfrage gestellt wird, unbestimmt. Dieses Vorgehen lässt sich nun optimieren wenn die Anfrage zunächst an Indizes gestellt wird, dessen Trefferwahrscheinlichkeiten am geringsten sind.

`experimental.catalogqueryplan`_ berechnet die durchschnittliche Trefferwahrscheinlichkeit jedes Index. Darauf aufbauend werden die Indizes so sortiert, dass zunächst die Anfragen mit den wenigsten Ergebnissen abgearbeitet werden.

.. _`experimental.catalogqueryplan`: http://pypi.python.org/pypi/experimental.catalogqueryplan

Installation
------------

Um ``experimental.catalogqueryplan`` zu installieren, wird es im ``[buildout]``-Abschnitt eingetragen::

 [buildout]
 ...
 eggs =
     ...
     experimental.catalogqueryplan

Anschließend kann es in der ``configure.zcml``-Datei eines Produkts eingetragen werden::

 <include package="experimental.catalogqueryplan" />

Alternativ kann es auch als Wert für ``zcml`` im Abschnitt der Zope-Instanz eingetragen werden::

 [instance]
 ...
 zcml =
     experimental.catalogqueryplan

Bogus-Index-Names
-----------------

Um unterschiedliche Query-Plans für ähnlich Anfragen zu erhalten, ermöglicht ``experimental.catalogqueryplan`` auch zusätzliche *Bogus Index Names*. Diese werden zwar vom Katalog ignoriert, sind jedoch Teil des Schlüssels zur Erstellung des *Query Plans*. So wird z.B. die Suche nach Seiten im Entwurfsstadium in einer anderen Reihenfolge die Indizes abarbeiten als die suche nach veröffentlichten Seiten, da sich wohl nur sehr wenige Artikel im Entwurfsstadium auf einer Site finden dürften.

Logging langsamer Kataloganfragen
---------------------------------

In Version 1.4 wird ``experimental.catalogqueryplan`` auch langsame Anfragen in das *Event-Log* schreiben. Hierzu werden die Umgebungsvariablen im Abschnitt für den oder die Zope-Server in die Buildout-Konfigurationsdatei eingetragen::

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

 Der Standardwert ist ``0.01``.

Die Ausgabe im *Event-Log* kann dann z.B. so aussehen::

 2009-04-17T16:56:47 INFO experimental.catalogqueryplan portal_catalog, query: 0.11ms (hits: 0), mean 128.41ms (key hits: 11),  priority: ('path', 'review_state', 'is_default_page', 'allowedRolesAndUsers', 'portal_type')

.. seealso::
    - `Wikipedia: Query plan`_
    - `Jarn: Catalog query plan`_
    - `experimental.catalogqueryplan: General ideas`_

.. _`Wikipedia: Query plan`: http://en.wikipedia.org/wiki/Query_plan
.. _`Jarn: Catalog query plan`: http://www.jarn.com/blog/catalog-query-plan
.. _`experimental.catalogqueryplan: General ideas`: http://svn.plone.org/svn/collective/experimental.catalogqueryplan/trunk/IDEAS.txt

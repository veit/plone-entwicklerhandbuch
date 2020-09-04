==========
haufe.ztop
==========

haufe.ztop erlaubt die Analyse von Zope-Requests zur Laufzeit.

Home
====

http://pypi.python.org/pypi/haufe.ztop

Anforderungen
=============

- `haufe.requestmonitoring`_

.. _`haufe.requestmonitoring`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/produktivserver/monitoring/haufe.requestmonitoring

Installation
============

Um ``haufe.ztop`` zu installieren, muss es einfach in der ``buildout.cfg``-Datei hinzugefügt werden::

 [buildout]
 parts =
     ...
    ztop
 ...
 [ztop]
 recipe = zc.recipe.egg
 eggs = haufe.ztop

Nachdem Buildout durchlaufen wurde, stehen Ihnen die beiden Skripts ``ztop`` und ``zanalyse`` zur Verfügung.

``ztop``
 stellt die Request-Informationen dar indem es die Zope-Request-Logfiles auswertet. Diese werden identifiziert durch ``requestsBasename`` und ``startDate``.
``zanalyse``
 gibt regelmäßig Angaben der Request-Informationen auf der Konsole aus indem es die Zope-Request-Logfiles auswertet. Diese werden identifiziert durch ``requestsBasename`` und ``startDate``.

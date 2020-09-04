==============
Skalierbarkeit
==============

ZEO
===

Zwar ist Python beschränkt auf eine CPU, `ZEO`_ erlaubt jedoch die Verwendung mehrerer Zope-Applikationsserver, die sich eine Datenbank teilen können. Dabei sollte jedem dieser Zope-Clients eine andere CPU verwenden.

.. _`ZEO`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/anhang/glossar/zeo

Mount-Points
============

ZODB unterstützt `Mount-Points`_, womit sich Daten über mehrere Storages verteilen lassen. Dabei lassen sich die Memory-Cache-Settings für jede Datenbank getrennt angeben. Wird z.B. der Katalog in eine eigene Datenbank ausgelagert, so kann für diese ein deutlich höherer Memory-Cache angegeben werden um die Performance zu verbessern (siehe auch `Katalog in eigener ZODB`_).

.. `Mount-Points`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/produktivserver/zodbs-konfigurieren.html
.. _`Katalog in eigener ZODB`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/produktivserver/performance/zcatalog/katalog-in-eigener-zodb?searchterm=katalog

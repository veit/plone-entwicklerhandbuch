=====================================
Zusätzliche Informationen für Windows
=====================================

Für Windows sind entsprechende Dienste für den ZEO-Cluster einzurichten.

ZEO-Server
==========

Für den ZEO-Server wird der Dienst erstellt mit::

 > bin\zeoserver_service  install

bzw. in Plone-Versionen < 3.3::

 > bin\zeoservice install

Üblicherweise werden die Services mit ``--startup auto``
intstalliert, sodass sie beim Systemstart automatisch gestartet werden.

ZEO-Clients
===========

::

 > bin\instance install
 > bin\instance2 install

Zum Deinstallieren dieser Services können Sie einfach folgendes aufrufen::

 > bin\instance remove
 > bin\instance2 remove

=========================
ZODB Replication Services
=========================

Mt den  ZODB Replication Services (ZRS) können Systemadministratoren ihre ZODB auf zwei oder mehrere Storage-Server replizieren.

Erhöhte Ausfallsicherheit
=========================

Dies reduziert die Ausfallzeiten sowohl bei geplanten als auch bei ungeplanten
Ausfällen, indem Administratoren:

- unternehmenskritische Daten auf zwei oder mehrere Datenbank-Server replizieren
- des Storage-Cluster in einem Wide Area Network (WAN) verteilen
- die primären und sekundären Server verwalten und überwachen, sodass ggf. ein
  schneller Failover vom primärem zum sekundärem Storage-Server realisiert
  werden kann

Backup and Maintenance
======================

Wenn der primäre Storage-Server ausfällt, nimmt der sekundäre Server seinen
Platz ein und die ZEO-Clients verbinden sich transparent mit dem neuen ZRS-
Server. Die sekundären Server können jedoch auch vom Netz genommen werden, z.B.
für die Überprüfung und ggf. `Reparatur <zodb-reparieren>`_ von ``POSKeyError``
und ``CorruptedError`` oder für Upgrades. Wenn dieser sekundäre Server wieder
als Service eingebunden wird, synchronisiert er sich automatisch mit dem
primären Server. Damit vereinfachen die ZODB Replication Services (ZRS) die
routinemäßige Wartung ungemein.

Skalierbarkeit
==============

Die ZODB Replication Services (ZRS) verbessern auch die Skalierbarkeit, da
sekundäre Server zusätzliche schreibgeschützte ZEO-Verbindungen unter
Beibehaltung ihrer Replikationsfunktionen aufbauen können.

Konzept
=======

Die ZODB Replication Services (ZRS) erhalten einen primären Server für Schreib-
und Lesezugriffe und eine beliebige Anzahl von sekundären Servern mit Nur-Lese-
Zugriffen. Bei einer Transaktion auf dem primären Server wird diese auf alle
verfügbaren sekundären Server repliziert. Wird ein sekundärer kurzzeitig vom
Server vom Netz genommen oder ein weiterer sekundärer Server hinzugefügt, so
werden diese automatisch auf den aktuellen Stand gebracht.

Installation
============

Requirements
------------

`zc.zrs <https://pypi.python.org/pypi/zc.zrs/2.4.2>`_ setzt ZODB 3.9 oder größer
voraus.

Buildout
--------

#. In der Buildout-Konfiguration muss ``zc.zrs`` als zusätzliches Egg angegeben
   werden.

#. Anschließend kann der primäre Server konfiguriert werden mit::

    [zeoserver1]
    ...
    zeo-conf-additional =
        <zrs>
            replicate-to 5000
            <filestorage>
                path ${buildout:directory}/var/filestorage/Data.fs
            </filestorage>
        </zrs>

   ``replicate-to``
       Adresse des Replikationsservices

       Dies kann nur eine Port-Nummer oder ein Hostname mit Portnummer durch
       einen Doppelpunkt getrennt sein.

#. Konfigurieren eines sekündären Servers::

    [zeoserver2]
    ...
    zeo-conf-additional =
        <zrs>
            replicate-from primary-host: 5000
            replicate-to 5000
            keep-alive-delay 60
            <filestorage>
                path ${buildout:directory}/var/filestorage/Data.fs
            </filestorage>
        </zrs>

   ``replicate-from primary-host``
       Adresse des primären Servers
   ``replicate-to``
       Optionale Angabe.

       Wird diese Option genutzt, können andere sekundäre Server von diesem
       Service replizieren.

   ``keep-alive-delay``
       Optionale Angabe.

       In einigen Netzwerkkonfigurationen werden TCP-Verbindungen nach längerer
       Inaktivität unterbrochen. Um dies zu verhindern, sendet der sekundäre
       Server regelmäßige ``no-operation``-Nachrichten um die Verbindung
       aufrechtzuerhalten.

plone.recipe.zeoserver
----------------------

Ab Version 1.2.6 von `plone.recipe.zeoserver
<https://pypi.python.org/pypi/plone.recipe.zeoserver>`_ oder Plone 4.3.2 lässt
sich der ZRS einfacher installieren::

    [zeoserver]
    recipe = plone.recipe.zeoserver[zrs]
    ...

``replicate-to``
    Angabe von Host und Port für den primären Server.
``replicate-from``
    Angabe von Host und Port für den sekundären Server, der die Daten
    repliziert.
``keep-alive-delay``
    In manchen Netzwerkkonfigurationen wird die TCP-Verbindung unterbrochen bei
    einer längeren Zeit der Inaktivität. Um dies zu verhindern kann der
    sekundäre Server periodische Nachrichten an den primären Server schicken.

.. seealso::
    * `Repository <https://bitbucket.org/zc/zc.zrs>`_

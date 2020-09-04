Buildout für Produktivserver
============================

Wir haben eine Entwicklungsumgebung aufgesetzt, die einige Entwicklungswerkzeuge
enthält und für die an mehreren Stellen Debugging ermöglicht wurde. Mit Buildout
ist es nun einfach möglich, dieses Projekt in eine Produktivumgebung zu
überführen.

Zope Enterprise Objects
-----------------------

Zum Entwickeln haben wir eine einfache Zope-Instanz aufgesetzt. Für den
Produktivserver wollen wir Zope Enterprise Objects (ZEO) verwenden, da so
mehrere Zope-Instanzen auf eine ZODB, die vom ZEO-Server verwaltet wird,
zugreifen können. Dies bietet mehrere Vorteile:

- Der ZEO-Server und die ZEO-Clients sollten auf verschiedenen Maschinen sitzen
  und so für eine höhere Ausfallsicherheit sorgen.
- Mehrere ZEO-Clients verteilen ggf. auftretende Last in der Anwendungslogik.
- ZEO-Clients können unterschiedliche Aufgaben übernehmen und speziell dafür
  konfiguriert werden, z.B. für anonyme Betrachter, Redakteure und
  Administratoren.

Konfiguration
-------------

Wir verwenden unser bisheriges Buildout-Projekt und ergänzen es um eine
Konfiguration für den Produktivbetrieb. Hierzu erstellen wir eine weitere
Konfigurationsdatei ``deploy.cfg``::

 [buildout]
 extends =
     base.cfg

 parts =
     zeoserver
     instance1

 [zeoserver]
 recipe = plone.recipe.zeoserver
 zeo-address = 127.0.0.1:8000
 blob-storage = ${buildout:directory}/var/blobstorage

 [instance-base]
 zeo-client = True
 zeo-address = ${zeoserver:zeo-address}
 blob-storage = ${zeoserver:blob-storage}
 shared-blob = on
 zserver-threads = 4
 http-fast-listen = off

 [instance1]
 <= instance-base
 http-address = 8010
 debug-mode = off
 verbose-security = off

Ändern von IP und Ports
-----------------------

``[zeoserver]``
~~~~~~~~~~~~~~~

``zeo-address``
    gibt die Adresse des ZEO-Servers an.

    Der Standardwert ist 8100.

``[instance1], [instance-profile]``, ``[instance-debug]``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``zeo-client``
    wird der Wert auf ``true`` gesetzt, wird aus der Instanz ein ZEO-Client, der
    auf einen ZEO-Server mit einer bestimmten ``zeo-address`` verweist.
``http-address``
    Port des HTTP-Servers. Der Standardwert ist ``8080``.
``ip-address``
    ist die Standard-IP-Adresse, an der der ZEO-Client auf Anfragen horcht. Ist
    kein Wert angegeben, lauscht Zope auf allen IP-Adressen der Maschine. Die
    Anweisung kann überschrieben werden in den Server-Konfigurationen
    ``<http-server>`` etc. Üblicherweise ist keine IP-Adresse angegeben.
``zeo-address``
    gibt die Adresse des ZEO-Servers an, z.B. ``212.42.230.152:8100``.

    Der Standardwert ist ``8100``.

Temporary Storage
~~~~~~~~~~~~~~~~~

In ``temporary storages`` werden z.B. Session-Daten gespeichert. Da diese nicht
für jede einzelne Instanz gespeichert werden sollten sondern zentral, können Sie
auf den ZEO-Server verlagert werden.

#. Zunächst sollte hierzu jede Instanz so konfiguriert werden, dass sie den
   ``temporary storage`` auf dem ZEO-Server anlegen soll::

    eggs =
        tempstorage
    zodb-temporary-storage =
        <zodb_db temporary>
            # Temporary storage database (for sessions)
            <zeoclient>
                server ${zeoserver:zeo-address}
                storage temp
                name zeostorage
                var ${buildout:directory}/var/filestorage
            </zeoclient>
            mount-point /temp_folder
            container-class Products.TemporaryFolder.TemporaryContainer
        </zodb_db>

Verändern eines bestehenden Abschnitts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Um einen bestehenden Abschnitt zu ergänzen, kann mit += z.B. der PDBDebugMode
für den zweiten ZEO-Client hinzugefügt werden::

 [instance-profile]
 <= instance-base
 ...
 environment-vars +=
     PROFILE_PUBLISHER 1

Umgekehrt können auch einzelne Werte entfernt werden::

 eggs -=
     Products.PDBDebugMode

``[zeoserver]``
    verwendet ``plone.recipe.zope2zeoserver``, um einen ZEO-Server in
    ``parts/zeoserver`` aufzusetzen.

    ``zope2-location``
        verweist auf die im zope2-Abschnitt angegebene Installation.
    ``zeo-address``
        gibt den Port des ZEO-Servers an, der Standardwert ist 8100.

    Es können auch noch weitere Konfigurationsoptionen angegeben werden, z.B.

    ``zeo-conf``
        Ein relativer oder absoluter Pfad zur ``zeo.conf``-Datei. Wird kein Pfad
        angegeben, wird eine ``zeo.conf``-Datei mit den in ``[zeoserver]``
        angegebenen Werten generiert.
    ``zeo-conf-additional``
        Zusätzliche Angaben zur ``zeo.conf``-Datei. Dabei müssen die
        nachfolgenden Zeilen eingerückt sein.

    Einen vollständigen Überblick über alle Optionen erhalten Sie in
    `plone.recipe.zope2zeoserver
    <http://pypi.python.org/pypi/plone.recipe.zope2zeoserver>`_.

``[instance]``, ``[instance2]``
    verwenden plone.recipe.zope2instance

    ``zeo-client``
        wird der Wert auf ``true`` gesetzt, wird aus der Instanz ein ZEO-Client,
        der auf einen ZEO-Server mit einer bestimmten ``zeo-address`` verweist.
    ``zeo-address``
        gibt die Adresse des ZEO-Servers an, der Standardwert ist 8100.

        Meist empfiehlt es sich, den Wert aus dem ``zeoserver``-Abschnitt zu
        übernehmen::

         ${zeoserver:zeo-address}

    ``zodb-cache-size``
        Anzahl der Objekte, die der ZEO-Client im Cache halten kann.
    ``debug-mode``, ``verbose-security``
        Damit die instance-Instanz die Daten ausliefert und die ``instance2``-
        Instanz zum Debuggen verwendet werden kann, werden nur für die
        ``instance2``-Instanz die Werte auf On gesetzt.
    ``zope-conf-additional``
        erlaubt weitere Einstellungen der Zope-Konfiguration, in unserem Fall
        werden für den zweiten ZEO-Client die ``zserver-threads`` auf ``1``
        heruntergesetzt. Debugging und Maintenance werden deutlich vereinfacht,
        da immer nur eine Anfrage gleichzeitig abgearbeitet wird.

    Eine Übersicht über die für zope2instance verfügbaren Optionen erhalten Sie
    in http://pypi.python.org/pypi/plone.recipe.zope2instance.

Verschieben des Buildout-Projekts auf einen Produktivserver
-----------------------------------------------------------

Die Buildout-Umgebung unseres Projekts kann nun auf den Produktivserver
verschoben werden. Hierzu sind mindestens folgende Dateien erforderlich:

``bootstrap.py``
    erstellt die Struktur des Buildout-Projekts einschließlich ``bin/buildout``.
``base.cfg``, ``devel.cfg``, ``deploy.cfg``, ``versions.cfg``
    die Konfigurationsdateien.
``src/``
    das Verzeichnis, das die gesamte Eigenentwicklung des Projekts enthält.

Anschließend kann das Projekt neu erstellt werden mit::

    $ python2.7 bbootstrap.py -c deploy.cfg
    $ ./bin/buildout -c deploy.cfg

Würde die Konfigurationsdatei nicht spezifiziert, würde Buildout die Standard-Konfigurationsdatei ``buildout.cfg``-Datei erwarten.

Anschließend können ZEO-Server und ZEO-Client gestartet werden::

    $ ./bin/zeoserver start
    $ ./bin/instance1 start

Nun sollte Zope über den Port 8010 erreichbar sein. Falls dies nicht der Fall
sein sollte, können Sie statt ``start`` auch ``fg`` verwenden, um die Prozesse
im Vordergrund laufen zu lassen und eventuelle Fehlermeldungen auf der Konsole
ausgegeben zu bekommen.

**Anmerkung 1:** Wird die Zope-Instanz unter Linux oder Mac OS X von root
gestartet, muss in der ``buildout.cfg``-Datei im ``[instance]``-Abschnitt eine
Direktive für ``effective-user`` angegeben werden, an dessen User ID der Prozess
gebunden wird, nachdem die Ports zugewiesen wurden, z.B.::

    [instance]
    ...
    effective-user = plone

So können für die Zope-Instanz auch Ports mit Nummern kleiner 1024 verwendet
werden.

Anmerkung 2: Unter Windows lässt sich eine Zope-Instanz als Service
installieren, z.B. mit::

    > bin\instance install

Konfigurieren des NFS für blobstorage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``zeoserver``:
    In ``/etc/exports`` kann folgendes eingetragen werden::

        /plone/vs_buildout/var/blobstorage 192.168.110.0/24(rw)

    Damit erlaubt der NFS-Server ``zeoserver`` NFS-Exporte an Server des
    internen Netzes ``192.168.110.0/24``.

    Anschließend wird der NFS-Server neu gestartet mit::

        # service nfs restart
        NFS-Daemon beenden:                                        [  OK  ]
        NFS mountd beenden:                                        [  OK  ]
        NFS-Dienste beenden:                                       [  OK  ]
        NFS-Dienste starten:                                       [  OK  ]
        NFS-mountd starten:                                        [  OK  ]
        NFS-Daemon starten:                                        [  OK  ]

``instance1``, ``instance-profile``, ``instance-debug``
    Hier kann das NFS gemountet werden, z.B. mit::

        mount -t nfs4 192.168.110.3:/plone/vs_buildout/var/blobstorage /plone/vs_buildout/var/blobstorage

    oder ``/etc/mtab`` konfigurieren::

        ...
        192.168.110.3:/plone/vs_buildout/var/blobstorage /plone/vs_buildout/var/blobstorage nfs4 rw,addr=192.168.110.3,clientaddr=192.168.110.4 0 0

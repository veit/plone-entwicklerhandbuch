===============
Backup der ZODB
===============

Zope bringt mit ``repozo.py`` ein Skript mit, das das Backup der ZODB im laufenden Betrieb ermöglicht. Es befindet sich wie schon ``zeopack.py`` in ``parts/zope2/utilities/ZODBTools/``. Zudem lassen sich mit ``repozo.py`` auch inkrementelle Backups erstellen. ``plone.recipe.zope2instance`` erstellt einen Wrapper ``bin/repozo``.

Um nun ein inkrementelles Backup zu erzeugen, erstellen wir zunächst das Verzeichnis ``backups``, bevor wir ``repozo`` mit den entsprechenden Parametern aufrufen::

 $ mkdir backups
 $ ./bin/repozo -BvzQ -r backups -f var/filestorage/Data.fs

Soll ein Backup wieder zurückgespielt werden, sollte die Zope-Instanz zunächst gestoppt werden, eine Kopie der voraussichtlich korrupten ``Data.fs`` erstellt werden und erst dann ``repozo`` aufgerufen werden::

 $ ./bin/repozo -Rv -r backups -o Data.fs

**Anmerkung 1:** Da ``repozo`` nach jedem `Packen der ZODB`_ wieder nur ein vollständiges Backup durchführen kann, empfiehlt sich das Packen deutlich weniger häufig als das Backup.

Dieser Eintrag kann auch automatisiert mit dem Rezept ``z3c.recipe.usercrontab`` erstellt werden. Hierzu wird in der ``deploy.cfg`` folgendes eingetragen::

 [buildout]
 parts =
     ...
     backup-crontab
 ...
 [backup-crontab]
 recipe = z3c.recipe.usercrontab
 times = 15 0 * * *
 command = ${buildout:bin-directory}/repozo  -BvzQ -r ${buildout:directory}/backups -f ${buildout:directory}/var/filestorage/Data.fs

Backup mehrerer ZODBs einer Instanz
===================================

Mit `collective.recipe.backup`_ wird ein Skript erstellt, das für mehrere ZODBs Backups erstellen kann, z.B. zusätzlich für den `Katalog in eigener ZODB`_::

 [buildout]
 parts =
     ...
     backup
 ...
 [backup]
 recipe = collective.recipe.backup
 additional_filestorages =
     Extra
     Super

Falls zum Anlegen mehrer Mount-Points ``collective.recipe.filestorage`` verwendet wurde, kann der ``[backup]``-Abschnitt auch vereinfacht werden::

 [backup]
 recipe = collective.recipe.backup
 additional_filestorages = ${filestorage:parts}

Folgende zusätzliche Optionen bietet ``collective.recipe.backup``:

``location``
 Ort, an dem die Backups gespeichert werden.

 Der Standardwert ist ``var/backups`` innerhalb des Buildout-Verzeichnisses.

 Bei der expliziten Verwendung von ``location`` ist zu beachten, dass der letzte Teil der Angabe als Präfix verwendet wird. Die Angabe::

  location = ${buildout:directory}/backups

 werden im Ordner des Buildout-Projekts die Unterordner ``backups_Catalog`` und ``backups_Extra`` erzeugt. Diese enthalten dann die Backups der jeweiligen Datenbank.

``keep``
 Anzahl der vollständigen Backups, die aufbewahrt werden.

 Der Standardwert ist ``2``.

 Alle älteren Backups einschließlich ihrer inkrementellen Backups werden automatisch gelöscht.

 Wird der Wert auf ``0`` gesetzt, werden alle Backups aufbewahrt.

``datafs``
     Falls sich die Data.fs nicht im Standardordner var/filestorage/Data.fs befindet kann der Pfad mit dieser Option überschrieben werden.

``full``
 Üblicherweise werden inkrementelle Backups erstellt. Wird der Wert hier auf ``true`` gesetzt, werden jedesmal vollständige Backups erstellt.
``debug``
 In seltenen Fällen sollte in die Log-Datei im ``debug``-Level geschrieben werden. Dann sollte hier der Wert auf ``true`` gesetzt werden.
``snapshotlocation``
 Ort, an dem die Schnappschüsse gespeichert werden sollen.

 Der Standardwert ist ``var/snapshotbackups`` innerhalb des Buildout-Verzeichnisses. Bei expliziter Festlegung gelten bezüglich des Pfads dieselben Regeln für das Ordner-Präfix wie bei ``location``.
``gzip``
 Der Standardwert ist ``true``.

 Dabei ist die Endung gezippter ZODBs ``*.fsz`` und nicht ``*.fs.gz``.

``additional_filestorages``
 Hier können Sie zusätzliche Angaben machen, z.B. wenn Sie Ihren Katalog in eine eigene ZODB ausgelagert oder weitere ZODBs als Mount-Point eingebunden haben.

Bei Verwendung von ``collective.recipe.backup`` nach diesem Muster ändert man den ``command`` im Abschnitt ``[backup-crontab]`` auf::

 [backup-crontab]
 ...
 command = ${buildout:bin-directory}/backup -q

Löschen alter Backups
=====================

Alte Backups sollten nach einer bestimmter Zeit wieder gelöscht werden. In unserem folgenden Beispiel werden inkrementelle Backups nach zwei Wochen und vollständige Backups nach fünf Wochen gelöscht::

 [buildout]
 parts =
     ...
     remove-incremental-backups
     remove-full-backups
 ...
 [remove-incremental-backups]
 recipe = z3c.recipe.usercrontab
 times = 8 0 * * *
 command = find ${buildout:directory}/backups -name \*deltafs -ctime +14 -delete

 [remove-full-backups]
 recipe = z3c.recipe.usercrontab
 times = 8 0 * * *
 command = find ${buildout:directory}/backups -name \*dat -ctime +35 -delete

.. _`Packen der ZODB`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/produktivserver/zodb-packen.html
.. _`collective.recipe.backup`: http://pypi.python.org/pypi/collective.recipe.backup
.. _`Katalog in eigener ZODB`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/produktivserver/performance/zcatalog/katalog-in-eigener-zodb

Blob-Storages
=============

Mit ``plone.recipe.backup`` ab Version 2.0 lassen sich auch Sicherungskopien des Blob-Storage anlegen. Plone speichert seit ersion 4.0 üblicherweise alle Bilder und Dateien (*Binary large objects*) im Dateisystem. Daher müssen von diesen Blob-Storages ebenfalls Sicherheitskopien erstellt werden. Falls der Speicherort der Blob-Storages nicht aus ``plone.recipe.zope2instance`` hervorgeht, kann mit ``blob_storage`` auch explizit der Pfad angegeben werden::

 [buildout]
 parts =
     instance
     backup

 [instance]
 recipe = plone.recipe.zope2instance
 user = admin:admin
 blob-storage = ${buildout:directory}/var/blobstorage

 [backup]
 recipe = collective.recipe.backup

Falls erforderlich, kan Buildout verschiedene Skripts zum Erstellen der Sicherungskopien für die ZODBs und die Blob-Storages erstellen::

 [buildout]
 parts =
     ...
     filebackup
     blobbackup

 [filebackup]
 recipe = collective.recipe.backup
 backup_blobs = false

 [blobbackup]
 recipe = collective.recipe.backup
 blob_storage = ${buildout:directory}/var/blobstorage
 only_blobs = true

Folgende Attribute kamen neu hinzu:

``blob-storage``
 Verzeichnis, in dem die Blob-Storages gespeichert werden.

 Diese Option wird ignoriert, falls ``backup_blobs = false``.

 Falls nichts für ``blob-storage`` angegeben wird, wird versucht, einen Wert zu ermitteln aus einem Abschnitt, in dem eines der folgenden Rezepte verwendet wird:

 - ``plone.recipe.zeoserver``
 - ``plone.recipe.zope2instance``
 - ``plone.recipe.zope2zeoserver``

``blob_storage``
 Alternative Schreibweise für ``blob_storage`` da ``plone.recipe.zope2instance`` ebenfalls diese Variable verwendet, in ``collective.recipe.backup`` jedoch Unterstriche verwendet werden.
``backup_blobs``
 Sofern ein Wert für ``blob-storage`` angegeben ist oder ermittelt werden kann, werden üblicherweise Sichrungskopien der Blob-Storages erstellt. Mit ``backup_blobs = false`` kann dies unterbunden werden.
``blobbackuplocation``
 Verzeichnis, in dem die Sicherungskopien gespeichert werden.

 Der Standardwert ist ``var/blobstoragebackups`` innerhalb des Buildout-Verzeichnisses.

``blobsnapshotlocation``
 Verzeichnis, in dem die Schnappschüsse erstellt werden.

 Der Standardwert ist ``var/blobstoragesnapshots`` im Buildout-Verzeichnis.

``only_blobs``
 Es wird ausschließlich ein Backup der Blob-Storages erstellt, nicht der ZODBs.

 Der Standardwert ist ``false``.

``use_rsync``
 Das Programm ``rsync`` mit *Hard Links* zum Erstellen der Blob-Backups wird verwendet.

 Der Standardwert ist ``true``.

 Sofern ``rsync`` nicht installiert ist, oder *Hard Links* nicht funktionieren (*Windows*), sollte dieses Attribut auf ``false`` gesetzt werden. Dann wird eine einfache Kopie mit Pythons ``shutil.copytree`` erstellt.

Mehrere Blob-Storages
=====================

Aktuell unterstützt ``collective.recipe.backup`` nicht zusätzliche Blob-Storages. Für diese müsste ggf. ein eigener Buildout-Abschnitt erstellt werden, der ein zweites Set von Backup-Skripten erstellt, z.B.::

 [extrablobbackup]
 recipe = collective.recipe.backup
 blob_storage = ${buildout:directory}/var/extrablobstorage
 only_blobs = true

rsync
=====

Üblicherweise verwendet ``collective.recipe.backup`` ``rsync`` zum Erstellen der Backups. Dabei werden sog. *hard links* erstellt um Plattenplatz zu sparen und inkrementelle Backups zu erzeugen. Dies erfordert jedoch Linux/Unix oder Mac OS X.

``rsync`` kann nun auch verwendet werden um Backups auf entfernte Hosts zu erstellen: `rsync-backup.sh`_

.. _`rsync-backup.sh`: rsync-backup.sh/view

Für Windows liegen uns zum aktuellen Zeitpunkt keine Erfahrungen vor, auf der Basis von Cygwin sollte es jedoch auch auf Windows-Systemen lauffähig sein. Falls nicht, kann ``use_rsync = false`` gesetzt werden und das Blob-Storage-Verzeichnis wird nach dem Backup einfach kopiert.

collective.recipe.rsync
-----------------------

Alternativ kann das Rezept `collective.recipe.rsync`_ verwendet werden. Hierzu kann z.B. die Datei ``rsync.cfg`` mit folgendem Inhalt erstellt werden::

 [rsync-file]
 recipe = collective.recipe.rsync
 source = veit-schiele.de:/srv/www.veit-schiele.de/var/filestorage/Data.fs
 target = var/filestorage/Data.fs
 script = true

 [rsync-blob]
 recipe = collective.recipe.rsync
 source = veit-schiele.de:/srv/www.veit-schiele.de/var/blobstorage/
 target = var/blobstorage/
 script = true

.. _`collective.recipe.rsync`: http://pypi.python.org/pypi/collective.recipe.rsync

``script``
 Üblicherweise ruft ``collective.recipe.rsync`` ``rsync`` während der Installation des Rezepts auf. Sofern ein entsprechendes Skript erstellt wird, kann dieses später z.B. als Cronjob aufgerufen werden um ``rsync`` auszuführen. Hierbei ist lediglich darauf zu achten, dass ``rsync-file`` vor ``rsync-blob`` ausgeführt wird.
``port``
 Optional kann ein alternativer Port für ``rsync`` angegeben werden.

.. seealso::
    Weitere Informationen zu ``rsync`` erhaltet Ihr in den Artikel von Mike Rubel: `Easy Automated Snapshot-Style Backups with Linux and Rsync`_.

.. _`Easy Automated Snapshot-Style Backups with Linux and Rsync`: http://www.mikerubel.org/computers/rsync_snapshots/

.. Plone 4
   =======

   Ab Plone 4.0 werden üblicherweise Bilder und Dateien in ein sog. ``blobstorage`` im Dateisystem geschrieben. Um von diesen Daten ebenfalls ein Backup zu erstellen, sollte nach dem Durchlauf des ``repozo``-Skripts von diesem Verzeichnis ebenfalls ein Backup erstellt werden. Dies kann z.B. mit folgendem Eintrag in der ``deploy.cfg``-Datei geschehen::

    [buildout]
    ...
    parts =
        –
        backup
        backup-template
        backup-crontab

    [backup]
    recipe = collective.recipe.backup
    keep = 7
    full = true
    gzip = true

    [backup-template]
    recipe = collective.recipe.template
    inline =
        #!/bin/bash
        ${buildout:bin-directory}/zeopack
        ${buildout:bin-directory}/backup -q
        blob=$(basename `ls ${backup:location}|tail -n1` .fsz)
        cd ${buildout:directory}
        tar zcf ${backup:location}/$blob.tar.gz var/blobstorage
        deletemark=`ls ${backup:location}/*.tar.gz|sort -r|tail -n+8`
        if [ ! -z "$deletemark"]; then rm $deletemark; fi
        rsync -a --delete ${backup:location}/ plone@veit-schiele.de:/home/plone/vs_buildout/backups/
        rsync -a --delete ${buildout:directory}/var/log/ plone@veit-schiele.de:/home/plone/vs_buildout/log/
    output = ${buildout:bin-directory}/backup.sh
    mode = 755

    [backup-crontab]
    recipe = z3c.recipe.usercrontab
    times = 37 2 * * *
    command = ${backup-template:output}

   Hiermit sollten im ``var/backups``-Verzeichnis Dateien der folgenden Art erzeugt werden::

    2011-08-21-01-00-06.dat
    2011-08-21-01-00-06.fsz
    2011-08-21-01-00-06.tar.gz

   Für das Wiederherstellen der Daten sind nun folgende drei Schritte erforderlich::

    $ ./bin/restore
    $ rm -rf var/blobstorage/*
    $ tar xvf var/backups/2011-08-21-01-00-06.tar.gz

.. Um auch inkrementelle Backups des Blob-Storages zu erstellen, kann folgendes angegeben werden::

 # start a full backup on day 0:
 tar cf bak0.tar var/blobstorage
 # on day 1, do an incremental backup, it backups only newer file:
 find var/blobstorage ! -type d -newer bak0.tar -print | xargs tar cf bak0.1.tar
 # on day 2:
 find var/blobstorage ! -type d -newer bak0.tar -print | xargs tar cf bak0.2.tar

.. Um die inkrementellen Backups wiederherstellen zu können, kann z.B. folgendes angegeben werden::

 $ rm -rf var/blobstorage/*
 $ tar xf bak0.tar
 $ tar xf bak0.2.tar

.. s.a. `backup of blobstorage in collective.recipe.backup`_

.. _`backup of blobstorage in collective.recipe.backup`: http://plone.293351.n2.nabble.com/backup-of-blobstorage-in-collective-recipe-backup-td5411264.html

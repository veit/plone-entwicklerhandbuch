===================
Verzeichnisstruktur
===================

::

 vs_buildout
 ├── README.rst
 ├── base.cfg
 ├── bootstrap.py
 ├── deploy.cfg
 ├── devel.cfg
 ├── develop-eggs
 │   └── vs.policy.egg-link
 ├── docs
 │   └── HISTORY.rst
 ├── eggs
 │   ├── AccessControl-2.13.10-py2.7-macosx-10.4-x86_64.egg
 │   ├── Acquisition-2.13.8-py2.7-macosx-10.4-x86_64.egg
 │   ├── …
 ├── etc
 │   ├── logrotate.conf
 │   └── plone.vcl
 ├── rsync.cfg
 ├── src
 │   ├── README.txt
 │   └── vs.policy
 ├── templates
 │   ├── haproxy.conf.in
 │   ├── logrotate.conf.in
 │   └── plone.vcl.in
 ├── var
 │   ├── blobbackup-blobstorages
 │   ├── blobbackup-blobstoragesnapshots
 │   ├── blobstorage
 │   │   └── tmp
 │   ├── filebackup-snapshots
 │   ├── filebackups
 │   ├── filestorage
 │   │   ├── Data.fs
 │   │   ├── Data.fs.index
 │   │   ├── Data.fs.lock
 │   │   └── Data.fs.tmp
 │   ├── instance
 │   │   └── import
 │   ├── instance-base
 │   │   └── import
 │   └── log
 │       └── zeoserver.log
 ├── versions.cfg
 └── vs_buildout.txt

``bin/``
 enthält ausführbare Dateien, u.a. ``buildout`` und das Zope-Kontrollskript ``instance``.
``bootstrap.py``
 Bootstrap-Skript des Buildout-Projekts.
``*.cfg``
 Konfigurationsdateien von Buildout, siehe `Buildout-Konfiguration <buildout-konfiguration>`_.
``develop-eggs/``
 Verweise auf Eggs, die in diesem Buildout-Projekt entwickelt werden sollen und die in der ``buildout.cfg`` angegeben wurden.
``downloads/``
 Rezepte wie ``plone.recipe.plone`` und ``plone.recipe.distros`` laden ihre Archive von Produkten und Paketen in diesem Verzeichnis herunter.
``eggs/``
 Eggs, die Buildout automatisch heruntergeladen hat. Aktiviert werden die Eggs explizit in den Kontrollskripten im ``bin``-Verzeichnis.
``fake-eggs/``
 In Buildout-Projekten für Plone ≤ 3.1 enthält dieses Verzeichnis die sog. ``fake-zope-eggs``, wobei in der ``*.egg-info``-Datei die Version angegeben werden kann.
``.installed.cfg``
 Buildout speichert die aktuellen Konfigurationsdaten in dieser Datei.
``parts/``
 Dateien, die für die jeweiligen Abschnitte der Buildout-Konfiguration verwendet werden.
``products/``
 Für ältere Plone-Versionen lassen sich hier die Zope-Produkte erstellen, die in diesem Buildout-Projekt entwickelt werden.
``src/``
 Eggs, die in diesem Buildout-Projekt entwickelt werden.
``var/``
 var-Dateien der Zope-Instanz: z.B. ZODBs in ``filestorage/`` Log-Dateien in ``logs/`` und ``zopectlsock`` und kompilierte Übersetzungsdateien in ``instance-base``.

Ein solches Buildout-Projekt kann anderen Entwicklern in einem Repository zur Verfügung gestellt werden, wobei die Verzeichnisse ``bin``, ``eggs``, ``download``, ``var`` und ``parts`` ignoriert werden können, da sie sich mit ``bootstrap.py`` wiederherstellen lassen.

===========
ZODB packen
===========

Die Zope Objects Database (ZODB) speichert die Daten, indem sie neue Transaktionen anhängt. Daher wächst die ZODB mit jeder Änderung weiter an, auch wenn Dateien gelöscht oder Transaktionen rückgängig gemacht werden. Durch das Packen der ZODB werden nur noch die Ergebnisse der Transaktionen bis zu einem bestimmten Zeitpunkt zusammengefasst. Dabei wird der Zeitpunkt in Tagen angegeben, für die die Transaktionen noch erhalten werden.

Mit ZEO lässt sich das Packen der Datenbank einfach Automatisieren mit dem
Skript ``ClientStorage.py`` in ``eggs/ZODB3-3.9.5-py2.6-linux-x86_64.egg/ZEO/``.
Und ``plone.recipe.zeoserver`` stellt mit ``bin/zeopack`` auch einen Wrapper mit
den nötigen Pfadangaben in unserem Buildout-Projekt bereit::

    $ ./bin/zeopack days=7

Dabei lässt sich mit ``days`` die Anzahl der Tage angeben, für die alle älteren
Objekte gepackt werden sollen.

Nach dem Packen ist die bisherige ZODB im Dateisystem verschoben worden nach
``var/filestorage/Data.fs.old``. Soll also durch das Packen Festplattenspeicher
gewonnen werden, muss diese Datei noch gelöscht werden.

.. note::
    In Plone 3 befindet sich das Skript ``ClientStorage.py`` in
    ``parts/zope2/lib/python/ZEO/``.

Cron Job definieren
===================

Schließlich kann mit ``crontab -e`` noch ein Cron Job definiert werden, der das
Skript regelmäßig aufruft. Fügen Sie in der Tabelle z.B. folgende Zeile hinzu um
die Datenbank jeden Montag um 0:05 Uhr zusammenzupacken und alle Änderungen
älter als 7 Tage zu löschen:

    5 0 * * 1 /home/veit/myproject/bin/zeopack days=7

Weitere Einstellmöglichkeiten erhalten Sie mit ``man 5 crontab``.

Dieser Eintrag kann auch automatisiert mit dem Rezept ``z3c.recipe.usercrontab``
erstellt werden. Hierzu wird in der ``deploy.cfg`` folgendes eingetragen::

    [buildout]
    parts =
        ...
        zeopack-crontab
    ...
    [zeopack-crontab]
    recipe = z3c.recipe.usercrontab
    times = 5 0 * * 1
    command = ${buildout:bin-directory}/zeopack days=7

Mehrere ZODBs packen
====================

Sind zusätzliche ZODB-Mount-Points definiert worden, so sollten diese ebenfalls
gepackt werden können. Hierfür ist dann jedoch ein eigenes Skript notwendig,
z.B. ``zeopackall``::

    #!/home/veit/myproject/bin/zopepy

    username = None
    blob_dir = "/home/veit/myproject/var/blobstorage-%(fs_part_name)s"
    realm = None
    storages = '1','extra'
    days = "7"
    unix = None
    address = "localhost:8100"
    host = "localhost"
    password = None
    port = "8100"
    import getopt; opts = getopt.getopt(sys.argv[1:], 'S:B:W1')[0];
    opts = dict(opts)
    storage = opts.has_key('-S') and opts['-S'] or '1'
    blob_dir = opts.has_key('-B') and opts['-B'] or blob_dir

    import plone.recipe.zeoserver.pack

    for storage in storages:
        print 'Packing storage %s' % storage
        plone.recipe.zeoserver.pack.main(host, port, unix, days, username, password, realm, blob_dir, storage)

``storages``
    Liste der Namen der zu packenden ZODBs.

    ``1`` ist der Standardwert für die ``main``-Datenbank.

.. note::
    ``plone.recipe.zeoserver`` steht ``zopepy`` üblicherweise nicht zur
    Verfügung. Daher sollte in der ``deploy.cfg``-Datei folgendes eingetragen
    werden::

        [zeoserver]
        eggs = plone.recipe.zeoserver
        ...
        [zopepy]
        ...
        eggs =
            ${instance:eggs}
            ${zeoserver:eggs}

    Und auch im Abschnitt ``zeopack-crontab`` sollte auf das neue Skript
    verwiesen werden::

        [zeopack-crontab]
        ...
        command = ${buildout:directory}/zeopackall

.. note::
    Für Plone 3 sollte statt ``plone.recipe.zeoserver`` das Rezept
    ``plone.recipe.zope2zeoserver`` verwendet und die Zeilen mit ``blob_dir`` im
    ``zeopackall``-Skript gelöscht werden.

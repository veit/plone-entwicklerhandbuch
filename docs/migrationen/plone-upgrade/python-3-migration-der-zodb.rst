===========================
Python-3-Migration der ZODB
===========================

ZODB selbst ist mit Python 3 kompatibel, eine in Python 2.7 erstellte Datenbank kann
jedoch nicht ohne vorherige Migration in Python 3 verwendet werden. Hierfür müssen folgende Schritte ausgeführt werden:

#. Aktualisieren der Site auf Plone 5.2 mit Python 2, s.a. `Upgrading Plone 5.1 to
   5.2 <https://docs.plone.org/manage/upgrading/version_specific_migration/upgrade_to_52.html>`_.
#. Stellt sicher, dass der Code aller von euch verwendeten Add-Ons in Python 3
   funktioniert, s.a. :doc:`../upgrade-von-zusatzprodukten/python-3-migration`.
#. :doc:`../../produktivserver/zodb-packen`.
#. :doc:`../../produktivserver/backup-der-zodb`.
#. Im Buildout mit ``py2env`` und `zodbverify
   <https://pypi.org/project/zodbverify/>`_ überprüfen, ob die Integrität eurer
   Datenbank gewährleistet ist:

   #. Installation von ``zodbverify``. Hierfür wird zunächst die ``devel.cfg``
      geändert und anschließend das ``bin/buildout`` aufgerufen::

        [instance]
        eggs +=
            zodbverify
        ...

   #. Anschließend kann die Datenbank überprüft werden mit::

        $ bin/zodbupdate --convert-py3 --file=var/filestorage/Data.fs --encoding utf8
        ...
        Updating magic marker for var/filestorage/Data.fs
        Ignoring index for /Users/pbauer/workspace/projectx/var/filestorage/Data.fs
        Loaded 2 decode rules from AccessControl:decodes
        Loaded 12 decode rules from OFS:decodes
        Loaded 2 decode rules from Products.PythonScripts:decodes
        Loaded 1 decode rules from Products.ZopeVersionControl:decodes
        Committing changes (#1).

      Zusätzlich können noch weitere Optionen angegeben werden, z.B.:

      ``-D``
          falls defekte *Pickles* entdekckt werden, können diese direkt debugged
          werden.
      ``--encoding-fallback``
          falls ``UnicodeDecodeError`` auftreten, ist die Instanz vermutlich nicht
          einheitlich ``utf-8`` kodiert. Hier empfiehlt es sich, als Fallback
          ``latin1`` zu verwenden, da dies die frühere Standardkodierung von Zope
          war, also ``--encoding-fallback latin1``.

   Falls Integritätsprobleme, auftreten, müssen diese vor der Migration gelöst
   werden. Weitere typische Probleme sind:

   #. defekter ``Data.fs.index``, z.B.::

        $ ./bin/zodbupdate --convert-py3 --file=var/filestorage/Data.fs --encoding=utf8
        Updating magic marker for var/filestorage/Data.fs
        loading index
        Traceback (most recent call last):
          File "/home/erral/downloads/eggs/ZODB-5.5.1-py3.6.egg/ZODB/FileStorage/FileStorage.py", line 465, in _restore_index
            info = fsIndex.load(index_name)
          File "/home/erral/downloads/eggs/ZODB-5.5.1-py3.6.egg/ZODB/fsIndex.py", line 134, in load
            v = unpickler.load()
        UnicodeDecodeError: 'ascii' codec can't decode byte 0x80 in position 249: ordinal not in range(128)

      Diesen Fehler solltet ihr beheben können indem ihr vor der Migration die Datei
      ``Data.fs.index`` löscht.

   #. fehlerhafte Suche

      In diesem Fall solltet ihr den Katalog neu erstellen. Hierzu geht ihr in eurer
      Plone-Site in den ``portal_catalog``, wählt den *Advanced*-Reiter und klickt
      dann auf *Clear and Rebuild*.

#. Kopiert die Datenbank nun in ein Buildout mit ``py3env``, startet jedoch **nicht**
   die Instanz.
#. Migriert die Datenbank mit `zodbupdate <https://pypi.org/project/zodbupdate/>`_.

   #. Zunächst wird ``zodbupdate`` mit Buildout installiert::

        [buildout]

        parts =+
            zodbupdate

        [zodbupdate]
        recipe = zc.recipe.egg
        eggs =
            zodbupdate
            ${buildout:eggs}

   #. Anschließend kann die ZODB aktualisiert werden mit::

        $ bin/zodbupdate -f var/filestorage/Data.fs

#. Überprüft die Integrität eurer Datenbank mit ``zodbverify``. Wenn Probleme
   auftreten, behebt diese und wiederholt die Migration.
#. Startet die Instanz und überprüft manuell ob alles wie erwartet funktioniert.

Siehe auch
==========

* `Migrating the ZODB <https://zope.readthedocs.io/en/latest/zope4/migration/zodb.html>`_

===============
ZODB reparieren
===============

Eine Zope-Datenbank kann z.B. durch einen Systemabsturz oder einen Festplattendefekt korrumpiert werden. Dies macht sich meist durch einen POSKeyError oder einen CorruptedError und nicht mehr bearbeitbare Objekte bemerkbar.

CorruptedError
==============

Dieser Fehler kann verschiedene Ursachen haben, z.B. falsche Längen oder Zeiten
von Transaktionen.

``fsrecover.py`` ist ein Skript, das die Integrität von Transaktionen überprüft
und diejenigen mit korrupten Daten entfernt. Daher ist es auch nicht für
*POSKeyErrors* geeignet sondern empfiehlt sich vielmehr für *CorruptedErrors*.
Darüberhinaus kann es auch zu weiteren *POSKeyErrors* führen wenn eine
fehlerhafte Transaktion entfernt wird und dadurch den Verweis auf ein nicht mehr
vorhandenes Objekt zurücklässt::

    $ ./bin/zopepy -m ZODB.scripts.fsrecover -P 0 var/filestorage/Data.fs var/filestorage/Data.fs.recovered &> logrecover.txt

In ``logrecover.txt`` können Sie anschließend nachschauen, wieviele Daten Ihnen
verloren gingen, z.B.::

    Recovering var/filestorage/Data.fs into var/filestorage/Data.fs.recovered
    . 1 . 2 . 3 . 4 . 5 . 6 . 7 . 8 . 9 . 0
    0 bytes removed during recovery
    Packing ...

POSKeyError
===========

Um diesen Fehler zu verstehen ist es wichtig zu wissen, dass jedes Objekt in der
Datenbank eine eindeutige ID (``OID``) zugewiesen bekommen hat. Diese ``OID``
ist eine binäre Zahl, wie z.B. ``0x40A90L``, die auf ein serialisiertes Objekt
verweist. Bei einem *POSKeyError* kann nun für eine ``OID`` kein passendes
Objekt gefunden werden. So speichert z.B. ein Ordner, der von
``OFS.ObjectManager`` abgeleitet ist, die enthaltenen Objekte als Werte des
``_objects``-Attributs. Die daraus resultierende Liste wird beim Speichern in
eine Liste von OIDs übersetzt. Kann nun beim Laden von ``objectValues()`` eine
OID nicht mehr einem serialisierten Objekt zugewiesen werden, wird ein
*POSKeyError* ausgegeben.

#. Mit `zc.zodbdgc`_ kommt ein Skript mit, das die Überprüfung von mehreren
   ZODBs erlaubt: ``multi-zodb-check-refs``. Dabei traversiert es ab der Wurzel
   durch die gesamten Datenbanken. Dies soll sicherzustellen, dass alle Objekte
   erreichbar sind und jedes nicht-erreichbare Objekt protokolliert werden kann.
   Darüberhinaus wird bei Blob-Eintragen überprüft, ob ihre Dateien geladen
   werden können.

#. Zum Installieren von `zc.zodbdgc <http://pypi.python.org/pypi/zc.zodbdgc>`_ wird zunächst eine ``virtualenv``-
   Umgebung aufgesetzt::

    $ easy_install-2.6 virtualenv
    $ virtualenv --no-site-packages zeo_check

#. Anschließend wird in dieser ``virtuelenv``-Umgebung ``zc.zodbdgc``
   installiert::

    $ cd zeo_check
    $ ./bin/easy_install zc.zodbdgc

#. Packen Sie anschließend Ihre ZODB und kopieren diese in Ihre ``virtuelenv``-
   Umgebung.
#. Erzeugen Sie eine Konfigurationsdatei ``storages.cfg`` mit folgendem Inhalt::

    <zodb>
      <filestorage my>
         path var/filestorage/my.fs
         blob-dir var/blobstorage-my
      </filestorage>
    </zodb>

#. Anschließend kann das ``multi-zodb-check-refs``-Skript aufgerufen werden
   mit::

    $ ./bin/multi-zodb-check-refs storages.cfg

   Sind alle Referenzen Ihrer Datenbank gültig, so erhalten Sie keine Ausgabe.
   Bei POSKeyErrors sieht die Ausgabe beispielsweise so aus::

    !!! main 26798 ?
    POSKeyError: 0x68ae

Regelmäßige Überprüfung und E-Mail-Benachrichtigung
===================================================

Dieses Skript sollte nun regelmäßig als Cronjob ausgeführt werden::

    # Check ZEO Storages
    0 6 * * * cd /home/veit/zeo_check; ./bin/multi-zodb-check-refs |mailx -s "Check Storages" -c admin@veit-schiele.de

Wiederherstellen
================

#. Möglicherweise können die fehlenden Objekte aus dem Backup zurückgespielt
   werden.

#. Mit der ``-r``-Option erhalten Sie eine Datenbank mit entgegengesetzten
   Referenzen, womit sich gegebenenfalls herausfinden lässt, welche Objekte
   fehlen::

    $ ./bin/multi-zodb-check-refs -r var/filestorage/refdb.fs storages.cfg
    !!! main 26798 main 16717
    POSKeyError: 0x68ae

#. Nun schreiben Sie eine ``refdb.cfg`` mit folgendem Inhalt::

    <zodb main>
        <filestorage 1>
              path /home/veit/zeo_check/var/filestorage/refdb.fs
        </filestorage>
    </zodb>

#. Anschließend können Sie die Datenbank öffnen::

    $ ../myproject/bin/zopepy
    >>> import ZODB.config
    >>> db = ZODB.config.databaseFromFile(open('./refdb.cfg'))
    >>> conn = db.open()
    >>> refs = conn.root()['references']

   Sie dürften nun eine Fehlermeldung wie diese bekommen::

    !!! main 13184375 ?
    POSKeyError: 0xc92d77

#. Nun können Sie die OID desjenigen Objekts herausfinden, von dem aus
   referenziert wird::

    >>> parent = list(refs['main'][13184375])
    >>> parent
    [13178389]

#. Wird nun dieses Objekt geladen, sollten Sie einen POSKeyError erhalten::

    >>> app._p_jar.get('13178389')
    2010-07-16 15:30:18 ERROR ZODB.Connection Couldn't load state for 0xc91615
    Traceback (most recent call last):
    …
    ZODB.POSException.POSKeyError: 0xc92d77

#. Wir können jedoch die aktuellen Daten des Elternobjekts laden um eine
   Vorstellung von diesem Objekt zu erhalten::

    >>> app._p_jar.db()._storage.load('\x00\x00\x00\x00\x00\xc9\x16\x15', '')
    ('cBTrees.IOBTree
    IOBucket
    q\x01.((J$KT\x02ccopy_reg
    _reconstructor
    q\x02(cfive.intid.keyreference
    KeyReferenceToPersistent
    …

#. Nun erzeugen wir ein Fake-Objekt, das dieselbe OID (``13184375``) wie das fehlenden Objekt hat mit::

    $ ./bin/instance-debug debug
    Starting debugger (the name "app" is bound to the top-level Zope object)
    …
    >>> import transaction
    >>> transaction.begin()
    >>> from ZODB.utils import p64
    >>> p64(26798)
    '\x00\x00\x00\x00\x00\x00h\xae'
    >>> from persistent import Persistent
    >>> a = Persistent()
    >>> a._p_oid = '\x00\x00\x00\x00\x00\x00h\xae'
    >>> a._p_jar = app._p_jar
    >>> app._p_jar._register(a)
    >>> app._p_jar._added[a._p_oid] = a
    >>> transaction.commit()

#. Sie sollten nun wieder das Objekt selbst wie auch das Elternobjekt aufrufen
   können::

    >>> app._p_jar.get('\x00\x00\x00\x00\x00\x00h\xae')
    <persistent.Persistent object at 0xab7f9cc>
    >>> app._p_jar.get('\x00\x00\x00\x00\x00\xc9\x16\x15')
    BTrees.IOBTree.IOBucket([(39078692, <five.intid.keyreference…

#. Schließlich sollten Sie noch die Verbindung zur Datenbank schließen::

    >>> conn.close()
    >>> db.close()

Fehlende BLOB-Dateien
---------------------

Falls Sie die Fehlermeldung erhalten ``POSKeyError: 'No blob file'``, hat Mikko
Ohtamaa das Skript `fixblobs.py`_  geschrieben, mit dem sich Inhalte aus der
ZODB löschen lassen, für die kein BLOB mehr vorhanden ist. Siehe auch `Fixing
POSKeyError: ‘No blob file’ content in Plone`_.

.. _`fixblobs.py`: fixblobs.py/view
.. _`Fixing POSKeyError: ‘No blob file’ content in Plone`: http://opensourcehacker.com/2012/01/05/fixing-poskeyerror-no-blob-file-content-in-plone/

Weitere nützliche Werkzeuge
===========================

``analyze.py``
    zeigt Informationen wie OID, Größe etc. der Objekte in der Datenbank, z.B.::

        $ ./Processed 123816 records in 2601 transactions
        Average record size is 1276.43 bytes
        Average transaction size is 60762.18 bytes
        Types used:
        Class Name                                       Count    TBytes    Pct AvgSize
        ---------------------------------------------- ------- ---------  ----- -------
        AccessControl.User.UserFolder                        1       185   0.0%  185.00
        App.ApplicationManager.ApplicationManager            1       189   0.0%  189.00
        App.Product.ProductFolder                            1        34   0.0%   34.00
        BTrees.IIBTree.IIBTree                            6705   1783379   1.1%  265.98
        BTrees.IIBTree.IIBucket                           6957   4584392   2.9%  658.96
        …
        webdav.LockItem.LockItem                          1203    323529   0.2%  268.94
        ...PersistentAdapterRegistry                         2      7074   0.0% 3537.00
        zope.ramcache.ram.RAMCache                           1       288   0.0%  288.00
        ============================================== ======= =========  ===== =======
                                    Total Transactions    2601                   59.34k
                                         Total Records  123816   154338k 100.0% 1276.43
                                       Current Objects   74107    78439k  50.8% 1083.87
                                           Old Objects   47124    75898k  49.2% 1649.27

``fstest.py``
    überprüft die Datenbank auf korrupte Transaktionen.
``fsrecover.py``
    repariert Transaktionsfehler in der Datenbank.

.. ``fsrefs.py``
 versucht jedes Objekt der Datenbank zu laden um lose Referenzen zu erhalten.

.. ``checkbtrees.py``
 läd alle BTrees der Datenbank und überprüft deren Integrität.

Zum Weiterlesen
===============

- `Recovering from BTree corruption <http://www.mail-archive.com/zodb-dev@zope.org/msg02535.html>`_
- `Inspecting a ZODB to find the causes of bloat <http://www.zopelabs.com/cookbook/1114086617>`_
- `Introduction to the Zope Object Database <http://www.python.org/workshops/2000-01/proceedings/papers/fulton/zodb3.html>`_
- `Finding the last changed object in a ZODB <http://blogs.nuxeo.com/sections/blogs/lennart_regebro/2006_06_28_finding-last-changed-object-in-zodb>`_

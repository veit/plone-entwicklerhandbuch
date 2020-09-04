=================================================
Wiederherstellen versehentlich gelöschter Objekte
=================================================

Üblicherweise lassen sich versehentlich gelöschte Objekte in der Zope Object Database (ZODB) mit dm.historical wiederherstellen sofern die ZODB in der Zwischenzeit nicht gepackt wurde.

Im folgenden Beispiel gehen wir davon aus, dass der Ordner ``news`` in der
Plone-Site ``Plone`` versehentlich gelöscht und nun wiederhergestellt werden
soll.

Hierzu fügen Sie zunächst `dm.historical
<http://pypi.python.org/pypi/dm.historical>`_ im Buildout-Abschnitt der ``debug-
instance`` hinzu::

    [instance-debug]
    <= instance
    ...
    eggs =
        dm.historical
        ...

Nachdem das Buildout-Skript durchgelaufen ist, kann die Instanz im Debug-Modus
gestartet werden::

    $ ./bin/instance-debug debug
    Starting debugger (the name "app" is bound to the top-level Zope object)

    >>> from DateTime import DateTime
    >>> from dm.historical import getObjectAt
    >>> site = getObjectAt(app.Plone, DateTime('2014-03-28 14:00:00'))
    >>> folder = site['news']
    >>> folder.manage_exportObject()

#. Damit wird der Zustand der Plone-Site ``Plone`` zum Zeitpunkt
   ``2014-03-28 14:00:00`` aufgerufen.
#. Anschließend wird das Objekt ``news`` in das Dateisystem exportiert als
   ``news.zexp``.
#. Dann kann die Datei ``news.zexp`` verschoben werden in den ``import``-
   Ordner von ``instance``, also in ``${buildout:directory}/var/import/``.
#. Nun können Sie den Ordner ``news`` im Zope-Management-interface
   importieren.
#. Schließlich sollten Sie im ``portal_catalog`` die Site neu indizieren.

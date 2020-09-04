=================
ZopeHealthWatcher
=================

Mit ZopeHealthWatcher können die Threads der Zope-Anwendung beobachtet werden.

- `ZopeHealthWatcher`_ kann die Threads sowohl von ZEO-Clients als auch von einfachen Zope-Servern anzeigen.
- Für jeden Thread wird angegeben, ob dieser beschäftigt ist, und wenn ja, wird der *execution stack* angezeigt.
- ZopeHealthWatcher kann auch zum Debuggen von *locked threads* verwendet werden.
- ZopeHealthWatcher basiert auf dem Code von `DeadlockDebugger`_.
- Die Darstellung erfolgt entweder auf der Konsole oder im Web-Browser.

.. _`ZopeHealthWatcher`: http://pypi.python.org/pypi/ZopeHealthWatcher/
.. _`DeadlockDebugger`: http://pypi.python.org/pypi/z3c.deadlockdebugger

Installation
============

Erweitern Sie Ihre ``buildout.cfg``-Datei folgendermaßen::

 [buildout]

 parts =
      ...
     zhw

 eggs =
      ...
     ZopeHealthWatcher

 [zhw]
 recipe = zc.recipe.egg
 eggs = ZopeHealthWatcher
 scripts = zope_health_watcher

Konfiguration
=============

Nachdem das Egg installiert ist, müssen in ``eggs/ZopeHealthWatcher-0.3-py2.6.egg/Products/ZopeHealthWatcher/custom.py`` die Werte für ``ACTIVATED`` und ``SECRET`` geändert werden, z.B.::

 ACTIVATED = True
 SECRET = 'secret'

Verwendung
==========

ZopeHealthWatcher kann sowohl in der Konsole als auch im Web-Browser verwendet werden.

``zope_health_watcher``-Skript
------------------------------

Sie können nun ``zope_health_watcher`` aufrufen mit der URL Ihres Zope-Servers oder ZEO-Clients::

 $ zope_health_watcher http://localhost:8080
 Idle: 3	Busy: 1
 OK - Everything looks fine

Ist der Server mit hohem ``load`` ausgelastet, z.B. mit 4 Threads, werden die relevanten Informationen wie Zeit, ``sysload``, Speicherinformationen und  für jeden ausgelasteten Thread Stack, Query, URL als auch den *User Agent* anzeigt::

 $ zope_health_watcher http://localhost:8080
 Information:
     Time: 2011-06-02T10:52:31.522557
     Sysload: 0.25 0.18 0.20 4/1003 32523
     Meminfo: MemTotal:       11759712 kB
     MemFree:         4799368 kB
     Buffers:             204 kB
     Cached:          2933200 kB
     SwapCached:            0 kB
     Active:          4051368 kB
     Inactive:        1678532 kB
     Active(anon):    2830948 kB
     Inactive(anon):    46644 kB
     Active(file):    1220420 kB
     Inactive(file):  1631888 kB
     Unevictable:        2764 kB
     Mlocked:            2764 kB
     SwapTotal:       4000176 kB
     SwapFree:        4000176 kB
     ...
 Dump:
 Thread -162882704
 QUERY: GET /VirtualHostBase/http/www.plone-entwicklerhandbuch.de:80/pen/VirtualHostRoot/@@downloadPDF?
 URL: http://www.plone-entwicklerhandbuch.de/@@downloadPDF
 HTTP_USER_AGENT: Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.2.17) Gecko/20110422 Ubuntu/10.04 (lucid) Firefox/3.6.17
 File "/home/veit/plone40_buildout/eggs/Zope2-2.12.17-py2.6-linux-x86_64.egg/ZServer/PubCore/ZServerPublisher.py", line 31, in __init__
    response=b)
 ...
 Thread -184550544
 ...

Ist der Server nicht erreichbar, gibt das Skript folgendes aus::

 $ ./bin/zope_health_watcher http://localhost:8080
 Idle: 0 Busy: 0
 FAILURE - [Errno socket error] (61, 'Connection refused')

ZopeHealthWatcher gibt dabei Fehlercodes so aus, dass sie auch von Nagios o.ä. weiterverarbeitet werden können:

- ``OK = 0``
- ``WARNING = 1``
- ``FAILURE = 2``
- ``CRITICAL =3``

Web-Browser
-----------

Die Ausgabe kann auch als HTML auf einen Web-Browser erfolgen, wenn z.B. folgende Adresse eingegeben wird::

 http://www.plone-entwicklerhandbuch.de/manage_zhw?secret

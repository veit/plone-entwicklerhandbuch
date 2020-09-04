============
Installation
============

``plone.app.theming`` lässt sich einfach mit Buildout installieren. Hierzu nehmen Sie folgende Änderungen in der ``buildout.cfg``-Datei vor::

 [buildout]
 ...
 extends =
     http://dist.plone.org/release/4.1b2/versions.cfg
     http://good-py.appspot.com/release/plone.app.theming/1.0b5

 find-links =
     http://dist.plone.org/release/4.1b2/
     ...

 versions = versions

 ...
 eggs =
     ...
     plone.app.theming

Nun sollte Buildout problemlos durchlaufen und die Instanz neu gestartet werden können::

 $ ./bin/buildout
 ...
 $ ./bin/instance fg

**Anmerkung:** Während der Entwicklung empfiehlt sich, Zope im Debug-Modus laufen zu lassen da dann die Änderungen an ``theme`` oder ``rules`` sofort übernommen werden.

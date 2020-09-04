=================================
Statische Code-Analyse mit jsHint
=================================

`gocept.jslint <http://pypi.python.org/pypi/gocept.jslint>`_ integriert `jsHint <http://jshint.com/about/>`_ in das Python-Unittest-Modul.

Es bietet eine ``JSLint``-TestCase-Klasse, die konfigurierbar alle Javascript-Dateien einsammelt und dynamisch für jede dieser Dateien eine Testmethode generiert. Diese Methoden können einfach verwendet werden, z.B. mit::

 class MyJSLintTest(gocept.jslint.TestCase):

     include = ('my.package.browser:js',
                'my.package.browser:js/lib')
     options = (gocept.jslint.TestCase.options +
                ('browser', 'jquery',))

``include``
 ist eine Liste von Pfasen zu Ressourcen, ausgehend
 von ``packagename:path``.
``options``
 ist eine Liste von Optinen für jsHint, s.a.
 `Enforcing Options <http://www.jshint.com/docs/>`_.
``predefined``
 Liste globaler Variablen, die mit der
 ``undef``-Option verwendet werden können.
``exclude``
 Liste von Dateinamen, die *nicht* getestet werden
 sollen.

Anforderungen
=============

- Python 2.6 oder Python 2.7
- `node.js <http://nodejs.org/>`_ ≥ 0.3
- ``jshint``-npm-Modul::

   $ npm install jshint -g

  Achten Sie darauf, dass das jshint-Binary in
  ``$PATH`` verfügbar ist.

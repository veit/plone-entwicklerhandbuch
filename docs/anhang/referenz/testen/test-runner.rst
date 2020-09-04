===========
Test Runner
===========

Es gibt verschiedene Möglichkeiten, Tests in Zope ablaufen zu lassen.

In den Versionen Zope 2.9 bis 2.11 lässt sich der TestRunner folgendermaßen
aufrufen um ein ganzes Paket zu testen::

    $ ./bin/test -s vs.policy

Filter
======

``-s my.package``, ``--package my.package``, ``--dir my.package``
    durchsucht die angegebenen Verzeichnisse nach Tests.
``-m test_setup``, ``--module test_setup``
    spezifiziert ein Testmodul als regulären Ausdruck, z.B.::

        $ ./bin/test -s my.package  -m 'test_setup'

``-t  '.*installed.*'``, ``--test test_theme_installed``
    spezifiziert einen Testfilter als regulären Ausdruck, z.B.::

        $ ./bin/test -s vs.policy -m '.*setup.*' -t '.*installed.*'

    Hiermit werden im Paket ``vs.policy`` alle, mit ``installed`` endenden,
    Methoden in allen Testmodulen, die auf ``setup`` enden, durchlaufen.

``-u``, ``--unit``
    durchläuft ausschließlich Unit tests und ignoriert andere ``layer``-
    Optionen.
``-f``, ``--non-unit``
    durchläuft alle Tests, die keine Unit Tests sind

Report
======

``-v``, ``--verbose``
    führt zu ausführlicherer Ausgabe
``--ndiff``
    falls ein Doctest fehlschlägt, wird ``ndiff.py`` zur Darstellung der Unterschiede verwendet
``--udiff``
    falls ein Doctest fehlschlägt, wird Unified Diff zur Darstellung der
    Unterschiede verwendet
``--cdiff``
    falls ein Doctest fehlschlägt, wird Context Diff zur Darstellung der
    Unterschiede verwendet

Analyse
=======

``-d``, ``post-mortem``
    stoppt die Ausführung nach dem ersten nicht-bestandenen Test und ermöglicht
    *post-mortem*-Debugging, d.h. die Debug-Session wird nur gestartet, wenn ein
    Test fehlschlägt.

Setup
=====

``--path src/my.package``
    fügt einen Pfad zu Pythons Suchpfad hinzu, wobei die Option mehrfach
    angegeben werden kann.

Weitere Optionen
================

Diese erhalten Sie mit::

    $ ./bin/test --help

Wenn die relevanten Tests erfolgreich verliefen, sollten schließlich noch alle Tests durchgeführt werden um sicherzustellen, dass nicht an anderer Stelle etwas gebrochen ist. Wenn alle Tests erfolgreich durchlaufen wurden, erscheint eine Meldung::

    Ran 10 tests with 0 failures and 0 errors in 4.830 seconds.

Falls nicht alle Tests erfolgreich durchlaufen wurden, ändert sich die Meldung::

    Ran 10 tests with 2 failures and 3 errors in 9.688 seconds.

Dabei wurden dann zwei Tests nicht bestanden und drei Tests enthielten Fehler.

roadrunner
==========

`roadrunner`_ ist ein Testrunner, der die testgetriebene Entwicklung deutlich beschleunigen kann, da er vorab das Standard-Zope- und Plone-Environment für PloneTestCase läd. zur Installation wird einfach folgendes in die ``buildout.cfg``-Datei eingetragen::

    [buildout]
    parts =
        …
        roadrunner

    [roadrunner]
    recipe = roadrunner:plone
    packages-under-test = vs.policy

Anschließend kann es wie der reguläre Zope-Testrunner aufgerufen werden::

    $ ./bin/roadrunner -s vs.policy

.. _`roadrunner`: http://pypi.python.org/pypi/roadrunner

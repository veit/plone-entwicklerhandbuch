======
Testen
======

Verschiedene Arten von Tests
============================

Hier eine Übersicht über verschiedene Arten von Tests, deren konkrete Unterscheidung jedoch schwierig werden kann.

Unit tests
  werden aus der Programmierperspektive geschrieben. Sie testen isoliert eine einzelne Methode oder Funktion.
Integrationstests
  untersuchen die Abhängigkeit von Methoden und Komponenten während Unit Tests meist mit möglichst wenig Abhängigkeiten geschrieben werden. Meist verwenden Unit Tests und Integrationstests jedoch dasselbe Framework.
Funktionale Tests
  beschreiben meist Nutzungsfälle (Use Cases) und deren Abläufe. Werden sie aus Nutzersicht geschrieben und beziehen sich nur auf die an der Oberfläche angebotenen Eingabemöglichkeiten, werden sie auch *Akzeptanztests* genannt.
Systemtests
  Auch Systemtests werden aus Nutzersicht geschrieben, jedoch ohne Kenntnis des Systems. Systemtests sollen Nutzer mit ihren üblichen Verhaltensmustern simulieren.

Tests und Dokumentation
=======================

Tests liefern häufig eine gute Beschreibung, wie einzelne Komponenten verwendet werden sollen, welche Schnittstellen und Zustände sie aufweisen können. Jim Fulton hat für den Zope-3-Entwicklungsprozess auf docstrings basierende Unit Tests eingeführt, die sich zunehmend auch in anderen Python-Projekten etablieren.

Siehe hierzu auch `Tim Peters, Jim Fulton: Literate unit testing: Unit Testing with Doctest <http://www.python.org/pycon/dc2004/papers/4/>`_.

Konzepte
========

Test Case
  testet eine einzelnes Szenario.
Test Fixture
  ist eine konsistente Testumgebung.
Test Suite
  ist eine Sammlung mehrerer Test Cases.
Test Runner
  durchläuft eine Test Suite und stellt die Ergebnisse dar.

.. `Grok Testing`_

.. _`Grok Testing`: http://grok.zope.org/doc/current/reference/testing.html

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    einfuehrung-in-unit-tests
    test-runner
    testen-mehrerer-eggs
    testabdeckung-code-coverage
    unit-tests-schreiben
    doctests
    unit-tests-als-doctests-schreiben
    doctest-unit-tests-in-separaten-dateien
    funktionale-und-systemtests-mit-zope-testbrowser
    aufzeichnen-funktionaler-tests-mit-zope-testrecorder
    javascripts-testen/index
    robot-framework/index
    jenkins-continuous-integration-server/index
    travis-ci/index

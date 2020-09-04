=====
Spies
=====

Jasmine’s `Test-Doubles <http://en.wikipedia.org/wiki/Test_double>`_ werden
*Spy* genannt. Wesentlich sind momentan sog. `Test stubs <http://en.wikipedia.org/wiki/Test_stubs>`_ möglich, für die Jasmine spezielle *Matchers* bereitstellt:

``toHaveBeenCalled``
 ist wahr wenn der *Spy* aufgerufen wird
``toHaveBeenCalledWith``
 ist wahr wenn die Liste der Argumente übereinstimmt
 mit den aufgezeichneten Aufrufen des *Spy*.
``andCallThrough``
 lässt den *Spy* alle Aufrufe nachverfolgen und
 zusätzlich an die aktuelle Implementierung übertragen
``andReturn``
 gibt einen spezifischen Wert beim Aufruf der Funktion
 aus
``andCallFake``
 gibt die Aufrufe an die angebotene Funktion weiter
``createSpy``
 ``jasmine.createSpy`` kann einen minimalen *Spy*
 erzeugen, der Aufrufe und Argumente nachverfolgt etc.
``createSpyObj``
 ``jasmine.createSpyObj`` erzeugt ein `Mock-Objekt
 <http://de.wikipedia.org/wiki/Mock-Objekt>`_ mit
 mehreren *Spies*

``jasmine.any``
===============

``jasmine.any`` ist wahr, wenn der Name des Konstruktors oder der Klasse dem erwarteten Wert entspricht.

Mock der JavaScript-Clock
=========================

Zum Testen von Timeouts und Intervallen kann
``setTimeout``- und ``setInterval`` verwendet werden.

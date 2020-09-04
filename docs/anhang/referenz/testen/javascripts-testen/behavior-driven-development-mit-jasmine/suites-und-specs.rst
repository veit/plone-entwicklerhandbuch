================
Suites und Specs
================

Erstellen einer Test-Suite
==========================

Eine Test-Suite beginnt mit dem Aufruf der globalen Jasmine-Funktion und  zwei Paremetern:

#. Der Name oder Titel einer ``spec``-Suite
#. Die Funktion, die die Suite implementiert

*Specs*
=======

Spezifikationen (*specs*) sind definiert durch die
globale Jasmine-Funktion `˚ìt`` mit den Parametern
Titel und Funktion.

Dabei kann die Funktion sowohl eine *spec* sein als
auch ein Test. Eine *spec* enthält eine oder
mehrere Erwartungen (*expectations*), deren
Überprüfung entweder wahr oder falsch sein können.

Bewahrheiten sich alle Erwartungen einer *spec* so
wird diese bestanden.

Da ``describe`` und  ``it`` Funktionen sind, können
sie jeden ausführbaren Code enthalten, der zur
Implementierung eines Tests erforderlich ist. Dabei
lassen sich in ``describe`` definierte Variablen in
jedem `ìt``-Block innerhalb der Suite verwenden.

Asynchrone Specs
----------------

Jasmine unterstützt auch das Testen asynchroner Operationen. Entsprechende *Specs* können mit einer Reihe von Blöcken mit ``runs``-Aufrufen geschrieben werden, die üblicherweise asynchron abgearbeitet werden.

``waitsFor``
 wird verwendet mit einer `Latch
 <http://de.wikipedia.org/wiki/Latch>`_-Funktion,
 einer Fehlermeldung und einem Timeout.

 Die Latch-Funktion stellt Anfragen bis es
 ``true`` zurückerhält oder der Timeout überschritten
 ist. Wenn der Timeout überschritten wird, ist die
 *Specs* fehlgeschlagen und gibt die Fehlermeldung
 aus.

Gruppieren von *Specs* mit ``describe``
---------------------------------------

Mit der ``describe``-Funktion lassen sich einfach *specs* gruppieren wobei die Namen der *specs* sich idealerweise zu einem Satz aneinanderreihen lassen.

Setup und Teardown
``````````````````

Jasmine stellt die globalen Funktionen ``beforeEach``
und ``afterEach`` bereit, die vor bzw. nach jeder
*spec* in ``describe`` aufgerufen werden. So lässt
sich der Initialisierungscode in die ``beforeEach``-
Funktion verschieben und das Zurücksetzen der Variablen in die ``afterEach``-Funktion.

Verschachteln von ``describe``-Blöcken
``````````````````````````````````````

``describe``-Blöcke können verschachtelt werden sodass
eine Test-Suite als Funktionsbaum zusammengestellt
werden kann. Bevor eine *Spec* ausgeführt wird, läuft
Jasmine durch den Baum und führt alle ``beforeEach``-
Funktionen in der Reihenfolge aus. Umgekehrt werden, nachdem die *Spec* ausgeführt wurde, alle ``afterEach``-Funktionen durchlaufen.

Deaktivieren von *Specs* und *Suites*
-------------------------------------

*Suites* und *Specs* können deaktiviert werden mit den ``xdescribe`` und ``xit``-Funktionen.

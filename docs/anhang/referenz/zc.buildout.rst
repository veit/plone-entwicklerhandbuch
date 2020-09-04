===========
zc.buildout
===========

Buildout erlaubt, identische Entwicklungsumgebungen einfach aufzusetzen. Hierzu nutzt Buildout die Fähigkeit der setuptools, automatisch Abhängigkeiten aufzulösen und Aktualisierungen durchzuführen.

Variablensubstitution
=====================

Buildout-Konfigurationsdateien erlauben verschiedene Ersetzungen von Variablen, z.B.::

 [buildout]
 parts =
     variables
     source

 [variables]
 var = ${source:path}/var
 logs = ${variables:var}/logs

 [source]
 path = instance

Die Namen von Abschnitten und Optionen in Variablenersetzungen dürfen nur alphanumerische Zeichen, Bindestriche, Punkte und Leerzeichen enthalten.

Der Name des Abschnitts kann im selben Abschnitt weggelassen werden, soll jedoch der aktuelle Name des Abschnitts ermittelt werden, so ist dies mit ``_buildout_section_name_`` möglich, also z.B.::

 [variables]
 ...
 base_variables = ${:_buildout_section_name_}

Abschnitte erweitern – Makro
=============================

Ein Abschnitt kann ein oder mehrere Abschnitte  erweitern wobei die Optionen des referenzierten  Abschnitts zunächst kopiert und anschließend die Variablen substituiert werden. Dies ermöglicht die Verwendung von Abschnitten als Makros.

Beispiel::

 [instance-base]
 recipe = plone.recipe.zope2instance
 ...

 [instance1]
 <=instance-base
 http-address = 8081

 [instance2]
 <=instance
 http-address = 8082

Optionen hinzufügen und entfernen
=================================

Attributen lassen sich Werte hinzufügen und entfernen mit den Operatoren ``+`` und ``-``. Folgendes Beispiel kann dies illustrieren::

 [instance-debug]
 <=instance-base
 eggs +=
     Products.PDBDebugMode
     z3c.deadlockdebugger

oder umgekehrt::

 [instance1]
 <=instance-base
 eggs -=
     Products.PDBDebugMode

Mehrere Konfigurationsdateien
=============================

Eine Buildout-Konfigurationsdatei kann eine andere *erweitern*. Dabei werden die Optionen der erweiterten Konfigurationsdatei gelesen sofern sie nicht bereits definiert sind::

 [buildout]
 extends = base.cfg

Weitere Informationen
=====================

- `Detailed Buildout Documentation <http://pypi.python.org/pypi/zc.buildout/1.5.2#detailed-documentation>`_

============
mr.developer
============

mr.developer ist eine Buildout-Erweiterung, mit der sich Projekte, die über mehrere Repositories verteilt sind, verwalten lassen.

``mr.developer`` wird in der ``extensions``-Option im ``[buildout]``-Abschnitt
hinzugefügt. Anschließend können folgende weitere Optionen festgelegt werden:

``sources-dir``
 Das Verzeichnis, in das die Pakete heruntergeladen werden.

 Der Standardwert ist ``src``.

``sources``
 Liste der Repository-Informationen der Pakete.

 Das Format ist ``<kind> <url> [key=value]``.

 ``kind``
  ``svn``, ``hg`` oder ``git``
 ``url``
  Die URL des Repository
 ``key=value``
  Hier können Optionen für jedes einzelne Paket angegeben werden.

  Es können weder Leerzeichen in ``key`` noch in ``value`` noch um das Gleichheitszeichen herum verwendet werden.

  Im Folgenden einige der gebräuchlichsten Optionen:

  ``path``
   Optionale Angabe des Pfads, in den das Paket ausgecheckt wird, wobei der Name
   des Pakets dem Pfad angehängt wird.

   Wird keine Angabe für ``path`` getroffen, wird stattdessen ``sources-dir``
   verwendet.

  ``full-path``
   Angabe des Pfades, in das ein Paket ausgecheckt wird ohne dass der Paketname
   angehängt wird.
  ``update``
   spezifiziert, ob ein Paket beim Durchlaufen von Buildout aktualisiert
   werden soll oder nicht. Die Angabe überschreibt die globale
   ``always-checkout``-Anweisung.
  ``egg``
   Diese Option erlaubt, die Verwaltung von Paketen, die keine Python-Eggs sind
   mit ``egg=false``. Dann wird das Paket nicht der ``develop``-Option von
   Buildout hinzugefügt.

``auto-checkout``
 Pakete, die beim initialen Aufruf des ``buildout``-Skripts automatisch ausgecheckt werden. ``*`` kann angegeben werden falls alle Pakete in ``sources`` ausgecheckt werden sollen.

``always-checkout``
 Der Standardwert ist ``false``.

 ``true``
  Alle in ``auto-checkout`` angegebenen Pakete, die im *develop mode* sind, werden aktualisiert sobald das ``buildout``-Skript aufgerufen wird.

 ``force``
  Wie bei ``true``, jedoch werden auch die als ``dirty`` markierten Pakete ohne Rückfrage aktualisiert.

Hier ein Beispiel für einen solchen Eintrag in die ``buildout.cfg``-Datei::

 [buildout]
 …
 extensions = mr.developer
 sources = sources
 auto-checkout =
     vs.policy
     some.package
     bootstrap
 always-checkout = true

 [sources]
 vs.policy = svn https://svn.veit-schiele.de/svn/vs.policy/trunk
 some.package = git git://example.com/git/some.package.git
 bootstrap = git git://github.com/twitter/bootstrap.git rev=d9b502dfb876c40b0735008bac18049c7ee7b6d2 path=${buildout:directory} egg=false

Buildout erzeugt nun ein Skript ``bin/develop``, das verschiedene Aktionen zu den einzelnen Paketen erlaubt, wie z.B. das Auschecken des Quellcodes ohne den Ort des Repositories kennen zu müssen. Für weitere Aktionen geben Sie einfach folgendes ein::

 $ ./bin/develop help

Wird der Quellcode aus einem Paket ausgecheckt, muss ``buildout`` erneut durchlaufen werden. Das Paket wird dann automatisch als *develop egg* markiert, und falls es in der Liste der ``versions``-Option festgeschrieben wurde wird dieser Eintrag gelöscht und das *develop egg* verwendet.

Die Liste der *develop eggs* kann mit den ``activate``- und ``deactivate``-Kommandos von ``bin/develop`` gesteuert werden.

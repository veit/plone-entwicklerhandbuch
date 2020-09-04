========
Storages
========

FileStorage
 schreibt die Daten in eine einzelne Datei auf dem Dateisystem. Diese Datei ist im wesentlichen ein großes Transaktionslog.
RelSotrage
 schreibt die Daten in eine relationale Datenbank.
DirectoryStorage
 Für jede Revision eines Objekts wird eine eigene Datei angelegt.
DemoStorage
 bietet inkrementelle Updates einer existierenden Datenbank ohne diese selbst zu aktualisieren.

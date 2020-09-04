==================
Weitere Funktionen
==================

Savepoints
 früher ``sub-transactions``

 erlaubt feingranulare Fehlersuche und *garbage collections* während einer Transaktion.

 verringert den Speicherverbrauch

Undo
 bezeiht sich ausschließlich auf eine einzelne Datenbank. Falls also z.B. der Katalog in eine eigene Datenbank ausgelagert wurde, ist dieser nach einem Undo nicht mehr synchron mit dem Datenbestand.

Pack
 entfernt alte Revisionen eines Objekts.

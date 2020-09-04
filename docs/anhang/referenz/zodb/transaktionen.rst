=============
Transaktionen
=============

Die ZODB kommt mit einem Transaktionssystem, das Nebenläufigkeit (Concurrency) und Atomarität unterstützt.

Nebenläufigkeit (Concurrency)
=============================

Beim Entwickeln für Anwendungen auf Basis der ZODB ist gewährleistet, dass gleichzeitige Anfragen, die zu einem Konflikt führen könnten, weitgehend vermieden und die Daten in der ZODB konsistent gespeichert werden. Gelegentlich auftretende *ConflictErrors* beim Schreiben können verringert werden durch Datenstrukturen, die eigene Konfliktlösungsstrategien mitbringen wie z.B. *B-Trees*.

Eine weitere Quelle für *ConflictErrors* unter hoher Schreiblast sind einige Indextypen, die keine Konfliktlösungsstrategien mitbringen. Eine Möglichkeit ist hier, nicht zu jedem Zeitpunkt den Katalog aktuell zu halten sondern asynchron den Katalog zu aktualisieren. Ein Produkt, das dies erlaubt, ist `collective.indexing`_.

.. _`collective.indexing`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/produktivserver/performance/zcatalog/collective-indexing

Atomarität
==========

Atomarität bedeutet, dass eine Transaktion entweder erfolgreich abgeschlossen wird oder fehlschlägt, die Daten jedoch nie in einem inkonsistenten Status verbleiben. Falls bei einer Transaktion ein *ConflictErrors* auftritt, wiederholt Zope üblicherweise bis zu drei Mal den Versuch, diese Transaktion erneut durchzuführen.

Wird mit einem externen System wie z.B. dem SQLAlchemy-Wrapper `collective.lead`_ gearbeitet, so sollte dieser mit dem Transaktionssystem der ZODB zusammenarbeiten.

.. _`collective.lead`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/relationale-datenbanken/datenbankanbindungen.html?searchterm=collective.lead

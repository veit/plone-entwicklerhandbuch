==========
SQLAlchemy
==========

SQLAlchemy ist eine Python-Bibliothek zur Integration relationaler Datenbanken.
`SQLAlchemy`_ unterstützt eine Vielzahl relationaler Datenbanken, bietet eine niedrigschwellige Verwaltung der Verbindungen, eine Python-API zur Erstellung von SQL-Anfragen und *Object/Relational Mapping* (ORM)-Funktionalität.

In unserem Beispiel werden wir SQLAlchemy verwenden um unsere beiden Datenbanken zu implementieren, um Objekte auf Relationen abzubilden und um SQL-Anfragen zu erstellen. Darüberhinaus werden wir mit ``collective.lead`` Datenbankverbindungen verwalten und SQL-Transaktionen in Zope-Transaktionen zu überführen.

Wesentliche Komponenten von SQLAlchemy sind:

``Engine``
 verwaltet die Datenbankverbindungen.

 In unserem Fall wird ``Engine`` verwaltet von ``collective.lead.interfaces.IDatabase``.

``Table``
 repräsentiert eine Datenbanktabelle.
``Metadata``
 bindet Tabellen an eine spezifische ``Engine``.
``Mapper``
 repräsentiert ein Eintrag in einer Datenbank als Python-Klasse.
``Session``
 verwaltet Instanzen von ``Mapper``-Klassen. Eine Session kann neue Instanzen von einer Datenbank laden, Änderungen an Objekten sichern und neue Objekte als *Records* in der Datenbank speichern.
``Connection``
 erlaubt die Ausführung von SQL-Anfragen, entweder als Python-Anweisung oder als String.

.. _`SQLAlchemy`: http://sqlalchemy.org

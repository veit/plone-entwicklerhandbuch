====================
Datenbankanbindungen
====================

SQLAlchemy bietet standardisierte Interaktionsmuster zur Erstellung von Engines, Metadata, Tabellen und Mapper. Dabei ist zu beachten, dass

- verschiedene Produkte ihre eigenen Datenbankverbindungen aufbauen;
- jede geteilte Datenbankquelle *thread-safe* ist;
- Datenbanktransaktionen mit Zope-Transaktionen synchronisiert werden;
- *Data Source names* (DSN) zur Laufzeit nicht bekannt sind.

`collective.lead`_ bietet eine Basisklasse zur Erstellung von Hilfsmethoden, die Verbindungseinstellungen, Tabellen und Mapper kapseln. Damit wir dies in unseren Hilfsmethoden ``vs.registrations`` und ``vs.reservations`` verwenden können, wird ``collective.lead`` als Abhängigkeit in ``vs.registration/setup.py`` eingetragen::

 install_requires=[
     'setuptools',
     # -*- Extra requirements: -*-
     'MySQL-python',
     'collective.lead>=1.0b3,<2.0dev',
 ],

Bei einem Aufruf von ``./bin/buildout`` sollte nun ``collective.lead`` mitinstalliert werden, welches dann die letzte unterstützte Version von SQLAlchemy installiert. Daneben benötigen wir noch das MySQL-python-Paket, welches MySQL-Treiber für Python bereitstellt.

Das Datenbank-Hilfsprogramm selbst wird dann in ``vs.registration/vs/registration/db.py`` erstellt. Die Datei enthält ebenfalls die Implementierung von ``IDatabaseSettings``, eine persistente, lokale Hilfsmethode zum Speichern der Verbindungseinstellungen::

 from persistent import Persistent

 from zope.interface import implements
 from zope.component import getUtility

 from collective.lead import Database
 from vs.registration.interfaces import IDatabaseSettings

 from sqlalchemy.engine.url import URL
 from sqlalchemy import Table, mapper, relation

 from vs.registration.occurrence import Occurrence
 from vs.registration.reservation import Reservation

 class ReservationsDatabaseSettings(Persistent):
     implements(IDatabaseSettings)

     drivername = 'mysql'
     hostname = 'localhost'
     port = None
     username = ''
     password = None
     database = ''

 class ReservationsDatabase(Database):
     @property
     def _url(self):
         settings = getUtility(IDatabaseSettings)
         return URL(drivername=settings.drivername, username=settings.username,
                    password=settings.password, host=settings.hostname,
                    port=settings.port, database=settings.database)

     def _setup_tables(self, metadata, tables):
         tables['occurrence'] = Table('occurrence', metadata, autoload=True)
         tables['reservation'] = Table('reservation', metadata, autoload=True)

     def _setup_mappers(self, tables, mappers):
         mappers['occurrence'] = mapper(Occurrence, tables['occurrence'])
         mappers['reservation'] = mapper(Reservation, tables['reservation'],
                                         properties = {
                                             'occurrence' : relation(Occurrence),
                                             })

Die ``collective.lead.Database``-Klasse erlaubt uns, nur   wenige Eigenschaften anzugeben, um eine Datenbankverbindung, Tabellen und Mapper zu erstellen.

Nun wird die ``ReservationsDatabase``-Methode noch in ``vs.registration/vs/registration/configure.zcml`` registriert::

 <utility
     provides="collective.lead.interfaces.IDatabase"
     factory=".db.ReservationsDatabase"
     name="vs.reservations"
     />

Da die lokale ``ReservationsDatabaseSettings``-Hilfsmethode jedoch erst mit der Installation des Produkts registriert werden muss, kann das Generic Setup-Profil ``vs.registration/vs/registration/profiles/default/componentregistry.xml`` hierfür verwendet werden::

 <?xml version="1.0"?>
 <componentregistry>
     <utilities>
         <utility
             interface="vs.registration.interfaces.IDatabaseSettings"
             factory="vs.registration.db.ReservationsDatabaseSettings"
             />
     </utilities>
 </componentregistry>

Nun sollte auf die Datenbank zugegriffen werden können mit::

 >>> from zope.component import getUtility
 >>> from collective.lead.interfaces import IDatabase
 >>> db = getUtility(IDatabase, name='vs.reservations')

Dem ``db``-Objekt stehen anschließend die Eigenschaften von ``collective.lead.interfaces.IDatabase`` zur Verfügung.

.. _`collective.lead`: https://svn.plone.org/svn/collective/collective.lead

=================
Datenbankabfragen
=================

Die Implementierung des ``IRegistrations``-Interfaces aus `Hilfsmethoden`_ erfolgt nun in ``occurrence.py``::

 from zope.interface import implements
 from zope.component import getUtility
 from zope.app.component.hooks import getSite

 from Products.CMFCore.interfaces import ISiteRoot
 from Products.CMFCore.utils import getToolByName

 from vs.registration.interfaces import IRegistrant
 from vs.registration.interfaces import IRegistration
 from vs.registration.interfaces import IOccurrence
 from vs.registration.interfaces import IRegistrations

 import sqlalchemy as sql
 from collective.lead.interfaces import IDatabase

 ...

 class Registrations(object):
     implements(IRegistrations)

     def registrations_for_registrant(self, registrant):
         db = getUtility(IDatabase, name='vs.reservations')
         connection = db.connection

         statement = sql.select([Occurrence.c.registration_key],
                                sql.and_(
                                     Occurrence.c.registrant_key == registrant.registrant_key,
                                ),
                                distinct=True)

         results = connection.execute(statement).fetchall()

         registration_keys = [row['registration_key'] for row in results]

         site = getSite()
         catalog = getToolByName(site, 'portal_catalog')

         return [ dict(registration_key=registration.registration_key,
                       url=registration.getURL(),
                       title=registration.Title,)
                  for registration in
                     catalog(object_provides=IRegistration.__keyentifier__,
                             registration_key=registration_keys,
                             sort_on='sortable_title')
                ]

In der ``Registrations``-Klasse werden *Occurrences* von *Registrants* in *Registrations* gefunden. Dabei wird zunächst die Datenbankverbindung hergestellt. Anschließend werden verschiedene SQLAlchemy-Konstrukte verwendet um eine Datenbankabfrage an der ``occurrence``-Datenbank vorzunehmen. So bedeutet z.B. die Syntax ``Occurrence.c.registrant_key``, dass ein Mapping zwischen der ``registrant_key``-Spalte (``c`` olumn) der ``occurrence``-Tabelle und der ``Occurrence``-Klasse stattfindet. Die Syntax ist umfangreich beschrieben in der `SQLAlchemy-Dokumentation`_. Schließlich wird eine Plone-Katalogabfrage nach ``registrant``-Objekten mit den in der ``occurrence``-Tabelle gefundenen ``registration_keys`` erstellt. Diese werden dann in eine Liste von Wörterbuchern, wie sie in ``IRegistrations`` definiert sind, gepackt.

Die ``occurrences``-Methode nutzt hingegen SQLAlchemys ORM-API um die *Occurrences* eines gegebenen *Registrant* als Liste von ``Occurrence``-Objekten auszugeben::

     def occurrences(self, registrant, registration):

         db = getUtility(IDatabase, name='vs.reservations')
         session = db.session

         occurrences = session.query(Occurrence).select(sql.and_(
                                                            Occurrence.c.registrant_key==registrant.registrant_key,
                                                            Occurrence.c.registration_key==registration.registration_key,
                                                            ),
                                                        )

         for occurrence in occurrences:
             occurrence.registrant = registrant
             occurrence.registration = registration

         return occurrences

Da kein Mapping zwischen den ``Registrant``- und ``Registration``-Klassen und der Datenbank stattfindet, können sie von SQLAlchemy nicht geladen und zurückgegeben werden. Stattdessen werden die ``registrant``- und ``registration``-Attribute direkt beim Laden des Objekts gesetzt.

.. _`Hilfsmethoden`: http://www.veit-schiele.de/dienstleistungen/technische-dokumentation/plone-entwicklerhandbuch/relationale-datenbanken/hilfsmethoden.html
.. _`SQLAlchemy-Dokumentation`: http://www.sqlalchemy.org/docs/

===============
Daten schreiben
===============

Im Gegensatz zur ``Registrations``- werden mit der ``Reservations``-Hilfsmethode nicht nur Abfragen an die Datenbank gestellt sondern auch Datensätze geschrieben. Die ``reservations.py``-Datei sieht so aus::

 from zope.interface import implements
 from zope.component import getUtility

 from vs.registration.interfaces import IReservations
 from vs.registration.interfaces import ReservationError

 from vs.registration.occurrence import Occurrence
 from vs.registration import RegistrationMessageFactory as _

 import sqlalchemy as sql
 from collective.lead.interfaces import IDatabase

 class Reservations(object):
     implements(IReservations)

     def __call__(self, reservation):
         db = getUtility(IDatabase, name='vs.reservations')
         session = db.session

         occurrence = reservation.occurrence
         session.refresh(occurrence)

         if occurrence.vacancies <= 0:
             raise ReservationError(_(u"There are not enough vacancies anymore!"))
         elif occurrence.vacancies < reservation.num_reservations:
             raise ReservationError(_(u"Not enough reservations remaining!"))

         occurrence.vacancies -= reservation.num_reservations
         session.update(occurrence)
         session.save(reservation)
         session.flush()

Die Klasse ``Reservations`` macht Reservierungen wobei zunächst überprüft wird, ob nach Plätze frei sind. Anschließend wird``occurrence`` aktualisiert (``refresh``) um zu vermeiden, dass eine andere Transaktion sich die freien Plätze genommen hat. Dann wird die Zahl der verbleibenden freien Plätze aktualisiert (``update``) und fügen die neue Reservierung hinzu (``save``). Sofort danach wird die Session beendet (``flush``) um zu gewährleisten, dass die Änderungen gespeichert werden.

Sind für die angefragte *Occurrence* keine Plätze mehr frei, wird die Fehlermeldung ``ReservationError`` ausgegeben. Diese ist definiert in ``interfaces.py``::

 class ReservationError(Exception):

     def __init__(self, message):
         Exception.__init__(self, message)
         self.error_message = message

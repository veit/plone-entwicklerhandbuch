=================
Datenmodellierung
=================

Für Registration als auch Registrant werden die Felder ``registration_key``, respektive ``occurrence_key`` angelegt, die auch im Katalog indiziert werden sollen. Mit ihnen werden die hierarchischen ZODB-Inhalte auf ein relationales Datenbankmodell abgebildet.

Anschließend erstellen wir entsprechende Interfaces in ``vs.registration.interfaces``::

 class IRegistration(Interface):
     """A folder containing registrants
     """
     contains('vs.registration.interfaces.IRegistrant',)

     registration_key = schema.ASCIILine(title=_(u"Registrant key"),
                                         description=_(u"This should match the registration key used by the booking system"),
                                         required=True)

     ...

 class IRegistrant(Interface):
     """A registrant
     """

     occurrence_key = schema.ASCIILine(title=_(u"Occurrence key"),
                                       description=_(u"This should match the occurrence key used by the booking system"),
                                       required=True)

     ...

Obwohl sie nicht in der ZODB gespeichert werden, werden *Occurrence*- und *Reservation*-Datensätze in Python-Code verarbeitet. Daher werden für beide zunächst ebenfalls Interfaces definiert::

 class IOccurrence(Interface):
     """A single occurrence
     """

     occurrence_key = schema.Int(title=_(u"Occurrence identifier"),
                                 description=_(u"A unique id for this occurrence"),
                               required=True,
                               readonly=True)

     registration = schema.Object(title=_(u"Registration"),
                                  schema=IRegistration
                                  required=True,
                                  readonly=True)

     occurrence_time = schema.Date(title=_(u"Date/time"),
                                   required=True,
                                   readonly=True)

     vacancies = schema.Int(title=_(u"Vacancies"),
                            description=_(u"Vacancies for this Occurrence"))

 class IReservation(Interface):
     """A reservation for a particular occurrence
     """

     customer_name = schema.TextLine(title=_(u"Customer name"),
                                     description=_(u"The name of the customer making the reservation"),
                                     required=True)

     num_reservations = schema.Int(title=_(u"Number of reservations"),
                                   description=_(u""),
                                   required=True,
                                   min=1)


     occurrence = schema.Object(title=_(u"Occurrence"),
                                description=_(u"Occurrence to book for"),
                                schema=IOccurrence,
                                required=True)

Diese Interfaces sind implementiert als einfache Domainklassen, die wir später auf die Datenbanktabellen abbilden.

- ``occurrence.py``::

   class Occurrence(object):
       """A single occurrence.
       """

       implements(IOccurrence)

       occurrence_key = None
       registration = None
       occurrence_time = None
       vacancies = 0

- ``reservation.py``::

   class Reservation(object):
       """A reservation for a particular occurrence
       """

       implements(IReservation)

       customer_name = u""
       num_reservations = 0
       occurrence = None

In diesem Fall wird nicht wie in :doc:`../../archetypes-artikeltypen/index` letztlich abgeleitet von ``persistence.Persistent``, und somit sind die Daten auch nicht in der ZODB verfügbar.

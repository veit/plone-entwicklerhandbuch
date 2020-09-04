=============
Hilfsmethoden
=============

Im weiteren Verlauf sollen Listen der *Occurrences* in die Ansichten des *Registration*-Artikeltyps eingeblendet werden. Angemeldete Nutzer sollen so in der Lage sein, für eine bestimmte *Occurrence* Reservierungen vorzunehmen.

Um jedoch die Views nicht direkt mit der Datenbank kommunizieren zu lassen, werden Hilfsmethoden eingeführt, wobei die Datenbankoperationen abstrahiert werden. Hiermit werden dann auch Tests möglich, die nicht auf eine produktive Datenbank zurückgreifen müssen.

Zunächst werden die Interfaces für die Hilfsmethoden in ``vs.registration.interfaces`` definiert::

 class IRegistrations(Interface):
     """Searches appropriate occurrences
     """

     def registrations_for_registrant(registrant):
         """Return a list of all registrations of a specific registrant as
         list of dictionaries with keys 'registration_key', 'url' and
         'title'.
         """

     def occurrence_by_key(occurence_key):
         """Get an IOccurrence from an occurrence key
         """

 class IReservations(Interface):
     """A utility capable of making reservations
     """

     def __call__(reservation):
         """Make a reservation
         """

Im weiteren Verlauf werden diese Hilfsmethoden dann `implementiert`_ und `Views`_ erstellt, die diese nutzen.

.. _`implementiert`: http://www.veit-schiele.de/dienstleistungen/technische-dokumentation/plone-entwicklerhandbuch/relationale-datenbanken/datenbankabfragen.html
.. _`Views`: http://www.veit-schiele.de/dienstleistungen/technische-dokumentation/plone-entwicklerhandbuch/relationale-datenbanken/views.html

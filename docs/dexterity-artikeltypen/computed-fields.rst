===============
Computed Fields
===============

In unserem speziellen Fall wollen wir aus den zwei Feldern *Vorname* und *Nachname* den Titel unseres *Employee*-Artikeltyps erstellen lassen.

Hierzu erhält die Klasse ``Employee`` die Eigenschaft ``title``, die sich aus den Feldern ``first_name`` und ``surname`` zusammensetzt::

 class Employee(Item):
 """Customised Employee content class"""
     @property
     def title(self):
         if hasattr(self, 'first_names') and hasattr(self, 'surname'):
             return self.first_name + ' ' + self.surname
         else:
             return ''

Generieren der ID
-----------------

Etwas komplexer ist das Erstellen der ID aus einem berechneten Titel::

 from plone.app.content.interfaces import INameFromTitle
 class INameFromEmployeeTitle(INameFromTitle):
     def title():
         """Return a processed title"""

 class NameFromEmployeeTitle(object):
     implements(INameFromEmployeeTitle)

     def __init__(self, context):
         self.context = context

     @property
     def title(self):
         return self.context.first_name + ' ' + self.context.surname

     def setTitle(self, value):
         return

Nun registrieren wir noch einen Adapter für die Dexterity-Interface-Klasse::

 <adapter
     for="vs.registration.employee.ISampleEmployee"
     provides="vs.registration.employee.INameFromEmployeeTitle"
     factory="vs.registration.employee.NameFromEmployeeTitle"
 />

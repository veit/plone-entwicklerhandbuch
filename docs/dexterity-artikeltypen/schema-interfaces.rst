=================
Schema Interfaces
=================

Für unsere Registrierungssoftware erstellen wir zunächst den Artikeltyp *Attendee* in ``attendee.py``::

 from five import grok
 from zope import schema

 from plone.directives import form, dexterity

 from plone.app.textfield import RichText
 from plone.namedfile.field import NamedImage

 from vs.registration import _

 class IAttendee(form.Schema):
     """An attendee for the event.
     """

     title = schema.TextLine(
             title=_(u"Name"),
         )

     description = schema.Text(
             title=_(u"A short summary"),
         )

``from vs.registration import _``
 importiert die *Message Factory* aus der ``__init__.py``-Datei::

   from zope.i18nmessageid import MessageFactory
   _ = MessageFactory("vs.registration")

Die Ereignisse, für die die Anmeldungen erfolgen können, werden in ``registration.py`` definiert::

 from five import grok
 from zope import schema

 from plone.directives import form, dexterity
 from plone.app.textfield import RichText

 from vs.registration import _

 class IRegistration(form.Schema):
     """A registration container for attendees.
     """

     title = schema.TextLine(
             title=_(u"Event name"),
         )

     description = schema.Text(
             title=_(u"Event summary"),
         )

     start = schema.Datetime(
             title=_(u"Start date"),
             required=False,
         )

     end = schema.Datetime(
             title=_(u"End date"),
             required=False,
         )

     details = RichText(
             title=_(u"Details"),
             description=_(u"Details about the event"),
             required=False,
         )

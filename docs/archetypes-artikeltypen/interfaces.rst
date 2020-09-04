==========
Interfaces
==========

Interfaces können als formale Dokumentation der Fähigkeiten eines Artikeltyps betrachtet werden.

Folgende Interfaces beschreiben z.B. Registrierungen und die darin enthaltenen registrierten Personen in ``myproject/src/vs.registration/vs/registration/interfaces.py``::

 from zope.interface import Interface
 from zope import schema

 from zope.app.container.constraints import contains

 class IRegistration(Interface):
     """A folder containing registrants
     """
     contains('vs.registration.interfaces.IRegistrants',)

     text = schema.SourceText(title=_(u"Descriptive text"),
                              description=_(u"Descriptive text about this registration"),
                              required=True)

 class IRegistrant(Interface):
     """A registrant
     """

     name = schema.TextLine(title=_(u"Registrant name"),
                            required=True)

     address = schema.Text(title=_(u"Address"),
                           description=_(u""),
                           required=True)

     email = schema.TextLine(title=_(u"Email"),
                             description=_(u""),
                             required=True)

Im Gegensatz zu ``zope.formlib`` nutzt Archetypes die angegebenen Titel und Beschreibungen nicht, dennoch sind die Angaben meines Erachtens nützlich um leicht den  Funktionsumfang der Artikeltypen erkennen zu können.

Einen Überblick über die verschiedenen Feldtypen erhalten Sie in `zope.schema.interfaces`_.

Damit die Feldattribute übersetzt werden können, wird folgendes in ``src/vs.registration/vs/registration/__init__.py`` eingetragen::

 from zope.i18nmessageid import MessageFactory
 RegistrationMessageFactory = MessageFactory('vs.registration')

Und in ``src/vs.registration/vs/registration/interfaces.py``::

 from vs.registration import RegistrationMessageFactory as _

.. _`zope.schema.interfaces`: http://svn.zope.de/zope.org/zope.schema/trunk/src/zope/schema/interfaces.py

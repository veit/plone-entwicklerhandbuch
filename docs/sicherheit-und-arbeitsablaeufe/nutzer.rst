======
Nutzer
======

Plone 4 ermöglicht mit `plone.app.users`_ neue Felder zum Registrieren an der Website und den persönlichen Einstellungen hinzuzufügen.

.. _`plone.app.users`: http://pypi.python.org/pypi/plone.app.users

Überschreiben des bestehenden Schemas
=====================================

Das Standardschema von ``plone.app.users`` ist in einem Hilfsprogramm (*Utility*) definiert, das überschrieben werden muss um ein neues Schema anzulegen. Dies geschieht in der Datei ``profiles/default/componentregistry.xml``::

 <?xml version="1.0"?>
 <componentregistry>
   <utilities>
     <utility
       interface="plone.app.users.userdataschema.IUserDataSchemaProvider"
       factory="vs.policy.userdataschema.UserDataSchemaProvider"
     />
   </utilities>
 </componentregistry>

Nun wird die *factory* in ``userdataschema.py`` erstellt::

 from plone.app.users.userdataschema import IUserDataSchemaProvider

 class UserDataSchemaProvider(object):
     implements(IUserDataSchemaProvider)

     def getSchema(self):
         """
         """
         return IEnhancedUserDataSchema

Schließlich wird eine Unterklasse des Standardschemas ``IUserDataSchema`` erstellt::

 from plone.app.users.userdataschema import IUserDataSchema

 class IEnhancedUserDataSchema(IUserDataSchema):
     """ Use all the fields from the default user data schema, and add various
     extra fields.
    """

Hinzufügen neuer Felder
=======================

Nun können neue Felder definiert werden, z.B.::

 newsletter = schema.Bool(
     title=_(u'label_newsletter', default=u'Subscribe to newsletter'),
     description=_(u'help_newsletter',
                   default=u"If you tick this box, we'll subscribe you to "
                     "our newsletter."),
     required=False,
     )

Bedingungen
-----------

Felder mit Bedingungen für eine erfolgreiche Anmeldung können als ``constraint`` angegeben werden, z.B.::

 def validateAccept(value):
     if not value == True:
         return False
     return True

 class IEnhancedUserDataSchema(IUserDataSchema):
     # ...
     accept = schema.Bool(
         title=_(u'label_accept', default=u'Accept terms of use'),
         description=_(u'help_accept',
                       default=u"Tick this box to indicate that you have found,"
                       " read and accepted the terms of use for this site. "),
         required=True,
         constraint=validateAccept,
         )

Eigenschaften
=============

Neue Eigenschaften lassen sich in den *memberdata properties* speichern indem eine Datei ``memberdata_properties.xml`` in ``profiles/default/`` erstellt wird. Dabei werden alle Felder hinzugefügt bis auf das ``accept``-Feld, das zwingend für die Registrierung erforderlich ist::

 <?xml version="1.0"?>
 <object name="portal_memberdata" meta_type="Plone Memberdata Tool">
 <property name="subscribe_newsletter" type="boolean"></property>
 </property>
 </object>

Registrierung
=============

Die Felder für die Registrierung werden in ``profiles/default/propertiestool.xml`` angegeben::

 <?xml version="1.0"?>
 <object name="portal_properties" meta_type="Plone Properties Tool">
  <object name="site_properties" meta_type="Plone Property Sheet">
   <property name="user_registration_fields" type="lines">
    <element value="newsletter" />
    <element value="accept" />
   </property>
  </object>
 </object>

Persönliche Informationen
=========================

Um die Felder auch im Formular mit den persönlichen Informationen ``@@personal-information``  zu sehen, wird zunächst der Adapter des Nutzerobjekts in der ``overrides.zcml`` überschrieben::

 <configure
     xmlns="http://namespaces.zope.org/zope"
     i18n_domain="vs.policy.userdata">
   <adapter
     provides=".userdataschema.IEnhancedUserDataSchema"
     for="Products.CMFCore.interfaces.ISiteRoot"
     factory=".adapter.EnhancedUserDataPanelAdapter"
     />
 </configure>

Anschließend müssen leider die Felder nochmals angegeben werden. Hierzu fügen wir ``adapter.py`` hinzu mit::

 from plone.app.users.browser.personalpreferences import UserDataPanelAdapter

 class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
     """
     """
     def get_newsletter(self):
         return self.context.getProperty('newsletter', '')
     def set_newsletter(self, value):
         return self.context.setMemberProperties({'newsletter': value})
     newsletter = property(get_newsletter, set_newsletter)

     def get_accept(self):
         return self.context.getProperty('accept', '')
     def set_accept(self, value):
         return self.context.setMemberProperties({'accept': value})
     accept = property(get_accept, set_accept)

Zum Weiterlesen
===============

`Member manipulation <http://developer.plone.org/members/member_basics.html>`_
    Getting logged-in member, any member and member information
`collective.examples.userdata <http://pypi.python.org/pypi/collective.examples.userdata>`_
    Python-Egg mit Beispielen, wie das Schema der Nutzerdaten erweitert werden
    kann.

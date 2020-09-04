=============
Lokale Rollen
=============

Seit Plone 4.0 lassen sich Rollen mit dem GenericSetup-Profil ``sharing.xml`` für die *Freigabe*-Ansicht konfigurieren.

Lokale Rollen erstellen
=======================

Im folgenden Beispiel wird die Rolle *Event-Manager* erstellt::

 <?xml version="1.0"?>
 <sharing xmlns:i18n="http://xml.zope.org/namespaces/i18n"
          i18n:domain="vs.policy">
   <role
       id="Event-Manager"
       title="Manages the registrations for events"
       permission="Add Registration"
       i18n:attributes="title"
       />
 </sharing>

Lokale Rollen überschreiben
===========================

Soll z.B. die Rolle *Reviewer* an die Berechtigung *Modify portal content* geknüpft werden, so kann dies mit folgendem Eintrag geschehen::

   <role
       id="Reviewer"
       title="Review submitted articles"
       permission="Modify portal content"
       i18n:attributes="title"
       />

Lokale Rollen löschen
=====================

::


 <role
   remove="True"
   id="Reviewer"
   />

Hinzufügen einer Rolle zum *Freigabe*-Reiter
============================================

Um  eine Rolle der Tabelle im *Freigabe*-Reiter hinzuzufügen kann einfach
ein entsprechendes GenericSetup-Profil ``sharing.xml`` erstellt werden,
z.B.::

    <sharing xmlns:i18n="http://xml.zope.org/namespaces/i18n"
             i18n:domain="plone">
      <role
          id="Site Manager"
          title="Is a site coordinator"
          permission="Manage portal"
          i18n:attributes="title"
          />
    </sharing>

The title is the name to be shown on the sharing page. The required_permission is optional. If given, the user must have this permission to be allowed to manage the particular role.

Siehe auch
==========

- `Local roles <http://docs.plone.org/develop/plone/security/local_roles.html>`_

Plone 3
=======

#. Zunächst wird in der ``permissions.py``-Datei die Rolle für die Ansicht im *Freigabe*-Reiter registriert und die Rolle angegeben, auf der unsere neue Rolle basieren soll::

    from Products.CMFCore.permissions import setDefaultRoles
    from AccessControl import ModuleSecurityInfo

    security = ModuleSecurityInfo('vs.policy')

    security.declarePublic('MyRole')
    MyRole = 'Sharing page: My Role'
    setDefaultRoles(MyRole, ('Reviewer',))

#. Dann wird die Rolle für die *Freigabe*-Seiten registriert in ``localroles.py``::

    from zope.interface import implements
    from plone.app.workflow.interfaces import ISharingPageRole

    import permissions

    class ManagerRole(object):
        implements(ISharingPageRole)

        title = u'My Role'
        required_permission = permissions.MyRole

#. Schließlich wird in der ``configure.zcml``-Datei die entsprechende Berechtigung angelegt::

    <permission
        id="plone.MyRole"
        title="Sharing page: My Role"
        />

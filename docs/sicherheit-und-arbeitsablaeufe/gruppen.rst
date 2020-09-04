=======
Gruppen
=======

Um neue Gruppen programmatisch hinzuzufügen, erstellen wir in der
``setuphandlers.py``-Datei die Methode ``setupGroups``, die sowohl den Pluggable
Authentication Service (PAS) als auch das ``portal_groups``-Tool verwendet::

    import plone.api
    def setupGroups(portal):
        acl_users = plone.api.portal.get_tool('acl_users')
        if not acl_users.searchGroups(name='Staff'):
            gtool = getToolByName(portal, 'portal_groups')
            gtool.addGroup('Staff', roles=['StaffMember'])
    def importVarious(context):
        """Miscellanous steps import handle
        """
        if context.readDataFile('vs.policy-various.txt') is None:
           return
        portal = context.getSite()
        setupGroups(portal)

Für Plone ≤ 4.2 steht `plone.api <https://pypi.python.org/pypi/plone.api>`_ noch
nicht zur Verfügung. Stattdessen muss noch ``getToolByName`` verwendet werden::

    from Products.CMFCore.utils import getToolByName
    def setupGroups(portal):
        acl_users = getToolByName(portal, 'acl_users')
        if not acl_users.searchGroups(name='Staff'):
            gtool = getToolByName(portal, 'portal_groups')
            gtool.addGroup('Staff', roles=['StaffMember'])
    …

Tests
=====

::

    def test_staffmember_group_added(self):
        portal = self.layer['portal']
        acl_users = portal['acl_users']
        self.assertEqual(1,
            len(acl_users.searchGroups(name='Staff')))

========================================
Rechte, Rollen und Arbeitsabläufe testen
========================================

::

    def test_role_added(self):
        portal = self.layer['portal']
        self.assertTrue("StaffMember" in portal.validRoles())
    def test_workflow_installed(self):
        portal = self.layer['portal']
        workflow = getToolByName(portal, 'portal_workflow')
        self.assertTrue('vs_sitecontent_workflow' in workflow)
    def test_workflows_mapped(self):
        portal = self.layer['portal']
        workflow = getToolByName(portal, 'portal_workflow')
        self.assertEqual(('vs_sitecontent_workflow',),
            workflow.getDefaultChain())
    def test_view_permisison_for_staffmember(self):
        portal = self.layer['portal']
        self.assertTrue('View' in [r['name']
            for r in portal.permissionsOfRole('Reader')
            if r['selected']])
        self.assertTrue('View' in [r['name']
            for r in portal.permissionsOfRole('StaffMember')
            if r['selected']])
    def test_staffmember_group_added(self):
        portal = self.layer['portal']
        acl_users = portal['acl_users']
        self.assertEqual(1,
            len(acl_users.searchGroups(name='Staff')))

.. Um die Rechte, Rollen und Arbeitsabläufe zu testen, werden die entsprechenden Tests in  ``src/vs.registration/vs/registration/tests/test_setup.py`` hinzugefügt::

        import unittest
        from vs.registration.tests.base import RegistrationTestCase

        from Products.CMFCore.utils import getToolByName

        class TestSetup(RegistrationTestCase):

            def afterSetUp(self):
                self.workflow = getToolByName(self.portal, 'portal_workflow')
                self.acl_users = getToolByName(self.portal, 'acl_users')
                self.types = getToolByName(self.portal, 'portal_types')

            def test_workflows_installed(self):
                self.failUnless('registrant_workflow' in self.workflow.objectIds())
                self.failUnless('registration_workflow' in self.workflow.objectIds())

            def test_workflows_mapped(self):
                for portal_type, chain in self.workflow.listChainOverrides():
                    if portal_type in ('Registration',):
                        self.assertEquals(('registration_workflow',), chain)
                for portal_type, chain in self.workflow.listChainOverrides():
                    if portal_type in ('Registrant',):
                        self.assertEquals(('registrant_workflow',), chain)

            def test_view_permisison_for_staffmember(self):
                # The API of the permissionsOfRole() function sucks - it is bound too
                # closely up in the permission management screen's user interface
                self.failUnless('View' in [r['name'] for r in
                                        self.portal.permissionsOfRole('Reader') if r['selected']])

        def test_suite():
            suite = unittest.TestSuite()
            suite.addTest(unittest.makeSuite(TestSetup))
            return suite

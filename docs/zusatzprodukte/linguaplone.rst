===========
LinguaPlone
===========

Um `LinguaPlone`_ ordnungsgemäß in einer Plone-Site aktivieren zu können, muss folgende Reihenfolge eingehalten werden:

#. Zunächst muss die Sprachauswahl im *Plone Language Tool* angegeben werden.
#. Erst im Anschluss daran kann LinguaPlone installiert werden.
#. Und schließlich wird der ``@@language-setup-folders``-View von LinguaPlone aufgerufen um auch das Site-Root-Objekt mehrsprachig darzustellen.

.. _`LinguaPlone`: http://pypi.python.org/pypi/Products.LinguaPlone/

Programmatisch lässt sich dies realisieren, indem in  ``vs.policy/vs/policy/setuphandlers.py`` zunächst die Spracheinstellungen gesetzt werden, anschließend LinguaPlone aktiviert und der View ``@@language-setup-folders`` aufgerufen wird::

 def installLinguaPlone(site):

      # LP must be installed a last step in order to deal with
      # several strange annoyances and expecations that LP relies on.

     pl = getToolByName(site, 'portal_languages')
     pl.supported_langs = ('de', 'en')

     qi = getToolByName(site, 'portal_quickinstaller')
     qi.installProducts(['Products.LinguaPlone'])

     transaction.savepoint(1)#
     site.restrictedTraverse('@@language-setup-folders')()

 …

 def setupVarious(context):
     if context.readDataFile('ise.policy_various.txt') is None:
         return
     …
     installLinguaPlone(site)

Tests
=====

In ``test_language_settings.py`` können folgende Tests geschrieben werden::

 import unittest2
 from base import TestBase

 class LanguageTests(TestBase):
     def testInstalledProducts(self):
         …
         self.assertEqual('LinguaPlone' in installed, True)

     def testLanguageSettings(self):
         lang_tool = self.portal.portal_languages
         default_language = self.portal.portal_languages.getDefaultLanguage()
         self.assertEqual(default_language == 'de', True)
         # return [(country code, countryname), ...]
         supported_languages = [r[0] for r in self.portal.portal_languages.listSupportedLanguages()]
         self.assertEqual('en' in supported_languages, True)
         self.assertEqual('de' in supported_languages, True)
         self.assertEqual(lang_tool.use_cookie_negotiation, True)
         self.assertEqual(lang_tool.use_request_negotiation, True)
         self.assertEqual(lang_tool.use_content_negotiation, True)

 def test_suite():
     from unittest2 import TestSuite, makeSuite
     suite = TestSuite()
     suite.addTest(makeSuite(LanguageTests))
     return suite

TinyMCE-Erweiterungen
=====================

Sollen sprachneutrale Inhalte wie z.B. Bilder erstellt werden, sollte TinyMCE so gepatcht werden, dass er über die sprachspezifischen Ordner hinaus referenzieren kann. Dies lässt sich am einfachsten realisieren mit `collective.monkeypatcher`_.

.. _`collective.monkeypatcher`: http://pypi.python.org/pypi/collective.monkeypatcher

Anschließend erweitern wir unsere ``configure.zcml``-Datei um ``patches.zcml``::

 <include file="patches.zcml" />

Nun legen wir  ``patches.zcml`` mit folgendem Inhalt an::

 <configure
     xmlns="http://namespaces.zope.org/zope"
     xmlns:monkey="http://namespaces.plone.org/monkey"
     i18n_domain="vs.policy">

     <include package="collective.monkeypatcher" />

     <monkey:patch
         description="TinyMCE JSON Folder listing should ignore INavigationRoot"
         class="Products.TinyMCE.adapters.JSONFolderListing.JSONFolderListing"
         original="getListing"
         replacement=".patches.getListing"
         />

     <monkey:patch
         description="Navigation support RefBrowserWidget across INavigationRoot"
         class="archetypes.referencebrowserwidget.browser.view.ReferenceBrowserPopup"
         original="breadcrumbs"
         replacement=".patches.breadcrumbs"
         />

    <monkey:patch
         description="Unrestrict TinyMCE image search"
         class="Products.TinyMCE.adapters.JSONSearch.JSONSearch"
         original="getSearchResults"
         replacement=".patches.getSearchResults"
         />
 </configure>

Schließlich schreiben wir noch die Datei :download:`patches.py`, die die Originalklassen mit den entsprechenden Änderungen enthält.

==================
Inhalte übersetzen
==================

LinguaPlone
===========

`LinguaPlone`_ ist ein Produkt, das mehrsprachige **Inhalte** in einer Plone-Site ermöglicht. Um LinguaPlone verwenden zu können, müssen zunächst mehrere Sprachen im `Plone Language Tool`_ ausgewählt worden sein, für das ein Profil mit der Datei ``portal_languages.xml`` angelegt werden kann. Diese sieht z.B. so aus::

 <?xml version="1.0"?>
 <object name="portal_languages">
  <default_language value="de"/>
  <use_cookie_negotiation value="True"/>
  <use_content_negotiation value="True"/>
  <use_request_negotiation value="True"/>
  <display_flags value="False"/>
  <start_neutral value="False"/>
  <supported_langs>
    <element value="en"/>
    <element value="de"/>
  </supported_langs>
 </object>

Anschließend sollte der View ``/@@language-setup-folders`` aufgerufen werden, damit auch die Startseite für beide Sprachen zur Verfügung gestellt werden kann. Dieser View liefert dann folgende Ausgabe::

 Setup of language root folders on Plone site 'mysite'
 Added 'en' folder: en
 INavigationRoot setup on folder 'en'
 Added 'de' folder: de
 INavigationRoot setup on folder 'de'
 Translations linked.
 Portal default page removed.
 Moved default page 'front-page' to folder 'de'.
 Root language switcher set up.

Der View strukturiert die Site in folgenden Schritten um:

#. Zunchst wird für jede der angegebenen Sprachen ein Ordner erstellt.
#. Jeder dieser Ordner wird an das ``INavigationRoot``-Interface gebunden.
#.  Nun werden die entsprechenden Verlinkungen zwischen diesen Ordnern für die Übersetzung erstellt.
#. Anschließend wird die Standardseite in den Ordner verschoben, dessen Sprache sie zugeordnet ist.
#. Schließlich wird der *root language switcher* aufgesetzt um vom ``ISiteRoot``-Objekt auf den Ordner der Standardsprache umzuleiten.

Programmatisch kann dies in der ``setuphandlers.py``-Datei geschehen::

 import transaction
 ...
 class Generator:

     def configureLinguaPlone(self, portal):

         pl = getToolByName(portal, 'portal_languages')
         pl.supported_langs = ('de', 'en')

         transaction.savepoint(1)
         portal.restrictedTraverse('@@language-setup-folders')()

 def setupVarious(context):
     ...
     gen.configureLinguaPlone(site)

TinyMCE für sprachneutrale Inhalte
==================================

Werden sprachneutrale Inhalte in mehreren Sprachen benötigt, z.B. für Bilder, so kann es sich empfehlen, einen Ordner mit diesen Inhalten auf derselben Ebene wie die Sprachenordner anzulegen.

Damit nun die Bilder in diesem Ordner auch aus dem Popup-Fenster von TinyMCE eingebunden werden können, erstellen wir einen MonkeyPatch mit `collective.monkeypatcher`_. Zunächst wird folgendes  in die ``configure.zcml``-Datei eingetragen::

 <configure
     ...
     xmlns:monkey="http://namespaces.plone.org/monkey">
 ...
     <monkey:patch
         description="TinyMCE JSON Folder listing should ignore INavigationRoot"
         class="Products.TinyMCE.adapters.JSONFolderListing.JSONFolderListing"
         original="getListing"
         replacement=".patches.getListing"
         />

.. _`collective.monkeypatcher`: http://pypi.python.org/pypi/collective.monkeypatcher

Anschließend erstellen wir die ``patches.py``-Datei mit der Methode ``getListing``. Diese ist übernommen aus ``Products.TinyMCE.adapters.JSONFolderListing.py`` mit folgender Änderung::

 68c68,69
 < if INavigationRoot.providedBy(object) or (rooted == "True" and document_base_url[:-1] == object.absolute_url()):
 ---
 > #if INavigationRoot.providedBy(object) or (rooted == "True" and document_base_url[:-1] == object.absolute_url()):
 > if (rooted == "True" and document_base_url[:-1] == object.absolute_url()):

ReferenceBrowserWidget für sprachneutrale Inhalte
=================================================

Damit auch sprachneutrale Referenzen eingebunden werden können, muss auch für das ReferenceBrowserWidget ein MonkeyPatch bereitgestellt werden. Zunächst wird dieser registriert in der ``configure.zcml``::

 <monkey:patch
     description="Navigation support for the ReferenceBrowserWidget across INavigationRoot"
     class="archetypes.referencebrowserwidget.browser.view.ReferenceBrowserPopup"
     original="breadcrumbs"
     replacement=".patches.breadcrumbs"
     />

Nun wird in ``patches.py` die Methode ``breadcrumbs`` kopiert aus ``archetypes.referencebrowserwidget.browser.view.ReferenceBrowserPopup`` und folgendermaßen abgeändert::

 12c14,21
 <                     portal_state.navigation_root_url())}]
 ---
 >                     portal_state.portal_url())}]
 >
 > if portal_state.portal_url() != portal_state.navigation_root_url():
 >     nav_root_path = portal_state.navigation_root_path()
 >     nav_root = self.context.restrictedTraverse(nav_root_path)
 >     newcrumbs.append({'Title': nav_root.Title(),
 >                   'absolute_url': self.genRefBrowserUrl(
 >                         portal_state.navigation_root_url())})

Mehrsprachige Inhaltstypen erstellen
------------------------------------

Wollen Sie LinguaPlone mit ihren eigenen Inhaltstypen verwenden, werden die Klassen und Methoden nicht direkt von Archetypes importiert, sondern es wird zunächst versucht, sie von LinguaPlone zu übernehmen::

 try:
     from Products.LinguaPlone.public import *
 except ImportError:
     # No multilingual support
     from Products.Archetypes.public import *

Sprachunabhängige Felder
------------------------

Sprachunabhängige Felder, z.B. für Namen und Datum, werden vom Originalartikel (*canonical item*) übernommen. Die Werte werden jedoch in jedem übersetzten Artikel gespeichert, sodass jeder Artikel jedes Attribut enthält und damit aus dem Kontext verschoben oder direkt referenziert werden können.

Die Sprachunabhängigkeit wird für ein Feld in der AT-Schemadefinition angegeben mit ``languageIndependent=1``.

Sprachauswahl
-------------

Beim ersten Aufruf einer LinguaPlone-Site wird der Header ``HTTP_ACCEPT_LANGUAGE``, der vom Browser gesendet wird, verwendet, um zu entscheiden, welche Sprache verwendet wird. Anschließend wird ein Cookie mit dieser Entscheidung zurückgesendet. Diese Sprache wird dann solange verwendet, bis vom Nutzer explizit eine andere Sprache in der Plone-Site ausgewählt wird – dann wird auch der Cookie aktualisiert. Steht an einer anderen Stelle der Site ein Artikel nicht in der gewünschten Sprache zur Verfügung, wird eine Seite mit den verfügbaren Sprachen angezeigt.

Sprachspezifische Suche
-----------------------

LinguaPlone filtert in der Suche für alle Artikeltypen, die verschiedene Sprachen unterscheiden, diejenigen heraus, die nicht der Sprachauswahl entsprechen.

Soll in allen verfügbaren Sprachen gesucht werden, kann in der Suche ``Language=all`` angegeben werden.

Weitere Module
==============

Mit `slc.linguatools`_ und `raptus.multilanguagefields`_ stehen noch zwei weitere Werkzeuge für mehrsprachige Inhalte in Plone zur Verfügung.

.. _`LinguaPlone`: http://plone.org/products/linguaplone
.. _`Plone Language Tool`: http://www.veit-schiele.de/dienstleistungen/technische-dokumentation/plone-entwicklerhandbuch/internationalisierung/internationalisieren-des-user-interfaces.html
.. _`slc.linguatools`: http://pypi.python.org/pypi/slc.linguatools/
.. _`raptus.multilanguagefields`: http://pypi.python.org/pypi/raptus.multilanguagefields

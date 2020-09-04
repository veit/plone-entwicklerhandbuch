===========================
Views und browser resources
===========================

Nachdem die Artikeltypen mit ihrem jeweiligen Schema erstellt wurden, gehen wir
nun zum User-Interface über, dessen Code sich im ``browser``-Paket befindet.

Icons und Stylesheet-Dateien
============================

Für jeden Artikeltyp wird ein eigenes Icon definiert in
``browser/configure.zcml``, in unserem Fall::

 <browser:resource
    name="registration_icon.gif"
    image="registration_icon.gif"
    />

Dieses Icon kann referenziert werden mit ``++resource++registration_icon.gif``.
Um das Icon innerhalb eines Page Templates aufzurufen, können Sie folgendes
angeben::

 <img tal:attributes="src context/++resource++registration_icon.gif" />

Dem Icon analog lässt sich auch ein Stylesheet-Dokument hinzufügen mit::

 <browser:resource
    name="registration.css"
    file="registration.css"
    />

Diese Datei können Sie mit folgendem Code in ein Page Template einfügen::

 <metal:css fill-slot="css_slot">
     <style type="text/css" media="all"
            tal:content="string: @import url(${context/++resource++registration.css});"></style>
 </metal:css>

Views
=====

Auch die Views werden in ``browser/configure.zcml`` registriert::

 <browser:page
     for="..interfaces.IRegistration"
     name="view"
     class=".registration.RegistrationView"
     permission="zope2.View"
     />

Üblicherweise wird die Standardansicht eines Artikeltyps mit ``@@view``
aufgerufen.

Sollen Autoren zwischen verschiedenen Ansichten eines Artikeltyps in Plones
Ansicht-Menü wählen können, müssen diese Ansichten einerseits in einer Liste im
GenericSetup-Profil angegeben werden, andererseits jedoch auch in
``browser/configure.zcml`` registriert werden::

 <include package="plone.app.contentmenu" />
 ...
 <browser:menuItem
     for="..interfaces.IRegistration"
     menu="plone_displayviews"
     title="Registration view"
     action="@@view"
     description="Default view of a registration"
     />

``action`` verweist auf den Namen der Ansicht, wobei der Menüeintrag nur für das
``IRegistration``-Interface angezeigt wird.

Die View-Klasse selbst enthält die Methoden ``name`` und ``details``::

 from Products.Five import BrowserView

 class RegistrationView(BrowserView):
    """A view of a Registration object"""
    def name(self):
        return self.context.Title()

    def details(self):
        return self.context.Description()

Der Decorator ``@memoize`` stellt sicher, dass der Aufruf in einer Instanz nur einmal ausgeführt wird – und der zurückgegebene Wert gespeichert wird. Wenn Templates eine Methode mehrfach aufrufen, kann so die Performance deutlich gesteigert werden (s.a. `Memoize <../produktivserver/caching/memoize.html>`_). Das Template ``registration.pt`` sieht dann so aus::

 <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"
       xmlns:tal="http://xml.zope.org/namespaces/tal"
       xmlns:metal="http://xml.zope.org/namespaces/metal"
       xmlns:i18n="http://xml.zope.org/namespaces/i18n"
       lang="en"
       metal:use-macro="context/main_template/macros/master"
       i18n:domain="vs.registration">
 <body>

 <metal:main fill-slot="main">
     <tal:main-macro metal:define-macro="main"
            tal:define="text context/text;">

         <div tal:replace="structure provider:plone.abovecontenttitle" />

         <h1 class="documentFirstHeading">
             <span metal:use-macro="python:context.widget('title', mode='view')" />
         </h1>

         <div tal:replace="structure provider:plone.belowcontenttitle" />

         <div class="documentDescription">
             <span metal:use-macro="python:context.widget('description', mode='view')" />
         </div>

         <div tal:replace="structure provider:plone.abovecontentbody" />

         <p tal:condition="python: not text and is_editable"
            i18n:translate="no_body_text"
            class="discreet">
             This item does not have any body text, click the edit tab to change it.
         </p>

         <div tal:condition="text" metal:use-macro="python:context.widget('text', mode='view')" />

         <form action="createObject">
             <input name="type_name"
                    type="hidden"
                    value="Registrant"
                    />
             <input class="standalone"
                    value="Registration"
                    type="submit"
                    i18n:attributes="value"
                    />
         </form>

         <tal:registrants condition="view/have_registrants">
             <h2 i18n:translate="title_registration_contents">Registrants</h2>
             <dl>
                 <tal:block repeat="registrant view/registrants">
                     <dt>
                         <a tal:attributes="href registrant/url"
                            tal:content="registrant/title" />
                     </dt>
                     <dd tal:content="registrant/address" />
                 </tal:block>
             </dl>
         </tal:registrants>

         <div metal:use-macro="context/document_relateditems/macros/relatedItems">
             show related items if they exist
         </div>

         <div tal:replace="structure provider:plone.belowcontentbody" />

     </tal:main-macro>
 </metal:main>

 </body>
 </html>

Das Template entspricht weitgehend Plones ``document_view.pt``.

Beachten Sie, dass verschiedene Viewlet-Manager angegeben wurden, wie z.B.::

 <div tal:replace="structure provider:plone.abovecontenttitle" />

Im Kapitel `Viewlets <../erscheinungsbild/viewlets>`_ wird ausführlich auf diese
Zope3-Komponenten eingegangen.

Content-Menü
------------

Üblicherweise wird das Content-Menü mit den Menüs *Darstellung, *Hinzufügen* und
*Workflow* in Views nicht angezeigt. Falls es dennoch angezeigt werden soll,
müssen Sie das ``IViewView``-Interface aus ``plone.app.layout`` erhalten::

    from zope.interface import implements
    from Products.Five.browser import BrowserView
    from plone.app.layout.globals.interfaces import IViewView

    class MyView(BrowserView):
       implements(IViewView)

Inline Editing
--------------

In diesem Template wurde auch das Inline-Editing mit Kinetic Style Sheets
ermöglicht, z.B. mit::

 <span metal:use-macro="python:context.widget('title', mode='view')" />

Soll ein Feld nicht direkt editiert werden können, genügt ein einfacheres
Konstrukt::

 <span tal:content="context/title" />

Mehr über das JavaScript-Framework erfahren Sie im Kapitel
:doc:`../erscheinungsbild/kinetic-style-sheet/index`.

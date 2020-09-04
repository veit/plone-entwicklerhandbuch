=====
Views
=====

Üblicherweise werden die benötigten Views zum Editieren und Ansehen der Artikel automatisch generiert. Falls diese Ansichten geändert werden sollen kann dies mittels ``five.grok`` einfach geschehen, indem z.B. in ``registration.py`` ein View erstellt werden mit::

 from Acquisition import aq_inner
 from Products.CMFCore.utils import getToolByName

 from vs.registration.attendee import IAttendee

 class View(grok.View):
     grok.context(IRegistration)
     grok.require('zope2.View')

     def attendees(self):
         """Return a catalog search result of attendees to show
         """

         context = aq_inner(self.context)
         catalog = getToolByName(context, 'portal_catalog')
         return catalog(object_provides=IAttendee.__identifier__,
                        path='/'.join(context.getPhysicalPath()),
                        sort_on='sortable_title')

``class View``
 Der Klassenname wird umgewandelt in Kleinbuchstaben und biltet dann den Namen des Views, in unserem Fall ``@@view``.

 Ggf. kann mit ``grok.name('other-name')`` ein anderer Klassenname vergeben werden.

``grok.context()``
 Diese Anweisung spezifiziert, dass der View in Artikeln mit dem ``ÌRegistration``-Interface verwendet wird.

 Soll zusätzlich ein Browser-Layer spezifiziert werden, so kann dies mit der ``grok.layer()``-Anweisung erfolgen.

``grok.require()``
 Diese Anweisung spezifiziert die erforderliche Berechtigung zur Anzeige dieses Views.

 Es wird der Zope3-Deklaration verwendet.

 ``zope2.View`` und ``zope.Public`` sind die am häufigsten verwendeten Berechtigungen. Eine Liste weiterer Berechtigungen finden Sie z.B. in ``parts/omelette/Products/Five/permissions.zcml``.

Anschließend kann auf derselben Ebene wie ``registration.py`` ein Ordner ``registration_templates`` und darin die Datei ``view.pt`` erstellt werden::

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
         tal:define="toLocalizedTime nocall:context/@@plone/toLocalizedTime">

         <div tal:replace="structure provider:plone.abovecontenttitle" />

         <h1 class="documentFirstHeading" tal:content="context/title" />

         <div class="discreet">
             <tal:block condition="context/start">
                 <span i18n:translate="label_from">From:</span>
                 <span tal:content="python:context.start.strftime('%x %X')" />
             </tal:block>
             <tal:block condition="context/end">
                 <span i18n:translate="label_to">To:</span>
                 <span tal:content="python:context.end.strftime('%x %X')" />
             </tal:block>
         </div>

         <div tal:replace="structure provider:plone.belowcontenttitle" />

         <p class="documentDescription" tal:content="context/description" />

         <div tal:replace="structure provider:plone.abovecontentbody" />

         <h2 i18n:translate="heading_attendees">Attendees</h2>
         <dl>
             <tal:block repeat="attendee view/attendees">
                 <dt>
                     <a tal:attributes="href attendee/getURL"
                        tal:content="attendee/Title" />
                 </dt>
                 <dd tal:content="attendee/Description" />
             </tal:block>
         </dl>

         <div tal:replace="structure provider:plone.belowcontentbody" />

     </tal:main-macro>
 </metal:main>

 </body>
 </html>

.. note::
    Damit im Feld mit dem visuellen Editor die HTML-Tags nicht ausgefiltert weren, muss hier die Angabe ``/output`` angegeben werden.

.. seealso::
    * `Asko Soukka: Create custom views for Dexterity-types TTW <http://datakurre.pandala.org/2013/01/create-custom-views-for-dexterity-types.html>`_

=================
Portlet erstellen
=================

Portlet mit *Site Actions* erstellen
====================================

Für dieses Portlet erstellen wir ein Unterpaket entsprechend den Konventionen in ``plone.app.portlets``. Für unser ``Site-Actions``-Portlet wird das Page Template ``siteactions.pt`` im Ordner ``portlets`` erstellt::

 <dl class="portlet portletSiteActions"
     i18n:domain="vs.theme">

     <dt class="portletHeader">
         <span class="portletTopLeft"></span>
         Site Actions
         <span class="portletTopRight"></span>
     </dt>

     <tal:actions tal:define="accesskeys python: {'sitemap' : '3', 'accessibility' : '0', 'contact' : '9'};"
                  tal:condition="view/site_actions">
         <dd class="portletItem"
             tal:repeat="saction view/site_actions"
             tal:attributes="id string:siteaction-${saction/id}">
             <a href=""
                tal:define="title saction/title;
                            id saction/id;
                            accesskey python: accesskeys.get(id, '');"
                i18n:attributes="title"
                i18n:translate=""
                tal:content="title"
                tal:attributes="href saction/url;
                                target saction/link_target|nothing;
                                title title;
                                accesskey accesskey;"
             >Site action</a>
         </dd>
     </tal:actions>
 </dl>

Dies entspricht dem Aufbau der meisten Plone-Portlets. Dabei ist die
Darstellungslogik, welche ``siteactions`` angezeigt werden, in den View
``siteactions.py`` ausgelagert worden.

Auch der Aufbau von ``siteactions.py`` entspricht der üblichen Konvention.
Zunächst wird einiges importiert, darunter auch das ``base``-Modul von
``plone.app.portlets``, das verschiedene Basisklassen wie ``Assignment`` und
``Renderer`` zum Erstellen eines neuen Portlets bereitstellt::

 from zope import schema
 from zope.component import getMultiAdapter
 from zope.formlib import form
 from zope.interface import implements

 from plone.app.portlets.portlets import base
 from plone.portlets.interfaces import IPortletDataProvider
 from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

 from vs.theme import VsThemeMessageFactory as _

 class ISiteActionsPortlet(IPortletDataProvider):
     """A portlet which shows the available site actions.
     """

 class Assignment(base.Assignment):
     implements(ISiteActionsPortlet)


     @property
     def title(self):
         return _(u"Site actions")

 class Renderer(base.Renderer):
     render = ViewPageTemplateFile('siteactions.pt')
     title = _('box_siteactions', default=u"Site actions")

     def site_actions(self):
         context_state = getMultiAdapter((self.context, self.request),
                                         name=u'plone_context_state')
         self.siteactions = context_state.actions('site_actions')
         return self.siteactions

Schließlich werden noch Klassen für ``AddForm`` definiert, die Nutzern das Erstellen des Site-Action-Portlets erlauben::

 class AddForm(base.NullAddForm):
     form_fields = form.Fields(ISiteActionsPortlet)
     label = _(u"Add Site Actions Portlet")
     description = _(u"This portlet lists the available site actions.")

     def create(self):
         return Assignment()

Konfigurieren und Registrieren neuer Portlet-Typen
==================================================

Um neue Portlet-Typen zu konfigurieren, wird die Datei ``portlets/configure.zcml`` mit folgendem Inhalt erstellt::

 <configure
     xmlns="http://namespaces.zope.org/zope"
     xmlns:plone="http://namespaces.plone.org/plone">

     <include package="plone.app.portlets" />

     <plone:portlet
         name="vs.theme.SiteActionsPortlet"
         interface=".siteactions.ISiteActionsPortlet"
         assignment=".siteactions.Assignment"
         renderer=".siteactions.Renderer"
         addview=".siteactions.AddForm"
         />

 </configure>

Damit werden einige Hilfsmethoden, Adapter und Views registriert, Und falls Sie ein editierbares Portlet erstellen wollen, können Sie das ``editview``-Attribut hinzufügen und statt ``NullAddForm`` die ``AddForm``-Klasse angeben. Ein solches
Portlet ist beschrieben in `Portlet erstellen <../archetypes-artikeltypen/portlet-erstellen>`_.

Registrieren von Portlets
=========================

Ab Plone 3.1 muss das Portlet zusätzlich in ``src/vs.theme/vs/theme/profiles/default/portlets.xml`` angegeben werden::

 <?xml version="1.0"?>
 <portlets>
     <portlet
        addview="vs.theme.SiteActionsPortlet"
        title="Site Actions"
        description="A portlet which can show the available site actions."
        />
 </portlets>

Dabei entspricht die Angabe für ``addview`` dem Namen des Portlets, der in ``portlets/configure.zcml`` angegeben wurde.

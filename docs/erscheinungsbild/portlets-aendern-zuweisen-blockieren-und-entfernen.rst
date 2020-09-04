===================================================
Portlets ändern, zuweisen, blockieren und entfernen
===================================================

Portlet ändern
==============

Um eine angepasste SearchBox in der linken Spalte anzeigen, wird zunächst in ``browser/templates/`` die Datei ``search_portlet.pt`` mit den gewünschten Anpassungen angelegt. Anschließend wird in ``browser/configure.zcml`` dieses Template angegeben::

 <configure
     xmlns="http://namespaces.zope.org/zope"
     xmlns:browser="http://namespaces.zope.org/browser"
     xmlns:plone="http://namespaces.plone.org/plone"
     i18n_domain="vs.theme">

 <include package="plone.app.portlets" />
 …
 <plone:portletRenderer
     portlet="plone.app.portlets.portlets.search.ISearchPortlet"
     layer=".interfaces.IThemeSpecific"
     template="templates/search_portlet.pt"
     />
 …
 </configure>

Portlets zuweisen
=================

Plone 3.0
---------

In ``setuphandlers.py`` lässt sich das Search-Portlet der linken Spalte zuweisen::

 from zope.component import getMultiAdapter
 from zope.component import getUtility
 from plone.portlets.interfaces import IPortletAssignmentMapping
 from plone.portlets.interfaces import IPortletManager
 from plone.app.portlets import portlets

 class Generator:
     def setupPortlets(self, portal):
         leftColumn = getUtility(IPortletManager, name=u'plone.leftcolumn', context=portal)
         rightColumn = getUtility(IPortletManager, name=u'plone.rightcolumn', context=portal)

         left = getMultiAdapter((portal, leftColumn,), IPortletAssignmentMapping, context=portal)
         right = getMultiAdapter((portal, rightColumn,), IPortletAssignmentMapping, context=portal)

         if u'search' not in left:
             left[u'search'] = portlets.search.Assignment(enableLivesearch=True,)

 def setupVarious(context):
     if context.readDataFile('vs.theme_various.txt') is None:
         return

     site = context.getSite()
     gen = Generator()
     gen.setupPortlets(site)

Plone 3.1
---------

Hier erfolgt die Zuweisung in ``profiles/default/portlets.xml``::

 <?xml version="1.0"?>
 <portlets
     xmlns:i18n="http://xml.zope.org/namespaces/i18n"
     i18n:domain="plone">

 <assignment
            manager="plone.leftcolumn"
            category="context"
            key="/"
            type="portlets.Search"
            name="search"
            insert-before="*"
            >

     <property name="enableLivesearch">True</property>

 </assignment>
 </portlets>

``type`` (erforderlich)
 Der Name des Portlets entsprechend dem name-Atribut in der ``<portlet />``-
 Anweisung in ``portlets.xml``.
``manager`` (erforderlich)
 Der Name des Portlet-Manager, der verwendet werden soll. Portlet-Manager werden
 registriert in ``portlets.xml``, z.B.::

  <portletmanager
    name="plone.leftcolumn"
    type="plone.app.portlets.interfaces.ILeftColumn"
    />

 In Plone verfügbare Portlet-Manager sind:

 plone.leftcolumn und plone.rightcolumn
  für die linke und rechte Spalte
 plone.dashboard1 bis plone.dashboard4
  für die vier Spalten des Dashboard.

``category`` (erforderlich)
 Die zu verwendende Kategorie. Mögliche Kategorien sind:

 - ``context``
 - ``content_type``
 - ``group``
 - ``user`` (Diese Angabe ist vmtl. nur für die Dashboard-Portlet-Manager
   sinnvoll.)

``key`` (erforderlich)
 Der Schlüssel, mit dem das Portlet zugewiesen wird.

 - Für die context-Kategorie ist der Schlüssel die Angabe des Pfades relativ zur Site-Root, z.B. ``/``.
 - Für die ``content_type``-Kategorie ist der Schlüssel die Angabe des Artikeltyps.
 - Für die ``group``-Kategorie ist der Schlüssel die Angabe der ID einer bestimmten Gruppe.
 - Für die ``user``-Kategorie ist der Schlüssel die Angabe der user-ID.
``name`` (optional)
 Der Name der Zuweisung. Wird keine Name angegeben, wird ein eindeutiger Name erzeugt. Wird ein bereits bestehender Name verwendet, der denselben key, dieselbe Kategorie und denselben Portlet-Manager verwendet, so wird dieser überschrieben.
``insert-before`` (optional)
 Dieser Parameter kann verwendet werden um die Reihenfolge der Portlets festzulegen.

 - Ist der Wert ``*``, wird das Porlet an oberster Stelle platziert.
 - Ist der Wert der Name eines anderen Portlets, wird das einzufügende Portlet direkt über diesem angezeigt.
 - Wird kein Wert angegeben, wird das Porlet zuunterst angezeigt.

 Die Portlets werden dabei in der Reihenfolge verarbeitet und eingefügt, wie sie in der ``portlets.xml``-Datei angegeben sind.

 Hier noch ein Beispiel für das Zuweisen eines Portlets im Dashboard eines Nutzers::

  <assignment name="quick-links" category="user" key="veit"
     manager="plone.dashboard1" type="plone.portlet.collection.Collection">
   <property name="show_more">True</property>
   <property name="header">Quick links</property>
   <property name="limit">10</property>
   <property
      name="target_collection">/quick-links/quick-links</property>
   <property name="random">False</property>
   <property name="show_dates">False</property>
  </assignment>

Übernommene Portlets blockieren
===============================

Plone 3.0
---------

Von übergeordneten Objekten übernommene Portlets lassen sich in ``setuphandlers.py`` blockieren, z.B. mit::

 from plone.portlets.constants import CONTEXT_CATEGORY as CONTEXT_PORTLETS

 class Generator:

     def setupPortlets(self, portal):
         rightColumn = getUtility(IPortletManager, name=u'plone.rightcolumn', context=portal)
         portletAssignments = getMultiAdapter((members, rightColumn,), ILocalPortletAssignmentManager)
         portletAssignments.setBlacklistStatus(CONTEXT_PORTLETS, True)

Plone 3.1
---------

Das Blockieren lässt sich hier in ``profiles/default/portlets.xml`` konfigurieren, z.B.::

 <blacklist
     manager="plone.rightcolumn"
     location="/Members"
     category="context"
     status="block"
     />

``manager`` (erforderlich)
 Der Name des Portlet-Managers (Spalte), für die die Portlets nicht übernommen werden sollen.
``category`` (erforderlich)
 Die Kategorie, die geblockt werden soll: context, group oder content_type.
``location`` (erforderlich)
 Ein relativer Pfad, der den Ordner angibt, in dem die Portlets geblockt werden sollen.
``status`` (erforderlich)
 Der Status für übernommene Portlets einer Kategorie in einem bestimmten Ordner:

 ``block``
  Portlets des übergeordneten Objekts werden übernommen.
 ``show``
  Portlets der angegebenen Kategorie werden angezeigt.
 ``acquire``
  Portlets des übergeordneten Objekts werden übernommen.

Portlets ausblenden
===================

Portlets lassen sich in setuphandlers.py ausblenden, z.B. mit::

 from zope.component import getUtility
 from zope.component import getMultiAdapter
 from plone.portlets.interfaces import IPortletManager
 from plone.portlets.interfaces import IPortletAssignmentMapping

 class Generator:
     def setupPortlets(self, portal):
         rightColumn = getUtility(IPortletManager, name=u'plone.rightcolumn', context=portal)
         right = getMultiAdapter((portal, rightColumn,), IPortletAssignmentMapping, context=portal)
         if u'calendar' in right:
             del right["calendar"]

 def setupVarious(context):
     if context.readDataFile('vs.theme_various.txt') is None:
         return
     site = context.getSite()
     gen = Generator()
     gen.setupPortlets(site)

Portlets entfernen
==================

Plone 3.0
---------

Portlets lassen sich in setuphandlers.py entfernen, z.B. mit::

 from zope.component import getSiteManager
 from zope.component import getUtilitiesFor
 from plone.portlets.interfaces import IPortletType
 from Products.CMFCore.utils import getToolByName

 def removeRegistrantsPortlet(self):
     sm = getSiteManager()
     for name, portletType in getUtilitiesFor(IPortletType):
         if name == "portlets.Registrants":
             sm.unregisterUtility(provided=IPortletType, name=name)

Plone 3.1
---------

Hier erfolgt das entfernen von Portlets in ``profiles/default/portlets.xml``::

 <assignment
     remove="true"
     name="calendar"
     category="context"
     key="/"
     manager="plone.rightcolumn"
     type="portlets.Calendar" />

Plone 4
-------

In Plone 4 wurde das visible-Attribut zum Ein- oder Ausblenden der Portlets eingeführt::

 <assignment
     visible="0"
     name="calendar"
     category="context"
     key="/"
     manager="plone.rightcolumn"
     type="portlets.Calendar" />

Das Ausblenden aller Portlets in einem bestimmten Kontext erfolgt mit dem purge-Attribut::

 <assignment
     purge="True"
     manager="plone.rightcolumn"
     category="context"
     key="/Plone/news"
     />

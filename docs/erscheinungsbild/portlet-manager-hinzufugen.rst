==========================
Portlet-Manager hinzufügen
==========================

Zunächst wird ein Viewlet erstellt, das auf einen Portlet-Manager verweist – in unserem Fall ``vs.abovecontentportlets`` – und für den Viewlet-Manager ``IContentViews`` registriert wird. Anschließend wird für diesen Viewlet-Manager noch ein Management-View erstellt.

Viewlet erstellen
=================

Fügen Sie in ``browser/templates`` die Datei ``abovecontentportlets.pt`` mit folgendem Inhalt hinzu::

    <tal:block replace="structure provider:vs.abovecontentportlets" />

Dieses Viewlet wird nun registriert in ``browser/configure.zcml``::

    <browser:viewlet
        name="vs.abovecontentportlets"
        manager="plone.app.layout.viewlets.interfaces.IContentViews"
        layer=".interfaces.IThemeSpecific"
        template="templates/abovecontentportlets.pt"
        permission="zope2.View"
    />

Browserlayer registrieren
=========================

Das Viewlet steht nur zur Verfügung sofern das Interface ``IThemeSpecific`` in der Site zur Verfügung steht. Durch das ``plone3_theme``-Template sollte dieses Marker-Interface bereits in ``browser/interfaces.py`` erstellt worden sein::

    from plone.theme.interfaces import IDefaultPloneLayer

    class IThemeSpecific(IDefaultPloneLayer):
        """Marker interface that defines a Zope 3 browser layer.
           If you need to register a viewlet only for the
           "vs.theme" theme, this interface must be its layer.
        """

Nun wird dieses Interface als paketspezifischer Browserlayer registriert in ``profiles/default/browserlayer.xml``::

    <?xml version="1.0"?>
    <layers>
        <layer name="vs.theme.layer"
               interface="vs.theme.browser.interfaces.IThemeSpecific" />
    </layers>

Dieser Browserlayer steht nun jenen Sites zur Verfügung, in denen dieses Profil importiert wurde.

Portlet-Manager erstellen
=========================

Zunächst wird ein Marker-Interface in ``browser/interfaces.py`` erstellt::

    from plone.portlets.interfaces import IPortletManager

    class IVsAboveContent(IPortletManager):
        """Portlet manager above the content area.
        """

Anschließend wird in der Datei ``profiles/default/portlets.xml`` der neue Portlet-Manager registriert::

    <?xml version="1.0"?>
    <portlets>
        <portletmanager
             name="vs.abovecontentportlets"
             type="vs.theme.browser.interfaces.IVsAboveContent"
        />
    </portlets>

Erstellen eines Management-Views für den Portlet-Manager
========================================================

Um die Portlets des ``vs.abovecontentportlets`` zu verwalten, wird ein neuer View erstellt und hierfür zunächst folgende Zeilen in ``browser/configure.zcml`` eingetragen::

    <browser:page
        for="plone.portlets.interfaces.ILocalPortletAssignable"
        class="plone.app.portlets.browser.manage.ManageContextualPortlets"
        name="manage-vsabove"
        template="templates/managevsabove.pt"
        permission="plone.app.portlets.ManagePortlets"
    />

Und falls nicht bereits zu einem früheren Zeitpunkt geschehen, sollte noch das Paket ``plone.app.portlets`` eingeschlossen werden::

    <include package="plone.app.portlets" />

Schließlich wird dann noch das Page-Template ``browser/templates/managevsabove.pt`` erstellt::

    <html xmlns="http://www.w3.org/1999/xhtml"
          xmlns:metal="http://xml.zope.org/namespaces/metal"
          xmlns:tal="http://xml.zope.org/namespaces/tal"
          xmlns:i18n="http://xml.zope.org/namespaces/i18n"
          metal:use-macro="context/main_template/macros/master"
          i18n:domain="plone">
    <head>
        <div metal:fill-slot="javascript_head_slot" tal:omit-tag="">
            <link type="text/css" rel="kinetic-stylesheet"
                tal:attributes="href string:${context/absolute_url}/++resource++manage-portlets.kss"/>
        </div>
    </head>
    <body>
    <div metal:fill-slot="main">
      <h1 class="documentFirstHeading">Manage above content portlets</h1>
      <span tal:replace="structure provider:vs.abovecontentportlets" />
    </div>
    </body>
    </html>

Nach einem Neustart des Zope-Servers sollten sich nun die Portlets verwalten lassen wenn folgende URL aufgerufen wird::

    http://localhost/mysite/@@manage-vsabove

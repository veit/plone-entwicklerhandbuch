========
z3c.jbot
========

Mit `z3c.jbot <http://pypi.python.org/pypi/z3c.jbot>`_ lassen sich Views und
alle Objekte des *Skins Tool*, wie Page Templates, CSS- und Javascript-Dateie
einfach überschreiben oder erweitern.

Überschreiben eines bestehenden Views
=====================================

#.1 Zunächst tragen wir in unser Theme-Produkt die Abhängigkeit von ``z3c.jbot``
   in ``vs.theme/setup.py`` ein::

    ...
    install_requires=[
        'setuptools',
        'z3c.jbot',
        ...
    ],
    ...

#. Anschließend wird folgende Direktive in ``vs.theme/vs/theme/configure.zcml``
   angegeben::

    <configure
        ...
        xmlns:browser="http://namespaces.zope.org/browser">
    ...
    <include package="z3c.jbot" file="meta.zcml" />
    ...
    <browser:jbot
     directory="overrides"
     layer=".interfaces.IThemeSpecific"
     />

#. Der Layer wird nun konfiguriert in
   ``vs.theme/vs/theme/profiles/default/browserlayer.xml``::

    <?xml version="1.0"?>
    <layers>
        <layer name="vs.theme"
               interface="vs.theme.interfaces.IThemeSpecific" />
    </layers>

#. Der Layer erwartet das Interface ``IThemeSpecific`` in der Datei
   ``vs.theme/vs/theme/interfaces.py``::

    from plone.theme.interfaces import IDefaultPloneLayer
    from plone.portlets.interfaces import IPortletManager

    class IThemeSpecific(IDefaultPloneLayer):
        """Marker interface that defines a Zope 3 browser layer.
        """

#. Schließlich wird der Ordner ``overrides`` angelegt und darn z.B. eine Kopie
   von ``atct_topic_view.pt`` als ``vs.theme/vs/theme/overrides/Products.ATContentTypes.skins.ATContentTypes.atct_topic_view.pt``.

   Dieses PageTemplate lässt sich dann z.B. um ein Teaser-Element erweitern::

    <td>
        <img tal:condition="obj/hasTeaserImage"
             tal:attributes="src string:${obj/getURL}/@@teaserImage?scale=teaser"
             class="teaserImage"
             />
        <div class="teaserText"
             tal:condition="obj/teaserText"
             tal:content="structure obj/teaserText" />
    </td>

Erweitern bestehender Templates
===============================

Mit `z3c.jbot`_ lassen sich auch einfach neue Templates aus bestehenden
erstellen.

#. Hierzu wird nun in  ``vs.theme/vs/theme/overrides/Products.ATContentTypes.skins.ATContentTypes.atct_topic_view.pt``
   eine Bedingung für die Tabellenzeile mit dem Teaser eingefügt::

    <table class="listing"
           summary="Content listing"
           i18n:attributes="summary summary_content_listing;">
        <thead>
            <tr tal:condition="options/with_teaser  | request/with_teaser | nothing" >
            ...
            <td tal:condition="options/with_teaser | request/with_teaser | nothing">
                <tal:if condition="obj/hasTeaserImage">
                    <a tal:attributes="href obj/getURL">
                        <img tal:condition="obj/hasTeaserImage"
                            tal:attributes="src string:${obj/getURL}/@@teaserImage?scale=teaser"
                            class="teaserImage"
                        />
                    </a>
                </tal:if>
                <tal:if condition="not: obj/hasTeaserImage">
                    <div class="title" tal:content="obj/Title" />
                    <div class="description" tal:content="obj/Description" />
                    <a tal:attributes="href obj/getURL"
                       i18n:translate="label_more">
                        more
                    </a>
                </tal:if>
            </td>

#. Nun wird ``with_teaser`` definiert in ``vs.theme/vs/theme/browser/topic.py``::

    from Products.Five.browser import BrowserView

    class TopicTeaserView(BrowserView):
        """ Topic table view with teaser """

        def __call__(self):
            view = self.context.restrictedTraverse('atct_topic_view')
            return view(with_teaser=True)

#. ``hasTeaserImage`` wird aus dem Index abgefragt. Sehen Sie hierzu `plone.indexer`_.

   .. _`plone.indexer`: plone.indexer

#. Anschließend wird in ``vs.theme/vs/theme/browser/configure.zcml`` die neue Ansicht registriert::

    <browser:page
      name="atct_topic_teaser_view"
      for="Products.ATContentTypes.interfaces.topic.IATTopic"
      permission="zope2.View"
      class=".topic.TopicTeaserView"
      />

#. Schließlich wird dieser View in derselben ``zcml``-Datei noch für das `Hinzufügen`-Menü konfiguriert::

    <include package="plone.app.contentmenu" />
    ...
    <browser:menuItem
      for="Products.ATContentTypes.interfaces.topic.IATTopic"
        menu="plone_displayviews"
        title="Collection with teaser"
        action="atct_topic_teaser_view"
        description="Collection table view with teaser"
        />

=============
Browser Views
=============

Browser View überschreiben
==========================

Zope 3 Browser Views werden üblicherweise als Page Templates definiert. Meist liegen diese Page Templates in einem Unterpaket namens ``browser``. Um ein solches Page Template ändern zu können, wird zunächst in ``browser/configure.zcml`` der Skin an unser *vs.theme* gebunden::

 <interface
    interface=".interfaces.IThemeSpecific"
    type="zope.publisher.interfaces.browser.IBrowserSkinType"
    name="vs.theme"
    />

Um herauszufinden, wo sich das gesuchte Page Template im Dateisystem befindet, kann im ZMI *Plone View Customizations* verwendet werden. Sobald sich der Cursor über dem Namen des entsprechenden Templates befindet, wird der Pfad im Dateisystem angezeigt. Alternativ kann auch nach ``.zcml``-Dateien gesucht werden, die den Namen der Ansicht enthalten.

Suchen wir z.B.  nach *Dashboard*, so finden wir zwei Ergebnisse:

``plone.app.layout.dashboard``
 ::

    <browser:page
        for="Products.CMFCore.interfaces.ISiteRoot"
        name="dashboard"
        permission="plone.app.portlets.ManageOwnPortlets"
        class=".dashboard.DashboardView"
        template="dashboard.pt"
        />

``plone.app.portlets.browser``
 ::

    <browser:page
        for="Products.CMFCore.interfaces.ISiteRoot"
        class=".manage.ManageDashboardPortlets"
        name="manage-dashboard"
        template="templates/manage-dashboard.pt"
        permission="plone.app.portlets.ManageOwnPortlets"
        />

Um diese beiden Views zu ändern, tragen wir folgendes in ``vs.theme/vs/theme/browser/configure.zcml`` ein::

 <include package="plone.app.portlets" />

 <browser:page
     for="Products.CMFCore.interfaces.ISiteRoot"
     name="dashboard"
     permission="plone.app.portlets.ManageOwnPortlets"
     class="plone.app.layout.dashboard.dashboard.DashboardView"
     template="templates/dashboard.pt"
     layer=".interfaces.IThemeSpecific"
     />

 <browser:page
     for="Products.CMFCore.interfaces.ISiteRoot"
     name="manage-dashboard"
     permission="plone.app.portlets.ManageOwnPortlets"
     class="plone.app.portlets.browser.manage.ManageDashboardPortlets"
     template="templates/manage-dashboard.pt"
     layer=".interfaces.IThemeSpecific"
     />

Um die Templates überschreiben zu können, ist die Angabe für ``layer`` wesentlich.

Anschließend wird in ``browser`` der Ordner ``templates`` erstellt und dann die beiden Templates ``dashboard.pt`` und ``manage-dashboard.pt`` dahin kopiert und geändert.

Plone 3.x
---------

Sollen z.B. die Portlets der linken und rechten Spalte angezeigt werden, müssen nur die entsprechenden Zeilen auskommentiert werden, also::

<!-- <metal:left fill-slot="column_one_slot" /> -->
<!-- <metal:right fill-slot="column_two_slot" /> -->

Plone 4
-------

Ab Plone 4.0 lassen sich die Portlet-Manager besser kontrollieren. So finden Sie nun z.B. im Page Template ``dashboard.pt`` folgende Anweisung::

 <head>
     <metal:block fill-slot="top_slot"
                  tal:define="dummy python:request.set('disable_border',1);
                              disable_column_one python:request.set('disable_plone.leftcolumn',1);
                              disable_column_two python:request.set('disable_plone.rightcolumn',1);" />
 </head>

- Dies sorgt dafür, dass die linke und rechte Spalte üblicherweise nicht im Dashboard angezeigt werden.
- Setzen wir nun die Anweisung auf ``0``, so werden der linke und rechte Portlet-Manager wieder angezeigt.
- Werden die Anweisungen im Template weggelassen, so greift die übliche Logik, bei der unterschieden wird, ob Portlets zugewiesen sind oder nicht.

.. note::
    Eine Anleitung zu Page Templates erhalten Sie in `Zope Page Templates (ZPT)`_

.. _`Zope Page Templates (ZPT)`: zope-page-templates-zpt

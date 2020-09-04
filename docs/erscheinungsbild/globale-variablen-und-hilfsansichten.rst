====================================
Globale Variablen und Hilfsansichten
====================================

Globale Variablen
=================

In Plone 3.x mussten einige Variablen nicht explizit in einem Template definiert werden, da sie bereits als ``global_defines`` in das ``main_template`` eingefügt wurden. Ab Plone 4 müssen auch diese Variablen wieder explizit definiert werden. Hier ein Überblick über die gebräuchlichsten dieser globalen Variablen:

``portal``
 Das Plone-Site-Root-Objekt
``portal_url``
 Die URL des Plone-*site root*-Objekts
``member``
 Der aktuell angemeldete Nutzer
``checkPermission``
 Funktion, die überprüft ob der aktuell angemeldete Nutzer im aktuellen Kontext eine bestimmte Berechtigung hat. Hier ein Beispiel aus ``parts/plone/CMFPlone/skins/plone_forms/folder_rename_form.cpt``::

  tal:define="canModifyItem python:checkPermission('Modify portal content', obj);"

``isAnon``
 ``True`` wenn der aktuelle Nutzer nicht angemeldet ist
``is_editable``
 ``True`` wenn der aktuelle Nutzer den aktuellen Kontext editieren darf
``isLocked``
 ``True`` wenn das aktuelle Objekt für das Editieren gesperrt ist

Einen vollständigen Überblick über die verfügbaren Variablen erhalten Sie im Docstring der ``globalize()``-Methode in ``Products.CMFPlone.browser.interfaces.IPlone``.

Hilfsansichten
==============

In ``plone.app.layout.globals`` sind Hilfsansichten definiert, mit denen Sie sich häufig genutzte Informationen anzeigen lassen können:

``@@plone_tools``
 Zugang zu den gebräuchlichsten *CMF Tools*
``@@plone_context_state``
 Informationen des aktuellen Kontexts, wie URL, Pfad, Status und Editierbarkeit
``@@plone_portal_state``
 Informationen über die aktuelle Plone-Site, wie URL der Site, aktueller Nutzer und ob er anonym ist

Ein Vorteil dieser Hilfsansichten ist, dass ihre Methoden gecached werden, sodass sie nur bei der ersten Anfrage berechnet werden müssen.

Wie diese Hilfsansichten in Viewlets verwendet werden, können Sie  z.B. in ``plone/app/layout/viewlets/content.py`` sehen::

 self.portal_state = getMultiAdapter((self.context, self.request),
                                     name=u'plone_portal_state')
 self.portal_url = self.portal_state.portal_url()

Als Beispiel, wie diese Hilfsansichten in Page Templates verwendet werden können, hier ein Auszug aus ``plone/app/portlets/portlets/login.pt``::

 tal:attributes="value context/@@plone_context_state/current_page_url"

Eine vollständige Übersicht über die verfügbaren Interfaces finden Sie in ``plone.app.layout.globals.interfaces``.

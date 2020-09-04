==============
content-Macros
==============

Plone 4 kommt mit den folgenden Slots:

``content-title``
 Slot mit dem View des Titels

 Der Inhalt wird in ``main_template.pt`` generiert.

``content-description``
 Slot mit dem View der Beschreibung.

 Der Inhalt wird in ``main_template.pt`` generiert.

``content-core``
 Slot, der in ``main_template.pt`` unterhalb von ``content-description`` angezeigt wird. Er zeigt den Inhalt einer Seite, die Liste eines Ordners o.ä. an.

``main``
 Dieser Slot ist weiterhin in Plone 4 vorhanden um rückwärtskompatibel zu bleiben und Views zu rendern, die ohne Viewlet-Manager oder modifizierte Titel und Beschreibungen auskommen.

Viewlet-Manager
===============

Alle Viewlet-Manager für ``content`` werden nicht mehr wie in Plone 3 in eigenen Templates verwaltet sondern immer im ``main_template.pt``. Hierdurch werden die Templates für Artikeltypen nochmals deutlich vereinfacht, sehen Sie z.B. ``document_view``::

 <metal:content-core fill-slot="content-core">
     <metal:content-core define-macro="content-core">
         <metal:field use-macro="python:context.widget('text', mode='view')">
             Body text
         </metal:field>
     </metal:content-core>
 </metal:content-core>

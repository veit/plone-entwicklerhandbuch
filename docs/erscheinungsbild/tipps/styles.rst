Styles
======

Zentriertes Design und unterschiedlich gestaltete Bereiche der Website lassen sich in Plone einfach realisieren.

Zentriertes Design
------------------

::

 #visual-portal-wrapper {
     width: 62em;
     margin-left: auto;
     margin-right: auto;
 }

Unterschiedlich gestaltete Bereiche der Website
-----------------------------------------------

Bereiche
~~~~~~~~

In ``parts/plone/CMFPlone/skins/plone_templates/main_template.pt:`` wird für den ``body``-Tag eine css-Klasse defniniert, die es erlaubt, unterschiedliche Gestaltungen für einzelne Bereiche der Wwbsite anzugeben:

::

 <body tal:attributes="class string:${here/getSectionFromURL} .">

Dies führt dann z.B. zu folgenden ``body``-Tag, je nachdem in welchem Bereich sich die gerade aufgerufene Seite befindet:

::

 <body class="section-news">
 <body class="section-events">

So lassen sich die Bereiche auch gestalterisch unterscheiden:

::

 body.section-news {
     ...
 }

 body.section-events {
     ...
 }

Templates
~~~~~~~~~

Analog lassen sich auch die Gestaltungen für einzelne Templates unterscheiden:

::

 <body tal:attributes="class ... template-${template/id}; ...">

::

 body.template-frontpage_view {
     ...
 }

.. Artikel
.. ~~~~~~~

.. s.a. http://www.starzel.de/blog/how-to-get-a-different-look-for-some-pages-of-a-plone-site

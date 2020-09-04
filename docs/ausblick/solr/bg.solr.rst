=======
bg.solr
=======

bg.solr stellt Views für Plone bereit, mit denen sich in Solr suchen lässt und die Ergebnisse in Plone angezeigt werden.

Falls Solr nicht über :doc:`../deliverance/index` oder :doc:`../diazo/index` angezeigt werden soll, können die Ansichten für die Solr-Suche auch einfach mit `bg.solr`_ in Plone integriert werden.

.. _`bg.solr`: https://github.com/zopyx/bg.solr/

Installation
============

Die Installation kann in Buildout einfach erfolgen mit::

 [buildout]
 …
 extensions =
    mr.developer
 sources = sources
 auto-checkout =
     bg.solr

 [sources]
 bg.solr = git https://github.com/zopyx/bg.solr

 [instance]
 …
 eggs =
    …
    bg.solr

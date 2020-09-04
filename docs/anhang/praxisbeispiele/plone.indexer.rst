=============
plone.indexer
=============

plone.indexer vereinfacht die Erstellung und Verwaltung eigener Indizees in Plone.

`plone.indexer`_ erlaubt das Erstellen von Adaptern zum Indizieren des ZCatalog.

.. _`plone.indexer`: http://pypi.python.org/pypi/plone.indexer

#. Zunächst wird ein Adapter-Paket erstellt::

    $ mkdir vs.theme/vs/theme/adapters
    $ touch vs.theme/vs/theme/adapters/__init__.py

#. Anschließend wird es in die Konfiguration eingeschlossen in ``vs.theme/vs/theme/configure.zcml``::

    <include package=".adapters" />

#. Ein einzelner Adapter wird dann konfiguriert in ``vs.theme/vs/theme/adapters/configure.zcml``::

    <configure
        xmlns="http://namespaces.zope.org/zope"
        xmlns:five="http://namespaces.zope.org/five"
        xmlns:cmf="http://namespaces.zope.org/cmf"
        xmlns:i18n="http://namespaces.zope.org/i18n"
        i18n_domain="vs.theme">
      <adapter name="hasTeaserImage" factory=".indexer.hasTeaserImageDocument" />
    </configure>

#. Die Klasse ``hasTeaserImageDocument`` in ``vs.theme/vs/theme/adapters/indexer.py`` sieht dann so aus::

    from plone.indexer import indexer
    from Products.ATContentTypes.interfaces import ITextContent

    def _hasTeaserImage(obj, fieldname):
        """ generic wrapper """
        field = obj.getField(fieldname)
        if field is None:
            return False
        img = field.get(obj)
        img_data = str(img.data)
        return len(img_data) > 0

    @indexer(ITextContent)
        def hasTeaserImageDocument(obj):
        """ Returns True/False if an teaser image exists or not """
        return _hasTeaserImage(obj, 'teaserImage')

=====================================
Programmatische Änderung von Artikeln
=====================================

Erhalten des aktuellen Stadiums
    Für Plone 4.3 kann das aktuelle Stadium mit `plone.api
    <https://pypi.python.org/pypi/plone.api>`_ ermittelt werden::

        import plone.api
        wftool = plone.api.portal.get_tool('portal_workflow')
        review_state = wftool.getInfoFor(context, 'review_state')

    Für Plone ≤ 4.2 erhalten wir das Workflow-Tool noch mit ``getToolByName``::

        from Products.CMFCore.utils import getToolByName
        wftool = getToolByName(context, 'portal_workflow'
        review_state = wftool.getInfoFor(context, 'review_state')

    .. note::
        Wird das Stadium im *Catalog Tool* (``portal_catalog``)
        abgefragt, so wird das Stadium als Metaangabe des Objekts ausgegeben::

            from Products.CMFCore.utils import getToolByName
            catalog = getToolByName(context, 'portal_catalog')
            for result in catalog(portal_type = ('Document', 'News Item'),
                                  review_state = ('published', 'public', 'visible',)):
                review_state = result.review_state
                # do something with the review state

Ändern des Stadiums
    ::

        wftool.doActionFor(context, action='publish')

.. |Workflow-Permissions| image:: workflow-permissions.png/image_preview
.. _`Überschreiben von Plone-Übersetzungen`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/internationalisierung/uberschreiben-von-plone-ubersetzungen.html

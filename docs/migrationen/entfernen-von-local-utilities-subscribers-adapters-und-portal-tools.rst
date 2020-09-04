=====================================================================
Entfernen von Local Utilities, Subscribers, Adapters und Portal Tools
=====================================================================

Häufig werden Local Persistent Utilities beim Deinstallieren eines Produkts nicht ebenfalls entfernt.

.. note::

   Mit `wildcard.fixpersistentutilities <wildcard.fixpersistentutilities/>`_
   steht nun ein Modul zur Verfügung, mit dem sich Local Utilities, Subscribers,
   Adapters und Portal Tools auf der Web-Oberfläche entfernen lassen.

Symptome
========

Nach dem Deinstallieren solcher Produkte kann es z.B. folgende Fehlermeldungen
geben::

 AttributeError: type object 'IQueue' has no attribute '__iro__'

oder::

 AttributeError: type object 'ISalt' has no attribute '__iro__'

Entfernen von Local Persistent Utilities
========================================

#. Starten der Instanz im Debug-Modus::

    $ ./bin/instance debug

#. Anschließend holen wir uns den *site manager* der Site ``Plone``. `àpp``
   referenziert dabei auf das Zope-Root-Objekt::

    sm = app.Plone.getSiteManager()

#. Nun importieren wir das Interface des Utility.
   Anschließend melden wir es ab und löschen es
   schließlich. Dies sieht z.B. für `Singing & Dancing <http://pypi.python.org/pypi/collective.dancing>`_ so aus::

    from collective.singing.interfaces import ISalt
    from collective.singing.async import IQueue

    util_obj = sm.getUtility(ISalt)
    sm.unregisterUtility(provided=ISalt)
    del util_obj
    sm.utilities.unsubscribe((), ISalt)
    del sm.utilities.__dict__['_provided'][ISalt]
    del sm.utilities._subscribers[0][ISalt]

    util = sm.queryUtility(IQueue, name='collective.dancing.jobs')
    sm.unregisterUtility(util, IQueue, name='collective.dancing.jobs')
    del util
    del sm.utilities._subscribers[0][IQueue]

   Dabei unterscheidet sich das Vorgehen, da für ``ISalt`` ein *unnamed utility* und für ``IQueue`` ein *named utility* registriert sind.

#. Anschließend müssen die Änderungen noch an der ZODB *commited* werden::

    import transaction
    transaction.commit()
    app._p_jar.sync()

Entfernen von Subscribers, Adapters und Providers
=================================================

   ::

    sm = app.Plone.getSiteManager()

    adapters = sm.utilities._adapters
    for x in adapters[0].keys():
        if x.__module__.find("my.package") != -1:
          print "deleting %s" % x
          del adapters[0][x]
    sm.utilities._adapters = adapters

    subscribers = sm.utilities._subscribers
    for x in subscribers[0].keys():
        if x.__module__.find("my.package") != -1:
          print "deleting %s" % x
          del subscribers[0][x]
    sm.utilities._subscribers = subscribers

    provided = sm.utilities._provided
    for x in provided.keys():
        if x.__module__.find("my.package") != -1:
          print "deleting %s" % x
          del provided[x]
    sm.utilities._provided = provided

    from transaction import commit
    commit()
    app._p_jar.sync()

``Plone``
 Die ID der Site
``my.package``
 Das Paket, aus dem Subscriber, Adapter und Provider kommen

Entfernen von Portal Tools
==========================

Nach dem Entfernen von lokalen persistenten Komponenten muss ggf. auch noch das Portal Setup Tool bereinigt werden::

    setup_tool = app.Plone.portal_setup
    toolset = setup_tool.getToolsetRegistry()
    if 'my.package' in toolset._required.keys():
        del toolset._required['my.package']
        setup_tool._toolset_registry = toolset

    from transaction import commit
    commit()
    app._p_jar.sync()

Zum Weiterlesen
===============

- `Removing a persistent local utility <http://blog.fourdigits.nl/removing-a-persistent-local-utility>`_
- `Removing a persistent local utility part II <http://blog.fourdigits.nl/removing-a-persistent-local-utility-part-ii>`_
- `How to remove local utility <http://plone.org/support/forums/addons#nabble-td3341437>`_
- `gist.github.com/thet/thet/upgrades.py <https://gist.github.com/thet/e2c2b7dd6446c55cca9fad67eb6b2856>`_

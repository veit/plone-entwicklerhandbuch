============
Installation
============

``collective.xdv`` lässt sich einfach mit Buildout installieren. Hierzu nehmen Sie folgende Änderungen in der ``buildout.cfg``-Datei vor::

 [buildout]
 ...
 extends =
     http://dist.plone.org/release/3.3.5/versions.cfg
     lxml.cfg
     http://good-py.appspot.com/release/collective.xdv/1.0?plone=3.3.5

 versions = versions

 ...
 eggs =
     ...
     collective.xdv [Zope2.10]

 [versions]
 zope.i18n = 3.7.2

.. note::
    Beachten Sie bitte, dass in der URL durch ``1.0?plone=3.3.5`` die Version von collective.xdv auf die Version 1.0 und Plone auf die Version 3.3.5 festgeschrieben wird.

.. note::
    ``[Zope2.10]`` wird für Plone 3.3 oder früher benötigt um mit
    ``ZPublisherEventsBackport`` die  *publication events* aus Zope 2.12 auch
    Zope 2.10 zur Verfügung zu stellen. Verwenden Sie Zope 2.12 und Plone 4,
    genügt Ihnen einfach::

        eggs =
            ...
            collective.xdv

Die ``lxml.cfg``-Datei sieht dann folgendermaßen aus::

 [lxml]
 parts =
    staticlxml
    pylxml

 [pylxml]
 recipe=zc.recipe.egg
 interpreter=pylxml
 eggs=
     lxml

 [staticlxml]
 recipe = z3c.recipe.staticlxml
 egg = lxml

Nun sollte Buildout problemlos durchlaufen und die Instanz neu gestartet werden können::

 $ ./bin/buildout
 ...
 We have the distribution that satisfies 'collective.xdv[zope2.10]==1.0rc11'.
 Getting required 'collective.directoryresourcepatch==1.0'
 We have the distribution that satisfies 'collective.directoryresourcepatch==1.0'.
 Getting required 'ZPublisherEventsBackport==1.1'
 We have the distribution that satisfies 'ZPublisherEventsBackport==1.1'.
 Getting required 'five.globalrequest==1.0'
 We have the distribution that satisfies 'five.globalrequest==1.0'.
 Getting required 'repoze.xmliter==0.1'
 We have the distribution that satisfies 'repoze.xmliter==0.1'.
 Getting required 'plone.transformchain==1.0b1'
 We have the distribution that satisfies 'plone.transformchain==1.0b1'.
 Getting required 'plone.subrequest==1.3'
 We have the distribution that satisfies 'plone.subrequest==1.3'.
 Getting required 'plone.app.registry==1.0b2'
 We have the distribution that satisfies 'plone.app.registry==1.0b2'.
 Getting required 'lxml==2.2.4'
 We have the distribution that satisfies 'lxml==2.2.4'.
 Getting required 'xdv==0.4b2'
 We have the distribution that satisfies 'xdv==0.4b2'.
 ...

 $ ./bin/instance fg

**Anmerkung:** Während der Entwicklung empfiehlt sich, Zope im Debug-Modus laufen zu lassen da dann die Änderungen an ``theme`` oder ``rules`` sofort übernommen werden.

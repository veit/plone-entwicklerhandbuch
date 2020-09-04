==================================
Aktualisieren von Plone 4.1 zu 4.2
==================================

Aktualisieren von ``zc.buildout``
=================================

Üblicherweise verwendet ``bootstrap.py`` nun ``zc.buildout`` in Version 1.5.2 und nicht mehr 1.4.4. Die aktuelle Version von ``zc.buildout`` referenziert jedoch nicht mehr die globalen Python Site Packages, weshalb eigene Pakete nun in das lokale Build übernommen werden müssen.

In einem bestehenden Buildout-Projekt können Sie ``zc.buildout`` aktualisieren mit::

 $ python2.7 bootstrap --version 1.5.2

Search-Template
===============

Die Suche wurde in Plone 4.2 grundlegend überarbeitet, sodass frühere Anpassungen der Suche voraussichtlich nicht mehr funktionieren werden.

#. Um nun Ihre Änderungen für Plone 4.2 zu übernehmen, verwenden Sie am besten `z3c.jbot <http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/anhang/praxisbeispiele/z3c.jbot>`_.
#. Anschließend kopieren Sie ``plone.app.search/plone/app/search/search.pt`` in Ihr Produkt, z.B. nach ``vs.theme/vs/theme/overrides/plone.app.search.search.pt``.
#. Nun starten Sie Ihre Instanz um zu überprüfen, ob dies fehlerfrei geschieht.
#. Schließlich können Sie Ihre gewünschten Änderungen am Suchformular vornehmen.

Aktualisieren bestehender Kollektionen
======================================

Upgrade
-------

Beim Upgrade der Plone-Site bleiben die alten Kollektionen weiterhin erhalten als *Collection (old-style)*; sie werden nicht migriert.

Anpassungen für alte und neue Kollektionen
------------------------------------------

Die neuen Kollektionen implementieren die ``queryCatalog``-Methode in ``plone.app.collection.collection``, sodass in vielen Fällen voraussichtlich nur das Interface und die Referenzen auf den ``portal_type`` geändert werden müssen.

Um diese Änderungen rückwärtskompatibel implementieren zu können, empfiehlt sich, diese Methode nur in Views zu verwenden, die ausschließlich den neuen Kollektionen vorbehalten sind. Dies lässt sich mit  `Conditionally run ZCML <http://collective-docs.plone.org/en/latest/zcml/tricks.html#conditionally-run-zcml>`_ realisieren, also z.B. mit::

 <browser:page
   zcml:condition="installed plone.app.collection"
   name="mycollectionview"
   for="plone.app.collection.interfaces.ICollection"
   class=".views.MyCollectionView"
   permission="zope2.View"/>

Analog lassen sich auch Interfaces nur für neue Kollektionen registrieren, z.B.::

 <class class="plone.app.collection.collection.Collection"
  zcml:condition="installed plone.app.collection">
  <implements interface=".interfaces.IMyCollectionInterface" />
 </class>

``getRawQuery``-Methode
-----------------------

Die ``getRawQuery``-Methode können Sie selbst verwenden mit::

 from plone.app.querystring import queryparser
 query = queryparser.parseFormquery(collectionobj, collectionobj.getRawQuery())

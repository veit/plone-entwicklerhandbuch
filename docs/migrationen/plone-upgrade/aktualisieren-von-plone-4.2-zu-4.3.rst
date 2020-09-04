==================================
Aktualisieren von Plone 4.2 zu 4.3
==================================

Die Abhängigkeiten von Plone 4.3 sind deutlich verringert worden. Dadurch wird der Speicherverbrauch von Plone verringert und Importe beschleunigt. Es kann jedoch sein, dass Plone-Zusatzprodukte entsprechend angepasst werden müssen.

- Importierte ``zope.*``-Pakete haben in neueren
  Versionen weniger Abhängigkeiten
- Zusätzliche Abhängigkeiten können in der
  ``setup.py``-Datei angegeben werden.

  Weitere Informationen hierzu erhalten Sie in :doc:`../upgrade-von-zusatzprodukten//index`.

Im Folgenden eine Liste derjenigen Zusatzprodukte, die zwar in Plone 4.2, nicht jedoch in Plone 4.3 enthalten sind:

- `elementtree <http://effbot.org/zone/element-index.htm>`_

  stattdessen wird nun `lxml <http://lxml.de/>`_ verwendet

- `Products.kupu <https://pypi.python.org/pypi/Products.kupu/1.5.0>`_
- `plone.app.kss <https://pypi.python.org/pypi/plone.app.kss>`_

  kann z.B. für das *Inline Editing* zusätzlich
  installiert werden.

- `zope.app.cache
  <https://pypi.python.org/pypi/zope.app.cache>`_
- `zope.app.component
  <https://pypi.python.org/pypi/zope.app.component>`_
- `zope.app.container
  <https://pypi.python.org/pypi/zope.app.container>`_
- `zope.app.pagetemplate
  <https://pypi.python.org/pypi/zope.app.pagetemplate>`_
- `zope.app.publisher
  <https://pypi.python.org/pypi/zope.app.publisher/3.10.2>`_
- `zope.copypastemove
  <https://pypi.python.org/pypi/zope.copypastemove>`_
- `zope.dublincore
  <https://pypi.python.org/pypi/zope.dublincore>`_
- `zope.hookable
  <https://pypi.python.org/pypi/zope.hookable>`_

Einen Überblick über die gebräuchlichsten Importe und
deren neue Orte erhalten Sie in `Updating package dependencies <http://plone.org/documentation/manual/upgrade-guide/version/upgrading-plone-4.2-to-4.3/updating-package-dependencies>`_.

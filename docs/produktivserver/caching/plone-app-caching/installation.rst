 plone.app.caching: Installation
 ===============================

Voraussetzungen
---------------

`plone.app.caching`_ hat folgende Voraussetzungen:

- `plone.caching`_

  - `z3c.caching`_

- `plone.cachepurging`_
- `plone.app.registry`_

  - `plone.registry`_

- `plone.protect`_

.. _`plone.app.caching`: http://pypi.python.org/pypi/plone.app.caching
.. _`plone.caching`: http://pypi.python.org/pypi/plone.caching
.. _`z3c.caching`: http://pypi.python.org/pypi/z3c.caching
.. _`plone.cachepurging`: http://pypi.python.org/pypi/plone.cachepurging
.. _`plone.app.registry`: http://pypi.python.org/pypi/plone.app.registry
.. _`plone.registry`: http://pypi.python.org/pypi/plone.registry
.. _`plone.protect`: http://pypi.python.org/pypi/plone.protect

Installation
------------

plone.app.caching lässt sich einfach mit Buildout installieren indem in der Buildout-Konfigurationsdatei folgendes angegeben wird::

 [buildout]
 ...
 extends =
     ...
     http://good-py.appspot.com/release/plone.app.caching/1.0b2
 ...
 eggs =
     ...
     plone.app.caching

Anschließend rufen Sie das Buildout-Skript auf und starten Ihre Instanz neu.

Aktivieren
----------

Gehen Sie nun in das Kontrollfeld *Erweiterungen* der Plone-Konfiguration und aktivieren dort *HTTP caching support*.

Dies aktiviert automatisch auch die *Configuration registry* und *Plone z3c.form support*.

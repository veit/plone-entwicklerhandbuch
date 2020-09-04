====================
Testen mehrerer Eggs
====================

Mit ``zc.recipe.testrunner`` steht ein Buildout-Rezept zum Erstellen eigener TestRunner für mehrere Eggs zur Verfügung. Die Buildout-Konfiguration für das Testen aller in einer Instanz verwendete Eggs kann z.B. so aussehen::

 [buildout]
 ...
 parts =
     ...
     instance
     test

 [test]
 recipe = zc.recipe.testrunner
 defaults = ['--auto-color', '--auto-progress']
 eggs =
     ${instance:eggs}
 defaults = ['--auto-color', '--auto-progress', '-q', '--module', '^vs[.]']
 initialization =
     import warnings
     warnings.simplefilter('ignore', DeprecationWarning)

``eggs``
 Liste der zu testenden Eggs wobei jedes Egg in einer neuen Zeile stehen sollte.
``defaults``
 Standardoptionen, die üblicherweise als Python list literal angegeben werden.

 ``--ndiff``
  Wenn ein Doctest fehlschlägt, wird das ``ndiff.py``-Utility zum Anezigen der Unterschiede verwendet. Alternativen zu dieser Angabe sind:

  - ``--udiff`` für Unified Diffs
  - ``--cdiff`` für Context Diffs.

Weitere Informationen erhalten Sie in der Dokumentation auf PyPI zu `zc.recipe.testrunner`_.

Alle Eggs im Projekt testen
===========================

`plone.recipe.alltests`_ erlaubt das Testen aller Eggs eines Buildout-Projekts. ``bin/alltests`` durchläuft alle Tests aller Abhängigkeiten des Hauptprodukts. Hierzu sind lediglich folgende drei Zeilen in der ``buildout.cfg``-Datei hinzuzufügen::

 [buildout]
 ...
 parts =
     ...
     instance
     test
     alltests
 ...
 [alltests]
 recipe = plone.recipe.alltests

Darüberhinaus können noch folgende Optionen angegeben werden:

``eggs``
 Eine Liste von Paketen, die getestet werden sollen.

 Der Standardwert sind die im ``[tests]``-Abschnitt angegebenen Eggs.

``test-script``
 Der Ort im Dateisystem von ``zc.recipe.testrunner``.

 Der Standardwert ist ``bin/test``

``exclude``
 Eine Liste von Eggs, die aus dem Testen ausgeschlossen werden sollen. Als Werte können reguläre Ausdrücke angegeben werden, z.B.::

  [alltests]
  recipe = plone.recipe.alltests
  exclude =
      repoze.*

``groups``
 Ein Buildout-Abschnitt mit einem Mapping von Gruppen- zu Paketnamen, z.B.::

  [alltests]
  recipe = plone.recipe.alltests
  groups = test-groups

  [test-groups]
  Zope2 =
      Acquisition
      DateTime
      ExtensionClass
      Persistence
  ZODB =
      transaction
      zc.lockfile
  chameleon =
      chameleon.core
      cmf.pt
      z3c.pt

``package-map``
 Ein Buildout-Abschnitt mit einem Mapping von Distributions- zu Paketnamen, z.B.::

  [alltests]
  recipe = plone.recipe.alltests
  groups = test-groups

  [package-map]
  Plone = Products.CMFPlone

.. _`zc.recipe.testrunner`: http://pypi.python.org/pypi/zc.recipe.testrunner#detailed-documentation
.. _`plone.recipe.alltests`: http://pypi.python.org/pypi/plone.recipe.alltests

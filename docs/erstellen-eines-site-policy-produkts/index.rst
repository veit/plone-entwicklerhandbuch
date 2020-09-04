====================================
Erstellen eines Site-Policy-Produkts
====================================

#. Zum Erstellen eines Python-Eggs, das ein Zope2-Produkt enthält, verwenden wir
   das ZopeSkel-Template ``plone``::

    $ cd src
    $ $ ../bin/zopeskel plone_basic
    …
    Enter project name (or q to quit): vs.policy
    Expert Mode? (What question mode would you like? (easy/expert/all)?) ['easy']: all
    Namespace Package Name (Name of outer namespace package) ['vs']:
    Package Name (Name of the inner namespace package) ['policy']:
    Version (Version number for project) ['1.0']:
    Description (One-line description of the project) ['']: Policy package for demonstration purposes
    Register Profile (Should this package register a GS Profile) [False]: True
    Long Description (Multi-line description (in ReST)) ['']: Policy package for demonstration purposes
    Author (Name of author for project) ['']: Veit Schiele
    Author Email (Email of author for project) ['']: kontakt@veit-schiele.de
    Keywords (List of keywords, space-separated) ['']: Zope Plone
    Project URL (URL of the homepage for this project) ['http://svn.plone.org/svn/collective/']: https://github.com/veit/vs.policy
    Project License (Name of license for the project) ['GPL']:
    Zip-Safe? (Can this project be used as a zipped egg? (true/false)) [False]:
    Zope2 Product? (Are you creating a product for Zope2) [True]:
    Creating directory ./vs.policy
    …

   Hiermit werden folgende Dateien erzeugt::

    vs_buildout/src/vs.policy
    ├── CHANGES.rst
    ├── CONTRIBUTORS.rst
    ├── README.rst
    ├── bootstrap.py
    ├── buildout.cfg
    ├── docs
    │   ├── LICENSE.GPL
    │   └── LICENSE.txt
    ├── setup.cfg
    ├── setup.py
    └── src
        └── vs
            ├── __init__.py
            └── policy
                ├── __init__.py
                ├── configure.zcml
                ├── profiles
                │   ├── default
                │   │   └── metadata.xml
                │   └── testing
                │       └── metadata.xml
                ├── testing.py
                └── tests
                    ├── __init__.py
                    └── test_example.py

   ``setup.py``
    enthält Anweisungen für Setuptools, Distribute oder Buildout, wie die
    Paketdistribution verwaltet werden soll.
   ``setup.cfg``
    enthält zusätzliche Konfigurationsinformationen, in diesem Fall über das
    verwendete ZopeSkel-Template.
   ``README.rst``
    Dokumentation des Pakets.

    Soll das Paket im PyPI veröffentlicht werden, wird der Inhalt zusammen mit
    dem Wert für ``long_description`` in der ``setup.py``-Datei als HTML gerendert.

   ``docs/``
    Enthält zusätzliche Dokumentation einschließlich der Software-Lizenz
   ``CHANGES.rst``
    wird verwendet für die *Change Log*-Einträge im PyPI.

   ``src/vs``
    das Namespace-Package, das in der ``__init__.py``-Datei eine Methode für
    Setuptools und Distribute bereitstellt.

    ``src/vs/policy``
     Das Wurzelverzeichnis des Paketes selbst.

     ``src/vs/policy/__init__.py``
      Datei, die dieses Paket als Zope2-Produkt initiiert.

      Ggf. wird diese Datei auch benötigt um Archetypes-Artikeltypen zu
      erstellen. Siehe hierzu `Initialisierung und Hinzufügen-Rechte`_.

      .. _`Initialisierung und Hinzufügen-Rechte`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/artikeltypen/installation-und-registrierung/#initialisierung-und-hinzufugen-rechte

     ``src/vs/policy/configure.zcml``
      Die wesentliche Zope-Konfigurationsdatei für unser Paket. Diese wird
      automatisch von Plone beim Starten der Instanz geladen.
     ``src/vs/policy/testing.py``
      enthält ein Gerüst für Integrationstests. Wir werden dieses später durch
      unsere eigenen Tests ersetzen.

#. Nachdem das Python-Egg im ``src``-Verzeichnis erstellt worden ist, sollten
   wir es noch in der ``devel.cfg``-Datei eintragen. Der ``instance-base``-Abschnitt
   übernimmt die Eggs::

    [buildout]
    …
    develop =
        src/vs.policy
    …
    [instance-base]
    eggs +=
        …
        vs.policy

#. Für Eggs, die in Plone-Sites ≤ 3.3 verwendet werden sollen, kann
   `z3c.autoinclude <http://pypi.python.org/pypi/z3c.autoinclude>`_ nicht
   verwendet werden. Dieses Paket erstellt automatisch zwei neue ZCML-
   Anweisungen: ``includeDependencies`` und ``includePlugins``. Es ist mit dem
   ZopeSkel-Template bereits in der Datei ``src/vs.policy/setup.py`` verwendet
   worden::

    setup(name='vs.theme',
        …
        entry_points="""
        # -*- entry_points -*-
        [z3c.autoinclude.plugin]
        target = plone
        """,
        …
        )

   In Plone ≤ 3.3 muss hingegen noch folgendes in Die Buildout-Konfiguration
   eingetragen werden::

    [instance]
    …
    zcml =
        vs.policy

   Damit erstellt Buildout in der Instance einen sog. *zcml-slug* z.B. im
   Verzeichnis ``parts/instance/etc/package-includes/`` die Datei
   ``001-vs.policy-configure.zcml`` mit folgendem Einzeiler::

    <include package="vs.policy" file="configure.zcml" />

   Um zu Testen, ob das Python-Egg in der Instanz zur Verfügung steht, rufen wir
   den Python-Interpreter ``zopepy`` auf::

    $ ./bin/zopepy
    >>> from vs import policy

   Da kein Fehler für den Import ausgegeben wurde, scheint das Egg geladen zu
   werden, und der Python-Interpreter kann mit ``Strg-D`` (unter Windows
   ``Strg-Z``) wieder verlassen werden.

   Alternativ kann auch die Instanz gestartet werden mit ``./bin/instance``;
   anschließend sollten sich im Zope Management Interface  → Control_Panel →
   Products das ``vs.policy``-Produkt finden.

.. toctree::
    :titlesonly:
    :maxdepth: 0
    :hidden:

    andern-der-site-konfiguration
    zusaetzliche-aenderungen-der-site-konfiguration
    tests-schreiben
    installation

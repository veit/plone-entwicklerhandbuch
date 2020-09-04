===============
Paket erstellen
===============

Unsere Artikeltypen werden in einem eigenständigen Paket erstellt: ``vs.registration``. Folgende Schritte sind hierzu notwendig:

#. Im ``/src``-Verzeichnis erstellen wir aus der ZopeSkel-Vorlage ``dexterity``
   das Grundgerüst für unser neues Produkt::

    $ ../bin/zopeskel dexterity vs.registration

   Dabei verwenden wir den `èasy``-Modus und antworten mit ``True`` bei der
   Frage, ob wir eine GenericSetup_Profil erstellen wollen.

   Dies erzeugt folgende Paketstruktur::

    vs.registration
    ├── CHANGES.txt
    ├── CONTRIBUTORS.txt
    ├── DEXTERITY_README.rst
    ├── README.txt
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
            └── registration
                    ├── INTEGRATION.txt
                ├── __init__.py
                ├── configure.zcml
                ├── locales
                │   └── README.txt
                ├── profiles
                │   └── default
                │       ├── metadata.xml
                │       └── types.xml
                ├── static
                │   └── README.txt
                ├── testing.py
                └── tests
                    ├── __init__.py
                    ├── robot_test.txt
                    ├── test_example.py
                    └── test_robot.py



#. In der generierten ``setup.py``-Datei sind unter ``install_requires``
   folgende Pakete eingetragen::

    install_requires=[
        'setuptools',
        'plone.app.dexterity',
        'plone.namedfile [blobs]',

#. Darüberhinaus werden meistens noch die folgenden Erweiterungen benötigt::

    install_requires=[
        ...
        'collective.autopermission',
        'plone.app.referenceablebehavior',
        'plone.app.relationfield',
    ],

   `collective.autopermission <http://pypi.python.org/pypi/collective.autopermission>`_
    erstellt Berechtigungen in Zope2 sobald eine ``<permission />``-Anweisung verwendet wird.
   `plone.app.referenceablebehavior <http://pypi.python.org/pypi/plone.app.referenceablebehavior>`_
    ermöglicht, dass unsere Dexterity-Artikeltypen von Archetypes-Referenzfeldern aus verfügbar werden.
   `plone.app.relationfield <http://pypi.python.org/pypi/plone.app.relationfield>`_
    erlaubt uns, Referenzfelder zu verwenden
   `plone.namedfile <http://pypi.python.org/pypi/plone.namedfile>`_
    erlaubt uns zusammen mit dem ``[blobs]``-Extra, ZODB-Blobs zum Speichern unserer Dateien und Bilder zu verwenden.

   Weitere bekannte Erweiterungen sind

   `plone.app.stagingbehavior <http://pypi.python.org/pypi/plone.app.stagingbehavior>`_
    basierend auf `plone.app.iterate <http://pypi.python.org/pypi/plone.app.iterate>`_ bietet es Unterstützung von Staging für Dexterity-Artikeltypen. Erfordert Plone 4.1.

   `plone.app.versioningbehavior <http://pypi.python.org/pypi/plone.app.versioningbehavior>`_
    basierend auf `Products.CMFEditions <http://pypi.python.org/pypi/Products.CMFEditions>`_ bietet Unterstützung beim Speichern von Versionen für Dexterity-Artikeltypen. Erfordert Plone 4.0
   `collective.z3cform.datagridfield <http://pypi.python.org/pypi/collective.z3cform.datagridfield>`_
    ein ``z3c.form``-Widget zum Editieren von Listen von Subobjects mittels eines tabellenförmigen UI.
   `plone.app.lockingbehavior <https://pypi.python.org/pypi/plone.app.lockingbehavior>`_
    Locking-Integration für Dexterity-Artikeltypen.

#. Als nächstes fügen wir in der ``configure.zcml``-Datei die folgenden Zeile ein::

    <configure
        ...
        xmlns:grok="http://namespaces.zope.org/grok">
        <includeDependencies package="." />
        <grok:grok package="." />
        ...
    </configure>

  ``<includeDependencies package="." />``
   schließt die Konfiguration für die in der ``setup.py``-Datei aufgelisteten Abhängigkeiten ein.
  ``<grok:grok package="." />``
   ermöglicht Grok, automatisch Schema-Interfaces und ``content``-Klassen zu initialisieren.

#. Als nächstes ändern wir die ``buildout.cfg``-Datei um Dexteritys *Known Good Set of Versions* hinzuzufügen::

    [buildout]
    extensions =
        mr.developer
        ...
    extends =
        ...
        http://good-py.appspot.com/release/dexterity/1.0rc1?plone=4.1
        versions.cfg
    ...
    [test]
    recipe = zc.recipe.testrunner
    eggs =
        vs.registration
    defaults = ['--exit-with-status', '--auto-color', '--auto-progress']

    [sources]
    ...
    vs.registration = svn https://dev.plone.org/svn/pen/vs.registrtion/trunk

#. Nun können wir das ``vs.registration``-Paket auch als Abhängigkeit in unser ``vs.policy``-Produkt eintragen. Zunächst wird ``vs.registration`` in die Liste `ìnstall_requires`` in ``src/vs.policy/vs/policy/setup.py`` eingetragen::

    install_requires=[
        'setuptools',
        'Plone',
        'vs.event',
        'vs.theme',
        'vs.registration',
    ],

#. Schließlich editieren wir auch noch ``profiles/default/metadata.xml`` im selben Paket::

    <dependencies>
        <dependency>profile-vs.event:default</dependency>
        <dependency>profile-vs.theme:default</dependency>
        <dependency>profile-vs.registration:default</dependency>
    </dependencies>

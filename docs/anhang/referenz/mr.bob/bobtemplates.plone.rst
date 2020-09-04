==================
bobtemplates.plone
==================

bobtemplates.plone liefert Vorlagen für mr.bob template um Pakete für Plone-Projekte zu erstellen.

Erstellen eines Pakets
======================

Um ein Paket zu erstellen wie ``vs.policy``, geben Sie folgendes im Terminal ein::

    $ cd src/
    $ ../bin/mrbob -O vs.policy bobtemplates:plone_addon

Es können auch Pakete mit verschachtelten Namensräumen erstellt werden, z.B.::

    $ ../bin/mrbob -O vs.bootstrap.tinymce bobtemplates:plone_addon

Anschließend müssen Sie die folgenden Optionen beantworten:

Package Type?
   Optionen sind

    * ``Basic``
    * ``Dexterity``
    * ``Theme``

   Der Standardwert ist ``Basic``.

Author's name
    Hier sollte Ihr Name angegeben werden
Author's email
    Ihre E-Mail-Adresse
Author's github username
    Ihr Account-Name bei github
Package description
    Einzeilige Beschreibung des Pakets.

    Der Standardwert ist ``An add-on for Plone``

Plone version [4.3.6]
    Für welche Plone-Version wird das Paket entwickelt?

Dateistruktur
=============

``Basic``
---------

Die ``Basic``-Vorlage liefert die folgende Dateistruktur::

    vs.policy/
    ├── bootstrap-buildout.py
    ├── buildout.cfg
    ├── CHANGES.rst
    ├── CONTRIBUTORS.rst
    ├── docs
    │   ├── index.rst
    │   ├── LICENSE.GPL
    │   └── LICENSE.rst
    ├── MANIFEST.in
    ├── README.rst
    ├── setup.py
    ├── src
    │   └── vs
    │       ├── __init__.py
    │       └── policy
    │           ├── browser
    │           │   ├── configure.zcml
    │           │   ├── __init__.py
    │           │   ├── overrides
    │           │   └── static
    │           ├── configure.zcml
    │           ├── __init__.py
    │           ├── interfaces.py
    │           ├── locales
    │           │   ├── update.sh
    │           │   └── vs.policy.pot
    │           ├── profiles
    │           │   ├── default
    │           │   │   ├── browserlayer.xml
    │           │   │   ├── metadata.xml
    │           │   │   └── vspolicy_default.txt
    │           │   └── uninstall
    │           │       ├── browserlayer.xml
    │           │       └── vspolicy_uninstall.txt
    │           ├── setuphandlers.py
    │           ├── testing.py
    │           └── tests
    │               ├── __init__.py
    │               ├── robot
    │               │   └── test_example.robot
    │               ├── test_robot.py
    │               └── test_setup.py
    └── travis.cfg

``buildout.cfg``
    Das Paket enthält eine Buildout-Konfigurationsdatei, die z.B. zum Testen
    verwendet werden kann.
``src/vs/policy/tests/``
    Das Paket kommt mit einem Test-Setup und Beispieltests zur Installation des
    Pakets.

    Es enthält außerdem in ``src/vs/policy/tests/robot/test_example.robot`` einen
    Robot-Test für das Anmelden an der Plone-Site.

    Schließlich enthält das Paket mit ``travis.cfg`` auch eine Konfigurationsdatei,
    das das Testen des Pakets mit Travis erlaubt.

``src/vs/policy/profile``
    Das Paket enthält ein Generic Setup-Profil, das einen Browserlayer installiert.

    Für Plone 5 wird daneben noch ein ``uninstall``-Profil installiert.

``src/vs/policy/Locales``
    Das Paket registriert ein Verzeichnis für die Übersetzungsdateien.
``src/vs/policy/browser/overrides``
    Das Paket registriert einen Ordner, in dem Templates etc. mit `z3c.jbot
    <https://pypi.python.org/pypi/z3c.jbot>`_ überschrieben werden können.
``src/vs/policy/setuphandlers.py``
    Diese Datei kann verwendet werden um Code hinzuzufügen, der beim Installieren
    eines Pakets ausgeführt werden soll.

    Für Plone 5 gibt es innerhalb dieser Datei auch eine Methode, die beim
    Deinstallieren aufgerufen wird.

````

``setup.py``
   In ``install_requires`` werden zusätzlich die folgenden zwei Pakete angegeben:

   * ``plone.app.theming``
   * ``plone.app.themingplugins``

``src/vs/theme/configure.zcml``
    Hier wird der Ordner mit dem Theme konfiguriert::

        <configure
            ...
            xmlns:plone="http://namespaces.plone.org/plone"
            ...

        <plone:static
            directory="theme"
            type="theme"
            name="vs.theme"
            />

``src/vs/theme/profiles/default/metadata.xml``
    Hier wird als Abhängigkeit ``plone.app.theming`` angegeben::

        <dependency>profile-plone.app.theming:default</dependency>

``Dexterity``
-------------

``setup.py``
   In ``install_requires`` wird zusätzlich ``plone.app.dexterit`` angegeben
``src/vs/task/interfaces.py``
    Für den Dexterity-Artikeltyp wird ein Interface angegeben, in unserem Fall::

        from vs.task import _
        from zope import schema
        from zope.interface import Interface

        class ITask(Interface):

            title = schema.TextLine(
                title=_(u"Title"),
                required=True,
            )

            description = schema.Text(
                title=_(u"Description"),
                required=False,
            )

``src/vs/task/profiles/default/metadata.xml``
    Hier wird als Abhängigkeit ``plone.app.dexterity`` angegeben::

        <dependency>profile-plone.app.dexterity:default</dependency>

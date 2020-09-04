================
Private Releases
================

sdistmaker
==========

Mit `sdistmaker <https://pypi.python.org/pypi/sdistmaker>`_ gibt es eine
einfache Möglichkeit, *sdist tarballs* in svn-Repositories bereitzustellen.

sdistmaker übernimmt folgende Aufgaben:

#. Es durchsucht die ``tags``-Verzeichnisse Ihres svn-Repository. Dabei kann
sdistmaker auch auf bestimmte Bereiche Ihres Repository eingeschränkt werden.
#. Für jeden Tag erstellt es eine *source distribution* mit ``python setup.py
   sdist``.
#. Die *source distribution* wird anschließend in einem Unterverzeichnis Ihres
   Projekts gespeichert, ähnlich wie in https://pypi.python.org/simple/.

Installation
------------

``sdistmaker`` lässt sich einfach installieren mit::

    $ easy_install sdistmaker

Anschließend stehen Ihnen zwei Skripte zur Verfügung:

``make_sdist``
    ist im wesentlichen für Testzwecke gedacht. Dabei können Sie unter Angabe
    der ``tag``-URL und des Zielverzeichnisses einzelne Releases erstellen.
``sdists_from_tags``
    Es durchsucht die svn-Struktur nach geeigneten ``tags``-Verzeichnissen und
    erstellt aus diesen entsprechende Releases.

Konfiguration
-------------

Zunächst sollte sdistmaker seine eigene Basiskonfiguration erstellen mit::

    $ sdists_from_tags --print-example-defaults

Speichern Sie die Ausgabe in eine Konfigurationsdatei, z.B. ``defaults.py``.

Anschließend können Sie diese Konfiguration verwenden mit::

    $ sdists_from_tags --defaults-file=defaults.py

Schließlich werden Sie ``sdists_from_tags`` regelmäßig aufrufen wollen, entweder
als Cron-Job, svn post-commit-hook etc.

Verwendung in Buildout
----------------------

``sdistmaker`` kann mit Buildout folgendermaßen verwendet werden::

    [buildout]
    parts = sdists

    [sdists]
    recipe = zc.recipe.egg
    eggs = sdistmaker
    scripts = sdists_from_tags
    # arguments =
    #      defaults_file='${buildout:directory}/defaults.py'

Dabei wird die ``defaults.py``-Datei auf dieselbe Weise erzeugt wie oben
beschrieben.

sdistmaker und PyPI
-------------------

Üblicherweise kann immer nur ein Index für ``easy_install`` angegeben werden. Um
nun neben dem ``sdistmaker``-Index auch den von PyPI verwenden zu können, kann
z.B. eine Redirect-Anweisung definiert werden, falls im ``sdistmaker``-Index
nichts gefunden wird::

    # Allow indexing
    Options +Indexes
    IndexOptions FancyIndexing VersionSort

    # Start of rewriterules to use our own var/private/* packages
    # when available and to redirect to pypi if not.
    RewriteEngine On
    # Use our robots.txt:
    RewriteRule ^/robots.txt - [L]
    # Use our apache's icons:
    RewriteRule ^/icons/.* - [L]
    # We want OUR index.  Specified in a weird way as apache
    # searches in a weird way for index.htm index.html index.php etc.
    RewriteRule ^/index\..* - [L]

    # Use our var/private/PROJECTNAME if available,
    # redirect to pypi otherwise:
    RewriteCond /path/on/server/var/private/$1 !-f
    RewriteCond /path/on/server/var/private/$1 !-d
    RewriteRule ^/([^/]+)/?$ http://pypi.python.org/pypi/$1/ [L]

    # Use our var/private/PROJECTNAME/project-0.1.tar.gz if available,
    # redirect to pypi otherwise:
    RewriteCond /path/on/server/var/private/$1 !-d
    RewriteRule ^/([^/]+)/([^/]+)$ http://pypi.python.org/pypi/$1/$2 [L]

Verwenden des Index
-------------------

Dieser Index kann nun sowohl mit EasyInstall als auch mit Buildout aufgerufen
werden:

EasyInstall

    ::

        $ easy_install -i https://packages.veit-schiele.de/ vs.event

Buildout
    Sie können den Index in der Buildout-Konfigurationsdatei angeben::

        [buildout]
        index = https://packages.veit-schiele.de/
        parts =
            ...

gocept.zestreleaser.customupload
================================

`gocept.zestreleaser.customupload <https://pypi.python.org/pypi/gocept.zestreleaser.customupload>`_ ist ein Plugin
für `zest.releaser <http://pypi.python.org/pypi/zest.releaser>`_, das das
Hochladen erstellter Eggs via Secure copy (SCP) zu vorher konfigurierten Zielen
erlaubt.

Um es zu verwenden, kann in ``~/.pypirc`` z.B. folgendes konfiguriert werden::

    [gocept.zestreleaser.customupload]
    vs = scp://download.veit-schiele.de:/var/www/packages
    example = https://dav.veit-schiele.de:/var/www/example

Falls das veröffentlichte Paket mit einem der Schlüsselwörter (``vs``,
``example``) beginnt, werden Sie gefragt, ob das Egg auf den angegebenen Server
hochgeladen werden soll.

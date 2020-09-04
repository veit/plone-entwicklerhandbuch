======
mr.bob
======

mr.bob  ist ein Dateisystem-Template-Renderer.

Einleitung
==========

`mr.bob <https://pypi.python.org/pypi/mr.bob/>`_ ermöglicht, aus einer Vorlage eine Verzeichnisstruktur zu erstellen, die das Erstellen von Python-Paketen deutlich vereinfacht.

Im ``bobtemplate``-Namespace sind u.a. folgende Pakete zu finden:

`bobtemplates.plone <https://pypi.python.org/pypi/bobtemplates.plone/>`_
    erstellt Python-Pakete für Plone, ggf. auch mit *nested Namespaces*.
`bobtemplates.gillux <https://pypi.python.org/pypi/bobtemplates.gillux/1.1.0>`_
    liefer Vorlagen zum Erstellen von Buildout-Projekten, zum Erstellen eigener
    bobtemplates und Python-Namespace-Paketen, optional mit `nose
    <https://nose.readthedocs.org/en/latest/index.html>`_, `coverage
    <https://pypi.python.org/pypi/coverage/>`_ und `Sphinx
    <http://sphinx-doc.org/>`_-Dokumentationsvorlagen.
`bobtemplates.ielectric <https://github.com/iElectric/bobtemplates.ielectric>`_
    `Pyramid <http://www.pylonsproject.org/projects/pyramid/about>`_ und Python-
    Basis-Paket.
`bobtemplates.niteoweb <https://github.com/niteoweb/bobtemplates.niteoweb>`_
    Plone- und Pyramid-Vorlagen

Installation
============

``mr.bob``und ``bobtemplates``-Pakete lassen sich einfach mit Buildout installieren,
z.B.::

    [buildout]
    parts =
        ...
        mrbob

    [mrbob]
    recipe = zc.recipe.egg
    eggs =
        mr.bob
        bobtemplates.plone

Konfiguration
=============

Mit dem folgenden Aufruf können Antworten für zukünftige Pakete gespeichert werden::

    $ mrbob --remember-answers -O vs.policy bobtemplates:plone_addon
    ...

Anschließend kann diese Konfiguration immer wieder verwendet werden, z.B. mit::

    $ ../bin/mrbob --config .mrbob.ini -O vs.theme bobtemplates:plone_addon

Eine solche Konfigurationsdatei kann auch mit einer URL angespreochen werden, also
z.B.::

    $ ../bin/mrbob --config https://raw.github.com/veit/dotfiles/master/.mrbob.ini bobtemplates:plone_addon

Alternativ kann auch eine globale Konfigurationsdatei erstellt werden in
``~/.mrbob.ini``, z.B.::

    [mr.bob]
    verbose = True

    [variables]
    package.namespace = vs
    author.name = Veit Schiele
    author.email = kontakt@veit-schiele.de
    author.github.user = veit
    author.irc = irc.freenode.org#veit

.. seealso::
    * `mr.bob’s documentation <http://mrbob.readthedocs.org/en/latest/>`_
    * `Git repository <https://github.com/domenkozar/mr.bob>`_

.. toctree::
    :titlesonly:
    :maxdepth: 1

    bobtemplates.plone

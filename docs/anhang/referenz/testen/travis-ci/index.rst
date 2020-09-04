=========
Travis CI
=========

Travice CI ist ein hosted Continuous-Integration-Service.

`Travis CI <http://travis-ci.org/>`_ ist ein gehosteter Continous
Integration Service, mit dem sich Plone-Zusatzprodukte einfach testen lassen.

Installation
============

#. Travis lässt sich mit Ruby Gems installieren::

    $ gem install travis

#. Damit unser Paket getestet werden kann, muss zunächst die ``setup.py``-
   Datei dieses Produkts erweitert werden::

    ...
    install_requires=[
        'setuptools',
        'Products.CMFPlone>=4.2',
        ],
    extras_require={
        'test': ['plone.app.testing'],
        },
    ...

#. Aufsetzen von Travis

   Zunächst melden Sie sich einfach mit Ihrem Github-Account an: `App
   Authorization <http://travis-ci.org/users/auth/github>`_.

#. Anschließend konfigurieren Sie Ihren Travis CI-Server mit einer ``travis.yml``  -Datei im Wurzelverzeichnis
   Ihres Repository::

    ---
    language: python
    python: '2.7'
    install:
    - mkdir -p buildout-cache/eggs
    - mkdir -p buildout-cache/downloads
    - python bootstrap.py -c travis.cfg
    - ./bin/buildout -N -t 3 -c travis.cfg
    script: ./bin/test

   Weitere Konfigurationsmöglichkeiten erhalten Sie in `Travis CI-Konfiguration <travis-ci-konfiguration>`_.

#. Die Datei ``travis.cfg`` sieht dann z.B. so aus::

    [buildout]
    extends =
        http://svn.plone.org/svn/collective/buildout/plonetest/test-4.x.cfg

    parts = test

    package-name = vs.registration
    package-extras = [test]
    #test-eggs = Pillow

    allow-hosts +=
        code.google.com
        robotframework.googlecode.com

    [environment]
    ZSERVER_HOST = 0.0.0.0
    ROBOT_ZOPE_HOST = 0.0.0.0

    [test]
    environment = environment

    [test]
    eggs =
        ${buildout:package-name} ${buildout:package-extras}
        ${buildout:test-eggs}

   ``test-eggs = Pillow``
    Diese Zeile sollte auskommentiert werden sofern PIL für die Tests benötigt wird.

#. Schließlich können Sie noch ein Status-Bild in Ihre ``README.txt``-Datei
   einfügen::

    .. image:: https://secure.travis-ci.org/collective/vs.registration.png
    :target: http://travis-ci.org/collective/vs.registration

.. seealso::
    - `Héctor Verlarde: Integrating Travis CI with your Plone add-ons hosted on GitHub <http://hvelarde.blogspot.fi/2012/08/integrating-travis-ci-with-your-plone.html>`_
    - `Python Testing Tools Taxonomy <http://wiki.python.org/moin/PythonTestingToolsTaxonomy>`_

Apps, Clients and Tools
=======================

- `Travis CI Apps, Clients and Tools <http://docs.travis-ci.com/user/apps/>`_

  - `Travis CLI <https://github.com/travis-ci/travis#readme>`_
  - `TravisPy <http://travispy.readthedocs.org/>`_

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    travis-ci-konfiguration
    travis-ci-sauce-labs-support

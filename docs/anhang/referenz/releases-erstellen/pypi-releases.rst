=============
PyPI-Releases
=============

Python-Pakete werden üblicherweise auf dem Python Package Index (PyPI) veröffentlicht.

Registrieren am Python Package Index (PyPI)
===========================================

Falls Sie noch nicht am Python Package Index (PyPI) registriert sind, tragen Sie
sich bitte zunächst im `Registrierungsformular
<https://pypi.python.org/pypi?:action=register_form>`_ ein. Neben Name,
Passwort und E-Mail-Adresse können Sie sich ggf. auch noch mit dem PGP-Key
authentifizieren.

Anschließend sollten Sie Username und Passwort in einer ``.pypirc``-Datei in
Ihrem Home-Verzeichnis speichern, z.B.::

    [server-login]
    username:veit
    password:secret

``distutils`` benötigt diese Information beim ``register``-Befehl.

Metadaten
=========

In der ``setup.py``-Datei müssen bestimmte Metadaten angegeben werden. Beim
Aufruf von ``python setup.py register`` übermittelt das Skript diese Angaben
auf ``python.org``. Weitere Informationen zu diesen Metainformationen erhalten
Sie in der `PEP 241 <https://www.python.org/dev/peps/pep-0241/>`_: Metadata for
Python Software Packages.

Einige der Metadaten wie ``name`` und ``version`` werden verwendet um den
Dateinamen für die Distributionen zu erstellen. Andere, wie die `Trove
classifiers <https://pypi.python.org/pypi?:action=list_classifiers>`_ werden
ausschließlich von PyPI verwendet.

Folgende Metadaten sind notwendig:

Name
    Der Name des Pakets
Version
    Eine Versionsnummer, z.B. ``4.0.1`` oder ``4.1rc3``.
Summary
    Eine einzeilige Beschreibung des Pakets.
Home-page
    Die URL der Homepage des Pakets.
Author
    Der Name des Autors des Pakets.
Author-email
    Die E-Mail-Adresse des Autors.

    PEP 241 nennt die E-Mail-Adresse als eindeutigen Schlüssel für
    Paket-Kataloge.

License
    Der Name der Lizenz unter der das Paket veröffentlicht wird. Ggf. kann auch
    eine URL einer Lizenz angegeben werden.
Description
    Eine ausführlichere Beschreibung des Pakets.

    Laut PEP 241 ist diese Beschreibung optional, doch erleichtert dies anderen
    das Paket im Python package Index zu finden.

Platform
    Eine Komma-separierte-Liste unterstützter Plattformen.

    In vielen Fällen sollte hier ``Any`` der richtige Eintrag sein.

Außerdem können noch `Trove classifiers`_ für die Beschreibung der Software
anhand eines vordefinierten Vokabulars angegeben werden. Mit ihnen lassen sich
z.B. *Audience* und *Development status* des Pakets angeben.

Beispiel
--------

Schauen wir uns als konkretes Beispiel die `setup.py
<https://svn.plone.org/svn/collective/vs.event/trunk/setup.py>`_-Datei von
`vs.event <https://pypi.python.org/pypi/vs.event/>`_ an::

    from setuptools import setup, find_packages
    import os

    version = '0.2.19'

    setup(name='vs.event',
          version=version,
          description="An extended event content-type for Plone (and Plone4Artists calendar)",
          long_description=open("README.txt").read() + "\n" +
                           open(os.path.join("docs", "HISTORY.txt")).read(),
          # Get more strings from https://www.python.org/pypi?%3Aaction=list_classifiers
          classifiers=[
            "Framework :: Plone",
            "Programming Language :: Python",
            "Topic :: Software Development :: Libraries :: Python Modules",
            ],
          keywords='Zope Plone Event Recurrence Calendar Plone4Artists',
          author='Veit Schiele, Anne Walther, Andreas Jung',
          author_email='vs.event@veit-schiele.de',
          url='http://svn.plone.org/svn/collective/vs.event',
          license='GPL',
          packages=find_packages(exclude=['ez_setup']),
          namespace_packages=['vs'],
          include_package_data=True,
          zip_safe=False,
          install_requires=[
              'setuptools',
              'python-dateutil',
              'dateable.chronos',
              'dateable.kalends',
              'collective.calendarwidget',
              'Products.DataGridField',
              'zope.app.annotation',
              # -*- Extra requirements: -*-
          ],
          entry_points="""
          # -*- Entry points: -*-
          """,
          )

Beachten Sie bitte, dass ``long_description`` aus zwei externen Dateien zusammengesetzt wird,  nämlich ``README.txt`` und   ``HISTORY.txt``.

Dateien hinzufügen
==================
``include_package_data``
    Ist der Wert auf ``True`` gesetzt, so fügt ``setuptools`` automatisch alle
    Dateien innerhalb des Paketverzeichnisses hinzu, die entweder unter CVS-
    oder SVN-Versionskontrolle stehen oder in einer ``MANIFEST.in``-Datei
    beschrieben sind. Für aktuellere Versionen von SVN sowie weitere
    Versionsverwaltungen wie git und Mercurial sind jedoch Plugins erforderlich:

    - `setuptools_subversion
      <https://pypi.python.org/pypi/setuptools_subversion>`_
    - `setuptools_bzr <https://pypi.python.org/pypi/setuptools_bzr>`_
    - `setuptools_hg <https://pypi.python.org/pypi/setuptools_hg>`_
    - `setuptools-git <https://pypi.python.org/pypi/setuptools-git>`_

    Weitere Informationen erhalten Sie in `Including Data Files <https://pythonhosted.org/setuptools/setuptools.html#including-data-files>`_.

Überrüfen
=========

``PKG-INFO``
------------

Distutils ``PKG-INFO`` kann verwendet werden umd die Metadaten aus ``setup.py`` zu überprüfen. Beim Aufruf von ``python setup.py sdist`` erstellt distutils einen sog. *source tarball* im ``dist``-Verzeichnis. Der *tarball* enthält eine ``PKG-INFO``-Datei auf oberster Verzeichnisebene.

PyPI-Testing-Site
-----------------

Schließlich kann zum Testen kann auch die `PyPI-Testing-Site
<https://testpypi.python.org/pypi>`_ verwendet werden.

Registrieren
============

Falls Sie einen PyPI-Account haben und die Zugangsdaten eingetragen sind in ``~/.pypirc`` kann das Paket bei PyPI registriert werden mit::

    $ python setup.py register

Überprüfen der Registrierung
----------------------------

Rufen Sie mit Ihrem Webbrowser https://www.python.org/pypi auf. Dort sollten Sie Ihr Paket in der Liste der letzten 20 aktualisierten Pakete sehen. Sofern Sie angemeldet sind, erscheint Ihr Paket auch in der linken Navigation unter der Überschrift *Your Packages*.

Wenn Sie nun auf den Namen Ihres Pakets klicken, wird Ihnen das Paket angezeigt. In dieser Ansicht erhalten Sie auch einen *Edit*-Link mit dem Sie die generierte Seite korrigieren können.

Upload
======

::

    $ python setup.py sdist upload

``pythonpackages.com``
======================

`pythonpackages.com <https://pythonpackages.com/>`_ bietet eine alternative
Möglichkeit, Releases Ihrer Python-Packages aus einem Github-Repository zu
erstellen und zu testen. Weitere Informationen hierzu erhalten Sie unter
`Introduction <http://docs.pythonpackages.com/en/latest/introduction.html>`_.
Darüberhinaus bietet ``pythonpackages.com`` auch einen `Test Package Index
<http://index.pythonpackages.com/>`_::

    $ cd my.package
    $ python setup.py sdist upload -r http://index.pythonpackages.com
    $ pip install my.package -i http://index.pythonpackages.com

Siehe auch
==========

`jarn.mkrelease <https://pypi.python.org/pypi/jarn.mkrelease>`_
    Einfache Integration von Releases in Buildout-Projekte mit gepinnten
    Versionen.

    `jarn.viewdoc <https://pypi.python.org/pypi/jarn.viewdoc>`_
     erstellt eine Voransicht der Dokumentation eines Pakets, bevor eine Release
     erstellt wird.

`zest.releaser <https://pypi.python.org/pypi/zest.releaser>`_
    automatisiert die Aktualisierung von Versionsnummer, Änderungshistorie und
    Tagging.

    `gocept.zestreleaser.customupload <https://pypi.python.org/pypi/gocept.zestreleaser.customupload>`_
        Plugin für zest.releaser, das das Kopieren eines zuvor erstellten Egg zu
        einem konfigurierbaren Ziel erlaubt.

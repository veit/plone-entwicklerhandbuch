==================
Sphinx-Integration
==================

Sphinx- und ReadTheDocs-Unterstützung für das Robot-Framework.

`sphinxcontrib-robotdoc <http://pypi.python.org/pypi/sphinxcontrib-
robotdoc/>`_ ist eine Erweiterung von `Sphinx <http://sphinx.pocoo.org/>`_,
zur Übernahme der Robot-Framework-Tests.

Dabei werden zwei neue  `Docutils <http://docutils.sourceforge.net/>`_-
Direktiven eingeführt: ``robot_tests`` und ``robot_keywords``. Beide
Direktiven erlauben die folgenden Angaben:

- Filter in Form regulärer Ausdrücke
- Pfadangabe zu den Robot-Framework-Testdaten und -Ressourcen.
- Auswahl der Tests in Form einer Komma-separierten Tag-Liste

Beispiele
=========

Die folgenden Beispiele können z.B. eingebunden werden in ``vs_buildout/src/vs.registration/docs/index.rst``.

- Einbinden aller Tests einer Testsuite::

   .. robot_tests::
      :source: ../src/vs/registration/tests/my_suite.txt

- Alles Tests einer Testsuite, die mit ``Log`` beginnen::

   .. robot_tests:: Log.*
      :source: ../src/vs/registration/tests/my_suite.txt

- Einbinden aller Tests, die mit ``login`` oder ``logout`` getaggt sind::

   .. robot_tests::
      :source: ../src/vs/registration/tests/my_suite.txt
      :tags: login, logout

- Einbinden aller *user keywords* eines Tests oder eine Ressource::

   .. robot_keywords::
      :source: ../src/my_package/tests/acceptance/my_suite.txt

- Einbinden aller *user keywords*, die mit ``Log`` beginnen::

   .. robot_keywords:: Log.*
      :source: ../src/my_package/tests/acceptance/my_suite.txt

ReadTheDocs-Unterstützung
=========================

`ReadTheDocs <http://readthedocs.org/>`_ unterstützt eigene Sphinx-Plugins:

#. Zunächst wird das Plugin in der Sphinx-Konfigurationsdatei (``conf.py``)
   in die Liste der `èxtensions`` eingetragen::

    extensions = ['sphinxcontrib_robotdoc']

#. Das Plugin sollte auf PyPI veröffentlicht worden sein, siehe
   `sphinxcontrib-robotdoc <http://pypi.python.org/pypi/sphinxcontrib-
   robotdoc/>`_.
#. Desweiteren soll das ReadTheDocs-Project mit ``virtualenv`` erstellt
   werden::

    Use virtualenv
    [x]  Install your project inside a virtualenv using setup.py install

#. Es muss eine `pip requirements <http://www.pip-
   installer.org/en/latest/requirements.html>`_-Datei geben, das das Sphinx-
   Plugin (und ggf. die mindestens erforderliche Version) enthält::

    sphinxcontrib-robotdoc>=0.3.4

#. Ggf. kann die ``requirements``-Datei nur für ReadTheDocs bereitgestellt
   werden indem sie in einem Unterverzeichnis erstellt wird, z.B. in
   ``./docs/requirements.txt``.
#. Schließlich geben Sie im ReadTheDocs-Dashboard den Pfad zu Ihrer
   ``requirements``-Datei an::

    Requirements file:
    docs/requirements.txt

Weitere Informationen
=====================

- `Asko Soukka: Embedding Robot Framework tests and keywords into Sphinx
  documentation <http://datakurre.pandala.org/2012/10/embedding-robot-framework-tests-and.html>`_

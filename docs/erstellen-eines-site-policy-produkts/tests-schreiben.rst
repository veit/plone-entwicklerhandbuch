===============
Tests schreiben
===============

Tests erstellen
===============

Statt der bereits angelegten Datei ``src/vs.policy/vs/policy/tests.py`` erstellen wir ein eigenes ``tests``-Modul::

    $ rm -rf src/vs.policy/vs/policy/tests.py
    $ mkdir src/vs.policy/vs/policy/tests
    $ touch src/vs.policy/vs/policy/tests/__init__.py

Test-Fixture
------------

Anschließend definieren wir im neu erstellten ``tests``-Ordner zunächst ein Test-Fixture, eine gleichbleibende Testumgebung mit der Basisklasse ``TestCase``, die an den Layer ``VS_POLICY_INTEGRATION`` gebunden wird. Hierzu erstellen wir im ``tests``-Verzeichnis die Datei ``base.py`` mit folgendem Inhalt::

    import unittest2 as unittest

    from plone.testing import z2
    from plone.app.testing import TEST_USER_NAME
    from plone.app.testing import TEST_USER_PASSWORD

    from vs.policy.tests import layer

    def get_browser(app, loggedIn=True):
        browser = z2.Browser(app)
        if loggedIn:
            auth = 'Basic %s:%s' % (TEST_USER_NAME, TEST_USER_PASSWORD)
            browser.addHeader('Authorization', auth)
        return browser

    class TestCase(unittest.TestCase):
        layer = layer.VS_POLICY_INTEGRATION

    class FunctionalTestCase(unittest.TestCase):
        layer = layer.VS_POLICY_FUNCTIONAL

In ``layer.py`` werden anschließend die Test-Layer ``VS_POLICY_INTEGRATION`` und ``VS_POLICY_FUNCTIONAL`` definiert, die beide auf ``VS_POLICY_LAYER`` basieren::

    from plone.app.testing import applyProfile
    from plone.app.testing import PloneFixture
    from plone.app.testing import PloneSandboxLayer
    from plone.app.testing import PloneTestLifecycle
    from plone.app.testing import setRoles
    from plone.app.testing import TEST_USER_ID
    from plone.testing import z2
    from zope.configuration import xmlconfig

    class VsPolicyFixture(PloneFixture):
        # No sunburst please
        extensionProfiles = ()

    VS_POLICY_FIXTURE = VsPolicyFixture()

    class VsPolicyTestLifecycle(PloneTestLifecycle):
        defaultBases = (VS_POLICY_FIXTURE, )

    class IntegrationTesting(VsPolicyTestLifecycle, z2.IntegrationTesting):
        pass

    class FunctionalTesting(VsPolicyTestLifecycle, z2.FunctionalTesting):
        pass

    class VsPolicyLayer(PloneSandboxLayer):
        defaultBases = (VS_POLICY_FIXTURE, )

        def setUpZope(self, app, configurationContext):
            import vs.policy

            xmlconfig.file("configure.zcml", vs.policy,
                           context=configurationContext)
            z2.installProduct(app, 'vs.policy')

        def tearDownZope(self, app):
            z2.uninstallProduct(app, 'vs.policy')

        def setUpPloneSite(self, portal):
            applyProfile(portal, 'vs.policy:default')

            setRoles(portal, TEST_USER_ID, ['Manager'])
            portal.invokeFactory('Folder', 'test-folder')
            setRoles(portal, TEST_USER_ID, ['Member'])

    VS_POLICY_LAYER = VsPolicyLayer()
    VS_POLICY_INTEGRATION = IntegrationTesting(
        bases=(VS_POLICY_LAYER, ), name="VsPolicyLayer:Integration")
    VS_POLICY_FUNCTIONAL = FunctionalTesting(
        bases=(VS_POLICY_LAYER, ), name="VsPolicyLayer:Functional")

Tests
-----

Die eigentlichen Tests werden in der Datei ``test_test.py`` definiert::

    from vs.policy.tests.base import FunctionalTestCase

    class TestTest(FunctionalTestCase):

        def test_test(self):
            self.assertTrue(True)

Unit Tests, die auf dem Python unittest-Modul, ZopeTestCase und PloneTestCase basieren, müssen sich an einige Namenskonventionen halten:

- Alle Testdateien müssen mit ``test`` beginnen, z.B. ``test_setup.py``.
- In den Testdateien werden Klassen für Testfälle definiert, die ein oder mehrere Testmethoden enthalten können, die ebenfalls mit ``test`` beginnen müssen, z.B. ``test_portal_title``.
- Zunächst wird die Basisklasse importiert, dann die Klassen für die Testfälle und schließlich die Test Suite selbst definiert.
- Jede Testsuite kann aus mehreren Testklassen bestehen. Wird die Testsuite ausgeführt, werden alle Testmethoden aller Testklassen der Test-Suite ausgeführt.
- Innerhalb einer Testklasse kann die ``afterSetUp()``-Methode unmittelbar vor jedem Test aufgerufen werden um Testdaten für diesen Test anzugeben. Nachdem der Test durchgeführt wurde, werden die Transaktionen zurückgenommen, so dass normalerweise keine Artefakte zurückbleiben.
- Werden jedoch Änderungen außerhalb von Zope vorgenommen, müssen diese mit der Methode ``beforeTearDown()`` aufgeräumt werden.
- Die in einer Testklasse verwendeten Methoden wie ``self.assertEqual()`` oder ``self.failUnless()`` sind Assertion-Methoden, und wenn eine von ihnen fehlschlägt, gilt der ganze Test als fehlgeschlagen.

Test- und Hilfsmethoden
-----------------------

Testmethoden überprüfen, ob etwas wahr oder falsch ist. Daher kann aus den Tests auch herausgelesen werden, wie sich Ihr Produkt verhalten soll, welche Fähigkeiten es enthält. Die Liste der Testmethoden ist ausführlich in der Python-Dokumentation für `unittest.TestCaseObjects`_ enthalten. Die häufigsten sind:

``failUnless(expr)``
    stellt sicher, dass der Ausdruck ``expr`` wahr ist.
``assertEqual(expr1, expr2)``
    stellt sicher,dass ``expr1`` gleich ``expr2`` ist.
``assertRaises(exception, callable, ...)``
    stellt sicher, dass beim Aufruf von ``callable`` die Fehlermeldung
    ``exception``  ausgegeben wird.

    **Hinweis:** ``callable`` sollte der Name einer Methode oder ein
    aufrufbares Objekt sein, nicht ein aktueller Aufruf, z.B.::

        self.assertRaises(AttributeError, myObject.myMethod, someParameter)

``fail()``
    Dies ist sinnvoll, wenn ein Test noch nicht fertiggestellt ist oder in
    einem ``if``-Statement, das deutlich macht, dass der Test fehlgeschlagen ist.

.. _`unittest.TestCaseObjects`: http://docs.python.org/lib/testcase-objects.html

ZopeTestCase und PloneTestCase fügen zu den Assertion-Methoden noch weitere hilfreiche Methoden und Variablen hinzu, die mit Zope interagieren. Hier nur kurz die wesentlichen Variablen:

``self.portal``
    Die PloneSite, in der der Test ausgeführt wird.
``self.folder``
    Der ``member``-Ordner des Mitglieds, als der die Tests ausgeführt werden.

Und hier die wesentlichen Hilfsmethoden:

``self.logout()``
    abmelden, d.i. die Rolle ``anonymous`` bekommen;
``self.login()``
    sich erneut anmelden; wird ein Nutzername mit übergeben, erfolgt die
    Anmeldung als dieser Nutzer.
``self.setRoles(roles)``
    durchläuft eine Liste von Rollen, die angenommen werden sollen.

    ``self.setRoles((Manager,))`` lässt Sie beispielsweise die Rolle des
    Managers für eine bestimmte Zeit annehmen.

``self.setPermissions(permissions)``
    analog können auch Berechtigungen für den Testnutzer in ``self.folder``
    angegeben werden;
``self.setGroups(groups)``
    eine Liste von Gruppen, der der aktuelle Nutzer angehören soll.

Mehr über Unit Tests in Python erfahren Sie in der `unittest`_-Python-Dokumentation.

.. _`unittest`: http://docs.python.org/lib/module-unittest.html

Testen
======

Der Testrunner kann nun gestartet werden mit::

    $ ./bin/test -s vs.policy

Wären die Tests geschrieben worden, bevor die Profile erstellt wurden, hätten beide Tests fehlschlagen müssen und der Testrunner folgendes ausgeben::

     AssertionError:"Welcome to Veit Schiele != ''
    …
    AssertionError:'Veit Schiele != 'Plone site'
    Ran 2 tests with 2 failures and 0 errors

Nachdem die Profile angelegt wurden, sollte jedoch keiner der Tests fehlschlagen::

    Ran 2 tests with 0 failures and 0 errors.

Filter
------

``-s my.package``, ``--package my.package``, ``--dir my.package``
    durchsucht die angegebenen Verzeichnisse nach Tests.
``-m test_setup``, ``--module test_setup``
    spezifiziert ein Testmodul als regulären Ausdruck, z.B.::

        $ ./bin/test -s my.package  -m 'test_setup'

``-t  '.*installed.*'``, ``--test test_theme_installed``
    spezifiziert einen Testfilter als regulären Ausdruck, z.B.::

        $ ./bin/test -s vs.policy -m '.*setup.*' -t '.*installed.*'

    Hiermit werden im Paket ``vs.policy`` alle, mit ``installed`` endenden,
    Methoden in allen Testmodulen, die auf ``setup`` enden, durchlaufen.

``-u``, ``--unit``
    durchläuft ausschließlich Unit tests und ignoriert andere ``layer``-Optionen.
``-f``, ``--non-unit``
    durchläuft alle Tests, die keine Unit Tests sind

Report
------

``-v``, ``--verbose``
    führt zu ausführlicherer Ausgabe
``--ndiff``
    falls ein Doctest fehlschlägt, wird ``ndiff.py`` zur Darstellung der
    Unterschiede verwendet
``--udiff``
    falls ein Doctest fehlschlägt, wird Unified Diff zur Darstellung der
    Unterschiede verwendet
``--cdiff``
    falls ein Doctest fehlschlägt, wird Context Diff zur Darstellung der
    Unterschiede verwendet

Analyse
-------

``-d``, ``post-mortem``
    stoppt die Ausführung nach dem ersten nicht-bestandenen Test und ermöglicht
    *post-mortem*-Debugging, d.h. die Debug-Session wird nur gestartet, wenn ein
    Test fehlschlägt.

Setup
------

``--path src/my.package``
    fügt einen Pfad zu Pythons Suchpfad hinzu, wobei die Option mehrfach
    angegeben werden kann.

Weitere Optionen
----------------

Diese erhalten Sie mit::

    $ ./bin/test --help

Wenn die relevanten Tests erfolgreich verliefen, sollten schließlich noch alle Tests durchgeführt werden um sicherzustellen, dass nicht an anderer Stelle etwas gebrochen ist. Wenn alle Tests erfolgreich durchlaufen wurden, erscheint eine Meldung::

    Ran 10 tests with 0 failures and 0 errors in 4.830 seconds.

Falls nicht alle Tests erfolgreich durchlaufen wurden, ändert sich die Meldung::

    Ran 10 tests with 2 failures and 3 errors in 9.688 seconds.

Dabei wurden dann zwei Tests nicht bestanden und drei Tests enthielten Fehler.

roadrunner
==========

`roadrunner`_ ist ein Testrunner für Plone 2.5 bis 3.1, der die testgetriebene
Entwicklung deutlich beschleunigen kann, da er vorab das Standard-Zope- und
Plone-Environment für PloneTestCase läd. zur Installation wird einfach folgendes
in die ``devel.cfg``-Datei eingetragen::

    [buildout]
    parts =
        …
        roadrunner

    [roadrunner]
    recipe = roadrunner:plone
    packages-under-test = vs.policy

Anschließend kann es wie der reguläre Zope-Testrunner aufgerufen werden::

    $ ./bin/roadrunner -s vs.policy

.. _`zc.recipe.testrunner`: http://pypi.python.org/pypi/zc.recipe.testrunner/
.. _`roadrunner`: http://pypi.python.org/pypi/roadrunner

Tipps & Tricks
==============

- Übernehmen Sie Tests z.B. aus Plone wenn diese Ihren eigenen Absichten
  entsprechen.
- Dummy-Implementierungen sind häufig der einzige Weg um bestimmte Funktionen
  zu testen. Siehe auch `CMFPlone/tests/dummy.py`_ für einige Dummy-Objekt-
  Beispiele.
- Tests können auch verwendet werden um Dinge auszuprobieren – sie sind eine
  sichere Umgebung.
- Während des Debugging können ``print``-Statements in den Test eingefügt
  werden um nachvollziehbare Hinweise im Terminal zu erhalten.
- Es kann jedoch auch gleich der Python-Debugger in die Testmethoden importiert
  werden mit::

    import pdb; pdb.set_trace()

  Anschließend können Sie mit ``r`` schrittweise durch den Testkode gehen.

  Mehr zum Python-Debugger erfahren Sie in Debugging_ und in der
  `Python-Dokumentation`_.

.. _`CMFPlone/tests/dummy.py`: http://dev.plone.org/plone/browser/Plone/trunk/Products/CMFPlone/tests/dummy.py
.. _Debugging: ../entwicklungswerkzeuge/debugging
.. _`Python-Dokumentation`: http://docs.python.org/lib/module-pdb.html

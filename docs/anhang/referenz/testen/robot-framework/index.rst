===============
Robot-Framework
===============

Das Robot Framework ist ein generisches Framework zur Durchführung von automatisierten Softwaretests, v.a.  Akzeptanztests.

`Robot <https://code.google.com/p/robotframework/>`_ verwendet für das `Keyword-
Driven Testing <Keyword-Driven Testing>`_ eine tabellenartige Struktur zur
Verwaltung der Testdaten.

`Selenium2Library <http://rtomac.github.com/robotframework-
selenium2library/doc/Selenium2Library.html>`_ ermöglicht, die `Selenium 2
(WebDriver) <http://docs.seleniumhq.org/docs/03_webdriver.jsp>`_-Bibliothek
im Robot-Framework zu verwenden.

Weitere Informationen zur Selenium2Library finden Sie im `Wiki
<https://github.com/rtomac/robotframework-selenium2library/wiki>`_.

Installation
============

#. Beim Erstellen eines neuen Pakets sollte darauf geachtet werden, dass bei der
   Frage nach  ``robot tests`` mit ``true`` geantwortet wird::

    $ ../bin/zopeskel plone_basic vs.registration
    ...
    Expert Mode? (What question mode would you like? (easy/expert/all)?) ['easy']: all
    ...
    robot tests (should the default robot test be included) [false]: true

   Bei einem bestehenden Paket sollte folgendes in die ``setup.py``-Datei
   eingetragen werden::

    extras_require={
        'test': ['plone.app.testing[robot]>=4.2.2']
    },

   Damit wird neben `plone.app.testing
   <http://pypi.python.org/pypi/plone.app.testing>`_ noch die `robotsuite
   <http://pypi.python.org/pypi/robotsuite>`_ und die `robotframework-
   selenium2library
   <http://pypi.python.org/pypi/robotframework-selenium2library>`_ zum Testen
   installiert.

   Zudem ist in ``vs_buildout/src/vs.registration/src/vs/registration/tests/``
   eine ``test_robot.py``-Datei angelegt worden mit::

    from  vs.registration.testing import VS_REGISTRATION_FUNCTIONAL_TESTING
    from plone.testing import layered
    import robotsuite
    import unittest

    def test_suite():
        suite = unittest.TestSuite()
        suite.addTests([
            layered(robotsuite.RobotTestSuite("robot_test.txt"),
                    layer=VS_REGISTRATION_FUNCTIONAL_TESTING)
        ])
        return suite

   Die zugehörige ``robot_test.txt``-Datei sieht dann so aus::

    *** Settings ***

    Library  Selenium2Library  timeout=10  implicit_wait=0.5

    Suite Setup  Start browser
    Suite Teardown  Close All Browsers

    *** Variables ***

    ${BROWSER} =  firefox

    *** Test Cases ***

    Plone site
        [Tags]  start
        Go to  http://localhost:55001/plone/
        Page should contain  Plone site

    *** Keywords ***

    Start browser
        Open browser  http://localhost:55001/plone/  browser=${BROWSER}

#. Schließlich kann der Test aufgerufen werden mit::

    $ cd vs_buildout/src/vs.registration
    $ python bootstrap.py
    $ ./bin/buildout
    $ ./bin/test
    Running vs.registration.testing.VsregistrationLayer:Functional tests:
      Set up plone.testing.zca.LayerCleanup in 0.000 seconds.
      Set up plone.testing.z2.Startup in 0.394 seconds.
      Set up plone.app.testing.layers.PloneFixture in 10.463 seconds.
      Set up vs.registration.testing.VsregistrationLayer in 0.464 seconds.
      Set up plone.testing.z2.ZServer in 0.503 seconds.
      Set up vs.registration.testing.VsregistrationLayer:Functional in 0.000 seconds.
      Running:

      Ran 1 tests with 0 failures and 0 errors in 3.026 seconds.
    Running vs.registration.testing.VsregistrationLayer:Integration tests:
      Tear down vs.registration.testing.VsregistrationLayer:Functional in 0.000 seconds.
      Tear down plone.testing.z2.ZServer in 5.152 seconds.
      Set up vs.registration.testing.VsregistrationLayer:Integration in 0.000 seconds.
      Running:

      Ran 1 tests with 0 failures and 0 errors in 0.004 seconds.
    Tearing down left over layers:
      Tear down vs.registration.testing.VsregistrationLayer:Integration in 0.000 seconds.
      Tear down vs.registration.testing.VsregistrationLayer in 0.002 seconds.
      Tear down plone.app.testing.layers.PloneFixture in 0.092 seconds.
      Tear down plone.testing.z2.Startup in 0.007 seconds.
      Tear down plone.testing.zca.LayerCleanup in 0.004 seconds.
    Total: 2 tests, 0 failures, 0 errors in 20.510 seconds.

   Daneben werden noch Log-Dateien erstellt in ``parts/test/``, z.B. ``robot_log.html``:

   |Robot log|

   .. |Robot log| image:: robot-test-log.png
      :class: image-right

.. seealso::
    - `Asko Soukka: Getting started with Robot Framework and plone.app.testing
      <http://datakurre.pandala.org/2012/09/getting-started-with-robotframework-and.html>`_
    - `plone.act documentation <http://ploneact.readthedocs.org/en/latest/index.html>`_
    - `Asko Soukka: Meet the Robot family (for Plone developers) <http://datakurre.pandala.org/2013/09/meet-robot-family-for-plone-developers.html>`_
    - `Writing Robot Framework tests for Plone <http://developer.plone.org/reference_manuals/external/plone.app.robotframework/#writing-robot-framework-tests-for-plone>`_

    - Beispiele:

      - `plone.act <https://github.com/gotcha/plone.act/blob/master/src/plone/act/plone.txt>`_
        Robot-Framework-Ressourcen zum Testen von Plone

      - `plone.app.toolbar <https://github.com/plone/plone.app.toolbar/blob/master/plone/app/toolbar/tests/acceptance/toolbar.txt>`_
      - `plone.app.deco <https://github.com/plone/plone.app.deco/tree/master/plone/app/deco/tests/acceptance>`_
      - `plone.app.collection <https://github.com/plone/plone.app.collection/blob/master/plone/app/collection/tests/acceptance/test_collection.txt>`_

    - `Selenium2Library keywords <http://rtomac.github.com/robotframework-selenium2library/doc/Selenium2Library.html>`_
    - `Robot Framework built-in keywords <http://robotframework.googlecode.com/hg/doc/libraries/BuiltIn.html?r=2.7.5>`_

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    sphinx-integration
    accessibility-analyse

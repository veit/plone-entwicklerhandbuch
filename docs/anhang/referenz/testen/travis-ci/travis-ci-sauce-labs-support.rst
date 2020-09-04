============================
Travis CI Sauce Labs-Support
============================

Die Nutzung von `Sauce Labs <http://saucelabs.com/>`_ zusammen mit dem Robot-
Framework ist ähnlich einem eigenen Selenium-Grid. Vor allem erfordert es, dass
die Browser Passwörter eingeben können. Dies kann mit einigen wenigen Variablen
in ``vs_buildout/src/vs.registration/src/vs/registration/tests/robot_test.txt``
konfiguriert werden::

 *** Settings ***

 Library  Selenium2Library  timeout=10  implicit_wait=0.5

 Suite Setup  Start browser
 Suite Teardown  Close All Browsers

 *** Variables ***

 ${ZOPE_HOST} =  localhost
 ${ZOPE_PORT} =  55001
 ${ZOPE_URL} =  http://${ZOPE_HOST}:${ZOPE_PORT}

 ${PLONE_SITE_ID} =  plone
 ${PLONE_URL} =  ${ZOPE_URL}/${PLONE_SITE_ID}

 ${BROWSER} =  Firefox
 ${REMOTE_URL} =
 ${DESIRED_CAPABILITIES} =  platform:Linux
 ${BUILD_NUMBER} =  manual

 *** Test Cases ***

 Plone site
     [Tags]  start
     Go to  ${PLONE_URL}
     Page should contain  Plone site

 *** Keywords ***

 Start browser
     ${BUILD_INFO} =  Set variable
     ...           build:${BUILD_NUMBER},name:${SUITE_NAME} | ${TEST_NAME}
     Open browser  ${PLONE_URL}  ${BROWSER}
     ...           remote_url=${REMOTE_URL}
     ...           desired_capabilities=${DESIRED_CAPABILITIES},${BUILD_INFO}

Die Variablen bedeuten im Einzelnen:

``ZOPE_HOST``
 Angabe for den Host des ZServer.

 Dar Standardwert ist ``localhost``. For Tests mit dem Internet Explorer ist
 jedoch die Angabe ``0.0.0.0`` erforderlich.

``ZOPE_PORT``
 Angabe des Ports, an dem der ZServer lauscht.

 Der Standardwert ist ``55001``.

``ZOPE_URL``
 Root-Variable für die URL der Zope-Anwendung.
``PLONE_SITE_ID``
 ID der Plone-Site.
``PLONE_URL``
 URL der Plone-Site.
``BROWSER``
 Browser, mt dem der Test durchgeführt werden soll.
``REMOTE_URL``
 URL des zu verwendenden Selenium-Hubs.
``DESIRED_CAPABILITIES``
 spezifiziert verschiedene Parameter des Selenium-Hubs, z.B. die Browser-
 Version.
``BUILD_NUMBER``
 Travis-CI-Build auf Sauce Labs.

Nun wird eine ``.travis.yml``-Datei erstellt um Travis-CI mitzuteilen, welches
Envirinment verwendet und welche Tests ausgeführt werden sollen::

 ---
 language: python
 python: '2.7'
 install:
 - mkdir -p buildout-cache/eggs
 - mkdir -p buildout-cache/downloads
 - python bootstrap.py -c travis.cfg
 - ./bin/buildout -N -t 3 -c travis.cfg
 - curl -O http://saucelabs.com/downloads/Sauce-Connect-latest.zip
 - unzip Sauce-Connect-latest.zip
 - java -jar Sauce-Connect.jar $SAUCE_USERNAME $SAUCE_ACCESS_KEY -i $TRAVIS_JOB_ID -f CONNECTED &
 - JAVA_PID=$!
 before_script:
 - bash -c "while [ ! -f CONNECTED ]; do sleep 2; done"
 script: ./bin/test
 after_script:
 - kill $JAVA_PID
 env:
   global:
   - ROBOT_BUILD_NUMBER=travis-$TRAVIS_BUILD_NUMBER
   -  ROBOT_REMOTE_URL=http://$SAUCE_USERNAME:$SAUCE_ACCESS_KEY@ondemand.saucelabs.com:80/wd/hub
   matrix:
   - ROBOT_BROWSER=firefox ROBOT_DESIRED_CAPABILITIES=tunnel-identifier:$TRAVIS_JOB_ID
   - ROBOT_BROWSER=chrome ROBOT_DESIRED_CAPABILITIES=tunnel-identifier:$TRAVIS_JOB_ID
   - ROBOT_BROWSER=internetexplorer ROBOT_DESIRED_CAPABILITIES=tunnel-identifier:$TRAVIS_JOB_ID

``SAUCE_USERNAME`` und ``SAUCE_ACCESS_KEY``
 Nutzername und Passwort verschlüsselt als Umgebungsvariable.

 ``travis encrypt`` schreibt die verschlüsselten Werte direkt in die ``.travis.yml``-Datei::

 $ travis encrypt SAUCE_USERNAME=myusername -r mygithubname/example.product --add env.global
 $ travis encrypt SAUCE_ACCESS_KEY=myaccesskey -r mygithubname/example.product --add env.global

``matrix``
 Aktuell erlaubt Sauce Labs drei gleichzeitige Verbindungen für Open-Source-
 Projekte, z.B. für drei verschiedene Browser.

 Achten Sie bei Open-Source-Projekten darauf, dass Sie nicht Ihren privaten
 Zugang nutzen sondern denjenigen des Projekts. Hierfür ist die öffentliche URL
 des Repository erforderlich.

Schließlich sollten die Travis-CI-Tests für Ihr Produkt auf Travis-CI.org oder GitHub eingerichtet werden.

.. seealso::
    - `Asko Soukka: Cross-browser test your Plone add-on with Robot Framework, Travis-CI and Sauce Labs <http://datakurre.pandala.org/2013/03/cross-browser-test-your-plone-add-on.html>`_

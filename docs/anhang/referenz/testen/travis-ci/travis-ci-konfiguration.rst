=======================
Travis CI-Konfiguration
=======================

Travice CI bietet umfangreiche Konfigurationsmöglichkeiten.

Die Konfiguration des Travis CI-Server erfolgt in der ``travis.yml`` -Datei im
Wurzelverzeichnis Ihres Repository.

Hier stehen Ihnen u.a. zusätzliche Konfigurationsmöglichkeiten zur Verfügung,
u.a.:

``language``
 gibt nicht nur die Sprache an, sondern ggf. auch die Sprachversionen, mit
 denen getestet werden soll::

  language: python
  python:
    - 2.6
    - 2.7

``env``
 Umgebungen, in der die Tests ausgeführt werden sollen, also z.B.::

  env:
    - PLONE_VERSION=4.2
    - PLONE_VERSION=4.3

 Ein vollständiges Beispiel hierfür finden Sie in
 https://github.com/plone/plone.api/blob/master/.travis.yml.

``services``
 Dienste, die vor dem Testen bereitstehen sollen, z.B.::

  - riak     # will start riak
  - rabbitmq # will start rabbitmq-server
  - memcache # will start memcached

 Eine vollständige Liste der zur Verfügung stehenden Services finden Sie in
 `Configure Your Projects to Use Services in Tests <http://about.travis-ci.org/docs/user/database-setup/#Configure-Your-Projects-to-Use-Services-in-Tests>`_.

``before_install``
 Aufruf, der vor der Installation ausgeführt werden soll, z.B. um ein GUI
 *headless* testen zu können::

  - "export DISPLAY=:99.0"
  - "sh -e /etc/init.d/xvfb start"

 Weitere Informationen hierzu erhalten Sie in `GUI & Headless browser testing on
 travis-ci.org <http://about.travis-ci.org/docs/user/gui-and-headless-browsers/#GUI-%26-Headless-browser-testing-on-travis-ci.org>`_.

``install``
 Installation der Testumgebung, z.B.::

  - unzip Sauce-Connect-latest.zip
  - java -jar Sauce-Connect.jar $SAUCE_USERNAME $SAUCE_ACCESS_KEY -i $TRAVIS_JOB_ID -f CONNECTED &
  - JAVA_PID=$!

``before_script``
 Aufruf, der unmittelbar vor einem Test aufgerufen werden soll, z.B.::

  bash -c "while [ ! -f CONNECTED ]; do sleep 2; done"

``test``
 Testaufruf, z.B.::

  ./bin/test

``after_script``
 Aufruf, der unmittelbar nach dem Test durchgeführt wird, z.B.::

  kill $JAVA_PID

``branches``
 Blacklist und Whitelist von zu testenden Branches, z.B.::

  # blacklist
  branches:
    except:
      - legacy
      - experimental

  # whitelist
  branches:
    only:
      - master
      - stable

``notifications``
 Benachrichtigungen, , z.B.::

  notifications:
    irc:
      email:
        - "kontakt@veit-schiele.de"
      channels:
        - "irc.freenode.org#sprint"
      on_success: never
      on_failure: always
      template:
        - "%{repository}#%{build_number} (%{branch} - %{commit} : %{author}): %{message}"
        - "Change view : %{compare_url}"
        - "Build details : %{build_url}"

Skip build
==========

Falls nach einem ``push`` kein neuer Travis-Build erstellt werden soll, z.B. bei Änderungen in der Dokumentation, so kann dies einfach beim Commit angegeben werden::

 $ git commit -m 'Typo in README.rst [ci skip]'

======
Sentry
======

Mit Sentry lassen sich in Echtzeit Fehler agregieren und protokollieren. Dabei kann Sentry plattform-unabhängig eingesetzt werden.

Das Sentry-Paket ist in seinem Kern nur ein einfacher Web-Server mit speziellem
UI. Es behandelt die Authentifizierung von Clients (wie `Raven
<https://github.com/getsentry/raven-python>`_) und die gesamte Logik zur
Speicherung und Aggregation. Dabei liefert Sentry eine vollständige API zum
Senden von Ereignissen aus jeder Sprache in jede Anwendung.

Buildout-Konfiguration
======================

::

    [buildout]
    ...
    eggs =
        ...
        raven

    [instance1]
    ...
    event-log-custom =
        %import raven.contrib.zope
        <logfile>
          path ${buildout:directory}/var/{:_buildout_section_name_}.log
          level INFO
        </logfile>
        <sentry>
          dsn YOUR_DSN
          level ERROR
        </sentry>

.. seealso::
    * `Documentation <http://sentry.readthedocs.org/en/latest/>`_

=======================
haufe.requestmonitoring
=======================

Detaillierte Request-Logging-Funktionalität für die ab Zope 2.10 verfügbaren Publication Events.

Home
====

http://pypi.python.org/pypi/haufe.requestmonitoring

Anforderungen
=============

- Zope 2.12

  Für Zope 2.10 ist ein Backport der *Publication Events* verfügbar in
`ZPublisherEventsBackport`_. Dieser wird benötigt und lässt sich mit
Buildout einfach durch `plone.postpublicationhook`_ unter Angabe von
``[Zope2.10]`` installieren::

    eggs =
        ...
        plone.postpublicationhook [Zope2.10]

.. _`ZPublisherEventsBackport`: http://pypi.python.org/pypi/ZPublisherEventsBackport
.. _`plone.postpublicationhook`: http://pypi.python.org/pypi/plone.postpublicationhook/

Installation
============

Um ``haufe.requestmonitoring`` zu installieren, muss es einfach in der
``buildout.cfg``-Datei den ``zcml``-Optionen im  ``Instanz``-Abschnitt
hinzugefügt werden::

    [instance-base]
    ...
    eggs +=
        ...
        haufe.requestmonitoring
        threadframe
        zope.app.appsetup
    zcml +=
        ...
        haufe.requestmonitoring

Aktivierung
===========

Zur Aktivierung von ``haufe.requestmonitoring`` erhält die Instanz einen Abschnitt ``product-config`` mit dem Namen ``successlogging`` und dem Schlüssel ``filebase``. Dieser gibt den Basisnamen der Log-Dateien an, in unserem Fall ``request``::

    [instance-base]
    ...
    zope-conf-additional =
        <product-config successlogging>
            filebase /home/veit/vs_buildout/var/log/request
        </product-config>

        %import haufe.requestmonitoring
        <requestmonitor requestmonitor>
            period 5s
            <monitorhandler dumper>
                factory haufe.requestmonitoring.DumpTraceback.factory
                # 0 means no repetition.
                # A negative value means indefinitely.
                repeat -1
                time 10s
            </monitorhandler>
        </requestmonitor>

Beim Logging werden dann zwei Dateien unterschieden: ``<base>_good.<date>``
und ``<base>_bad.<date>``. Üblicherweise werden Antwortzeiten über 500 ms
als `unsuccessful` bezeichnet. Falls dieser Standardwert geändert werden
soll, kann ein spezieller ``ISuccessFull``-Adapter registriert werden.

Nachdem das Buildout-Skript durchlaufen und der ZEO-Cluster neu gestartet
wurde, sind die Subscriber ``IPubStart`` und ``IPubSuccess`` bzw.
``IPubFailure`` registriert. Für jedes dieser Events wird nun ein Eintrag
in die Log-Datei geschrieben in der Form::

    timestamp status request_time type request_id request_info

Monitoring
==========

Mit ``DumpTraceback`` werden diejenigen Anfragen protokolliert, die nach
der in ``period`` angegebenen Zeit nach Anfragen sucht, die länger laufen
als die in ``time`` angegebene Zeit::

    %import haufe.requestmonitoring
    <requestmonitor requestmonitor>
        period 5s
        <monitorhandler dumper>
            factory Haufe.RequestMonitoring.DumpTraceback.factory
            # 0 --> no repetition
            repeat -1
            time 10s
        </monitorhandler>
    </requestmonitor>

Eine typische Ausgabe sieht dann so aus::

    2009-08-11 14:29:09 INFO Zope Ready to handle requests
    2009-08-11 14:29:09 INFO RequestMonitor started
    2009-08-11 14:29:14 INFO RequestMonitor monitoring 1 requests
    2009-08-11 14:29:19 INFO RequestMonitor monitoring 1 requests
    2009-08-11 14:29:24 INFO RequestMonitor monitoring 1 requests
    2009-08-11 14:29:24 WARNING RequestMonitor.DumpTrace Long running request
    Request 1 "/foo" running in thread -497947728 since 14.9961140156s
    Python call stack (innermost first)
    Module /home/junga/sandboxes/review/parts/instance/Extensions/foo.py, line 4, in foo
    Module Products.ExternalMethod.ExternalMethod, line 231, in __call__
    - __traceback_info__: ((), {}, None)
    Module ZPublisher.Publish, line 46, in call_object
    Module ZPublisher.mapply, line 88, in mapply
    Module ZPublisher.Publish, line 126, in publish
    Module ZPublisher.Publish, line 225, in publish_module_standard
    Module ZPublisher.Publish, line 424, in publish_module
    Module Products.ZopeProfiler.ZopeProfiler, line 353, in _profilePublishModule
    Module Products.ZopeProfiler.MonkeyPatcher, line 35, in __call__
    Module ZServer.PubCore.ZServerPublisher, line 28, in __init__

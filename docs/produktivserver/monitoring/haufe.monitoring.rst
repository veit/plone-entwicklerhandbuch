================
haufe.monitoring
================

Monitoring von Sets von ZEO-Clients mit Aggregation von Error Logs, Instanzen, Threads Loads und VM-Datengröße.

Home
====

http://pypi.python.org/pypi/haufe.monitoring

Installation
============

::

    [instance-base]
    …
    eggs +=
        haufe.monitoring
    zcml +=
        haufe.monitoring

Nachdem das Buildout-Skript durchlaufen und der ZEO-Cluster neu gestartet
wurde, können Sie in den Monitoring-View ``@@monitor`` aufrufen, z.B.
``http://mysite/@@monitor``.

.. note:: Da momentan noch einige Sicherheitsangaben offen sind, sollte
   ``haufe.monitoring`` aktuell nur in internen Netzen verwendet werden.

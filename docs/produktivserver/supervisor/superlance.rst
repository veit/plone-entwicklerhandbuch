==========
superlance
==========

superlance ist ein Plugin für supervisord zum Monitoring und Controlling der unter supervisor laufenden Prozesse.

Installation
============

`superlance <http://pypi.python.org/pypi/superlance>`_ kann einfach mit
Buildout installiert werden::

    [supervisor]
    recipe = collective.recipe.supervisor
    plugins =
        superlance

    eventlisteners =
        memmon  TICK_60  ${buildout:bin-directory}/memmon [-g app=1GB]
        httpok1  (startsecs=600)  TICK_3600  ${buildout:bin-directory}/httpok  [-p app:instance1 -t 30 http://127.0.0.1:8010/]
        httpok2  (startsecs=600)  TICK_3600  ${buildout:bin-directory}/httpok  [-p app:instance2 -t 30 http://127.0.0.1:8020/]

Nach dem Durchlaufen von Buildout sollten u.a. zusätzlich folgende Plugins im ``bin``-Verzeichnis installiert sein:

``crashmail``
    schickt eine E-Mail-Benachrichtigung an eine vorkonfigurierte Adresse
    wenn ein Prozess hängt.
``memmon``
    startet einen Prozess neu, wenn dieser zu viel Arbeitsspeicher
    verbraucht. Damit kann aktiv sog. ``MemoryErrors`` vorgebeugt werden.
``httpok``
    falls Threads hängen bleiben, wird der Prozess automatisch neu
    gestartet

.. seealso::
    * `Superlance documentation`_

.. _`Superlance documentation`: http://readthedocs.org/docs/superlance/en/latest/index.html

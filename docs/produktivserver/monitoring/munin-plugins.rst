=============
Munin-plugins
=============

`redturtle.munin`_ stellt aktuell vier Plugins für Munin bereit:

``zopethreads``
 protokolliert die freien Zope-Threads
``zopecache``
 protokolliert die Datenbank-Cache-Parameter
``zodbactivity``
 protokolliert die Aktivität der ZODB
``zopememory``
 protokolliert die Speicherverwendung von Zope unter Linux

Dabei wird `gocept.munin`_ für die Registrierung dr Plugins verwendet.

Installation und Konfiguration
==============================

#. Zur Installation kann folgendes in der ``deploy.cfg``-Datei angegeben werden::

    [instance]
    ...
    eggs =
        ...
        redturtle.munin
    zcml =
        ...
        redturtle.munin

#. Um das Plugin-Hilfsskript zu erstellen, wird zusätzlich noch ein ``[munin]``-Abschnitt in die ``deploy.cfg`` eingetragen::

    [buildout]
    parts =
        ...
        munin1

    [munin1]
    recipe = zc.recipe.egg
    eggs = redturtle.munin
    arguments = http_address='${instance:http-address}', user='${instance:user}'

   Die Werte in der ``arguments``-Option werden zur Generierung des Hilfsskripts verwendet, das dann als Munin-Plugin verwendet wird. Die Angaben für ``ip_address``, ``http_address``, ``port_base`` und ``user`` können hier kommasepariert angegeben werden.

#. Für jeden weiteren ZEO-Client wird dann ein weiterer Abschnitt eingefügt.

#. Nun sollte das Plugin folgendermaßen aufgerufen werden können::

    http://localhost:8081/@@redturtle.munin.plugins/zopethreads

   Der Name des View ``zopethreads`` entspricht dabei dem Namen des Plugins. Der View selbst kann nur mit den Rechten ``View management screens`` aufgerufen werden.

#. Nun werden noch Symlinks für die Hilfsskripte in ``myproject/bin`` zum Munin-Plugin-Verzeichnis gelegt wobei das Hilfsskript selbst diese Symlinks setzen kann::

    $ bin/munin install /opt/munin/etc/plugins [<prefix>] [<suffix>]

   Alternativ können die Symlinks auch selbst erstellt werden::

    $ cd /opt/munin/etc/plugins
    $ ln -s ~/myproject/bin/munin vs_zodbactivity_mysite1

   ``/opt/munin/etc/plugins``
    ist dabei Ihr ``munin``-Verzeichnis
   ``~/myproject/``
    ist das Verzeichnis des Buildout-Projekts
   ``zodb_activity``
    ist der Name des Plugins
   ``vs``
    ist der Prefix-Wert
   ``mysite1``
    ist der Suffix-Wert, der in Munin angezeigt wird.

#. Schließlich können Sie noch überprüfen, ob das Plugin in Munin ordentlich konfiguriert ist::

    $ cd /opt/munin/etc/plugin-conf.d/
    $ vim redturtle.conf
    ... [vs_*_mysite1]
    ... env.AUTH admin:secret
    ... env.URL http://localhost:8081/@@redturtle.munin.plugins/%s

.. _`redturtle.munin`: http://plone.org/products/redturtle.munin
.. _`gocept.munin`: http://pypi.python.org/pypi/gocept.munin/

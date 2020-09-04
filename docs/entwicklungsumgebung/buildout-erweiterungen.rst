======================
Buildout-Erweiterungen
======================

``extends``
===========

Im Buildout-Abschnitt können mit ``extends`` mehrere Konfigurationsdateien eingebunden werden. Auf diese Weise können dann auch umfangreiche Konfigurationen, wie z.B. die Installation der libxml2- und libxslt-Bibliotheken in eine eigene Konfigurationsdatei ``lxml.cfg`` mit folgendem Inhalt ausgelagert werden::

 [lxml]
 parts =
    staticlxml
    pylxml

 [pylxml]
 recipe=zc.recipe.egg
 interpreter=pylxml
 eggs=
     lxml

 [staticlxml]
 recipe = z3c.recipe.staticlxml
 egg = lxml

Anschließend kann diese Konfigurationsdatei mit all ihren Abschnitten in die ``buildout.cfg``-Datei eingebunden werden mit::

 [buildout]
 extends =
     lxml.cfg

 parts =
     ${lxml:parts}
     …

Es kann auch eine URL angegeben werden, also z.B.::

 [buildout]
 extends =
     http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/entwicklungsumgebung/lxml.cfg

Umgekehrt kann auch die ``buildout.cfg``-Datei in eine andere Konfiguration übernommen werden, siehe hierzu `Buildout für Produktivserver`_.

Setuptool-Bugfix
================

Mit `jarn.setuptoolsfixer`_ wird ein Bug in den Setuptools behoben, der auftritt sofern die Homepage oder Download-URL eines Pakets nicht erreichbar ist, das Paket jedoch in PyPI zur Verfügung steht.

.. _`jarn.setuptoolsfixer`: http://pypi.python.org/pypi/jarn.setuptoolsfixer

Shell-Befehle
=============

Mit `plone.recipe.command`_ können Sie eigene Shell-Befehle während der Installation oder des Updates durchführen. Somit können Sie zum Beispiel der Zope-Instanz externe Methoden im Verzeichnis ``parts/instance/Extension`` zur Verfügung stellen::

 [extensions]
 recipe = plone.recipe.command
 command =
     ln -sf ${buildout:directory}/Extensions/*  ${instance:location}/Extensions/
 update-command =
     ${extensions:command}

Python-Skripte
==============

`buildout.extensionscripts`_ erlaubt die Verwendung von Python-Skripten als Buildout-Erweiterungen.

.. _`buildout.extensionscripts`: http://pypi.python.org/pypi/buildout.extensionscripts/

Die Buildout-Konfiguration kann dann z.B. so aussehen::

 [buildout]
 extensions =
     …
     buildout.extensionscripts
 …
 extension-scripts =
     ${buildout:directory}/buildout-utils.py:patchScriptGeneration

Und ``buildout-utils.py`` kann dann z.B. so aussehen::

 # Workaround for https://bugs.launchpad.net/zc.buildout/+bug/164629

 def patchScriptGeneration(buildout):
     from zc.buildout import easy_install
     if not 'sys.exit(' in easy_install.script_template:
         easy_install.script_template = easy_install.script_template.replace(
             "%(module_name)s.%(attrs)s(%(arguments)s)",
             "sys.exit(%(module_name)s.%(attrs)s(%(arguments)s))")

User-crontab
============

Das Rezept ``z3c.recipe.usercrontab`` ändert die *crontab*-Einträge des Nutzers. So kann z.B. für den ``@reboot``-Eintrag folgendes in der ``buildout.cfg``-Datei angegeben werden::

 [buildout]
 …
 parts =
     …
     crontab

 [crontab]
 recipe = z3c.recipe.usercrontab
 times = @reboot
 command = ${buildout:directory}/bin/instance start

Dabei kann eine Buildout-Konfigurationsdatei auch mehrere *crontab*-Abschnitte enthalten.

Templates verwenden
===================

Mit `collective.recipe.template`_ lassen sich Textdateien aus Vorlagen erstellen wobei die ``buildout``-Variablen verwendet werden können. Hierzu wird in der ``buildout.cfg``-Datei z.B. folgender neuer Abschnitt definiert::

 [buildout]
 parts =
    …
    logrotate

 …
 [logrotate]
 recipe = collective.recipe.template
 input = templates/logrotate.conf
 output = ${buildout:directory}/etc/logrotate.conf

Und wenn ein Auszug aus ``templates/logrotate.conf``-Datei so aussieht::

 …
 ${buildout:directory}/var/log/instance.log {
     postrotate
         ${buildout:bin-directory}/instance logreopen
     endscript
 }

sieht dieser Auszug in der generierten  Datei ``myproject/etc/logrotate.conf`` so aus::

 …
 /home/veit/myproject/var/log/instance.log {
     postrotate
         /home/veit/myproject/instance logreopen
     endscript
 }

.. _`Buildout für Produktivserver`: http://www.veit-schiele.de/dienstleistungen/technische-dokumentation/plone-entwicklerhandbuch/produktivserver
.. _`plone.recipe.command`: http://pypi.python.org/pypi/plone.recipe.command
.. _`collective.recipe.template`: http://pypi.python.org/pypi/collective.recipe.template

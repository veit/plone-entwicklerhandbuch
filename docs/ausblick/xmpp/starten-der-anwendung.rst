=====================
Starten der Anwendung
=====================

Nach der Installation und Konfiguration können die Diente gestartet werden::

 $ ./bin/ejabberdctl restart
 $ ./bin/nginx  start
 $ ./bin/instance start

supervisord
===========

Mit `supervisord <http://supervisord.org/>`_ lässt sich das Starten und Stoppen der Dienste automatisieren. Zur Installation von supervisord wird folgendes in der Buildout-Konfiguration eingetragen::

 [supervisor]
 recipe = zc.recipe.egg
 eggs = supervisor

 [supervisor-conf]
 recipe = collective.recipe.template
 input = ${buildout:directory}/templates/supervisord.conf.in
 output = ${buildout:directory}/etc/supervisord.conf

Die Vorlage für die Konfigurationsdatei sieht dann folgendermaßen aus: `supervisord.conf.in <supervisord.conf.in/view>`_.

Anschließend lassen sich die Dienste starten mit::

 $ ./bin/supervisord

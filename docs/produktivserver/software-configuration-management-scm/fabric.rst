======
Fabric
======

Fabric ist eine Python-Bibliothek, die die Verwaltung von Deployments und Aufgaben der Systemadministration deutlich vereinfacht.

Sie lässt sich einfach mit Buildout installieren. Hierzu erstellen wir z.B. eine ``fabric.cfg``-Datei mit folgendem Inhalt::

 [buildout]
 parts += fabric

 [versions]
 fabric = 1.0.0
 paramiko = 1.7.6
 pycrypto = 2.3

 [fabric]
 recipe = zc.recipe.egg
 eggs =
     setuptools
     fabric

Anschließend kann das Skript ``fabfile.py`` erstellt werden::

 from __future__ import with_statement
 from fabric.api import cd, env, local, run, sudo

 def www():
     env.hosts = ['www.veit-schiele.de']
     env.shell = '/bin/sh -c'
     env.sudo_prefix = "sudo -S -p '%s' -H "
     env.code_root = '/srv/www.veit-schiele.de'
     env.code_user = 'zope'

 def update():
     with cd(env.code_root):
         sudo('nice svn up', user=env.code_user)

 def rebuild():
     with cd(env.code_root):
         sudo('nice bin/buildout -c deploy.cfg', user=env.code_user)

 def restart():
     with cd(env.code_root):
         sudo('nice bin/supervisorctl reload', user=env.code_user)

 def start():
     with cd(env.code_root):
         sudo('nice bin/supervisord', user=env.code_user)

 def stop():
     with cd(env.code_root):
         sudo('nice bin/supervisorctl shutdown', user=env.code_user)

 def deploy():
     update()
     rebuild()
     restart()

Ein weiteres Beispiel zur lokalen Installation eines auf dem Server erstellten Snapshots finden Sie in diesem `fabric.py <fabfile.py/view>`_.

.. seealso::
    * `Fabric documentation`_

.. _`Fabric documentation`: http://docs.fabfile.org/

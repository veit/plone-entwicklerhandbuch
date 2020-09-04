============
Installation
============

``Deliverance``  lässt sich einfach mit Buildout installieren. Hierzu erstellen Sie eine ``deliverance.cfg``-Datei mit folgendem Inhalt::

 [buildout]
 parts =
     lxml
     server

 # Change the number here to change the version of Plone being used
 extends =

 versions = versions
 # Add additional egg download sources here. dist.plone.org contains archives
 # of Plone packages.
 find-links =

 # Add additional eggs here
 eggs =

 # Reference any eggs you are developing here, one per line
 # e.g.: develop = src/my.package
 develop =

 [versions]
 Deliverance = 0.6.0
 WebOb = 0.9.8
 lxml = 2.2.4

 [lxml]
 recipe = z3c.recipe.staticlxml
 egg = lxml
 force = false

 [server]
 recipe = zc.recipe.egg

 eggs =
     lxml
     PasteScript
     Deliverance
 interpreter = py

Nun sollte Buildout problemlos durchlaufen werden::

 $ ./bin/buildout -c deliverance.cfg
 ...
 Generated script '/home/veit/deliverance_buildout/bin/paster'.
 Generated script '/home/veit/deliverance_buildout/bin/deliverance-proxy'.
 Generated interpreter '/home/veit/deliverance_buildout/bin/py'.

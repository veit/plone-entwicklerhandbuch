=====
Diazo
=====

Diazo ist eine Weiterentwicklung von XDV und teilt mit `Deliverance`_ die folgenden Vorteile:

- Diazo ist im Gegensatz zu `plone.app.theming`_ nicht Plone-spezifisch, sodass das Theme auch für weitere Webanwendungen wie Trac, Mailman, Wordpress etc. genutzt werden kann.
- Mit `Diazo`_ lassen sich auch einfach Mashups verschiedener Webinhalte darstellen.

.. _`Deliverance`: http://packages.python.org/Deliverance/
.. _`plone.app.theming`: http://pypi.python.org/pypi/plone.app.theming
.. _`Diazo`: http://diazo.org/

Diazo hat gegenüber Deliverance die folgenden Vorteile:

- Die Regeln sind einfacher
- Die Entwicklung wird von der Plone-Community getragen.

Diazo lässt sich auf zweierlei Arten aufsetzen:

- als einfacher XSLT-Proxy
- zusammen mit WSGI-Middleware-Filtern; dann sollte beim Installieren des Diazo-Eggs zusätzlich ``[wsgi]`` angegeben werden.

Installation
============

#. Erstellen eines Buildout-Verzeichnisses::

    $ mkdir diazo

#. Herunterladen der ``bootstrap.py``-Datei::

    $ cd diazo
    $ curl -O http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py


#. Erstellen der ``buildout.cfg``-Datei::

    [buildout]
    # Adjust the version number as required. See
    # http://good-py.appspot.com/release/diazo for a full list

    extends = http://good-py.appspot.com/release/diazo/1.0rc4
    versions = versions

    parts =
        lxml
        diazo

    [diazo]
    recipe = zc.recipe.egg
    eggs =
        diazo [wsgi]
        PasteScript

    [lxml]
    recipe = z3c.recipe.staticlxml
    egg = lxml

#. Bootstrapping des Buildout-Projekts::

    $ python2.6 bootstrap.py

#. Erstellen des Buildout-Projekts::

    $ bin/buildout

   Dies sollte die drei Skripte ``./bin/paster``, ``./bin/diazocompiler`` und ``./bin/diazorun`` erstellen.

Konfiguration
=============

Die Konfigurationsdatei ``diazo/proxy.ini`` für den Proxy-Server nutzt Paste Deploy um eine WSGI-Anwendung zu erstellen::

 [server:main]
 use = egg:Paste#http
 host = 0.0.0.0
 port = 8000

 [composite:main]
 use = egg:Paste#urlmap
 /static = static
 / = default

 [app:static]
 use = egg:Paste#static
 document_root = %(here)s/theme

 [pipeline:default]
 pipeline = theme
            content

 [filter:theme]
 use = egg:diazo
 rules = %(here)s/rules.xml
 prefix = /static
 debug = true

 [app:content]
 use = egg:Paste#proxy
 address = http://127.0.0.1:8080/VirtualHostBase/http/127.0.0.1:8000/Plone


``[server:main]``
 Server, der mit ``./bin/paster serve proxy.ini`` aufgerufen werden kann.
``[composite:main]``
 definiert das grundlegende URL-Mapping.

 ``paster`` liefert alles aus ``/static`` mit ``[app:static]`` aus und alles andere mit ``[app:default]``.

``[app:static]``
 liefert das Theme unter ``/static`` aus dem ``static``-Verzeichnis aus.
``[pipeline:default]``
 liefert die durch Diazo transformierten Inhalte aus ``theme`` und ``content`` als ``default``.
``[filter:theme]``
 Hier wird der Pfad auf die ``rules.xml``-Datei und der Präfix für alle relativen Pfade (z.B. auf CSS-Dateien) angegeben.

 ``debug = true``
  Hiermit wird das Theme bei jeder Anfrage neu erstellt, sodass die Entwicklung deutlich leichter fällt. Für den produktiven Betrieb sollte jedoch ``debug = false`` gesetzt werden um die Performance zu verbessern.

``[app:content]``
 liefert die Inhalte aus ``http://127.0.0.1:8000/Plone``

Regeln
======

Schließlich sind noch die Transformationsregeln in ``diazo/rules.xml``-Datei anzugeben. In dem hier abgebildeten Beispiel werden jedoch nur einige grundlegende Transformationen ausgeführt::

 <rules
     xmlns="http://namespaces.plone.org/diazo"
     xmlns:css="http://namespaces.plone.org/diazo/css"
     xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

   <theme href="theme/theme.html" />

   <prepend theme="//head" content="//head/base"
            nocontent="ignore" />
   <prepend theme="//head" content="//head/link"
            nocontent="ignore" />
   <prepend theme="//head" content="//head/style"
            nocontent="ignore" />
   <append theme="//head" content="//head/script"
           nocontent="ignore" />
   <append theme="//head" content="//head/meta"
           nocontent="ignore" />

   <replace css:theme="title"
            css:content="title"
            nocontent="ignore" />
   <copy css:theme="div.container"
         css:content="body > *"
         nocontent="ignore" />

 </rules>

Theme
=====

Wesentlicher Bestandteil eines Themes ist eine HTML-Datei, ``theme/theme.html``::

 <!DOCTYPE html>
 <html>
   <head>
     <title>Dummy title</title>
     <link rel="stylesheet"
           href="./screen.css"
           type="text/css"
           media="screen, projection" />
     <link rel="stylesheet"
           href="./print.css"
           type="text/css"
           media="print" />
     <!--[if IE]>
     {% compress css %}
     <link rel="stylesheet"
           href="./ie.css"
           type="text/css"
           media="screen, projection" />
     {% endcompress %}
     <![endif]-->
   </head>
   <body>
     <div class="container">
       <h1>Dummy Headline</h1>
       <p>Sample content</p>
     </div>
   </body>
 </html>

Schließlich sollten Sie den Diazo-Server starten können mit::

 $ ./bin/paster serve --reload proxy.ini

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    diazo-regeln
    fortgeschrittene-diazo-regeln
    tipps-tricks
    deployment
    diazo-performance-monitoring

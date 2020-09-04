========================
Multi-Site-Konfiguration
========================

zc.recipe.macro liefert eine Reihe von Macros, womit einzelne Buildout-Abschnitte dynamisch aus einem Macro- und einem Parameter-Abschnitt generiert werden können. Dies ermöglicht Buildout, Konfigurationsdaten unabhängig vom Ausgabeformat zu halten und ermöglicht so die Konfiguration verschiedener Dienste für mehrere Sites.

Üblicherweise wird in einem  `zc.recipe.macro`_-Abschnitt ein Macro mit den Parametern dieses Abschnitts aufgerufen. Dies läßt sich anschaulich an einer Apache-Konfiguration zeigen.

.. _`zc.recipe.macro`: http://pypi.python.org/pypi/zc.recipe.macro

Apache-Konfiguration
====================

::

 [buildout]
 parts =
     ...
     apache

 [apache]
 recipe = zc.recipe.macro
 macro = apache-macro
 result-recipe=collective.recipe.template
 targets =
     my-apache:mysite-parameters

Im folgenden werden dann die Abschnitte ``[apache-macro]`` und ``[mysite-parameters]`` definiert::

 [apache-macro]
 domain=$${:domain}
 host=$${:host}
 port=$${:port}
 input = ${buildout:directory}/template/apache-vhost.in
 output = ${buildout:parts-directory}/$${:__name__}

 [mysite-parameters]
 domain=mysite.org
 host=83.223.91.163
 port=8080

Die Datei ``templates/apache-vhost.in`` sieht z.B. so aus::

 ${host}
 ${port}
 ${domain}

Das Ergebnis ist dann::

 [apache]
 recipe = zc.recipe.macro:empty
 result-sections = my-apache

 [my-apache]
 recipe = collective.recipe.template
 domain = mysite.org
 host = 83.223.91.163
 input = /home/veit/myproject/template/apache-vhost.in
 output = /home/veit/myproject/parts/my-apache
 port = 8080

Das Rezept ``zc.recipe.macro`` ändert sich zu ``zc.recipe.macro:empty``, hat jedoch keine Wirkung mehr. Dennoch muss der Abschnitt vorhanden sein, da er in ``[buildout]`` als Abschnitt angegeben wurde.

Und ``parts/my-apache`` sieht schließlich so aus::

 83.223.91.163
 8080
 mysite.org

Jede weitere Site kann dann einfach folgendermaßen eingetragen werden::

 [apache]
 ...
 targets =
     ...
     vs-apache:vs-parameters

 ...
 [vs-parameters]
 domain=veit-schiele.de
 host=83.223.91.163
 port=8090

awstats-Konfiguration
=====================

Analog kann mit ``tc.recipe.macro`` auch awstats konfiguriert werden::

 [buildout]
 parts =
     ...
     mysite-awstats

 [awstats]
 recipe = zc.recipe.macro
 macro = awstats-macro
 result-recipe=collective.recipe.template
 targets =
     mysite-awstats:mysite-parameters
     vs-awstats:vs-parameters

 [awstats-macro]
 domain=$${:domain}
 host=$${:host}
 port=$${:port}
 input = ${buildout:directory}/template/awstats-conf.in
 output = ${buildout:parts-directory}/$${:__name__}

Die Datei ``templates/awstats-conf.in`` sieht z.B. so aus::

 ${host}
 ${port}
 ${domain}

Das Ergebnis ist dann::

 [buildout]
 parts =
     ...
     awstats
     mysite-awstats
     vs-awstats

 ...

 [awstats]
 recipe = zc.recipe.macro:empty
 result-sections =
     mysite-awstats
     vs-awstats

 [mysite-awstats]
 domain = mysite.org
 host = 83.223.91.163
 input = /home/veit/myproject/template/awstats-conf.in
 output = /home/veit/myproject/parts/mysite-awstats
 port = 8080
 recipe = collective.recipe.template

 [vs-awstats]
 domain = veit-schiele.de
 host = 83.223.91.163
 input = /home/veit/myproject/template/awstats-conf.in
 output = /home/veit/myproject/parts/vs-awstats
 port = 8090
 recipe = collective.recipe.template

Und ``parts/my-awstats`` sieht schließlich so aus::

 83.223.91.163
 8080
 mysite.org

.. seealso::
    * `Martin Aspeli: Tools for a successful Plone project`_
    * `Martin Aspeli: An über-buildout for a production Plone server`_
    * `Martin Aspeli: The Über-Buildout Mark II - Windows (IIS) and Unix (nginx), production and development`_

.. _`Martin Aspeli: Tools for a successful Plone project`: http://www.martinaspeli.net/articles/tools-for-a-successful-plone-project
.. _`Martin Aspeli: An über-buildout for a production Plone server`: http://www.martinaspeli.net/articles/an-uber-buildout-for-a-production-plone-server
.. _`Martin Aspeli: The Über-Buildout Mark II - Windows (IIS) and Unix (nginx), production and development`: http://www.martinaspeli.net/articles/uber-buildout

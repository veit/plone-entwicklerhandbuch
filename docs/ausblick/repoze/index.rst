======
Repoze
======

Repoze vereinigt verschiedene Technologien um WSGI und Zope zu verbinden.

`WSGI`_
 Python-Standard (`PEP 333`_), der die Kommunikation zwischen Web-Servern und Web-Anwendungen spezifiziert.

 Server
  akzeptieren Anfragen eines Browser/Client und reichen die Daten an die Anwendungen weiter.

  Sie antworten auf Anfragen, wobei sie die von Anwendungen zurückgelieferten Daten verwenden.

 Anwendungen
  geben Antworten zurück.
 Middleware
  Anwendung, die die *nächste* Anwendung aufruft, wobei die funktionale Anordnung eine sog. Pipeline bildet.

`Repoze`_
 ermöglicht Zope in einer WSGI-Umgebung zu nutzen oder umgekehrt anderen WSGI-Anwendungen Zope-Technologien als Middleware bereitzustellen.

 Dabei besteht Repoze einerseits aus einer Reimplementierung von Zope-Funktionalitäten als Python-Bibliotheken und WSGI-Middleware, andererseits aus bestehender WSGI-Middleware (`Paste`_).

Beispiel
 ::

  [buildout]
  extends = http://dist.plone.org/release/4.1-latest/versions.cfg
  parts =
     instance
     paster
     wsgiconfig

  [instance]
  recipe = plone.recipe.zope2instance
  eggs =
      Plone
      PIL
  user = admin:admin

  [paster]
  recipe = zc.recipe.egg
  eggs =
      ${instance:eggs}
      Paste
      PasteScript
      repoze.tm2
      repoze.retry
  script = paster

  [wsgiconfig]
  recipe = collective.recipe.template
  input = inline:
      [app:zope]
      use = egg:Zope2#main
      zope_conf = ${buildout:directory}/parts/instance/etc/zope.conf

      [pipeline:main]
      pipeline =
          egg:paste#evalerror
          egg:repoze.retry#retry
          egg:repoze.tm2#tm
          zope

      [server:main]
      use = egg:paste#http
      host = localhost
      port = 8000
  output = ${buildout:directory}/zope2.ini

 Die Buildout-Konfiguration nutzt umfangreich Ian Bicking’s `Paste`_, speziell `PasteDeploy`_, das eine deklarative Syntax zum Konfigurieren von WSGI-Pipelines bereitstellt.

 Zope2 kann nun einfach gestartet werden mit::

  $ ./bin/paster serve zope2.ini

 **Anmerkung 1:** `infrae.wsgi`_ scheint eine sauberere und besser dokumentierte Lösung zu sein im Vergleich zu ``repoze.zope2`` und dem neuen Zope2 WSGI publisher. Um ``ìnfrae.wsgi`` zu verwenden, tragen Sie einfach im ``[wsgiconfig]``-Abschnitt stattdessen folgendes ein::

  use = egg:infrae.wsgi#zope2

 .. _`infrae.wsgi`: http://pypi.python.org/pypi/infrae.wsgi

 **Anmerkung 2:** Soll ein anderer Web-Server wie z.B. `gunicorn`_ verwendet werden, so kann einfach im Abschnitt ``[server:main]`` stattdessen folgendes eingetragen werden::

  use = egg:gunicorn#main

 .. _`gunicorn`: http://pypi.python.org/pypi/gunicorn

.. seealso::

    - `[Zope-dev] Zope 2 WSGI investigation`_

.. _`[Zope-dev] Zope 2 WSGI investigation`: https://mail.zope.org/pipermail/zope-dev/2012-January/043930.html

.. - `Install Plone 3 behind Apache and mod_wsgi using Repoze`_
.. - `Rolling out Repoze`_

.. _`Repoze`: http://repoze.org/
.. _`WSGI`: http://www.wsgi.org/wsgi
.. _`PEP 333`: http://www.python.org/dev/peps/pep-0333/
.. _`Paste`: http://pythonpaste.org/
.. _`repoze.zope2`: http://svn.repoze.org/repoze.zope2/trunk/
.. _`PasteDeploy`: http://pythonpaste.org/deploy/

.. _`Install Plone 3 behind Apache and mod_wsgi using Repoze`: http://plone.org/documentation/tutorial/install-plone-3-behind-apache-and-mod_wsgi-using-repoze
.. _`Rolling out Repoze`: http://martinaspeli.net/articles/rolling-out-repoze

.. toctree::
    :titlesonly:
    :maxdepth: 1

    verzeichnisstruktur
    konfiguration
    deliverance
    tipps-tricks

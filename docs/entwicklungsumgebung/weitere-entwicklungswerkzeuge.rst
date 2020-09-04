=============================
Weitere Entwicklungswerkzeuge
=============================

Wollen wir weitere Entwicklungswerkzeuge in einem Buildout-Projekt installieren, geben wir diese einfach in der ``buildout.cfg``-Datei an. Folgende Entwicklungswerkzeuge können die Arbeit deutlich vereinfachen:

`DocFinderTab <http://pypi.python.org/pypi/Products.DocFinderTab>`_
 Produkt, das alle Klassen und Methoden eines Objekts im Zope Management
 Interface (ZMI) auflistet.

 DocFinderTab kann direkt als Egg in der Instanz angegeben werden::

  [instance]
  ...
  eggs =
      Products.DocFinderTab

`pyflakes`_
 Pyflakes analysiert Python-Programme und entdeckt verschiedene Fehlerarten. Es ist sehr viel schneller als das Ausführen der Programme.

 .. _`pyflakes`: http://pypi.python.org/pypi/pyflakes

 pyflakes lässt sich einfach mit Buildout installieren::

  parts =
      ...
      pyflakes

  [pyflakes]
  recipe = zc.recipe.egg:scripts
  eggs = pyflakes
  scripts = pyflakes
  entry-points = pyflakes=pyflakes.scripts.pyflakes:main

`plone.app.debugtoolbar <http://pypi.python.org/pypi/plone.app.debugtoolbar>`_
 Debug-Toolbar, die einfach für eine Plone-Site aktiviert werden kann. Die Installation kann einfach mit Buildout erfolgen::

  [instance]
  ...
  eggs =
      plone.app.debugtoolbar

`pylint <http://www.logilab.org/857>`_
 Pylint analysiert Python-Code in Bezug auf Bugs und geringe Code-Qualität.

 Pylint lässt sich einfach mit Buildout installieren::

  parts =
      pylint
      ...

  [pylint]
  recipe = zc.recipe.egg
  eggs =
      ${instance:eggs}
      pylint
  entry-points = pylint=pylint.lint:Run
  arguments = sys.argv[1:]

`DeadlockDebugger <http://www.zope.org/Members/nuxeo/Products/DeadlockDebugger>`_
 Für entsprechende Prozesse wird Debugging möglich, indem ein Traceback aller
 laufenden Pythonprozesse sowohl zum Eventlog als auch zum Browser geschickt
 wird.
`PDBDebugMode <http://pypi.python.org/pypi/Products.PDBDebugMode>`_
 PDBDebugMode erlaubt sog. post-mortem-Debugging für *exceptions* im Debug-Modus, d.h., bei einem Fehler wird der Debugger aufgerufen, der den Traceback ausgibt. Sofern vorhanden, nutzt ``PDBDebugMode`` ``ipdb`` statt ``pdb``.


 Diese Entwicklungswerkzeuge lassen sich einfach angeben mit::

  [instance]
  ...
  debug-mode = on
  eggs =
      Products.PDBDebugMode
      z3c.deadlockdebugger

`Products.PrintingMailHost`_
 Monkey Patch, der MailHost-Nachrichten nicht verschickt, sondern auf der Konsole ausgibt, d.h., Zope versendet damit keine Mails mehr.

.. _`Products.PrintingMailHost`: http://pypi.python.org/pypi/Products.PrintingMailHost

`roadrunner`_
 Testrunner, der die testgetriebene Entwicklung deutlich beschleunigen kann.

 ``roadrunner`` läd vorab das Standard-Zope- und Plone-Environment für PloneTestCase. zur Installation wird einfach folgendes in die ``buildout.cfg``-Datei eingetragen::

  [buildout]
  parts =
      ...
      roadrunner

  [roadrunner]
  recipe = roadrunner:plone
  packages-under-test = vs.policy

 Anschließend kann es wie der reguläre Zope-Testrunner aufgerufen werden::

  $ ./bin/roadrunner -s vs.policy

.. _`roadrunner`: http://pypi.python.org/pypi/roadrunner

`collective.recipe.grp`_
 Rezept, mit dem in Buildout auf ``${grp:GROUP}`` referenziert werden kann um
 die Gruppe des aktuellen Nutzers herauszubekommen.

 Zusammen mit `gocept.recipe.env
 <http://pypi.python.org/pypi/gocept.recipe.env>`_, das Environment-Variablen in
 einem Buildout-Abschnitt zur Verfügung stellt, lassen sich hiermit die
 Eigentümer (*Owner*) der Buildout-Inhalte setzen lassen, z.B. mit::

  chown -R ${env:USER}:${grp:GROUP} ${buildout:directory}

 Installieren lassen sich die Pakete mit::

  [env]
  recipe = gocept.recipe.env

  [grp]
  recipe = collective.recipe.grp

.. _`gocept.recipe.env`:
.. _`collective.recipe.grp`: http://pypi.python.org/pypi/collective.recipe.grp

`IPython <http://ipython.org/>`_
 Python-Shell, die Ihnen u.a. folgende Vorteile bietet:

 - Objekt-Introspektion
 - Code- Introspektion
 - Dokumentation-Introspektion (mit ``%pdoc``)
 - Eingabehistorie, persistent auch über Sessions hinweg.

 Zur Installation fügen Sie bitte folgendes  in Ihrer ``devel.cfg``-Datei hinzu::

  [buildout]
  _
  parts =
      ...
      ipzope
  ...
     [ipzope]
     # An IPython Shell for interactive use with Zope running.
     #
     # It requires the `ipy_profile_zope.py` configuration script. Get this from
     # git@github.com:collective/dotipython.git and put it in your profile
     # directory. Depending on your setup, this may be at
     # `$HOME/.ipython/profile_zope/startup`,
     # `$HOME/.config/ipython/profile_zope/startup` (Ubuntu 12.04), or see
     # http://ipython.org/ipython-doc/dev/config/overview.html#configuration-file-location
     # for more details.
     #
     recipe = zc.recipe.egg
     eggs =
         ipython
         ${instance}
     initialization =
         import sys, os
         os.environ["INSTANCE_HOME"] = "${instance:location}"
         sys.argv[1:1] = "--profile=zope".split()
     scripts = ipython=ipzope

 Rufen Sie dann zunächst das buildout-Skript auf. Anschließend können Sie dann
 die IPython-Sell aufrufen::

  $ ./bin/buildout
  $ ./bin/ipzope

 Beim ersten Aufruf von ``ipzope`` wird ein neues ``IPython``-Profil in Ihrem
 Home-Verzeichnis erstellt. In \*ix-Betriebssystemen finden Sie das
 entsprechende Verzeichnis unter ``$HOME/.ipython/``, in Windows unter
 ``%userprofile%\_ipython``.  In dieses Verzeichnis sollten das Profil aus
 ``https://github.com/collective/dotipython/blob/master/ipy_profile_zope.py``
 legen. Anschließend sollten Sie die IPython-Session  mit ``Ctrl-d`` beenden und
 erneut starten.

 Anschließend lässt sich z.B. ``portal.error_log.get`` eingeben und durch
 Drücken der *Tab*-Taste erhalten Sie alle verfügbaren Methoden des
 `èrror_log``, die mit ``get`` beginnen.

 Falls Sie Änderungen an Ihrer Plone-Site vorgenommen haben, können Sie diese
 speichern mit::

  utils.commit()

 Und falls auch andere auf der Zope-Instanz arbeiten, sollten Sie gelegentlich die Änderungen übernehmen mit::

  utils.sync()

 Weitere Informationen zu iPython erhalten Sie im `iPython-Tutorial
 <http://ipython.org/ipython-doc/stable/interactive/tutorial.html>`_.

`ipdb <https://pypi.python.org/pypi/ipdb>`_, `iw.debug <http://pypi.python.org/pypi/iw.debug>`_
 ``ipdb`` ist Python-Debugger, der viele Vorteile von IPython nutzt, z.B.
 automatische Vervollständigung. ``iw.debug`` erlaubt Ihnen, den ``ipdb``-
 Debugger über jedem veröffentlichten Objekt einer Zope2-Anwendung aufzurufen.

 Zum Installieren fügen Sie in Ihrer ``devel.cfg``-Datei folgendes hinzu::

  [buildout]
  _
  [instance]
  eggs +=
      ...
      iw.debug
  _
  [instance]
  _
  zcml +=
      iw.debug

 Anschließend wird das Buildout-Skript aufgerufen und die Instanz im Vordergrund gestartet::

  $ ./bin/buildout
  $ ./bin/instance fg

 .. note::
    Wenn in Ihrem Code an irgendeiner  Stelle ein ``ipdb`` oder ``pdb`` Code enthalten ist, erhalten Sie die Exception ``BdbQuit``.

 Nun kann der URL eines jeden Objekts der Plone-Site ``/ipdb`` angehängt werden
 um eine IPython-Shell für diese Plone-Site zu erhalten::

  ...
  --Return--
  None
  > /Users/veit/.buildout/eggs/iw.debug-0.3-py2.7.egg/iw/debug/pdbview.py(92)pdb()
       91             else:
  ---> 92                 set_trace()
       93

 Um die lokalen Variablen zu erhalten, können Sie nun zunächst ``ll`` eingeben::

  ipdb> ll
  {'request': <HTTPRequest, URL=http://localhost:8080/Plone/ipdb>, 'portal': <PloneSite at /Plone>, 'context': <PloneSite at /Plone>, 'meth': None, 'view': None}
  ipdb> context
  <PloneSite at /Plone>
  ipdb> context == portal
  True
  ipdb> portal.Title()
  'Website'
  ipdb> portal.portal_quickinstaller.listInstallableProducts()
  [{'status': 'new', 'hasError': False, 'id': 'plone.app.dexterity', 'title': u'Dexterity Content Types'}, {'status': 'new', 'hasError': False, 'id': 'plone.app.theming', 'title': u'Diazo theme support'}, {'status': 'new', 'hasError': False, 'id': 'plone.app.caching', 'title': u'HTTP caching support'}, {'status': 'new', 'hasError': False, 'id': 'Marshall', 'title': 'Marshall'}, {'status': 'new', 'hasError': False, 'id': 'plone.app.openid', 'title': u'OpenID Authentication Support'}, {'status': 'new', 'hasError': False, 'id': 'plone.app.debugtoolbar', 'title': u'Plone debug toolbar'}, {'status': 'new', 'hasError': False, 'id': 'plone.session', 'title': u'Session refresh support'}, {'status': 'new', 'hasError': False, 'id': 'plone.resource', 'title': u'Static resource storage'}, {'status': 'new', 'hasError': False, 'id': 'CMFPlacefulWorkflow', 'title': u'Workflow Policy Support (CMFPlacefulWorkflow)'}, {'status': 'new', 'hasError': False, 'id': 'plone.app.iterate', 'title': u'Working Copy Support (Iterate)'}, {'status': 'new', 'hasError': False, 'id': 'collective.z3cform.datetimewidget', 'title': u'collective.z3cform.datetimewidget'}]
  ipdb>

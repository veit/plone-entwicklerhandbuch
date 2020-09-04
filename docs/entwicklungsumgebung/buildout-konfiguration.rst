Buildout-Konfiguration
======================

Die ``base.cfg``-Datei gliedert sich in die folgenden Abschnitte:

``[buildout]``
 Hier werden die globalen Einstellungen für diesen Buildout angegeben.

 ``parts``
  Die in dieser Konfiguration angegebenen Abschnitte, die in der
  angegebenen Reihenfolge durchlaufen werden::

   parts =
       instance-base
       zopepy
       i18ndude
       zopeskel

 ``extends``
  Eine bestehende Buildout-Konfiguration wird erweitert, nämlich
  ``http://dist.plone.org/release/4.3/versions.cfg`` und
  ``versions.cfg``.
 ``find-links``
  URLs, Datei- oder Verzeichnisnamen, in denen Buildout nach Links
  zu Distributionen suchen soll.
 ``extensions``
  Erweiterungen, die den Funktionsumfang von Buildout vergrößern:

  - `mr.developer <http://pypi.python.org/pypi/mr.developer>`_
  - `buildout.threatlevel
    <http://pypi.python.org/pypi/buildout.threatlevel>`_
  - `jarn.setuptoolsfixer
    <http://pypi.python.org/pypi/jarn.setuptoolsfixer>`_

 ``allow-picked-versions``
  Mit dem Wert ``false`` kann gewährleistet werden, dass alle Versionen
  festgeschrieben wurden.
 ``versions``
  Es wird auf einen Abschnitt verwiesen, in dem die Versionen der
  Python-Packages festgeschrieben werden können, in unserem Fall ist
  der Abschnitt ``versions`` genannt worden. Weiter Hinweise zur
  Verwaltung von Versionen erhalten Sie in `Aktualisierung und Versionierung <aktualisierung-und-versionierung>`_.
 ``unzip``
   Üblicherweise packt Buildout keine gezippten Python Eggs aus.

``[instance-base]``
 Dieser Abschnitt erstellt und konfiguriert eine Zope-Instanz unter Verwendung von `plone.recipe.zope2instance <http://cheeseshop.python.org/pypi/plone.recipe.zope2instance>`_::

  [instance-base]
  recipe = plone.recipe.zope2instance
  user = admin:admin
  http-address = 8080
  debug-mode = on
  verbose-security = on
  blob-storage = var/blobstorage

  eggs =
      Plone
      Pillow

  zcml =

  environment-vars =
      PTS_LANGUAGES en de
      zope_i18n_allowed_languages en de
      zope_i18n_compile_mo_files true

 ``eggs``
  Hier können zusätzliche Python-Eggs angegeben werden, wobei ``elementtree`` von Plone benötigt wird. Auf diese Eggs wird später in ``[instance]`` verwiesen.

  Es können auch spezifische Versionen angegeben werden. Soll z.B. ``SQLAlchemy 0.3`` installiert werden, sieht der Eintrag so aus::

   eggs =
       ...
       SQLAlchemy>=0.3,<0.4dev

  Auch die in diesem Projekt entwickelten Eggs werden hier angegeben::

   eggs =
       ...
       my.package

   develop =
       src/my.package

 ``verbose-security``
  Damit lässt sich angeben,

  - Für welche Objekte wurde der Zugriff verweigert?
  - Welche Rechte sind notwendig?
  - Welche Rollen und Rechte sind den Objekten und Eigentümern zugeteilt?
  - Welches sind die wirksamen Proxy-Rollen?

  Damit wir alle ``unauthorized``-Ereignisse auch im Fehlerprotokoll angezeigt bekommen, müssen wir später im *Site Error Log* im Zope Management Interface (ZMI) der Plone-Site ``Unauthorized`` aus der Liste *Ignored exception types* entfernen.

 ``eggs``
  Hier geben wir die der Instanz zur Verfügung stehenden Eggs an. In unserer
  Konfiguration werden die in den ``buildout``- und ``plone``-Abschnitten
  angegebenen Eggs verwendet.
 ``zcml``
  Da die Konfigurationsdateien nicht automatisch für ältere Eggs oder Pakete
  geladen werden, kann Buildout angewiesen werden, einen sog. *ZCML slug* in
  ``parts/instance/etc/package-includes`` zu erstellen, indem die entsprechenden
  Pakete unter dieser Option aufgelistet werden::

   zcml =
       my.package

  Es kann auch explizit angegeben werden, welche Art von *ZCML slug* erstellt
  werden soll, z.B.::

   zcml =
       my.package-overrides
       my.package-meta

  ``overrides``
   Dies erstellt eine ``*-overrides.zcml``-Datei in
   ``myproject/parts/instance/etc/package-includes/``, mit der sich eine per
   ``zcml`` angegebene Konfiguration wieder überschrieben wird.

   Anschließend wird in der ``configure.zcml``-Datei von ``my.package`` eine
   ``overrides``-Konfigurationsdatei eingefügt::

    <includeOverrides file="overrides.zcml" />

   Diese ``overrides.zcml``-Datei enthält dann die Ersetzung einer bestehenden
   Konfiguration.

  ``meta``
   Dies erstellt eine ``*-meta.zcml``-Datei in
   ``myproject/parts/instance/etc/package-includes/``, die  gewährleistet, dass
   die gesamte Konfiguration dieses Pakets zur Verfügung steht bevor die
   weiteren ``zcml``-Anweisungen abgearbeitet werden.

 Weitere Konfigurationsoptionen von ``plone.recipe.zope2instance`` sind:

 ``default-zpublisher-encoding``
  Liefert ein Request eine Unicode-Antwort und ist für
  ``ZPublisher.HTTPResponse`` kein spezifischer Zeichensatz angegeben, dann wird
  der Unicode-String mit dem ``default-zpublisher-encoding`` kodiert.

  Der Standardwert ist ``utf-8``.

 ``zope-conf``
  Ein relativer oder absoluter Pfad zu einer Zope-Konfigurationsdatei. Eine ``zope.conf``-Datei wird dann mit den Angaben in diesem Abschnitt generiert in ``parts/instance/etc/zope.conf``.
 ``zope-conf-additional``
  Sollen nur die Werte einiger Attribute der ``zope.conf``-Datei geändert werden, können diese in ``zope-conf-additional`` angegeben werden. Dabei müssen die nachfolgenden Zeilen eingerückt sein.
``environment-vars``
 definiert Umgebungsvariablen zur Laufzeit von Zope, z.B.::

  environment-vars =
      zope_i18n_compile_mo_files = true

 Einen vollständigen Überblick über alle Optionen des ``[instance]``-Abschnitts erhalten Sie in  `plone.recipe.zope2instance`_.

``[zopepy]``
 In diesem Abschnitt wird ein Python-Interpreter definiert, der alle Eggs und Pakete, aber keine Zope2-Produkte enthält und sich daher gut zum Debuggen und Testen eignet::

  [zopepy]
  recipe = zc.recipe.egg
  eggs = ${instance:eggs}
  interpreter = zopepy
  extra-paths = ${zope2:location}/lib/python
  scripts = zopepy

 Mit dem Rezept wird das ``./bin/zopepy``-Skript erstellt und sowohl die Eggs aus dem ``[instance]``-Abschnitt als auch die Zope-Module aus ``parts/zope2/lib/python`` der Zope-Installation eingeschlossen. Es muss also nicht mit jedem neuen Buildout-Projekt auch die ``PYTHONPATH``-Umgebungsvariable neu gesetzt werden. Mit ``zopepy`` sollte sich z.B. auch einfach das Modul ``PageTemplates`` aus ``Products`` importieren lassen::

  $ ./bin/zopepy
  >>> from Products import PageTemplates

Da kein Fehler für den Import angegeben wurde, wird das Modul geladen, und der Python-Interpreter kann mit ``Strg-D`` (unter Windows ``Strg-Z``) wieder verlassen werden.

``annotate``
============

Mit der Buildout-Option ``annotate`` werden alle Abschnitte alphabetisch
sortiert angezeigt. Innerhalb jedes Abschnitts werden alle Schlüssel-Wert-Paare
zusammen mit der Quelle angezeigt. Eine solche Quelle kann entweder ein
Dateiname oder die Variablen ``COMPUTED_VALUE``, ``DEFAULT_VALUE`` oder
``COMMAND_LINE_VALUE`` sein. Die Ausgabe kann z.B. folgendermaßen aussehen::

    $ ./bin/buildout -c deploy.cfg  annotate
    Setting socket time out to 3 seconds.

    Annotated sections
    ==================

    [backup]
    enable_snapshotrestore= false
        /home/veit/sandboxes/vs_buildout/deploy.cfg
    ...
    [buildout]
    ...
    develop-eggs-directory= develop-eggs
        DEFAULT_VALUE
    directory= /home/veit/vs_buildout
        COMPUTED_VALUE
    ...

``annotate`` kann auch genutzt werden um herauszufinden, welche Version aufgrund
welcher Konfiguration verwendet wird, z.B.::

    [versions]
    ...
    six= 1.2.0
        /home/veit/vs_buildout/plone-versions.cfg
    ...

Plone 3.2
=========

Für Plone 3.2 sieht die Buildout-Konfigurationsdatei etwas anders aus. Sie gliedert sich in die folgenden Abschnitte::

 parts =
     zope2
     productdistros
     instance
     zopepy

``[zope2]``
 Dieser Abschnitt lädt und erstellt Zope 2 aus der im Abschnitt ``plone`` angegebenen URL::

  [zope2]
  recipe = plone.recipe.zope2install
  fake-zope-eggs = true
  additional-fake-eggs =
      ZODB3
  url = ${versions:zope2-url}

 Mit dem Rezept wird Zope 2 in ``parts/zope2`` installiert, die Variable ``ZOPE_HOME`` ist also ``parts/zope2`` und die Variable ``SOFTWARE_HOME`` ``parts/zope2/lib/python``.

 ``fake-zope-eggs``
  Falls der Wert auf ``true`` gesetzt wird, werden Links auf die Zope-3-Bibliotheken gesetzt. Wenn nun ein Egg in seiner ``setup.py``-Datei auf ein ``zope.*``-Egg verweist, finden die setuptools diese in ``/parts/zope2/lib/python/zope/`` und installieren nicht erneut Versionen dieser Eggs in womöglich inkompatiblen Versionen. Ab Version 3 ist der Standardwert auf ``true`` gesetzt.

 ``additional-fake-eggs``
  Hiermit lasst sich eine Liste zusätzlicher *fake eggs* angeben, wobei nur Python-Packages angegeben werden sollten, die sich auch in ``PYTHONPATH`` befinden. Der Standardwert schließt ``Acquisition``, ``ClientForm``, ``DateTime``, ``docutils``, ``ExtensionClass``, ``mechanize``, ``Persistence``, ``pytz``, ``RestrictedPython``, ``tempstorage``, ``ZConfig``, ``zLOG``, ``zodbcode``, ``ZODB3``, ``zdaemon`` und ``Zope2`` ein.

  Die Versionen von ``additional-fake-eggs`` lassen sich einfach angeben, z.B.::

   additional-fake-eggs =
       ZODB3 = 3.7.1
       zope.annotation = 3.3.2

  Wird keine Version für ``additional-fake-eggs`` angegeben, haben die *faked eggs* immer die Version ``0.0``.

 ``skip-fake-eggs``
  Hier kann eine Liste von Packages angegeben werden, für die keine Fake eggs erstellt werden sollen. Somit können neuere Versionen spezifischer  Zope-Packages installiert werden auch wenn ``fake-zope-eggs = true`` gesetzt ist, z.B.::

   [buildout]
   versions = versions

   [versions]
   zope.app.catalog = 3.5.2
   zope.component = 3.5.1
   zope.i18n = 3.6.0
   zope.sendmail = 3.5.1
   zope.testing = 3.7.1
   five.intid = 0.3.0

   [zope2]
   fake-zope-eggs = true
   additional-fake-eggs =
       ZConfig
       ZODB3
       pytz
   skip-fake-eggs =
       zope.component
       zope.i18n
       zope.sendmail
       zope.testing

 ``url``
  Die URL, unter der Zope heruntergeladen werden kann, in unserem Fall wird auf die ``versions.cfg``-Datei verwiesen und den dort angegebenen Wert für ``zope2-url``.

``[productdistros]``
 Der Abschnitt kann verwendet werden, um Archive von Produkten herunterzuladen und zu installieren, z.B.::

  urls =
      http://www.zope.org/Members/shh/DocFinderTab/1.0.2/DocFinderTab-1.0.2.tar.gz

 ``nested-packages``
  Archive, die mehrere Zope2-Produkte enthalten.

  Im folgenden Beispiel soll PloneLDAP 1.0 installiert werden::

   [productdistros]
   recipe = plone.recipe.distros
   urls =
       http://plone.org/products/ploneldap/releases/1.0/PloneLDAP-bundle-1.0.tar.gz
   nested-packages =
       PloneLDAP-bundle-1.0.tar.gz
   version-suffix-packages =

  Nach dem Aufruf von ``./bin/buildout`` finden sich die Produkte ``LDAPMultiPlugins``, ``LDAPUserFolder`` und ``PloneLDAP`` in ``parts/productdistros``.

 ``version-suffix-packages``
  Produkte, deren Verzeichnisnamen die Version enthält und die daher vor ihrer Verwendung umbenannt werden müssen.

 In den Abschnitten ``products`` in ``[instance]`` wird dann auf den Installationsort von ``productdistros`` verwiesen::

  ${productdistros:location}

``[instance]``
 Dieser Abschnitt erstellt und konfiguriert eine Zope-Instanz unter Verwendung von ``plone.recipe.zope2instance``::

  [instance]
  recipe = plone.recipe.zope2instance
  zope2-location = ${zope2:location}
  ...
  products =
      ${buildout:directory}/products
      ${productdistros:location}

 ``zope2-location``
  Es wird das im ``zope2``-Abschnitt angegebene Verzeichnis für die Zope2-Installation verwendet.

Plone 3.1
=========

Für Plone 3.1 sieht die ``buildout.cfg``-Datei etwas anders aus::

 [buildout]
 parts =
 ...
 plone

``index``
 URL eines Index-Servers. In diesem Index sucht Buildout sofern in den unter ``find-links`` angegebenen Distributionen nichts gefunden wurde.

 Ohne spezifische Angabe für ``index`` wird der `Python Package Index <http://cheeseshop.python.org/pypi>`_ verwendet. Aus Gründen der Stabilität und Performance kann sich jedoch ein anderer Index empfehlen::

  index = http://download.zope.org/ppix

``[plone]``
 verwendet `plone.recipe.plone <http://cheeseshop.python.org/pypi/plone.recipe.plone>`_ um die Plone Produkte und Eggs herunteruladen::

  [plone]
  recipe = plone.recipe.plone

 Dabei ist zu beachten, dass immer die aktuellste Version verwendet wird. Soll immer nur ein Plone-3.1.x-Release verwendet wird, wird beim Erstellen des Buildout-Projekts zunächst auf die Frage ``Enter plone_version`` mit ``3.1`` geantwortet, und anschließend kann man sich zunutze machen, dass die Versionsnummern des ``plone.recipe.plone`` immer mit denen von Plone übereinstimmen::

  recipe = plone.recipe.plone>=3.1,<3.2dev

 Und für ein bestimmtes Plone-Release sieht die Angabe so aus::

  recipe = plone.recipe.plone==3.1.7

 Das ``plone``-Rezept gibt jeweils passende Zope-Versionen, Produkte und Eggs an, die in den Abschnitten ``[zope2]`` und ``[instance]`` mit den Buildout-Variablen ``${plone:zope2-url}``, ``${plone:eggs}`` und ``${plone:products}`` referenziert werden.

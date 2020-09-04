================================
Aktualisierung und Versionierung
================================

Aktualisierung
==============

Damit Änderungen der buildout.cfg wirksam werden, müssen wir ``./bin/buildout``
erneut aufrufen. Diese Aktualisierung kann häufig beschleunigt werden, indem
buildout im *non-updating*-Modus aufgerufen wird, also::

 $ ./bin/buildout -N

Eine Übersicht über alle für ``buildout`` verfügbaren Optionen erhalten Sie mit::

 $ ./bin/buildout -h

Versionen festschreiben
=======================

zc.buildout < 2.0 verwendet üblicherweise immer die neueste Version eines Eggs.
Sollen jedoch nur finale Versionen verwendet werden, kann im buildout-Abschnitt
folgendes angegeben werden::

 prefer-final = true

zc.buildout < 2.0 aktualisiert üblicherweise immer auf die neueste Version. Dies
unterbleibt jedoch, wenn im buildout-Abschnitt folgendes angegeben wird::

 newest = false

Darüberhinaus kann ``buildout`` eine Fehlermeldung ausgeben, wenn Versionen noch
nicht festgeschrieben wurden mit::

 allow-picked-versions = false

In den oben angegebenen Beispielen wurde gezeigt, wie sich die Versionen für
Eggs, Recipes und Products fest vorgeben lassen.

Eine Liste der noch nicht festgeschriebenen Versionen erhalten wir in buildout ≥
2.0 mit::

 [buildout]
 …
 show-picked-versions = true

In früheren Buildout-Versionen können wir diese Angabe erhalten mit::

 $ ./bin/buildout -Nv | sed -ne 's/^Picked: //p' | sort | uniq

Ab Plone 4.1 werden die benötigten Versionen festgeschrieben indem in der
``buildout.cfg``-Datei auf eine externe ``versions.cfg``-Datei angegeben wird::

 [buildout]
 …
 extends =
    http://dist.plone.org/release/4.1/versions.cfg

 versions = versions

In der Datei ``http://dist.plone.org/release/4.1/versions.cfg`` werden dann im
``[versions]``-Abschnitt die von Plone benötigten Eggs in definierten Versionen
angegeben::

 [buildout]
 extends = http://download.zope.org/zopetoolkit/index/1.0.3/zopeapp-versions.cfg
           http://download.zope.org/Zope2/index/2.13.8/versions.cfg

 [versions]
 # Buildout infrastructure
 mr.developer = 1.17
 …

 # External dependencies
 …

 # Plone release
 Plone                                 = 4.1
 Products.ATContentTypes               = 2.1.3
 …

Falls weitere Eggs festgeschrieben werden sollen, kann nicht in der
``buildout.cfg``-Datei ein weiterer ``versions``-Abschnitt angegeben werden, es
kann jedoch in ``extends`` eine eigene ``versions.cfg``-Datei angegeben werden,
die ebenfalls wieder einen ``[versions]``-Abschnitt enthält. So kann z.B. die
``buildout.cfg``-Datei folgendermaßen aussehen::

 [buildout]
 …
 extends =
     http://dist.plone.org/release/4.1/versions.cfg
     versions.cfg

 versions = versions

Und in der ``versions.cfg``-Datei werden dann weitere Versionen festgeschrieben::

 [versions]
 …

Plone 3.1
---------

Sollen spezifische, in einem Rezept angegebene Versionen überschrieben werden, wird zunächst im ``buildout``-Abschnitt mit der Option ``versions`` auf einen Abschnitt verwiesen, der die zu verwendenden Versionen enthält::

 [buildout] … versions = release1

 [release1] plone.locking = 1.0.5

Anschließend muss das Egg noch im ``[plone]``-Abschnitt angegeben werden, um die
Festlegung der Version für dieses Produkt in ``plone.recipe.plone`` aufzuheben::

 [plone]
 recipe = plone.recipe.plone
 eggs =
     plone.locking

Siehe auch: `Repeatable buildouts: controlling eggs used <http://pypi.python.org/pypi/zc.buildout/1.0.0b30#repeatable-buildouts-controlling-eggs-used>`_

``buildout.dumppickedversions``
===============================

`buildout.dumppickedversions
<http://pypi.python.org/pypi/buildout.dumppickedversions>`_ ist eine
``buildout-extension`` für zc.buildout < 2.0, die alle Eggs, deren Versionen
bisher nicht festgeschrieben wurden, in einer ``versions.cfg``-Datei
festschreiben kann. Eine Beispielkonfiguration kann z.B. so aussehen::

 [buildout]
 …
 extensions =
     buildout.dumppickedversions
 dump-picked-versions-file = versions.cfg
 overwrite-picked-versions-file = false

Sofern noch nicht vorhanden, wird nun beim Aufruf von ``./bin/buildout`` eine ``versions.cfg``-Datei erzeugt, die z.B. so aussehen kann::

     [versions]
     Cheetah = 2.2.1
     Paste = 1.7.5.1
     PasteScript = 1.7.3
     ZopeSkel = 2.19
     i18ndude = 3.2.2

     #Required by:
     #PasteScript 1.7.3
     PasteDeploy = 1.3.4

     #Required by:
     #i18ndude 3.2.2
     ordereddict = 1.1

Kontrollierte Updates
=====================

`z3c.checkversions <http://pypi.python.org/pypi/z3c.checkversions/>`_
findet neuere Versionen der im Buildout-Projekt verwendeten Python-Pakete.

Es kann folgendermaßen installiert werden::

 [buildout]
 parts =
     …
     checkversions
 …
 [checkversions]
 recipe = zc.recipe.egg
 eggs = z3c.checkversions [buildout]

.. Subversion
   ==========

   Auch Versionen von Produkten aus einem Subversion-Repository lassen sich
   festschreiben::

    [buildout]
    …
    productcheckouts
    instance
    …

    [productcheckouts]
    recipe = infrae.subversion
    urls =
        https://svn.plone.org/svn/collective/eXtremeManagement/tags/1.5.2/ eXtremeManagement
        http://getpaid.googlecode.com/svn/trunk/products/PloneGetPaid@1132 PloneGetPaid

    [instance]
    …
    products =
        …
        ${productcheckouts:location}

   Darüberhinaus erlaubt `infrae.subversion
   <http://pypi.python.org/pypi/infrae.subversion>`_ auch, ausgecheckte
   Verzeichnisse als *development eggs* in das Buildout-Pojekt einzubinden.

   ``location``
    gibt das Zielverzeichnis an, sodass z.B. auch direkt in ``src`` heruntergeladen
    werden kann.
   ``as_eggs``
    Mit dem Wert ``true`` werden die Eggs als development eggs installiert.

   So kann die Buildout-Konfiguration z.B. so aussehen::

    [buildout]
    …
    ourpackages
    instance
    …

    [ourpackages]
    recipe = infrae.subversion
    urls =
        https://dev.veit-schiele.de/svn/vs/vs.policy/trunk vs.policy
        https://dev.veit-schiele.de/svn/vs/vs.theme/trunk vs.theme
    location = src
    as_eggs = true

    [instance]
    …
    eggs =
        ${buildout:eggs}
        ${plone:eggs}
        ${ourpackages:eggs}

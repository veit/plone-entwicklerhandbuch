==========================================
Migrieren beliebiger Webinhalte nach Plone
==========================================

Mit `collective.transmogrifier`_ lassen sich sog. Pipelines für den Ex- und Import von Webinhalten konfigurieren. Und zum Crawlen und Parsen einer statischen Website wird `funnelweb`_ verwendet.

.. _`collective.transmogrifier`: http://pypi.python.org/pypi/collective.transmogrifier
.. _`funnelweb`: http://pypi.python.org/pypi/funnelweb

Am Beispiel der auf dem Documentation-Server `Sphinx`_ basierenden Website des `Plone-Nutzerhandbuch`_ zeige ich exemplarisch, wie eine solche Migration aussehen kann: https://dev.veit-schiele.de/svn/plone-nutzerhandbuch/trunk/

.. _`Sphinx`: http://sphinx.pocoo.org/
.. _`Plone-Nutzerhandbuch`: http://www.plone-nutzerhandbuch.de/

Voraussetzungen
===============

- `Git`_

  Linux::

   $ sudo apt-get install git-core

  Mac::

   $ sudo port install git-core

.. _`Git`: http://git-scm.com/

Installation
============

Erstellen des ``migration``-Skripts::

 $ ./bin/buildout -c migration.cfg

Aufrufen des Skripts mit::

 $ ./bin/migration --ploneupload:target=http://admin:secret@localhost:8080/Plone/documentation/manual/plone-nutzerhandbuch

**Anmerkung 1:** In userem Fall wird das Plone-Nutzerhandbuch in eine lokale Plone-Site mit der ID Plone importiert wobei das Plone Help Center die ID documentation und das reference Manual die ID plone-nutzerhandbuch hat. Falls Sie die Dokumentation in eine andere Plone-Site mit anderen HTTP Basic Auth-Credentials importieren möchten, können Sie diese Zeile selbstverständlich entsprechend abändern.

Folgende Schritte werden während der Migration ausgeführt:

#. Aus der Sphinx-Dokumentation werden Titel, Beschreibung und Haupttext von jeder Seite extrahiert.
#. Anschließend werden die Inhalte für das Plone Help Center mit XML-RPC erzeugt.
#. Veröffentlichen der Artikel sofern notwendig und Verstecken des Ordners, der die Bilder enthält in der Navigation.

**Anmerkung 2:** Das Skript zum Hochladen der Dateien überschreibt momentan noch nicht bereits vorhandene Artikel. Falls Seiten umbenannt oder verschoben wurden, sollte zunächst die gesamte Dokumentation gelöscht werden bevor die Dateien erneut hochgeladen werden.

Konfiguration
=============

``migration.cfg``
-----------------

Das Skript ``bin/migration`` wird erstellt mit der in der ``migration.cfg`` angegebenen Konfiguration::

 [buildout]
 ...
 migration

 [migration]
 recipe = funnelweb
 crawler-url=file://${buildout:directory}/docs/html
 crawler-ignore=
     cgi-bin
     javascript:
     _static
     _sources
     genindex\.html
     search\.html
     saesrchindex\.js
 cache-output =
 template1-title = text //div[@class='body']//h1[1]
 template1-_permalink = text //div[@class='body']//a[@class='headerlink']
 template1-text = html //div[@class='body']
 template1-_label = optional //p[contains(@class,'admonition-title')]
 template1-description = optional //div[contains(@class,'admonition-description')]/p[@class='last']/text()
 template1-_remove_useless_links = optional //div[@id = 'indices-and-tables']
 templateauto-condition = python:False
 titleguess-condition = python:True
 indexguess-condition = python:True
 hideguess-condition =  python:item.get("_path","").startswith('_images') and item.get('_type')=='Folder'
 changetype-value=python:{'Folder':'HelpCenterReferenceManualSection','Document':'HelpCenterLeafPage'}.get(item['_type'],item['_type'])
 ploneprune-condition=python:item.get('_type') in ['HelpCenterReferenceManualSection','HelpCenterReferenceManual'] or item['_path'] == ''

``recipe``
 Verwendet wird funnelweb. Weitere Informationen zu diesem Abschnitt erhalten Sie auf der `Homepage`_.

 .. _`Homepage`: http://pypi.python.org/pypi/funnelweb

``crawler-url``
 legt die zu migrierende Website fest, in unserem Fall ``file://${buildout:directory}/docs/html``. Es könnte jedoch auch eine URL wie z.B. ``http://www.plone-nutzerhandbuch.de`` angegeben werden.
``crawler-ignore``
 Links, denen nicht gefolgt werden soll, können mit regulären Ausdrücken angegeben werden.

 In Falle des Documentation Servers Sphinx werden u.a. die Verzeichnisse ``_static`` und ``_sources`` ignoriert.

``cache-output``
 Da unsere Inhalte aus dem Dateisystem kommen, ist hier kein lokaler Cache nötig.
``titleguess-condition``, ``indexguess-condition``
 Bilder erhalten ihren Titel aus dem Backlink-Text
``hideguess-condition``
 Bilder werden nicht in der Navigation angezeigt
``changetype-value``
 Statt Ordnern werden HelpCenterLeafPage- und statt Seiten HelpCenterLeafPage-Artikeltypen angelegt
``ploneprune-condition``
 Die Inhalt aller ordnerähnlichen Artikel wird daraufhin überprüft, ob sie Inhalte enthalten, die noch nicht lokal gespeichert sind.

``pipeline.cfg``
----------------

Die ``pipeline.cfg`` definiert dann die Reihenfolge, in der die Anweisungen abgearbeitet werden. Ein Beispiel finden Sie wieder für das Plone-Nutzerhandbuch: `pipeline.cfg`_

.. _`pipeline.cfg`: https://dev.veit-schiele.de/svn/plone-nutzerhandbuch/trunk/pipeline.cfg

``drop-resources``
 filtert Ressourcen wie css-, Javascript- und Anwendungen aus
``drop-unneeded-html``
 filtert nicht benötigten HTML-Code aus
``treeserializer``
 muss vor dem localconstructor ausgeführt werden
``templatefinder``
 extrahiert Titel, Beschreibung und Haupttext aus den von Sphinx generierten Seiten.

 Beachten Sie bitte, dass *Note*-Leerzeichen in XPaths als ``&#32;`` angegeben werden müssen.

 Weitere Infos zu XPath erhalten Sie unter

 - http://www.w3schools.com/xpath/default.asp
 - http://blog.browsermob.com/2009/04/test-your-selenium-xpath-easily-with-firebug/

``mark-container-remote-content-type``
 erstellt einen Hinweis, sodass Verzeichnisse beim Hochladen als HelpCenterReferenceManualSection angelegt werden
``mark-page-remote-content-type``
 erstellt einen Hinweis, sodass HTML-Dateien beim Hochladen als HelpCenterLeafPage-Artikel angelegt werden
``mark-image-folders-to-navigation-exclusion``
 versteckt den images-Ordner in der Navigation.
``mark-remote-folder-to-be-cleaned``
 überprüft, ob ein Ordner Objekte enthält, die noch nicht lokal gespeichert wurden.
``mark-remote-root-to-be-cleaned``
 löscht alle Inhalte aus dem ausgewählten Reference Manual
``topublish``
 erstellt einen Hinweis, damit nach dem Hochladen der Workflow-Status auf veröffentlicht gesetzt wird.

 Dabei wird berücksichtigt, dass Bilder keinen Workflow unterliegen.

``ploneuploader``
 erstellt die Artikel in der Plone-Site
``schemaupdater``
 aktualisiert die Inhalte der Plone-Site mit den extrahierten Inhalten aus der Sphinx-Dokumentation
``set-folder-default-page``
 setzt index.html als Standardseite eines Ordners
``publish``
 veröffentlicht die hochgeladene Dokumentation sofern sie noch nicht veröffentlicht ist
``excludefromnavigation``
 versteckt Artikel in der Navigation
``cleanremotefolder``
 löscht Objekte, die auf der Plone-Site sind, jedoch nicht in der lokalen Kopie

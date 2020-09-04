=======================
Katalog in eigener ZODB
=======================

Wird der Katalog in einer eigenen ZODB gespeichert, können unterschiedliche Cache-Einstellungen für die Inhalte der Plone-Site und den Katalog angegeben werden. Damit werden bei einer umfangreichen Anfrage am Katalog keine Inhaltsobjekte mehr aus dem Cache  verdrängt. Wird darüberhinaus die ZODB mit dem Katalog noch auf einer eigenen Platte gespeichert, lässt sich die Performance noch weiter steigern.

In `ZODBs konfigurieren <....//produktivserver/zodbs-konfigurieren>`_ wird
allgemein beschrieben, wie zusätzlich ZODBs angegeben werden können.

#. Fügen Sie in der ``deploy.cfg``-Datei eine neue ZODB hinzu::

    [zeoserver]
    ...
    zeo-conf-additional =
        <filestorage 2>
            path ${buildout:directory}/var/filestorage/CatalogData.fs
        </filestorage>

    [instance1]
    ...
    zope-conf-additional =

        <zodb_db catalog>
            mount-point /mysite/portal_catalog
            container-class Products.CMFPlone.CatalogTool.CatalogTool
            cache-size 300000
            <zeoclient>
                server ${zeo:zeo-address}
                storage 2
                name catalogstorage
                var ${buildout:parts-directory}/instance1/var
                cache-size 400MB
            </zeoclient>
        </zodb_db>

#. Rufen Sie ``./bin/buildout`` aufund starten anschließend den ZEO-Cluster.
#. Nun erstellen wir eine neue Plone-Site mit der ID ``mysite``.

#. Löschen Sie ``portal_catalog`` in dieser Plone-Site.

   Beachten Sie, dass die Plone-Site anschließend nicht mehr funktioniert.

#. Gehen Sie in das ZMI dieser Site und wählen dort *ZODB Mount Point* aus.

   #. Im folgenden Formular sollte der ``portal_catalog``-Mount-Point
      verfügbar sein.
   #. Aktivieren Sie *create missing folders...*

#. Wechseln Sie anschließend in das ``portal_catalog``-Objekt.
#. Wechseln Sie in den *advanced*-Reiter und aktivieren dann *clear and
   rebuild*. Beachten Sie, dass dies einige Zeit dauern kann.

Schließlich ist der Katalog Ihrer Plone-Site in einem eigenen Mount-Point
verfügbar.

===========================
Upgrade von Zusatzprodukten
===========================

Häufig sind mit einer Aktualisierung von Plone auch die verwendetenZusatzprodukte zu aktualisieren. Dies ist nur eine generelle Anleitung, die keine Rücksicht auf produktspezifische Upgrade-Prozeduren nimmt.

#. Haben Sie weitere Produkte in Ihrer alten Plone-Site verwendet, müssen für diese ebenfalls aktuelle Versionen in der neuen Zope-Instanz installiert werden.
#. Starten Sie Ihre neue Zope-Instanz und überprüfen anschließend, ob im *Product Management*-Ordner des Zope Management Interface (ZMI) (``INSTANCE_URL/Control_Panel/Products/manage_main``) alle Produkte korrekt installiert wurden.
#. Navigieren Sie anschließend im ZMI zu Ihrer Site und dort in das *Plone QuickInstaller Tool* (``portal_quickinstaller``). Führen Sie ein Upgrade oder eine Neuinstallation der jeweiligen Produkte durch.

.. toctree::
    :titlesonly:
    :maxdepth: 0

    migration-eines-produkts-zu-plone-4.0
    migration-eines-produkts-zu-plone-4.1
    eigene-upgrade-skripte-schreiben
    python-3-migration

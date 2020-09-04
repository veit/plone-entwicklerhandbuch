=============
Plone-Upgrade
=============

Ein schneller Überblick, wie für eine Plone-Site ein Upgrade durchgeführt werden kann.

#. Erstellen Sie eine neue Zope-Instanz mit :doc:`Buildout
   <../../entwicklungsumgebung/index>`.
#. Geben Sie im ``[productdistros]``-Abschnitt Ihrer ``buildout.cfg``-Datei alle erforderlichen Zusatzprodukte an.
#. Ihre eigenen aktualisierten Produkte können Sie in das ``Products``-Verzeichnis Ihres Buildout-Projekts kopieren.
#. Fahren Sie Ihre alte Zope-Instanz herunter.
#. Kopieren Sie die ``var/Data.fs``-Datei aus Ihrer alten Instanz in das ``var/filestorage``-Verzeichnis Ihres Buildout-Projekts.
#. Konfigurieren Sie Ihre neue Zope-Instanz, s.a. :doc:`../../entwicklungsumgebung/buildout-konfiguration`.
#. Starten Sie Ihre neue Zope-Instanz.
#. Gehen Sie in das Zope Management Interface (ZMI) Ihrer Plone-Site und anschließend zum *Plone Migrations Tool* (``portal_migrations``).
#. Nachdem Sie den *Upgrade*-Reiter gewählt haben, erhalten Sie eine Angabe wie diese::

    Instance version: 4.3.18
    File system version: 5.2

#. Klicken Sie die *Upgrade*-Taste.

.. toctree::
    :titlesonly:
    :maxdepth: 0
    :hidden:

    aktualisieren-von-plone-4.1-zu-4.2
    aktualisieren-von-plone-4.2-zu-4.3
    python-3-migration-der-zodb

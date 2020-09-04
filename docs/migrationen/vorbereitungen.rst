Vorbereitungen
==============

Bevor Sie eine Plone-Site aktualisieren, sollten Sie verschiedenes vorbereiten.

Sammeln Sie die notwendigen Informationen zusammen
--------------------------------------------------

#. Lesen Sie *What's new in...* und die *release notes* der für Sie relevanten Plone-Version. Sie finden diese im CMFPlone-Ordner Ihrer Distribution.
#. Überprüfen Sie die Abhängigkeiten

   #. Die Abhängigkeiten werden in den *release notes* angegeben:

      - Welche Python-Version?
      - Welche Zope-Version?
      - Welche Python-Bibliotheken?

   #. Achten Sie darauf, dass alle der von Ihnen verwendeten
      Zusatzprodukte die neue Plone-Version unterstützen.

      Einen Überblick über alle Artikel einer Plone 2.5- oder
      3.x-Site erhalten Sie mit `mr.inquisition
      <http://pypi.python.org/pypi/mr.inquisition>`_. Dabei
      erhalten Sie Informationen

      - zur Art der Artikeltypen
      - zur Anzahl der Artikel je Artikeltyp
      - zum Ort der Artikel
      - zu Artikeln, die mit deinstallierten Produkten
        erstellt wurden

      Installiert werden kann ``mr.inquisition`` mit::

       [buildout]
       ...
       eggs =
           ...
           mr.inquisition

       [instance]
       ...
       zcml =
           mr.inquisition

      Nach dem Durchlaufen des Buildout-Skripts und dem
      Starten der Instanz erhalten Sie z.B. unter
      ``http://localhost:8080/Plone/@@inquisition`` einen
      Überblick über die verfügbaren Ansichten zur Analyse
      der ZODB.

   #. Falls die neue Version von Plone auf
      einer aktuelleren Zope-Version basiert,
      sollten Sie diese vor dem Plone-Update
      installieren.

      - **Achtung:** Zope hat seine eigenen Migrationsrichtlinien, die in den *release notes* derjenigen Zope-Version zu finden sind, auf die Sie migrieren möchten. Im allgemeinen aktualisiert Plone jedoch mit seinen Migrationsskripten auch die Zope-Version.

   #. Lesen Sie die folgenden Dateien in Ihrem CMFPlone-Ordner:

      - ``README.txt``
      - ``INSTALL.txt``
      - ``UPGRADE.txt``

      Diese Dateien können wichtige *last minute* Informationen und spezifische Anweisungen enthalten.

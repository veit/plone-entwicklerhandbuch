==============
Fehlerbehebung
==============

Prozeduren beim Auftreten von Problemen während des Plone-Upgrades.

#. Fährt die Zope-Instanz nicht mit ``ZOPE_INSTANCE/bin/zopectl start`` hoch, erhalten Sie mit ``ZOPE_INSTANCE/bin/zopectl fg`` Hinweise, an welcher Stelle Zope hängen bleibt.

#. Überprüfen der Log-Dateien

   Wenn ein Fehler auf der aktualisierten Plone-Site ausgegeben wird, gibt es möglicherweise eine informative Fehlermeldung in den Log-Dateien der Zope-Instanz. Gehen Sie zu ``ZOPE_INSTANCE/logs/event.log`` und suchen dort nach ``error``, ``exception`` oder ``traceback``.

   Detailliertere Informationen zu den Fehlermeldungen finden Sie in

   - `Version-specific migration procedures and tips`_;
   - `Plone Error References`_

#. Testen der Anpassungen

   Wenn Sie Page Templates und Python-Skripte angepasst haben, mögen diese Änderungen mit der neuen Plone-Versionen interferieren. Entfernen Sie temporär diese Anpassungen indem Sie die Layer aus dem von Ihnen verwendeten Skin entfernen.

#. Testen der Zusatzprodukte

   #. Um Bugs oder Kompatibilitätsprobleme in den installierten Zusatzprodukten herauszufinden, deinstallieren Sie alle Produkte, die nicht zusammen mit Plone ausgeliefert werden, in *Site Setup*, *Add/Remove Products*. Anschließend entfernen Sie diese Produkte aus dem Produktverzeichnis Ihrer Zope-Instanz.

   #. Falls das Problem hiermit beseitigt wird, überprüfen Sie für jedes der betreffenden Produkte:

      - ob dessen Version auch mit den aktuellen Versionen von Plone, Zope und Python kompatibel ist?
      - ob dieses Produkt zusätzliche Upgrade-Prozeduren benötigt?
      - ob das Produkt korrekt installiert ist? Installieren Sie es erneut und überprüfen Sie die Ausgabe beim Starten der Zope-Instanz mit ``ZOPE_INSTANCE/bin/zopectl fg``.

      - Liegt ein Produkt nicht für die aktuelle Plone-Version vor und hinterlässt beim Deinstallieren »verwaiste« Inhalte, so können Sie sich mit folgendem Skript solche Inhalte auflisten lassen::

         portal_types = context.portal_types.objectIds()

         print "Orphaned items:"
         print

         for i in context.portal_catalog.uniqueValuesFor('portal_type'):
            if i in portal_types: continue
            print i
            results = context.portal_catalog(portal_type=i)
            for i in results:
                print i.getURL()
            print
         return printed

        Um das Skript zu verwenden, erstellen Sie im ZMI des Wurzelverzeichnisses Ihrer Plone-Site ein Python-Skript, kopieren den Code in das Formular und sichern es anschließend. Zum Ausführen des Skripts müssen Sie nun nur noch in den «Test»-Reiter klicken.

   #. Wie Sie Upgrade-Skripte für Ihre eigenen Produkte schreiben können, erfahren Sie hier: `Eigene Upgrade-Skripte schreiben`_.

#. Testen Sie in einer neu aufgesetzten Plone-Site.

   Falls das Problem nicht in einer neu aufgesetzten Plone-Site auftritt, bedeutet dies, dass die Ursache zu suchen ist

   - in einer Anpassung
   - einem Zusatzprodukt
   - oder in Inhalten, die nicht sauber migriert wurden.

#. Machen Sie das Problem reproduzierbar

   Bevor Sie andere um Hilfe bitten, sollten Sie das Problem so beschreiben können, dass es für andere in deren Systemumgebung nachvollziehbar ist. Schränken Sie hierzu die Fehlerquellen so weit wie möglich ein um es anderen zu erleichtern, Ihr Problem nachvollziehen zu können.

.. _`Version-specific migration procedures and tips`: http://plone.org/documentation/manual/upgrade-guide/version
.. _`Plone Error References`: http://plone.org/documentation/error
.. _`Eigene Upgrade-Skripte schreiben`: eigene-upgrade-skripte-schreiben.html

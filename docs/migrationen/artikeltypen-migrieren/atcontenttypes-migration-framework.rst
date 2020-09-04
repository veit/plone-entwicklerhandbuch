==================================
ATContentTypes Migration Framework
==================================

Das ATContentTypes-Produkt wird mit einem eigenen Migration Framework ausgeliefert.

ATContentTypes verwendet eine *Registry* für Migrationen, die im ATCT Tool (``portal_atct``) verwaltet werden. Dies ermöglicht, Migrationen in einem einfach zu bedienenden Web-Interface durchzuführen. In vielen Fällen reicht jedoch eine manuell erstellte *External Method* vollkommen aus, da Migrationen meist nur einmal aufgerufen werden müssen.

Beispiel
========

Zu einem früheren Zeitpunkt wurde ein CMF-Inhaltstyp *PhotoAlbum* erstellt und dieser soll nun in einen einfachen  Archetypes  *Folder* zurückverwandelt werden. Hierzu wird, sofern noch nicht vorhanden, in unserem Produkt ``src/vs.photo/vs/photo/upgrades.py`` und folgendem Inhalt angelegt::

 from Products.CMFCore.utils import getToolByName
 from StringIO import StringIO
 from Products.ATContentTypes.migration.walker import CatalogWalker
 from Products.ATContentTypes.migration.migrator import CMFFolderMigrator

 class  PhotoAlbumMigrator(CMFFolderMigrator):
     """Base class to migrate PhotoAlbum to Folder.
     """
     walkerClass = CatalogWalker
     src_meta_type = 'PhotoAlbum'
     src_portal_type = 'PhotoAlbum'
     dst_meta_type = 'ATFolder'
     dst_portal_type = 'Folder'

  def migrate(self):
      """Run the migration"""

      out = StringIO()
      print >> out, "Starting migration"

      portal_url = getToolByName(self, 'portal_url')
      portal = portal_url.getPortalObject()

      migrators = (PhotoAlbumMigrator,)

      for migrator in migrators:
          walker = migrator.walkerClass(portal, migrator)
          walker.go(out=out)
          print >> out, walker.getOutput()

      print >> out, "Migration finished"
      return out.getvalue()

Nun muss nur noch im Wurzelverzeichnis der Site eine neue *External Method* erstellt werden mit

ID
 ``migrateTypes``
Module
 vs.photo.migrate
function name
 migrate

Um die externe Methode auszuführen, müssen Sie nur noch in den «Test»-Reiter klicken [#]_.

Konzept
=======

In dem oben genannten Beispiel wird in der ``migrate()``-Funktion ein *Migrator* auf alle mit einem  *Walker* gefundenen Objekte angewendet.

Walker
------

Sie werden zum Finden der zu migrierenden Inhalte verwendet. Der einfachste *Migrator* ist der *CatalogWalker* in `walker.py`_, der eine Katalogabfrage für alle Inhalte eines bestimmten Typs durchführt.

Migrator
--------

Sie sind einfache Klassen, die die gegebenen Inhaltstypen migrieren. Das Framework enthält Basisklassen, die das Schreiben von *Migrators* stark vereinfachen.

Ein *Migrator* ist meist eine von ``CMFFolderMigrator`` oder ``CMFItemMigrator`` abgeleitete Klasse. Diese beiden und weitere Basis-Migrationsklassen sind in `migrator.py`_ definiert:

``CMFItemMigrator``
 migriert einen CMF-Typ einschließlich seiner Meta-Angaben, lokalen Rollen etc.
``CMFFolderMigrator``
 gewährleistet darüberhinaus, dass auch die Inhalte migriert werden.

Es gibt drei Arten von Migrationen:

#. Jede Methode in einer Klasse, die mit ``migrate_`` beginnt, wird automatisch aufgerufen.

   Wenn Sie sich z.B. die ``BaseMigrator``-Klasse  anschauen, sehen Sie eine Reihe solcher Methoden, ``migrate_properties``, ``migrate_owner``, etc.

   Auch die Reihenfolge, in der die Methoden aufgerufen werden, sind durch Präfixe definiert:

   ``beforeChange_``
      Methoden, wie z.B. ``beforeChange_storeDates`` oder ``beforeChange_storeSubojects``, die vor der Migration angewandt werden.
   ``last_migrate_``
      Methoden, wie ``last_migrate_date``, die aufgerufen werden, bevor der *Migrator* die Migration eines Objekts beendet.

#. Die Methode ``custom()`` wird nach den ``migrate_``- aber vor den ``last_migrate_``-Methoden aufgerufen. Die Standardimplementierung ist leer und dient nur dazu,von einer eigenen Migrationsmethode überschrieben zu werden. Hier ein Beispiel aus `atctmigrator.py`_::

    class FileMigrator(CMFItemMigrator):
        walkerClass = CatalogWalker
        ...

        def custom(self):
            ctype = self.old.getContentType()
            file = str(self.old)
            self.new.setFile(file, mimetype = ctype)

#. Schließlich noch die einfachste Methode mit der ``map class``-Variablen, die eine Zuordnung von Attributen und/oder Methoden erlaubt. Auch hier wieder ein Beispiel aus `atctmigrator.py`_::

    class LinkMigrator(CMFItemMigrator):
        walkerClass = CatalogWalker
        map = {'remote_url' : 'setRemoteUrl'}

.. [#] **Warnung:** Migrationen können normalerweise nur selten rückgängig gemacht werden da sie meist mehrere Transaktionen zugleich umfassen. Daher sollten Sie unbedingt vor der Migration eine Sicherungskopie Ihrer Plone-Site erstellen.

.. _`walker.py`: http://dev.plone.org/collective/browser/ATContentTypes/trunk/migration/walker.py?rev=9994
.. _`migrator.py`: http://dev.plone.org/collective/browser/ATContentTypes/trunk/migration/migrator.py?rev=9994
.. _`atctmigrator.py`: http://dev.plone.org/collective/browser/ATContentTypes/trunk/migration/atctmigrator.py?rev=9994

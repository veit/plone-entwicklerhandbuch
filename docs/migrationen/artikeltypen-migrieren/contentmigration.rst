================
contentmigration
================

Das contentmigration-Produkt wird für Migrationen verschiedener Versionen desselben Typs genutzt.

Häufiger als die Migration von einem Inhaltstyp zu einem anderen ist die Änderung der internen Organisation eines Inhaltstyps. Das Archetypes-Tool bietet einige Hilfsmittel zur Durchführung von solchen Migrationen über den *Update Schema*-Reiter. Diese synchronisieren die ZODB-Schemata Ihrer Inhaltstypen mit dem auf Dateisystem-Ebene definierten Inhaltstyp. Beachten Sie jedoch, dass Sie dabei Daten verlieren können. Wenn Sie z.B. ein Feld umbenannt haben, führt *Update Schema* für bestehende Objekte zu leeren oder Standardwerten für das neue Feld. Um die alten Daten zu erhalten, ist eine Migration nötig.

Für solche Fälle wurde das `contentmigration`_-Produkt geschreiben. Sie können *contentmigration* installieren, indem Sie in ``buildout.cfg`` folgendes eintragen::

 [buildout]
 ...
 eggs =
     ...
     Products.contentmigration

Beispiel
========

Anschließend kann es von Ihren eigenen Migrationsmethoden aufgerufen werden, z.B.::

 from Products.contentmigration.walker import CustomQueryWalker
 from Products.contentmigration.migrator import FieldActionMigrator
 from Products.Archetypes.public import *

 class MyMigrator(FieldActionMigrator):
     src_portal_type = 'MyType'
     src_meta_type = 'MyType'

     fieldActions = ({'fieldName'    : 'someField',
                      'storage'      : AttributeStorage(),
                      'newFieldName' : 'renamedField',
                      'newStorage'   : AnnotationStorage(),
                      'transform'    : lambda obj, val, **kw: val + 10,
                      })

Methoden
========

*contentmigration* erweitert die ATContentTypes-Migrator um folgende Methoden:

CustomQueryWalker
-----------------

Der ``CustomQueryWalker`` spezifiziert eine Katalogabfrage, z.B. kann die Migration auf Teilinhalte Ihrer Site beschränkt werden mit::

 walker = CustomQueryWalker(portal, migrator,
                            query = {'path' : '/some/path'})
 walker.go()

Gegebenenfalls können ``src_portal_type`` und ``src_meta_type`` aus dem Migrator in die Anfrage eingefügt werden.

Der ``CustomQueryWalker`` kann von jedem *Migrator* genutzt werden.

BaseInlineMigrator
------------------

Der ``BaseInlineMigrator`` ist dem ``BaseMigrator`` ähnlich; während jedoch der ``BaseMigrator`` ein altes Objekt temporär kopiert, ein neues Objekt erstellt und dann die Migrationsmethoden anwendet, werden beim ``BaseInlineMigrator`` die Migrationsmethoden auf der Stelle angewendet. Dies vereinfacht den Code deutlich, da Attribute, lokale Rollen etc. nicht kopiert werden müssen. Er eignet sich daher für Migrationen, in denen sich die Felder bestimmter Objekte ändern.

Folgende Methoden können verwendet werden: ``migrate_``, ``beforeChange_`` ``last_migrate_`` und ``custom()``, nicht jedoch das ``map class``-Attribut.

**Achtung:**  Sie können nur ``self.obj`` verwenden, nicht ``self.old`` und ``self.new``.

Auch ``BaseInlineMigrator`` kann von jedem *Walker* verwendet werden.

FieldActionMigrator
-------------------

Der ``FieldActionMigrator`` ist eine Erweiterung von ``BaseInlineMigrator`` um Aktionen, die auf Felder angewendet werden können. Dafür wird eine Liste der zu migrierenden Attribute und der auszuführenden Aktion angegeben. Detaillierte Informationen zu diesen Aktionen erhält man direkt in der `field.py`_-Datei. Beispiele finden sich in `testATFieldMigration.py`_.

.. _`contentmigration`: https://svn.plone.org/svn/collective/contentmigration/trunk
.. _`field.py`: http://svn.plone.org/svn/collective/Products.contentmigration/trunk/Products/contentmigration/field.py
.. _`testATFieldMigration.py`: http://svn.plone.org/svn/collective/Products.contentmigration/trunk/Products/contentmigration/tests/testATFieldMigration.py

.. Poi enthält ein `Migrationsskript`_, das contentmigration nutzt.
.. _`Migrationsskript`: https://svn.plone.org/svn/collective/Poi/trunk/Extensions/Migrations.py

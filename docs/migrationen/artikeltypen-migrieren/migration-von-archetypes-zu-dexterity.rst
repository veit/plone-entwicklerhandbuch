=====================================
Migration von Archetypes zu Dexterity
=====================================

`plone.app.contenttypes <https://pypi.python.org/pypi/plone.app.contenttypes>`_
kann alle Standard-Plone-Artikeltypen zu Dexterity migrieren. Hierzu gehören
auch *Topics*, die früheren Kollektionen. Die Migration schließt auch die
meisten Features ein, wie Portlets, Kommentare, Contentrules, lokale Rollen und
lokale Workflows.

.. warning::
   Frühere Versionen der Inhalte bleiben bei der Migration nicht erhalten.

Migration einzelner Artikeltypen
================================

Mit ``@@pac_installer`` gibt es eine Ansicht, die die Installation von ``plone.app.contenttypes`` erlaubt ohne dass die alten Archetypes-basierten
Artikeltypen ersetzt werden. Anschließend wird auf das Migrationsformular
weitergeleitet und die zu migrierenden Artikeltypen können ausgewählt werden.
Dies erlaubt ihnen, nur bestimmte Archetypes-Artikeltypen zu migrieren.

Migrieren von *Topics*
======================

*Topics* unterstützten sog. *Subtopics*, ein Feature, das in Kollektionen nicht
mehr exisitert. Daher müssen Kollektionen zunächst *folderish* werden bevor eine
Migration von Subtopics durchgeführt werden kann. Hierfür muss die Basisklasse
von ``plone.dexterity.content.Container`` abgeleitet werden und nicht von
``plone.dexterity.content.Item``::

    from plone.app.contenttypes.behaviors.collection import ICollection
    from plone.dexterity.content import Container
    from zope.interface import implementer

    @implementer(ICollection)
    class FolderishCollection(Container):
        pass

Falls die bestehende Kollektion überschrieben werden soll, kann die
``Collection.xml`` verwendet werden::

    <?xml version="1.0"?>
    <object name="Collection" meta_type="Dexterity FTI">
        <property name="klass">my.package.content.FolderishCollection</property>
    </object>

Und falls die Suche der übergeordneten Kollektion vererbt werden soll, sind die
Änderungen aus `acquire query
<https://github.com/plone/plone.app.contenttypes/commit/366cc1a911c81954645ec6aabce925df4a297c63>`_ erforderlich.

Migrieren von Inhalten, die mit LinguaPlone übersetzt wurden
============================================================

Da LinguaPlone die Dexterity-Artikeltypen nicht unterstützt, muss zunächst von LinguaPlone zu `plone.app.multilingual
<https://pypi.python.org/pypi/plone.app.multilingual>`_ migriert werden. Weitere
Hinweise finden Sie in `LinguaPlone-Migration <linguaplone-migration>`_.

Migrieren von ``collective.contentleadimage``
=============================================

`collective.contentleadimage <https://plone.org/products/content-lead-image/>`_
erweiterte die Standard-Plone-Artikeltypen um ein Bild. Dieses Bild bleibt bei
der Migration erhalten sofern der zugehörige Dexterity-Artikeltyp das *Behavior*
«Lead Image» hat. Dabei informiert zunächst das Navigationsformular mit dem
Kommentar *extended fields: ‘leadImage’, ‘leadImage_caption’* und auch das
Migrationsformular zeigt für jeden Dexterity-Typ an, ob er das *Behavior* hat.

Migrieren eigener Artikeltypen
==============================

Während der Migration der Standard-Artikeltypen werden die eigenen Artikeltypen
nicht migriert. ``plone.app.contenttypes`` enthält jedoch auch ein
Migrationsformular für solche Artikeltypen: ``@@custom_migration``. Dabei muss
der Dexterity-Artikeltyp, zu dem migriert werden soll existieren und die Klasse
des alten Artikeltyps noch existieren. Der alte Artikeltyp muss hingegen nicht
in ``portal_types`` registriert sein – er kann dort auch bereits durch den
Dexterity-Typ ersetzt worden sein.

Im View ``@@custom_migration`` kann für jeden Archetypes- der entsprechende
Dexterity-Typ ausgewählt werden. Anschließend können die Felder aufeinander
abgebildet werden oder auch Felder ignoriert werden.

Anschließend wird die Konfiguration überprüft indem ein migrierter Artikel
aufgerufen wird: Geschieht dies fehlerfrei, ist der Test bestanden. Anschließend
werden die Änderungen wieder zurückgerollt.

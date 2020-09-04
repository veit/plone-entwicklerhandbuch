==========
Archetypes
==========

**Anmerkung:** Eine vollständige Referenz zu Archetypes finden Sie in http://plone.org/documentation/manual/archetypes-developer-manual oder in ``Products.Archetypes.atapi``.  Für Beispiele empfehlen sich die Quellen von ``Products.ATContentTypes``.

Content-Basisklassen
====================

Üblicherweise sind die Content-Klassen von einer der folgenden Klassen abgeleitet:

``BaseContent``
 ein einfacher, *non-folderish* Artikeltyp, der die Dublin Core-Metaangaben (über die ``ExtensibleMetadata``-Mixin-Klasse) enthält.
``BaseFolder``
 eine ``folderish``-Version von ``BaseContent``.
``OrderedBaseFolder``
 Version von ``BaseFolder``, der die Sortierung der enthaltenen Objekte erlaubt.
``BaseBTreeFolder``
 Version von ``BaseFolder``, der die Inhalte in einem *binary tree* speichert und damit gut geeignet ist, mehrere tausend Objekte zu enthalten.

Alle vier Klassen sind importierbar von ``Products.Archetypes.atapi``.

In unserem Fall sollen *Registration* und *Registrant* jedoch den Plone-Artikeltypen ähnlich sein, z.B. beim Editieren sollen die Felder in verschiedene Reiter kategorisiert werden und auch ein Feld für Verweise soll enthalten sein. Daher werden die Artikeltypen von Plone erweitert, die in ``Products.ATContentTypes.content`` implementiert sind. *Registrant* erweitert dabei ``base.ATCTContent``, in dem das übliche Verhalten aller einfachen (non-folderish) Artikeltypen von Plone bereits definiert ist::

 class Registrant(base.ATCTContent):
     implements(IRegistrant)

     portal_type = "Registrant"
     _at_rename_after_creation = True
     schema = RegistrantSchema

``Registrant``
 erweitert ``base.ATCTContent`` und implementiert ``IRegistrant``.
``portal_type``
 ist der eindeutige Name des Artikeltyps.
``at_rename_after_creation``
 benennt Objekte in die normalisierte Version ihres Titels um.

Schema
======

Für den obigen Artikeltyp wird das Schema direkt oberhalb der Klasse definiert::


 RegistrantSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

     atapi.StringField('email',
         required=True,
         searchable=True,
         storage=atapi.AnnotationStorage(),
         widget=atapi.StringWidget(label=_(u"Email"),
                                   description=_(u""))
         ),

     ))

 RegistrantSchema['title'].storage = atapi.AnnotationStorage()
 RegistrantSchema['title'].widget.label = _(u"Registrant name")
 RegistrantSchema['title'].widget.description = _(u"")

 RegistrantSchema['description'].storage = atapi.AnnotationStorage()
 RegistrantSchema['description'].widget.label = _(u"Address")
 RegistrantSchema['description'].widget.description = _("")

 RegistrantSchema['email'].storage = atapi.AnnotationStorage()
 RegistrantSchema['email'].widget.label = _(u"Email")
 RegistrantSchema['email'].widget.description = _(u"")

 finalizeATCTSchema(RegistrantSchema, folderish=False, moveDiscussion=False)

 class Registrant(base.ATCTContent):
     """Describe a registrant.
     """
     implements(IRegistrant)

     portal_type = "Registrant"
     _at_rename_after_creation = True
     schema = RegistrantSchema

     name = atapi.ATFieldProperty('title')
     address = atapi.ATFieldProperty('description')
     email = atapi.ATFieldProperty('email')

 atapi.registerType(Registrant, PROJECTNAME)

Zunächst wird das Schema von einem Basistypen, in diesem Fall ``ATContentTypeSchema``, kopiert und anschließend das eigene Schema angehängt.

Felder
======

Im Folgenden eine Liste der gebräuchlichsten Felder:

+-----------------+--------------------------+-----------------------------------+
| Feld            | dazugehörige             | Beschreibung                      |
|                 | Widgets                  |                                   |
+=================+==========================+===================================+
| StringField     | StringWidget,            | Eine einzelne Textzeile           |
|                 | SelectionWidget,         |                                   |
|                 | PasswordWidget           |                                   |
+-----------------+--------------------------+-----------------------------------+
| TextField       | TextAreaWidget,          | Mehrzeiliges Textfeld, wobei      |
|                 | RichWidget               | das ``RichWidget``  den           |
|                 |                          | WYSIWYG-Editor einbindet          |
+-----------------+--------------------------+-----------------------------------+
| LinesField      | LinesWidget,             | Liste von Zeichenketten,          |
|                 | MultiSelectionWidget,    | mehrzeilig                        |
|                 | InAndOutWidget           |                                   |
+-----------------+--------------------------+-----------------------------------+
| IntegerField    | IntegerWidget            | Ganze Zahl                        |
+-----------------+--------------------------+-----------------------------------+
| FixedPointField | DecimalWidget            | Dezimalzahl                       |
+-----------------+--------------------------+-----------------------------------+
| BooleanField    | BooleanWidget            | Wahr/falsch-Checkbox              |
+-----------------+--------------------------+-----------------------------------+
| FileField       | FileWidget               | Feld um Dateien hochzuladen       |
+-----------------+--------------------------+-----------------------------------+
| ImageField      | ImageWidget              | Feld um Bilder hochzuladen        |
+-----------------+--------------------------+-----------------------------------+
| DateTimeField   | CalendarWidget           | Feld um ein Datum auszuwählen     |
+-----------------+--------------------------+-----------------------------------+
| ReferenceField  | ReferenceWidget,         | Referenz auf ein anderes          |
|                 | InAndOutWidget           | Archetypes-Objekt                 |
+-----------------+--------------------------+-----------------------------------+

.. Das ``TextField`` mit ``TextAreaWidget`` ist nur in der Bearbeiten-Ansicht mehrzeilig. Alle Zeilenumbrüche werden für die Ansicht entfernt. Das ``LinesField`` mit ``LinesWidget`` ist mehrzeilig in Bearbeiten- und Ansichtsmodus. Mehrfache aufeinander folgende Zeilenumbrüche werden zu einem zusammengefasst.

Werden für SelectionWidgets Vokabularien (Wertelisten) verwendet hängt die Umsetzung des Widgets von der Größe der Werteliste ab. Bei bis zu drei Werten werden Radiobuttons verwendet, ab vier Werten erhält man eine Select-Box.

Die Felder lassen sich mit beliebig vielen Eigenschaften versehen. Im Folgenden nur eine Übersicht über die gebräuchlichsten Eigenschaften:

+--------------------------+-----------------------------------------------------+
| Feldeigenschaft          | Beschreibung                                        |
+==========================+=====================================================+
| required                 | Erforderlich, die möglichen Werte sind              |
|                          | ``true`` oder ``false``.                            |
+--------------------------+-----------------------------------------------------+
| searchable               | Der Wert ``true`` schließt das Feld in die          |
|                          | ``Searchable Text``-Suche ein.                      |
+--------------------------+-----------------------------------------------------+
| default                  | Bietet einen Standardwert für dieses Feld.          |
|                          |                                                     |
+--------------------------+-----------------------------------------------------+
| default_method           | Name einer Methode (als Zeichenkette), die          |
|                          | aufgerufen wird, um den Standardwert zu             |
|                          | liefern.                                            |
+--------------------------+-----------------------------------------------------+
| schemata                 | Der Name eines Reiters in der Editieransicht.       |
|                          | Das Standardschema ist ``Default``.                 |
|                          | Durch den Aufruf von ``finalizeATCTSchema()``       |
|                          | werden verschiedene Änderungen am Schema            |
|                          | vorgenommen, die das Plone-spezifische              |
|                          | Erscheinungsbild ermöglichen.                       |
+--------------------------+-----------------------------------------------------+
| read_permission,         | Die Namen der Berechtigungen, die zum Lesen         |
|                          | bzw. Schreiben des Feldes erforderlich sind.        |
| write_permission         | Die Standardwerte sind ``View`` bzw.                |
|                          | ``Modify portal content``.                          |
+--------------------------+-----------------------------------------------------+
| vocabulary,              | Definieren eines Vokabulars für das                 |
|                          | Auswahlfeld, s.u.                                   |
| vocabulary_factory,      |                                                     |
|                          |                                                     |
| enforceVocabulary        |                                                     |
+--------------------------+-----------------------------------------------------+
| validators               | Eine Liste von Feldvalidatoren, s.u.                |
+--------------------------+-----------------------------------------------------+
| accessor,                | Überschreibt die Namen der Accessor-,               |
|                          | Edit-Accessor- oder Mutator-Methode.                |
| edit_accessor,           |                                                     |
|                          |                                                     |
| mutator                  |                                                     |
+--------------------------+-----------------------------------------------------+
| widget                   | Widget, mit dem das Feld dargestellt werden         |
|                          | soll                                                |
+--------------------------+-----------------------------------------------------+
| storage                  | Speicherabstraktion,  die für dieses Feld           |
|                          | verwendet werden soll                               |
|                          | Der Standardwert ist ``AttributeStorage``           |
|                          |                                                     |
|                          | ``AttributeStorage``                                |
|                          |  die Feldwerte werden in Attributen dieses          |
|                          |  Objekts gespeichert. Die Attribute haben           |
|                          |  dabei denselben Namen wie das Feld                 |
|                          | ``AnnotationStorage``                               |
|                          |  speichert die Werte in Zope3-Annotations,          |
|                          |  wodurch das Risiko von Namenskonflikten            |
|                          |  vermieden wird                                     |
+--------------------------+-----------------------------------------------------+

Widgets
=======

Widgets werden in ``Products.Archetypes.Widget`` definiert. Und ähnlich wie für Felder gibt es auch für Widgets eine Reihe von Eigenschaften, wovon die Häufigsten unten aufgeführt sind:

+--------------------------+-----------------------------------------------------+
| Widget-Eigenschaft       | Beschreibung                                        |
+==========================+=====================================================+
| ``label``                | Eine Zeichenkette oder übersetzbare Nachricht,      |
|                          | die als Etikett des Widgets verwendet wird          |
+--------------------------+-----------------------------------------------------+
| ``description``          | Eine Zeichenkette oder übersetzbare Nachricht,      |
|                          | die als Hilfe-Text verwendet wird                   |
+--------------------------+-----------------------------------------------------+
| ``condition``            | Ein TALES-Ausfruck, die bestimmt, ob ein            |
|                          | Widget angezeigt wird. Die Variablen                |
|                          | ``object``, ``portal`` und ``folder`` sind in       |
|                          | diesem Kontext verfügbar                            |
+--------------------------+-----------------------------------------------------+
| ``size``                 | Die Länge einer Textbox oder die Höhe einer         |
|                          | Auswahlbox                                          |
+--------------------------+-----------------------------------------------------+
| ``rows``                 | Höhe einer Textbox                                  |
|                          |                                                     |
+--------------------------+-----------------------------------------------------+
| ``default_output_type``  | Wird von ``RichWidget`` verwendet um den            |
|                          | eingegebenen Text bei der Ausgabe zu                |
|                          | verändern                                           |
|                          |                                                     |
|                          | ``text/x-html-safe``                                |
|                          |  nutzt Plone’s HTML-Filter-Richtlinien zum          |
|                          |  Ausfiltern potentiell gefährlicher Tags            |
|                          | ``text/html``                                       |
|                          |  kann verwendet werden, wenn Sie Ihren Nutzern      |
|                          |  trauen                                             |
+--------------------------+-----------------------------------------------------+

Vokabularien
============

``vocabulary``
 spezifisches Vokabular für ein Feld.
``enforceVocabulary``
 wenn der Wert ``True`` ist und der eingegebene Wert nicht im Vokabular vorhanden ist, gibt Archetypes einen *validation error* aus.
``vocabulary_factory``
 erwartet den Namen einer Zope3-``IVocabularyFactory``-Hilfsmethode. Damit kann Archetypes Zope3-Vokabularien nutzen und sie z.B. mit formlib-Formularen teilen.

Das einfachste Vokabular ist eine statische Liste von akzeptierten Werten (ganze Zahlen für das ``IntegerField`` und Zeichenketten für das ``StringField``).

Vokabularien werden im allgemeinen zusammen mit einem ``SelectionWidget``, ``MultiSelectionWidget`` oder ``InAndOutWidget`` verwendet, wobei nur die Werte des Vokabulars für die Auswahl verfügbar sind. Alternativ kann das ``AddRemoveWidget``, das eine flexiblere Handhabung des Vokabulars ermöglicht und über ein separates Egg importiert werden muss. Um das Vokabular zur Verfügung zu haben importieren wir die ``config.py`` in der ``__init__.py``::

 ...
 from zope.i18nmessageid import MessageFactory
 import config
 ...

Im Beispiel wollen wir für Gebrauchtwaren festhalten, wie es um die Funktionsfähigkeit bestellt ist. Für das Produkt definieren wir eine statische Liste von Tupeln, mit der die Werte "ja, nein, eingeschränkt" zur Wahl stehen. Die Angaben lauten beispielsweise wie folgt::

 ARTICLE_USABLE=DisplayList((
    ('yes', _(u'Yes')),
    ('no', _(u'No')),
    ('some', _(u'somewhat usable')),
    ))

Für die Internationalisierung des Produkts inklusive des Vokabulars ist die MessageFactory zu importieren und jeder String mit ``_(u'')`` zu definieren. Siehe auch `Erstellen der Übersetzungsdateien`_.

Dieses Vokabular wird in der ``content/vsresale.py`` verwendet::

 ...
 TypeSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((
    atapi.StringField('usable',
        vocabulary=config.ARTICLE_USABLE,
        default='yes',
        widget=atapi.SelectionWidget(label=_(u"usable"),
                                  description=(u"is the article usable?"))
        ),

Es kann auch gegen eine Liste von ``(value, label)``-Tupeln validiert werden, wobei die Etiketten andere Angaben als die Werte des Vokabulars annehmen können. Archetypes transformiert diese Liste in ``DisplayList`` (s.a. ``Products.Archetypes.utils``).

Für dynamische Vokabularien kann für ``vocabulary`` die Methode eines Objekts, eines übergeordneten Objekts oder ein Skript in einem Skin-Layer angegeben werden. Beim Aufruf erwartet Archetypes eine einfache Werteliste, eine Liste von Tupeln oder eine ``DisplayList``. Hier ein Beispiel für eine solche Implementierung in ATTopic (``Products/ATContentTypes/content/topic.py``)::


 LinesField('customViewFields',
             required=False,
             mode="rw",
             default=('Title',),
             vocabulary='listMetaDataFields',
             enforceVocabulary=True,
             write_permission = ChangeTopics,
             widget=InAndOutWidget(
                     label=_(u'label_custom_view_fields', default=u'Table Columns'),
                     description=_(u'help_custom_view_fields',
                                   default=u"Select which fields to display when "
                                            "'Display as Table' is checked.")
                     ),
              ),
 ...
 security.declareProtected(View, 'listMetaDataFields')
 def listMetaDataFields(self, exclude=True):
     """Return a list of metadata fields from portal_catalog.
     """
     tool = getToolByName(self, TOOLNAME)
     return tool.getMetadataDisplay(exclude)

Die Methode gibt eine ``DisplayList`` mit Werten und Etiketten zurück.

Schlagworte in einen eigenen Index schreiben
============================================

Will man die für einen bestimmten Content-Typen vergebenen Schlagworte für alle gleichartigen Objekte desselben Typs verfügbar machen, stellt man den Vokabelbestand über eine Abfrage des ``portal_catalog`` bereit. Als Auswahlfeld verwenden wir das AddRemoveWidget, das über die ``buildout.cfg`` hinzugefügt wird::

 eggs =
     ...
     Products.AddRemoveWidget

Diese Liste wird dann in der ``content/vsresale.py`` zusammengestellt::

 atapi.LinesField('category',
        required=True,
        searchable=True,
        vocabulary='getTagsVocab',
        enforceVocabulary=False,
        accessor="Category"
        widget=atapi.AddRemoveWidget(label=_(u"tags"),
                                description=_(u"")),
        ),

Das Vokabular entnehmen wir über über die Methode ``getTagsVocab`` aus dem Bestand, der in den vorhandenen Objekten desselben Content-Typs angelegt wurde. Die Methoden werden wie folgt definiert::

 class VsResale(base.ATCTContent):
 ...
   def getTagsVocab(self):
        """
        Get the available tags as a DisplayList.
        """
        tags = self.getTagsInUse()
        vocab = atapi.DisplayList()
        for t in tags:
            vocab.add(t, t)
        return vocab

   def getTagsInUse(self):
        """
        Get a list of the resale tags in use in this contenttype.
        """
        catalog = getToolByName(self, 'portal_catalog')
        issues = catalog.searchResults(portal_type = 'Resale Goods Type',)
        tags = {}
        result = set()
        for i in issues:
            issue = i.getObject()
            result.update(issue.Category())
        return sorted(result)

Darüberhinaus bringt Plone 3 in ``plone.app.vocabularies`` bereits eine Reihe von häufig verwendeten Vokabularien mit.

.. Eine komfortablere Methode, Vokabular zu verwalten, bietet der ATVocabularyManager. Damit lassen sich Vokabularien über Plone anlegen und verwalten. Man stellt den Vokabelbestand über eine Abfrage der ``portal_vocabularies`` bereit. Als Auswahlfeld verwenden wir das AddRemoveWidget, das so über eine Plone-Oberfläche bestückt werden kann. Es ist als egg in der ``buildout.cfg`` hinzuzufügen::

..  eggs =
..    ...
..    Products.AddRemoveWidget
..    Products.ATVocabularyManager

.. In ``content/resale.py`` werden Klasse und Methode definiert, z.B. so::

.. class VsResale(base.ATCTContent):
.. ...
..   def getTagsVocab(self):
..   """ return tags vocabulary (managed through ATVocabularyManager)"""
..   vocab_tool = getToolByName(self, 'portal_vocabularies')
..   vocab = vocab_tool[self.resaletypes_vocabulary].getVocabularyDict()
..   lst = list()
..   for k,v in vocab.items():
..     lst.append((k, v))
..   return DisplayList(lst)

.. Die Methode liefert den Inhalt des AddRemoveWidgets::

..    atapi.LinesField('category',
..        required=False,
..        searchable=True,
..        vocabulary='getTagsVocabulary',
..        enforceVocabulary=False,
..        accessor="Category",
..        widget=AddRemoveWidget(label=_(u"tags"),
..                                description=_(u""))
..        ),

.. Selektive Berechtigungen für die Vergabe von Schlagworten lassen sich über das ``AddRemoveWidget`` verwalten. Hierfür verwendet man den Aufruf ``role_based_add`` und setzt den Paramerterwert auf ``True``, und legt über das ``portal_properties``-Tool eine Liste der Rollen fest, die erweiterte Berechtigung zum Hinzufügen von Vokabular haben. ::

..        widget=AddRemoveWidget(...
..                               role_based_add=True,
..                               add_role_property='addRolesForAddRemoveWidget')

.. Programmatisch legt man neue ``portal_properties`` an, in man ``profiles/default/propertiestool.xml`` wie folgt definiert. Wir legen eine neue Property ``addRolesForAddRemoveWidget`` an und vergeben den Rollen ``Manager`` und ``Reviewer`` die Berechtigung, neues Vokabular hinzuzufügen::

.. <?xml version="1.0"?>
.. <object name="portal_properties" meta_type="Plone Properties Tool">
..  <object name="site_properties" meta_type="Plone Property Sheet">
..   <!-- we add this lines field as needed by AddRemoveWidget.py -->
..   <property name="addRolesForAddRemoveWidget" type="lines">
..    <element value="Manager"/>
..    <element value="Reviewer"/>
..   </property>
..  </object>
.. </object>




.. Referenzfelder
.. ==============

Feld- und Objektvalidierung
===========================

Wenn im Editierformular eines Archtetypes-Artikeltyps auf *Speichern* geklickt wird, wird die Methode ``validate()`` von ``BaseObject`` aufgerufen. Alle Felder bieten einfache Validierungen wie diejenigen, ob auch ein Eintrag in einem als *erforderlich* deklarierten Feld gemacht wurde oder ein Nummernfeld keine Buchstaben enthält.
Es lassen sich jedoch auch eigene Validatoren für spezifische Felder schreiben, z.B.::

 atapi.TextField('text',
     ....
     validators=("isTidyHtmlWithCleanup",),
     ....
     ),

Dies weist einem Feld einen oder mehrere Validatoren zu, die in der *validator registry* registriert sein müssen.

Wie solche Validatoren registriert werden können, sehen Sie in ``Products.ATContentTypes.lib.validators``::

 validatorList.append(TidyHtmlWithCleanupValidator('isTidyHtmlWithCleanup', title='', description=''))

Dies ist jedoch nur notwendig, wenn der Validator für mehrere Felder und Artikeltypen Verwendung finden soll. Wird nur ein feldspezifischer Validator benötigt, so lässt sich dieser einfach in einer Methode ``validate_fieldname()`` der Klasse dieses Artikeltyps hinzufügen wobei ``fieldname`` der Name des zu überprüfenden Feldes ist::

 def validate_text (self, value):
     if "maybe" in value:
         return _(u"You shouldn’t be so vague.")
     return None

Klassengenerator
================

::

 atapi.registerType(Registrant, PROJECTNAME)

registriert den Artikeltyp *Registrant*, indem der Klassengenerator aufgerufen wird und jedem Feld der  *Registrant*-Klasse drei Methoden hinzufügt:

Accessor
 *getter*-Methode
Edit accessor
 falls der Accessor eine Transformation vornimmt und das Editierfeld anders eingelesen werden muss.
Mutator
 *setter*-Methode

So werden z.B. für das Feld ``email`` die Methoden ``getEmail()``, ``getRawEmail()`` und ``setEmail()`` als Accessor, edit accessor und mutator erzeugt.

Manchmal kann es auch notwendig werden, eigene getter- und setter-Methoden zu schreiben. Entspricht der Name der Methode derjenigen eines Accessors oder Mutators, nimmt Archetypes an, dass diese Methode anstatt einer generierten verwendet werden soll.

Der Name einer solchen Methode kann in den Feldeigenschaften angegeben werden, z.B. in ``Products/Archetypes/ExtensibleMetadata.py``::

 BooleanField(
     'allowDiscussion',
     accessor="isDiscussable",
     mutator="allowDiscussion",
     edit_accessor="editIsDiscussable",
     ...
 ),

.. _`Erstellen der Übersetzungsdateien`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/internationalisierung/erstellen-der-ubersetzungsdateien.html

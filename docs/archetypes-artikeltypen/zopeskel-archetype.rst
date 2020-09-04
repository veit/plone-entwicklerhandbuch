===========================
ZopeSkel-archetype-Template
===========================

Mit dem archetype-Template und dessen local commands lassen sich Artikeltypen noch einfacher erstellen.

Statt des Templates ``plone`` kann auch das Template ``archetype`` mit *local commands* verwendet werden um neue Artikeltypen zu erstellen. Hierzu geben wir zunächst folgendes an::

 paster create -t archetype vs.registration

Anschließend wechseln wir in das gerade eben erstelle Verzeichnis und lassen uns die hier verfügbaren *local commands* anzeigen::

 $ cd vs.registration
 $ paster addcontent --list
 Available templates:
    atschema:     A handy AT schema builder
    contenttype:  A content type skeleton
    form:         A form skeleton
    formfield:    Schema field for a form
    i18nlocale:   An i18n locale directory structure
    portlet:      A Plone 3 portlet
    view:         A browser view skeleton
    zcmlmeta:     A ZCML meta directive skeleton

Weitere *local commands* sind für das ``plone_pas``-Projekt verfügbar. Eine Übersicht über alle verfügbaren **local commands** erhält man mit::

 $ paster addcontent -a
   N anonymous_user_factory_plugin:  A Plone PAS AnonymousUserFactory Plugin
     atschema:                       A handy AT schema builder
   N authentication_plugin:          A Plone PAS Authentication Plugin
   N challenge_plugin:               A Plone PAS Challenge Plugin
     contenttype:                    A content type skeleton
   N credentials_reset_plugin:       A Plone PAS CredentialsReset Plugin
   N extraction_plugin:              A Plone PAS Extraction Plugin
     form:                           A form skeleton
     formfield:                      Schema field for a form
   N group_enumeration_plugin:       A Plone PAS GroupEnumeration Plugin
   N groups_plugin:                  A Plone PAS Groups Plugin
     i18nlocale:                     An i18n locale directory structure
     portlet:                        A Plone 3 portlet
   N properties_plugin:              A Plone PAS Properties Plugin
   N role_assigner_plugin:           A Plone PAS RoleAssigner Plugin
   N role_enumeration_plugin:        A Plone PAS RoleEnumeration Plugin
   N roles_plugin:                   A Plone PAS Roles Plugin
   N update_plugin:                  A Plone PAS Update Plugin
   N user_adder_plugin:              A Plone PAS UserAdder Plugin
   N user_enumeration_plugin:        A Plone PAS UserEnumeration Plugin
   N user_factory_plugin:            A Plone PAS UserFactory Plugin
   N validation_plugin:              A Plone PAS Validation Plugin
     view:                           A browser view skeleton
     zcmlmeta:                       A ZCML meta directive skeleton

Die beim Anlegen des Projekts gemachten Angaben finden mit Erläuterungen in der ``setup.py``.

Mit den Angaben in der Datei ``vs.registration/vs/registration/configure.zcml`` wird das Produkt für das Generic Setup-Tool registriert, wenn hierfür der Default-Wert auf "True" belassen wurde. Titel und Beschreibungstext werden für die Anzeige im Generic Setup-Tool verwendet::

 <configure
     ...
     i18n_domain="vs.registration">

    <genericsetup:registerProfile
        name="default"
        title="Registration Content-types"
        directory="profiles/default"
        description="Short description of registration content-types"
        provides="Products.GenericSetup.interfaces.EXTENSION"
        />

Content-Types Registration und Registrant
=========================================

Um einen Content-Type zu unserem Projekt hinzuzufügen kann folgendes ausgeführt werden::

 $ cd vs.registration
 $ paster addcontent contenttype
 Enter contenttype_name (Content type name ) ['Example Type']: Registration
 Enter contenttype_description (Content type description ) ['Description of the Example Type']: Container for registrants
 Enter folderish (True/False: Content type is Folderish ) [False]: True
 Enter global_allow (True/False: Globally addable ) [True]:
 Enter allow_discussion (True/False: Allow discussion ) [False]:
  Inserting from README.txt_insert into /home/veit/Projects/IDG/idg_buildout/src/vs.registration/vs/registration/README.txt
  Inserting from config.py_insert into /home/veit/Projects/IDG/idg_buildout/src/vs.registration/vs/registration/config.py
  Recursing into content
    Copying +content_class_filename+.py_tmpl to /home/veit/Projects/IDG/idg_buildout/src/vs.registration/vs/registration/content/registration.py
    Inserting from configure.zcml_insert into /home/veit/Projects/IDG/idg_buildout/src/vs.registration/vs/registration/content/configure.zcml
  Recursing into interfaces
    Copying +content_class_filename+.py_tmpl to /home/veit/Projects/IDG/idg_buildout/src/vs.registration/vs/registration/interfaces/registration.py
    Inserting from __init__.py_insert into /home/veit/Projects/IDG/idg_buildout/src/vs.registration/vs/registration/interfaces/__init__.py
  Recursing into profiles
    Recursing into default
      Inserting from factorytool.xml_insert into /home/veit/Projects/IDG/idg_buildout/src/vs.registration/vs/registration/profiles/default/factorytool.xml
      Copying rolemap.xml_insert to /home/veit/Projects/IDG/idg_buildout/src/vs.registration/vs/registration/profiles/default/rolemap.xml
      Recursing into types
        Creating /home/veit/Projects/IDG/idg_buildout/src/vs.registration/vs/registration/profiles/default/types/
        Copying +types_xml_filename+.xml_tmpl to /home/veit/Projects/IDG/idg_buildout/src/vs.registration/vs/registration/profiles/default/types/Registration.xml
      Inserting from types.xml_insert into /home/veit/Projects/IDG/idg_buildout/src/vs.registration/vs/registration/profiles/default/types.xml

i18n-Layer
==========

Damit der Content-Type vollständig internationalisierbar angelegt wird fügen wir noch die Angaben für die Internationalisierung ``i18nlocale`` hinzu::

 $ cd vs.registration
 $ paster addcontent i18nlocale
 Enter language_code (The iso-code of the language) ['']: de
  Inserting from configure.zcml_insert into /home/veit/Projects/IDG/idg_buildout/src/vs.registration/vs/registration/configure.zcml
  Recursing into locales
    Creating /home/veit/Projects/IDG/idg_buildout/src/vs.registration/vs/registration/locales/
    Recursing into +language_iso_code+
      Creating /home/veit/Projects/IDG/idg_buildout/src/vs.registration/vs/registration/locales/de/
      Recursing into LC_MESSAGES
        Creating /home/veit/Projects/IDG/idg_buildout/src/vs.registration/vs/registration/locales/de/LC_MESSAGES/
        Copying README.txt to /home/veit/Projects/IDG/idg_buildout/src/vs.registration/vs/registration/locales/de/LC_MESSAGES/README.txt

Jetzt sollte die Instanz ohne Fehlermeldung gestartet werden können. Unser Content-Type ist beim Hinzufügen einer Plone-Site als "Extension Profile" mit dem vergebenen Titel "Registration Content-types" auswählbar.

Die Datei ``vs/registration/profiles/default/types.xml`` registriert neue Content-Typen am Types-Tool::

  <object name="portal_types" meta_type="Plone Types Tool">
    <object name="Registration"
            meta_type="Factory-based Type Information with dynamic views"/>
    <object name="Registrant"
            meta_type="Factory-based Type Information with dynamic views"/>
  </object>

In der neu erstellten Plone-Site lässt sich der Content-Typ global hinzufügen, soweit bei der Erstellung nichts anderes angegeben wurde.

Verwenden der Portal Factory
============================

Bei Content-Typen, die auf Archetypes oder CMF beruhen, wird das Objekt bereits angelegt bevor das zugehörige Formular ausgefüllt wird. Mit den Angaben in ``vs/registration/profiles/default/factorytool.xml`` wird das Produkt am Factory-Tool angemeldet. Dieses verwaltet neue Objekte nur solange, bis das Formular tatsächlich gespeichert wird und verschiebt das temporäre Objekt beim Speichern an die vorgesehene Stelle. Damit der Mechanismus für unseren Objekte greift sind diese Angaben hinzuzufügen::

   <factorytypes>
    ...
        <type portal_type="Registration"/>
        <type portal_type="Registrant"/>
  </factorytypes>

Struktur der Objekte
====================

Bisher stehen beiden Content-Typen lediglich die Strukturen zur Verfügung, die dem Default von ``ATContentType`` entsprechen, nämlich die Felder ``title`` und ``description``. Wir ergänzen im folgenden die übernommenen Felder um spezifische Informationen.

Um z.B. die Registrierung mit einen formatierbaren Textfeld zu versehen fügen wir eine entsprechende Definition in ``content/registration.py`` hinzu. Zunächst wird das Schema von einem Basistypen, in diesem Fall ATFolderTypeSchema, kopiert und anschließend das eigene Schema angehängt::

  RegistrationSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    atapi.TextField('text',
        required=True,
        searchable=True,
        storage=atapi.AnnotationStorage(),
        validators=('isTidyHtmlWithCleanup',),
        default_output_type='text/x-html-safe',
        widget=atapi.RichWidget(label=_(u"Body Text"),
                                description=_(u"Text for front page of registration"),
                                rows=25,
                                allow_file_upload=False),
        ),
    ))

  RegistrationSchema['title'].storage = atapi.AnnotationStorage()
  RegistrationSchema['description'].storage = atapi.AnnotationStorage()
  RegistrationSchema['text'].storage = atapi.AnnotationStorage()

  schemata.finalizeATCTSchema(
    RegistrationSchema,
    folderish=True,
    moveDiscussion=False
  )
  ...
  title = atapi.ATFieldProperty('title')
  description = atapi.ATFieldProperty('description')
  text = atapi.ATFieldProperty('text')

Das zusätzliche Feld erhält erhält den Status Pflichtfeld, wird durchsuchbar und wird auf valides  HTML validiert. Der Text kann formatiert werden. Alle Felder verwenden explizit den Speichertyp ``AnnotationStorage``.

Um z.B. das Teilnehmer-Objekt um ein Feld für eine Email-Adresse zu ergänzen fügen wir die Angaben für das Feld in ``content/registrant.py`` hinzu. Zunächst wird wieder das Schema von einem Basistypen, in diesem Fall ATContentTypeSchema, kopiert und anschließend das eigene Schema angehängt::

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

 schemata.finalizeATCTSchema(RegistrantSchema, moveDiscussion=False)

 class Registrant(base.ATCTContent):
     """Describe a registrant.
     """
     implements(IRegistrant)

     meta_type = "Registrant"
     _at_rename_after_creation = True
     schema = RegistrantSchema

     name = atapi.ATFieldProperty('title')
     address = atapi.ATFieldProperty('description')
     email = atapi.ATFieldProperty('email')

 atapi.registerType(Registrant, PROJECTNAME)

Dieses Schema implementiert ein Interface, ``IRegistrant``. Die Definition steht im Unterordner ``interfaces``. Die Klasse ``Registrant`` erweitert ``base.ATCTContent``. Die Angabe ``at_rename_after_creation`` benennt Objekte in die normalisierte Version ihres Titels um.

``meta_type`` setzt den eindeutigen Namen des Artikeltyps. Alternativ kann dieser auch mit ``portal_type`` gesetzt werden. Zur Unterscheidung siehe unten.

Um nun z.B. ein Portlet unserem Projekt hinzuzufügen, kann einfach folgendes angegeben werden::

 $ paster addcontent portlet
 Enter portlet_name (Portlet name (human readable)) ['Example portlet']: My portlet
 Enter portlet_type_name (Portlet type name (should not contain spaces)) ['ExamplePortlet']: registrants
 Enter description (Portlet description) ['']: My portlet
   Recursing into portlets
     Copying +portlet_filename+.pt_tmpl to /home/veit/vs.mytype/vs/mytype/portlets/registrants.pt
     Copying +portlet_filename+.py_tmpl to /home/veit/vs.mytype/vs/mytype/portlets/registrants.py
 File '__init__.py' already exists: skipped
     Inserting from configure.zcml_insert into /home/veit/vs.mytype/vs/mytype/portlets/configure.zcml
   Recursing into profiles
     Recursing into default
       Inserting from portlets.xml_insert into /home/veit/vs.mytype/vs/mytype/profiles/default/portlets.xml
   Recursing into tests
 File '__init__.py' already exists: skipped
     Copying base_+portlet_filename+.py_tmpl to /home/veit/vs.mytype/vs/mytype/tests/base_registrants.py
     Copying test_+portlet_filename+.py_tmpl to /home/veit/vs.mytype/vs/mytype/tests/test_registrants.py

Neben den neu erstellten Dateien ``portlets/registrants.py`` und ``portlets/registrants.pt`` wurden auch die Dateien ``portlets/configure.zcml`` und  ``profiles/default/portlets.xml`` aktualisiert.

Gestaltung
==========

Um z.B. den Ordnern für Registrierungen ein eigenes Icon zu geben kann man einfach diese Angaben in ``browser/configure.zcml`` hinzufügen::

  <browser:resource
     name="registration_icon.gif"
     image="registration_icon.gif"
     />

Die zugehörige Klasse ``class RegistrantView(BrowserView)`` wird in ``browser/registrant.py`` und ``browser/registration.py`` definiert.

Mit Hilfe des View-Templates lässt sich über Paster auf einfache Art ein neuer Browser View hinzufügen::

  paster addcontent view

Sofern noch nicht vorhanden werden die Dateien  ``browser/registrantview.py`` und ``browser/registrationview.py`` sowie ``browser/registrantview.pt`` und  ``browser/registrationview.pt`` erstellt. Die Templates können angepasst werden.

Damit das Icon vom Factory Tool verwendet wird ändert man das default-Icon in ``profiles/default/types/Registration.xml``::

  <object name="Registration"
    ...
    <property name="content_icon">++resource++registration_icon.gif</property>

Verwendung einschränken
=======================

Der Registrierungs-Ordner ist als Containerobjekt für Teilnehmer vorgesehen. Außerhalb dieser Ordner sollen sich auf der Site keine Teilnehmer hinfügen lassen. Diese Einschränkung wird in der ``profiles/default/types/Registration.xml`` getroffen, und die Eigenschaft ``filter_content_types`` auf ``True`` gesetzt::

  <object name="Registration"
    ...
    <property name="filter_content_types">True</property>
    <property name="allowed_content_types">
        <element value="Registrant" />
    </property>

Damit die Einschränkung übernommen wird und nur Teilnehmer einem Ordner "Registration" zugeordnet werden können muss bei einer bestehenden Site das Generic Setup-Profil aktualisiert werden. Gehen Sie hierzu in das ZMI der Site und dort ins Types-Tool, Reiter "Import", und wählen sie das Profil "vs.registration", und setzen das Häkchen bei "Types Tool - Import types tool's type information objects". Vor dem tatsächlich Import sollte noch "include dependencies" abgewählt werden. Nach dem Import sollten sich in Registration-Ordnern nur noch Teilnehmer hinzufügen lassen.

Rollen und Berechtigungen
=========================

Werden keine Änderungen an den voreingestellten Berechtigungen vorgenommen dürfen Manager und Redakteure Registrierungs-Container und Teilnehmer anlegen. Wir ändern die ``profiles/default/rolemap.xml``, so dass nur Manager neue Container anlegen können::

  <?xml version="1.0"?>
  <rolemap>
     <permissions>
         <permission name="vs.registration: Add Registration" acquire="False">
             <role name="Manager" />
         </permission>
         <permission name="vs.registration: Add Registrant" acquire="False">
             <role name="Manager" />
             <role name="Owner" />
             <role name="Contributor" />
         </permission>
     </permissions>
  </rolemap>

Um das Hinzufügen von Content über den ZMI-Reiter ``security`` festlegen zu können wird ``content/configure.zcml`` mit folgenden Angaben versehen::

  <configure
        ...
        i18n_domain="vs.registration">

        <class class=".registration.Registration">
        <require
            permission="zope2.View"
            interface="..interfaces.IRegistration"
            />
    </class>

    <class class=".registrant.Registrant">
        <require
            permission="zope2.View"
            interface="..interfaces.IRegistrant"
            />
    </class>
  ...
  </configure>

Nähere Erläuterungen der Berechtigungen finden Sie im Abschnitt `Sicherheit und Arbeitsabläufe`_.

In der Datei ``profiles/default/Registration.xml`` z.B. werden Eigenschaften des Objekts definiert, die sich auf die Sichtbarkeit beziehen. Die Aufrufe für Ansehen und Bearbeiten erfordern unterschiedliche Rechte::

  <action title="View"
            action_id="view"
            category="object"
            condition_expr=""
            url_expr="string:${folder_url}/"
            visible="True">
        <permission value="View"/>
    </action>
    <action title="Edit"
            action_id="edit"
            category="object"
            condition_expr=""
            url_expr="string:${object_url}/edit"
            visible="True">
        <permission value="Modify portal content"/>
    </action>



Dateisystemansicht des Produkts
===============================

Das fertige Produkt sollte im Dateisystem in etwa so aussehen::

  |-- README.txt
  |-- __init__.py
  |-- config.py
  |-- configure.zcml
  |-- browser
  |   |-- __init__.py
  |   |-- configure.zcml
  |   |-- registrant_icon.gif
  |   |-- registrantview.pt
  |   |-- registrantview.py
  |   |-- registration_icon.gif
  |   |-- registrationview.pt
  |   |-- registrationview.py
  |-- content
  |   |-- __init__.py
  |   |-- configure.zcml
  |   |-- registrant.py
  |   |-- registration.py
  |-- interfaces
  |   |-- __init__.py
  |   |-- registrant.py
  |   |-- registration.py
  |-- locales
  |   `-- de
  |       `-- LC_MESSAGES
  |-- portlets
  |   |-- __init__.py
  |   `-- configure.zcml
  |-- profiles
  |     `-- default
  |         |-- factorytool.xml
  |         |-- metadata.xml
  |         |-- portlets.xml
  |         |-- rolemap.xml
  |         |-- types
  |         |-- types.xml
  |         |-- workflows
  |         `-- workflows.xml
  `-- tests
      |-- __init__.py
      |-- base.py
      `-- test_doctest.py

Die Dateien und Ordner werden im folgenden kurz erläutert, die Angaben sind relativ zu ``/src/vs.registration/vs/registration``, außer wo abweichend angegeben::

- ``/__init__.py``: Das Initialisierungsmodul.
- ``/configure.zcml``: beschreibt Konfigurationsangaben, meldet das Produkt am Generic Setup-Tool an und enthält weitere Verweise auf Sub-packages (=Unterordner), die ihrerseits Konfigurationsangaben enthalten. Hier werden auch die Übersetzungen des i18n-Layers registriert.
- ``/config.py``: Fügt den Content-Typen die Berechtigungen für das Hinzufügen von Registrierungen und Teilnehmern zu hinzu. Die Berechtigungen werden durch ``__init__.py`` aufgerufen.
- ``/browser/``: kann zusätzliche Templates für die Gestaltung enthalten.
- ``/browser/configure.zcml`` registriert die Komponenten und legt fest, welche Pagetemplates für welchen Content-Typ verwendet werden, und definiert die angepassten Icons.
- ``/browser/registrantview.py``, ``browser/registrationview.py`` weisen dem View spezifische Templates zu. Die Angaben werden durch FTI (factory type information) in ``profiles/default/types/*.xml`` aufgerufen.
- ``browser/registrantview.pt``, ``browser/registrationview.pt`` sind Page-Templates in TAL/METAL.
- ``content``: enthält die Implementierungen der Content-types.
- ``content/configure.zcml`` legt die Berechtigungen für die Content-types fest, die mindestens erfüllt sein müssen.
- ``content/registrant.py``, ``content/registration.py`` enthalten die eigentliche Definition der Datenstrukturen, und melden die Content-typen bei Archetypes an
- ``interfaces/``: Ordner enthält Beschreibungen der Interfaces für unsere definierten Klassen, ``IRegistrant``und ``IRegistration``.
- ``interfaces/__init__.py`` importiert die Interface-Definitionen aus den Content-Types. Datei wird vom Template ``contenttype`` angelegt.
- ``interfaces/registrant.py``, ``interfaces/registration.py`` legt Pflichtfelder und die Benennungen der Felder fest. In ``registration.py`` contains('vs.registration.interfaces.IRegistrant',)
- ``locales/de/LC_MESSAGES/`` kann einmal die sprachspezifischen Übersetzungsdateien enthalten, in der Form ``vsregistration-de.po``. Genauere Informationen erhält man in `i18n-locales und Plone 3.0`_
- ``profiles/default``: die Dateien definieren das Extension Profile gegenüber Generic Setup; dieser Pfad wird in ``/configure.zcml`` festgelegt.
- ``profiles/default/factorytool.xml`` macht die Content-typen dem Factory-Tool bekannt. Datei wird vom Template ``contenttype`` angelegt.
- ``profiles/default/metadata.xml`` enthält eine Versionsnummer. Datei wird vom Template ``contenttype`` angelegt/modifiziert.
- ``profiles/default/portlets.xml`` sofern Portlets mit ``paster addcontent portlet`` erzeugt wurden.
- ``profiles/default/rolemap.xml`` Datei wird vom Template ``contenttype`` angelegt.
- ``profiles/default/types.xml`` Datei wird vom Template ``contenttype`` angelegt.
- ``profiles/default/workflows.xml`` Datei wird vom Template ``contenttype`` angelegt.
- ``profiles/default/types``
- ``profiles/default/types``
- ``tests/``: Unit-Tests für das Produkt.

Konventionen
============

The types are configured with the corresponding files in ``types/*.xml``. Note that spaces are allowed in type names, but the corresponding XML file uses an underscore instead.

Die ``types/*.xml``-Dateien werden mit Unterstrichen benannt werden

The "Factory-based Type Information with dynamic views" refers to an FTI from Products.CMFDynamicViewFTI, which supports Plone's "display" menu.

Metadaten zu vs.registration
============================

Die Kontaktdaten des Autors (Name, Emailadresse, Homepage) sowie die Adresse des SVN-Repository werden mit einigen kommentierenden Angaben in ``vs.registration.egg-info/PKG-INFO`` geschrieben. Vor der Weitergabe des Produkts sollten einige Angaben in dieser Datei sowie in ``CHANGES.txt`` präzisiert werden.

Zum Weiterlesen
===============

- `ZopeSkel Archetypes HOWTO`_

.. _`ZopeSkel Archetypes HOWTO`: http://lionfacelemonface.wordpress.com/zopeskel-archetypes-howto/

.. _`Sicherheit und Arbeitsabläufe`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/sicherheit-und-arbeitsablaufe

.. _`i18n-locales und Plone 3.0`: http://maurits.vanrees.org/weblog/archive/2007/09/i18n-locales-and-plone-3.0

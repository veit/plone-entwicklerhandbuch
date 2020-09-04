==============================
Installation und Registrierung
==============================

Nachdem die Artikeltypen und die zugehörigen Views erstellt sind, müssen diese Artikeltypen noch installiert werden. Dies geschieht mit einem Generic Setup Extension-Profil in ``vs/registration/profiles/default/types.xml``::

 <object name="portal_types" meta_type="Plone Types Tool">
     <object name="Registration"
             meta_type="Factory-based Type Information with dynamic views"/>
     <object name="Registrant"
             meta_type="Factory-based Type Information with dynamic views"/>
 </object>

Damit werden zwei verschiedene *factory-based type information* (FTI)-Objekte im ``portal_types``-Tool erstellt, wobei die *Dynamic Views* Editoren das Auswählen verschiedener Ansichten  im *Darstellung*-Menü von Plone erlauben.

Jede FTI ist detaillierter in der entsprechenden Datei in ``profiles/default/types/`` definiert. Dabei muss der Dateiname dem Namen des *portal type* entsprechen, wobei Leerzeichen als Unterstriche angegeben werden müssen. Schauen wir uns nun ``profiles/default/types/Registration.xml`` genauer an::

 <?xml version="1.0"?>
 <object name="Registration"
         meta_type="Factory-based Type Information with dynamic views"
         i18n:domain="vs.registration"
         xmlns:i18n="http://xml.zope.org/namespaces/i18n">
     <property name="title"
               i18n:translate="">Registration</property>
     <property name="description"
               i18n:translate="">A folder which can contain registrants.</property>
     <property name="content_icon">++resource++registration_icon.gif</property>

In diesen Zeilen wird dem Artikeltyp Name, Beschreibung und Icon zugewiesen, die Plone auch zur Darstellung nutzt.

::

     <property name="content_meta_type">Registration</property>
     <property name="product">vs.registration</property>
     <property name="factory">addRegistration</property>
     <property name="immediate_view">atct_edit</property>

Hier wird der Meta-Typ des Artikeltyps angegeben, der meist dem Namen des *portal type* entspricht. Anschließend wird die Methode angegeben, die das neue Artikelobjekt erstellt und initialisiert. ``immediate_view`` gibt die Ansicht, die unmittelbar nach dem Erstellen des Objekts gezeigt wird, an (auch wenn diese momentan nicht durch Plone unterstützt wird).

::

     <property name="global_allow">True</property>
     <property name="filter_content_types">True</property>
     <property name="allowed_content_types">
         <element value="Registrant" />
     </property>

Diese Eigenschaften bestimmen das Verhältnis von übergeordneten zu untergeordneten Objekten. ``Registration`` darf in allen Ordner-Objekten, für die ``filter_content_types`` auf ``False`` gesetzt wurde, hinzugefügt werden. Darüberhinaus darf in ``Registration`` mit ``filter_content_types`` und ``allowed_content_types`` nur der Artikeltyp ``Registrant`` hinzugefügt werden.

::

     <property name="allow_discussion">False</property>

Diese Eigenschaft bestimmt, ob für diesen Artikeltyp üblicherweise Diskussionen erlaubt sind oder nicht.

::

     <property name="default_view">view</property>
     <property name="view_methods">
         <element value="view"/>
         <element value="folder_summary_view"/>
         <element value="folder_tabular_view"/>
         <element value="folder_listing"/>
     </property>

Diese Eigenschaften geben die Standardansicht und die im *Darstellung*-Menü auswählbaren Ansichten (*dynamic views*) an.

::

     <alias from="(Default)" to="(dynamic view)"/>
     <alias from="edit" to="atct_edit"/>
     <alias from="sharing" to="@@sharing"/>
     <alias from="view" to="(selected layout)"/>

Üblicherweise nutzen die meisten Plone-Artikeltypen diese vier Aliase. Werden keine *dynamic views* FTIs verwendet, müssen die Namen der Views oder Templates  für die ``(Default)``- und ``view``-Aliase angegeben werden.

::

     <action title="View"
             action_id="view"
             category="object"
             condition_expr=""
             url_expr="string:${object_url}/"
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

Schließlich werden noch zwei typspezifische Aktionen definiert, die der Kategorie ``object`` zugeordnet werden und die oben definierten Aliase nutzen. Beachten Sie, dass bei *folderish*-Artikeltypen für die ``view``-Aktion  ``string:${folder_url}/``, hingegen für *non-folderish*-Artikeltypen ``string:${object_url}`` verwendet wird.

Initialisierung und Hinzufügen-Rechte
=====================================

Die oben bereits erwähnte Methode ``addRegistration`` zum Erstellen eines neuen Objekts des Artikeltyps *Registration* wird automatisch durch Archetypes erstellt, wenn das Produkt initiiert wird. Darüberhinaus werden in der Datei ``__init__.py`` auch die Rechte zum Hinzufügen der neuen Artikeltypen gesetzt.

::

 from vs.registration import config
 from Products.Archetypes import atapi
 from Products.CMFCore import utils

 def initialize(context):

Damit wird das Zope-2-Produkt initialisiert.

::

     from content import registration, registrant

     content_types, constructors, ftis = atapi.process_types(
         atapi.listTypes(config.PROJECTNAME),
         config.PROJECTNAME)

Die Artikeltypen aus ``content`` werden importiert und mit Archetypes ``registerType()``-Aufruf registriert.

::

     for atype, constructor in zip(content_types, constructors):
         utils.ContentInit("%s: %s" % (config.PROJECTNAME, atype.portal_type),
             content_types      = (atype,),
             permission         = config.ADD_PERMISSIONS[atype.portal_type],
             extra_constructors = (constructor,),
             ).initialize(context)

Nun werden die Artikeltypen mit den angegebenen Rechten zum Hinzufügen registriert. Diese Rechte sind in der ``config.py``-Datei angegeben::

 ADD_PERMISSIONS = {
     "Registration" : "vs: Add Registration",
     "Registrant"   : "vs: Add Registrant",
 }

Damit werden die zwei Artikeltypen entsprechenden Rechten zum Hinzufügen zugeordnet. Zudem sind diese Rechte auch noch definiert in ``content/configure.zcml``. Die Rechte erhalten mit ``vs`` ein Präfix, damit Sie im *Security*-Reiter des ZMI zusammen dargestellt werden.

Die den Hinzufügen-Rechten zugehörigen Rollen sind in ``profiles/default/rolemap.xml`` definiert::

 <rolemap>
     <permissions>
         <permission name="vs: Add Registration" acquire="False">
             <role name="Manager" />
         </permission>
         <permission name="vs: Add Registrant" acquire="False">
             <role name="Manager" />
             <role name="Owner" />
             <role name="Contributor" />
         </permission>
     </permissions>
 </rolemap>

Registrierung der Artikeltypen am *Factory Tool*
================================================

Für die meisten Artikeltypen empfiehlt sich die Registrierung am *Factory Tool*, um halbfertige Objekte beim Erstellen zu vermeiden. Die Registrierung geschieht auch hier mit einem Generic-Setup-Profil, nämlich ``factorytool.xml``::

 <object name="portal_factory"
         meta_type="Plone Factory Tool">
     <factorytypes>
         <type portal_type="Registration"/>
         <type portal_type="Registrant"/>
     </factorytypes>
 </object>

Registrierung der Artikeltypen am *CMFEditions Repository*
==========================================================

Die ATCT-Artikeltypen, mit denen Plone ausgeliefert wird, werden alle automatisch am *CMFEditions Repository* angemeldet, sodass für die entsprechenden Objekte auch die früheren Versionen angezeigt werden können. Um nun unsere beiden Artikeltypen am *CMFEditions Repository* zu registrieren, schreiben wir die Methode ``setupEditions``::

 from StringIO import StringIO
 from logging import getLogger

 from Products.CMFCore.utils import getToolByName
 from Products.Archetypes import atapi

 from config import PROJECTNAME

 class Generator:

     def setupEditions(self, p, out):


         content_types, constructors, ftis = atapi.process_types(
             atapi.listTypes(PROJECTNAME),
             PROJECTNAME)
         portal_repository = getToolByName(p, 'portal_repository')
         types = portal_repository.getVersionableContentTypes()

         for type in content_types:
             if type.portal_type not in types:
                 types.append("%s" %type.portal_type)

         portal_repository.setVersionableContentTypes(types)
         print >> out, " Editions enabled %s \n" % types

Diese Methode wird in der ``setuphandlers.py``-Datei erstellt und mit ``setupVarious`` aufgerufen::

 def setupVarious(context):

     if context.readDataFile('vs.registration_various.txt') is None:
         return
     # Add additional setup code here
     out = StringIO()
     site = context.getSite()
     gen = Generator()
     gen.setupEditions(site, out)
     logger = context.getLogger(PROJECTNAME)
     logger.info(out.getvalue())

Entsprechend erstellen wir die Konfigurationsdatei ``vs.registration/vs/registration/profiles/default/import_steps.xml`` mit folgendem Inhalt::

 <?xml version="1.0"?>
 <import-steps>
     <import-step id="idg.org.various"
                  version="20080617-01"
                  handler="vs.registration.setuphandlers.setupVarious"
                  title="vs.registration: miscellaneous import steps">
         <dependency step="typeinfo" />
             Various import steps that are not handled by GS import/export
             handlers.
     </import-step>
 </import-steps>

Und schließlich benötigen wir noch die Datei ``vs.registration/vs/registration/profiles/default/vs.registration_various.txt``, damit unsere ``setupVarious``-Methode auch ausgeführt wird.

Installation und Konfiguration im Policy-Produkt
================================================

Schließlich soll das ``vs.policy``-Produkt noch so geändert werden, dass es automatisch ``vs.registration`` bei der Installation in der Plone-Site mitinstalliert. Hierzu wird zunächst in ``src/vs.policy/vs/policy/configure.zcml`` folgende Zeile eingefügt::

 <include package="vs.registration" />

Für Plone 3.0 wird anschließend ``vs.registration`` auch noch in die benötigten Produkte in ``src/vs.policy/vs/policy/Extensions/Install.py`` eingetragen::

 PRODUCT_DEPENDENCIES = ('vs.theme',
                         'vs.registration')

Für Plone 3.1 wird ``src/vs.policy/vs/policy/profiles/default/metadata.xml`` um folgende Zeile ergänzt::

 <dependency>profile-vs.registration:default</dependency>

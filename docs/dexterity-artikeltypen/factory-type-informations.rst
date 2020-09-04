=========================
Factory Type Informations
=========================

Um die *Factory Type Informations* hinzuzufügen, erstellen wir in ``profiles/default`` das Profil ``types.xml``::

 <?xml version="1.0"?>
 <object name="portal_types">
  <object name="vs.registration.registration" meta_type="Dexterity FTI" />
  <object name="vs.registration.attendee" meta_type="Dexterity FTI" />
 </object>

- Um Konflikte zu vermeiden, wird der Paketname vorangestellt.
- Als ``meta_type`` muss ``Dexterity FTI`` verwendet werden.

Anschließend wird der Ordner ``profiles/default/types`` erstellt, in dem wir die Profile unserer beiden Artikeltypen erstellen, zunächst vs.reigistration.attendee.xml::

 <?xml version="1.0"?>
 <object name="vs.registrtion.attendee" meta_type="Dexterity FTI"
    i18n:domain="vs.registration" xmlns:i18n="http://xml.zope.org/namespaces/i18n">

  <!-- Basic metadata -->
  <property name="title" i18n:translate="">Attendee</property>
  <property name="description" i18n:translate="">An attendee</property>
  <property name="content_icon">user.gif</property>
  <property name="allow_discussion">True</property>
  <property name="global_allow">False</property>
  <property name="filter_content_types">False</property>
  <property name="allowed_content_types" />

  <!-- schema interface -->
  <property name="schema">vs.registration.attendee.IAttendee</property>

  <!-- class used for content items -->
  <property name="klass">plone.dexterity.content.Item</property>

  <!-- add permission -->
  <property name="add_permission">cmf.AddPortalContent</property>

  <!-- enabled behaviors -->
  <property name="behaviors">
      <element value="plone.app.content.interfaces.INameFromTitle" />
 </property>

  <!-- View information -->
  <property name="default_view">view</property>
  <property name="default_view_fallback">False</property>
  <property name="view_methods">
   <element value="view"/>
  </property>

  <!-- Method aliases -->
  <alias from="(Default)" to="(dynamic view)"/>
  <alias from="edit" to="@@edit"/>
  <alias from="sharing" to="@@sharing"/>
  <alias from="view" to="(selected layout)"/>

  <!-- Actions -->
  <action title="View" action_id="view" category="object" condition_expr=""
     url_expr="string:${object_url}" visible="True">
   <permission value="View"/>
  </action>
  <action title="Edit" action_id="edit" category="object" condition_expr=""
     url_expr="string:${object_url}/edit" visible="True">
   <permission value="Modify portal content"/>
  </action>
 </object>

Anschließend erstellen wir noch ``registration.xml``::

 <?xml version="1.0"?>
 <object name="vs.registration.registration"  meta_type="Dexterity FTI"
    i18n:domain="vs.registration" xmlns:i18n="http://xml.zope.org/namespaces/i18n">

  <!-- Basic metadata -->
  <property name="title" i18n:translate="">Registration</property>
  <property name="description" i18n:translate="">A folderish content type for attendees</property>
  <property name="content_icon">folder_icon.gif</property>
  <property name="allow_discussion">False</property>
  <property name="global_allow">True</property>
  <property name="filter_content_types">True</property>
  <property name="allowed_content_types">
      <element value="vs.registration.attendee" />
  </property>

  <!-- schema interface -->
  <property name="schema">vs.registration.registration.IRegistration</property>

  <!-- class used for content items -->
  <property name="klass">plone.dexterity.content.Container</property>

  <!-- add permission -->
  <property name="add_permission">cmf.AddPortalContent</property>

  <!-- enabled behaviors -->
  <property name="behaviors">
      <element value="plone.app.content.interfaces.INameFromTitle" />
  </property>

  <!-- View information -->
  <property name="default_view">view</property>
  <property name="default_view_fallback">False</property>
  <property name="view_methods">
   <element value="view"/>
  </property>

  <!-- Method aliases -->
  <alias from="(Default)" to="(dynamic view)"/>
  <alias from="edit" to="@@edit"/>
  <alias from="sharing" to="@@sharing"/>
  <alias from="view" to="(selected layout)"/>

  <!-- Actions -->
  <action title="View" action_id="view" category="object" condition_expr=""
     url_expr="string:${object_url}" visible="True">
   <permission value="View"/>
  </action>
  <action title="Edit" action_id="edit" category="object" condition_expr=""
     url_expr="string:${object_url}/edit" visible="True">
   <permission value="Modify portal content"/>
  </action>
 </object>

Schließlich können Sie Ihre Instanz starten mit::

 $ ./bin/instance fg

Beim Erstellen einer neuen Plone-Site wählen Sie das Profil ``vs.registration``. Und nachdem die Site erstellt wurde, sollten Sie *Registration* im hinzufügen-Menü finden. Schließlich sollten Sie in dem Artikel vom Typ *Registration* einen *Attendee* hinzufügen können.

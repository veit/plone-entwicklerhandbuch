=====
Tipps
=====

Tipps zu Migrationen und zukunftsfähigeren Produkten.

- Starten Sie Ihre Zope-Instanz im Debug-Modus (``ZOPE_INSTANCE/bin/zopectl fg``) und nutzen anschließend Ihr Produkt. Überprüfen Sie, ob auf der Konsole *deprecation warnings* ausgegeben werden.
- Entfernen Sie den ``plone_deprecated``-Skin-Layer und überprüfen, ob Ihre Anwendung anschließend noch problemlos funktioniert.
- Auf dem QuickInstaller basierende Installationen sollten stattdessen GenericSetup-Profile verwenden.

  - Ab CMF 2.1.0 steht ``addWorkflowFactory`` nicht mehr zur Verfügung. Workflows können von da an nur noch mit dem GenericSetup-Tool erstellt werden. Zur Migration installieren Sie einfach Ihr Produkt in einer Plone2.5-Site und exportieren den Workflow anschließend mit dem GenericSetup-Tool. Bevor Sie schließlich die alte Python-basierte Workflow-Definition aus dem *Extensions*-Ordner löschen, achten Sie darauf, dass ggf. die *workflow scripts* erhalten bleiben.

..  - Fügen Sie eine ``configure.zcml``-Datei im Wurzelverzeichnis Ihres Produkts hinzu, das das Standardprofil registriert::

..     <configure
           xmlns="http://namespaces.zope.org/zope"
           xmlns:gs="http://namespaces.zope.org/genericsetup"
           xmlns:five="http://namespaces.zope.org/five"
           i18n_domain="plone">

           <!-- Register the GenericSetup extension profile so that we can
                 install the product
             -->
           <gs:registerProfile
                 name="default"
                 title="PloneProductFramework"
                 directory="profiles/default"
                 description="A framework for developping plone products"
                 provides="Products.GenericSetup.interfaces.EXTENSION"
                 />
       </configure>

  - In Archetypes Schemata deklarierte Indizes werden ebenfalls in GenericSetup-Profile verschoben. Der Index für dieses Feld::

     StringField(
         name='issueType',
         index="FieldIndex:schema",
         widget=SelectionWidget(
             label="Issue type",
             description="Select the type of issue.",
             label_msgid='My_label_issueType',
             description_msgid='My_help_issueType',
             i18n_domain='MyProduct',
         ),
         enforceVocabulary=True,
         vocabulary='getIssueTypesVocab',
         required=True
     ),

    wird in ``catalog.xml`` folgendermaßen dargestellt::

     <index name="getIssueType" meta_type="FieldIndex">
       <indexed_attr value="getIssueType"/>
     </index>

     <column value="getIssueType"/>

- ``manage_``-Methoden sollten durch ``events`` ersetzt werden.
- Um die *Permissions* aus dem CMFCore-Produkt zu importieren, sollte in der ``__init__.py`` Datei folgender (rückwärtskompatibler) Code verwendet werden::

   try: # for Plone 2.5 and above
       from Products.CMFCore import permissions as CMFCorePermissions
   except: # for Plone 2.1
       from Products.CMFCore import CMFCorePermissions

- Archetypes 1.5, das zusammen mit Plone 3.0 ausgeliefert wird, enthält kein ``Transaction``-Modul mehr, statt::

   from Products.Archetypes import transaction

  kann nun einfach folgendes verwendet werden::

   import transaction

- Zope hat die Syntax, um Transaktionen zu importieren geändert. Ab Zope 2.10.x wird die bisherige Syntax::

   get_transaction().commit(1)

  durch folgende ersetzt::

   transaction.commit(1)

  ``transaction`` muss selbstverständlich zunächst importiert werden.

- CMF hat seit längerer Zeit ``ContentFactoryMetadata`` durch  ``FactoryTypeInformation`` ersetzt. Der Aufruf::

   from Products.CMFCore.TypesTool import ContentFactoryMetadata

  sollte also ersetzt werden durch::

   from Products.CMFCore.TypesTool import FactoryTypeInformation

- Berechtigungen wie z.B. ``cmf.ModifyPortalContent`` müssen in ``zcml`` angegeben werden::

   <include package="Products.CMFCore" file="permissions.zcml"
            xmlns:zcml="http://namespaces.zope.org/zcml"
            zcml:condition="have plone-41" />

  Dabei wird ``zcml:condition`` in Plone 4.1.3 definiert in der ``meta.zcml``-Datei::

   <configure
       xmlns="http://namespaces.zope.org/zope"
       xmlns:meta="http://namespaces.zope.org/meta">

       <meta:provides feature="plone-4" />
       <meta:provides feature="plone-41" />

   </configure>

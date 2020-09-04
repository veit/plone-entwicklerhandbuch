===========================================
plone.app.caching: Eigene Profile erstellen
===========================================

Zunächst wird ein GenericSetup-Profil registriert für das ``ICacheProfiles``-Marker-Interface registriert::

 <genericsetup:registerProfile
     name="with-caching-proxy"
     title="With caching proxy"
     description="Settings useful for setups with a caching proxy such as Squid or Varnish"
     directory="profiles/with-caching-proxy"
     provides="Products.GenericSetup.interfaces.EXTENSION"
     for="plone.app.caching.interfaces.ICacheProfiles"
     />

Dies bewirkt zugleich, dass dieses Profil nicht als Profil im  Erweiterungen-Kontrollfeld von Plone ausgewählt werden kann.

Das Verzeichnis ``profiles/with-caching-proxy`` enthält eine ``registry.xml``-Datei mit Einstellungen für die Regelsätze zum Verknüpfen von Objekten mit Caching-Operationen, z.B.::

 <record name="plone.caching.interfaces.ICacheSettings.operationMapping">
     <value purge="False">
         <element key="plone.resource">plone.app.caching.strongCaching</element>
         <element key="plone.stableResource">plone.app.caching.strongCaching</element>
         <element key="plone.content.itemView">plone.app.caching.weakCaching</element>
         <element key="plone.content.feed">plone.app.caching.moderateCaching</element>
         <element key="plone.content.folderView">plone.app.caching.weakCaching</element>
         <element key="plone.content.file">plone.app.caching.moderateCaching</element>
     </value>
 </record>

Um z.B. RAM-Caching für die *weak caching*-Operation von Ressourcen zu erlauben, wird der Regelsatz ``plone.content.itemView`` verwendet::

 <record name="plone.app.caching.weakCaching.plone.content.itemView.ramCache">
     <field ref="plone.app.caching.weakCaching.ramCache" />
     <value>True</value>
 </record>

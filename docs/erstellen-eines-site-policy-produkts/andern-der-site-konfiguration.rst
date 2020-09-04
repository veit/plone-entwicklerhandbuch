=============================
Ändern der Site-Konfiguration
=============================

In unserem Beispiel ändern wir Titel und Beschreibung der Site. Im ZMI könnten beide geändert werden unter ``localhost:8080/mysite/manage_propertiesForm``. Für die programmatische Änderung solcher Einstellungen gibt es seit Plone 2.5 das Generic Setup Tool, das unter ``localhost:8080/mysite/portal_setup/manage_workspace`` verfügbar ist. Wenn Sie hier auf den *Export*-Reiter klicken, können solche Konfigurationen auch als XML-Dateien exportiert werden.

Erstellen eines ``EXTENSION``-Profils
-------------------------------------

Um ein solches Profil zu erstellen wird ``src/vs.policy/vs/policy/configure.zcml`` folgendermaßen geändert::

 <configure
     xmlns="http://namespaces.zope.org/zope"
     xmlns:five="http://namespaces.zope.org/five"
     xmlns:genericsetup="http://namespaces.zope.org/genericsetup"
     i18n_domain="vs.policy">

 <five:registerPackage package="." initialize=".initialize" />

 <genericsetup:registerProfile
   name="default"
   title="vs.policy"
   directory="profiles/default"
   description="Policies for www.veit-schiele.de"
   provides="Products.GenericSetup.interfaces.EXTENSION"
   />

 </configure>

Anschließend sind noch die angegebenen Verzeichnisse zu erstellen::

 $ mkdir src/vs.policy/vs/policy/profiles src/vs.policy/vs/policy/profiles/default

Schließlich wird in ``src/vs.policy/vs/policy/profiles/default`` das Profil ``properties.xml`` erstellt mit::

 <?xml version="1.0"?>
 <site>
  <property name="title">Veit Schiele</property>
  <property name="description">Welcome to Veit Schiele</property>
 </site>

Eigene Upgrade-Skripte schreiben
================================

Falls ein EXTENSION-Profil zum Installieren eines Produkts verwendet wurde, können Upgrade steps des Generic Setup Tools verwendet werden, um Migrationsskripte zu verwalten.

Dabei kann das Generic Setup Tool die Versionsnummer entweder aus der ``version.txt``-Datei im Wurzelverzeichnis des Produkts auslesen oder aus einer ``metadata.xml``-Datei im Installationsprofil. Entsprechend wurde das ``Default``-Profil von ``vs.policy`` ergänzt um ``src/vs.policy/vs/policy/profiles/default/metadata.xml``::

 <?xml version="1.0"?>
 <metadata>
     <description>Policies for www.veit-schiele.de</description>
     <version>1.3</version>
 </metadata>

Die *Upgrade steps* werden dann in ``src/vs.policy/vs/policy/configure.zcml`` registriert::

 <configure
     xmlns="http://namespaces.zope.org/zope"
     xmlns:five="http://namespaces.zope.org/five"
     xmlns:genericsetup="http://namespaces.zope.org/genericsetup"
     i18n_domain="vs.policy">

     ...

     <!-- Upgrade step for the migration -->
     <genericsetup:upgradeStep
         sortkey="1"
         source="1.0"
         destination="1.1"
         title="Upgrade from 1.0 to 1.1"
         description="Fixes the front page title"
         profile="vs.policy:default"
         handler=".upgrades.v1_0_to_v1_1"
         />

     ...

 </configure>

Hier wird die Aktualisierung von Version 1.0 auf 1.1 definiert, wobei die Funktion ``v1_0_to_v1_1()`` aufgerufen wird.

Die Funktion ist definiert in ``src/vs.policy/vs/policy/upgrades.py``::

 from Products.CMFCore.utils import getToolByName

 def v1_0_to_v1_1(portal_setup):
     portal_url = getToolByName(portal_setup, 'portal_url')
     portal = portal_url.getPortalObject()
     front_page = portal['front-page']
     front_page.setTitle('Welcome to Veit Schiele communication design')

Die Aktualisierung von 1.1 auf 1.2 teilt sich in zwei Teile auf, ``v1_1_to_v1_2a`` und ``v1_1_to_v1_2b``. Dabei sorgt ``sortkey`` für die richtige Reihenfolge bei der Aktualisierung über mehrere Versionen::

     <genericsetup:upgradeSteps
         sortkey="2"
         source="1.1"
         destination="1.2"
         profile="vs.policy:default"
         >
         <genericsetup:upgradeStep
             title="Upgrade titles"
             description="Fix all other titles"
             handler=".upgrades.v1_1_to_v1_2a"
             />
         <genericsetup:upgradeStep
             title="Upgrade site title"
             description="Fixes the portal title"
             handler=".upgrades.v1_1_to_v1_2b"
             />
     </genericsetup:upgradeSteps>

Migrationsprofil
================

Falls eine große Anzahl von Migrationen durchlaufen werden soll, kann sich ein spezielles ``Extension``-Profil empfehlen::

     <genericsetup:registerProfile
           name="1.2_to_1.3"
           title="Migration profile for veit-schiele.de 1.2 to 1.3"
           description=""
           directory="profiles/migrations/v1_2_to_v1_3"
           for="Products.CMFPlone.interfaces.IMigratingPloneSiteRoot"
           provides="Products.GenericSetup.interfaces.EXTENSION"
           />
     <genericsetup:upgradeStep
         sortkey="3"
         source="1.2"
         destination="1.3"
         title="Upgrade from 1.2 to 1.3"
         description="Runs a migration profile"
         profile="vs.policy:default"
         handler=".upgrades.v1_2_to_v1_3"
         />

Zunächst wird das ``Extension``-Profil in ``profiles/migrations/v1_2_to_v1_3`` für das Interface ``Products.CMFPlone.interfaces.IMigratingPloneSiteRoot`` registriert, wodurch das Profil nicht beim Erstellen der Site oder in Plone’s Website-Konfiguration zum *Hinzufügen/Entfernen von Produkten* angezeigt wird. Anschließend wird noch ein *upgrade step* registriert, der das Profil angibt.

Schließlich muss noch das Verzeichnis ``src/vs.policy/vs/policy/profiles/migrations/v1_2_to_v1_3`` und darin die entsprechenden XML-Dateien erzeugt werden.

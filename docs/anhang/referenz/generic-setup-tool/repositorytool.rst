==============
Repositorytool
==============

Ab Plone 4.1 lässt sich das Repositorytool über ein Generic-Setup-Profil konfigurieren.

Die ``repositorytool.xml``-Datei kann z.B. so aussehen::

 <?xml version="1.0"?>
 <repositorytool>
     <policymap>
         <type name="MyType">
             <policy name="at_edit_autoversion"/>
             <policy name="version_on_revert"/>
         </type>
         <type name="AnotherType">
             <policy name="at_edit_autoversion"/>
             <policy name="version_on_revert"/>
         </type>
     </policymap>
 </repositorytool>

Soll das Produkt auch in Plone < 4.1 funktionieren, sollte in der ``setuphandlers.py``-Datei eine Bedingung angegeben werden. Sehen Sie hierzu `Generic-Setup-Profil für die Versionierung`_.

.. _`Generic-Setup-Profil für die Versionierung`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/migrationen/copy_of_migration-eines-produkts-zu-plone-4.1#generic-setup-profil-fur-die-versionierung

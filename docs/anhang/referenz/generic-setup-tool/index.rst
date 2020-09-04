==================
Generic Setup Tool
==================

Das Generic Setup Tool vereinfacht die Vorkonfigurierung einer Site.

Jede konfigurierbare Komponente stellt Handler zum Im- und Export von Profilen bereit.

Profile sind Konfigurationsdateien für bestimmte Komponenten einer Website. Diese können z.B. Rollen, Berechtigungen, Skin-Layer und vieles mehr festlegen. Dabei werden im wesentlichen zwei Arten von Profilen unterschieden:

base profile
 Profil für die Basiskonfiguration einer Site. ``Products.CMFPlone`` bringt ein solches Profil mit, das die Standardkonfiguration einer Plone-Site enthält.
extension profile
 Profil, das auf einem *base profile* aufbaut und an einigen Stellen die Standardkonfiguration ändert und neue Im- und Export-Schritte bereitstellen kann.

Registrieren eines Profils
==========================

GenericSetup-Profile können einfach mit ZCML registriert werden, z.B. in der ``configure.zcml``-Datei von ``vs.theme``::

 <configure
     xmlns="http://namespaces.zope.org/zope"
     xmlns:genericsetup="http://namespaces.zope.org/genericsetup"
     i18n_domain="vs.theme">

   <genericsetup:registerProfile
       name="default"
       title="Theme for the Websites of Veit Schiele Communications"
       directory="profiles/default"
       description="Default profile for vs.theme"
       provides="Products.GenericSetup.interfaces.EXTENSION"
       />

 </configure>

``name``
 Bestandteil der ID des GenericSetup-Profils. Die vollständige ID lautet ``profile-<package_name>:<profile_name>``, in unserem Fall also ``profile-vs.theme:default``.
``title``
 Der Titel des Profils, der Ihnen im Generic Setup Tool beim Import angezeigt wird und im Quickinstaller beim Aktivieren eines Pakets.
``directory``
 Relative Pfadangabe zum Verzeichnis mit den Profilinformationen. Meist entspricht der Verzeichnisname dem Profilnamen.
``description``
 Die Beschreibung des Profils sollte eine kurze Zusammenfassung für die Verwendung des Profils geben.
``provides``
 Die Art des Profils, also ``EXTENSION`` oder ``BASE``.

Tipps
=====

#. Häufig ist die einfachste Möglichkeit ein Profil zu schreiben diejenige, in einer Site Änderungen an der Konfiguration vorzunehmen und anschließend die Profile derjenigen Tools zu exportieren, deren Konfiguration geändert wurde.
#. Anschließend sollte dieses Profil jedoch nicht unmittelbar übernommen werden sondern nur diejenigen Teile, die auch tatsächlich geändert wurden.
#. Üblicherweise ersetzen die Werte von ``ÈXTENSION``-Profilen die bereits bestehenden Werte. Mit ``purge="False"`` kann dieses Verhalten jedoch geändert werden, z.B.::

    <?xml version="1.0"?>
    <object name="portal_properties">
        <object name="navtree_properties">
            <property name="metaTypesNotToList" type="lines" purge="False">
                <element value="Registration"/>
            </property>
        </object>
    </object>

 Hierdurch wird ``Registration`` der Liste der Artikeltypen hinzugefügt. Ohne ``purge="False"`` würde nur der ``Registration``-Artikeltyp nicht in der Navigation angezeigt werden.

Metadaten
=========

Das Profil in ``metadata.xml`` kann z.B. so aussehen::

 <?xml version="1.0"?>
 <metadata>
   <description>Policy for the Website of Veit Schiele Communications</description>
   <version>1.0dev $LastChangedRevision$ </version>
   <dependencies>
     <dependency>profile-vs.theme:default</dependency>
     <dependency>profile-Products.LinguaPlone:LinguaPlone</dependency>
   </dependencies>
 </metadata>

``description``
 Kurze Erläuterung des Profils
``version``
 Die Versionsnummer des Profils

 Diese wird auch verwendet um Upgrade-Schritte durchzuführen. Upgrades können immer nur zwischen definierten Versionsnummern durchgeführt werden.
``dependencies``
 Voraussetzungen für dieses Profil. Profile, die hier genannt werden, werden beim Import zuerst ausgeführt.

.. seealso::
    - `Plone Developer Manual: Generic Setup`_

.. _`Plone Developer Manual: Generic Setup`: http://plone.org/documentation/manual/developer-manual/generic-setup

.. toctree::
    :titlesonly:
    :maxdepth: 0

    content-rules
    repositorytool
    toolset

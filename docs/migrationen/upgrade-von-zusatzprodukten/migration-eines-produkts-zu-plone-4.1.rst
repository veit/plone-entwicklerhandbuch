=====================================
Migration eines Produkts zu Plone 4.1
=====================================

Für die Migration auf Plone 4.1 sollten die folgenden Änderungen beachtet werden.

Geänderte Abhängigkeiten von ``Plone`` zu ``Products.CMFPlone``
===============================================================

Aktualisieren der ``setup.py``-Datei
------------------------------------

In der ``setup.py``-Datei sollte bisher folgendes stehen::

 install_requires=[
     'setuptools',
     'Plone',
 ],

Stattdessen sollte in Plone 4.1 folgendes verwendet werden::

 install_requires=[
     'setuptools',
     'Products.CMFPlone',
 ],

Auch sollten hier die anderen Pakete aufgelistet werden, von denen das Paket abhängt, z.B. ``Products.Archetypes`` oder ``plone.app.portlets``.

Aktualisieren der Berechtigungen
--------------------------------

Sofern ``pages`` etc. in einer ``zcml``-Datei mit ener CMF-Core-Permission geschützt sind, muss die ``configure.zcml``-Datei ergänzt werden um::

 <include package="Products.CMFCore" file="permissions.zcml"
          xmlns:zcml="http://namespaces.zope.org/zcml"
          zcml:condition="have plone-41" />

Aktualisieren der Aliase
------------------------

Einige ältere Import-Aliase funktionieren in Plone 4.1 nicht mehr und müssen ersetzt werden:

+--------------------------------------------------------+--------------------------------------------------------+
| Frühere Plone-Versionen                                |  Plone 4.1                                             |
+========================================================+========================================================+
| ``from Products.CMFPlone import Batch``                |  ``from Products.CMFPlone.PloneBatch import Batch``    |
+--------------------------------------------------------+--------------------------------------------------------+
| ``from zope.app.interface import queryType``           | ``from zope.app.content import queryType``             |
+--------------------------------------------------------+--------------------------------------------------------+
| ``from Products.Five.formlib import formbase``         | ``from five.formlib import formbase``                  |
+--------------------------------------------------------+--------------------------------------------------------+

Generic-Setup-Profil für die Versionierung
==========================================

Ab Plone 4.1 kann die Konfiguration zur Versionierung eigener Artikeltypen im Profil ``repositorytool.xml`` angegeben werden. Genaue Angaben hierzu finden Sie in

- `Enabling versioning on your custom content-types`_
- `History and Versioning`_

.. _`Enabling versioning on your custom content-types`: http://plone.org/documentation/manual/developer-manual/archetypes/appendix-practicals/enabling-versioning-on-your-custom-content-types
.. _`History and Versioning`: http://collective-docs.readthedocs.org/en/latest/content/history.html

Wenn Sie von Plone 4.0 aktualisieren, erhalten Sie vermutlich folgende Fehlermeldung::

 ImportError: cannot import name DEFAULT_POLICIES

Um die Kompatibilität Ihres Produkts mit Plone 4.1 wiederherzustellen, muss für Ihren bisherigen Code in der  ``setuphandlers.py``-Datei eine Bedingung angegeben werden, also z.B. statt::

 from Products.CMFEditions.setuphandlers import DEFAULT_POLICIES

sollte folgendes angegeben werden::

 try:
     from Products.CMFEditions.setuphandlers import DEFAULT_POLICIES
     # we're on plone < 4.1, configure versionable types manually
     setVersionedTypes(portal)
 except ImportError:
     # repositorytool.xml will be used
     pass

Für Plone 4.1 wird die Konfiguration zur Versionierung der Artikel im Profil ``repositorytool.xml`` angegeben::

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

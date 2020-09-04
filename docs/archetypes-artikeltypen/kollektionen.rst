============
Kollektionen
============

Kollektionen sollen auch Felder unserer Artikeltypen suchen können. Hierzu sind doe folgenden beiden Profile hinzuzufügen:

Hinzufügen von Index und Metadaten zum *Catalog Tool*
=====================================================

Diese werden im ``catalog.xml``-Profil hinzugefügt::

 <?xml version="1.0"?>
 <object name="portal_catalog" meta_type="Plone Catalog Tool">
      <index name="myfield" meta_type="FieldIndex">
          <indexed_attr value="myfield"/>
     </index>
     <column value="myfield"/>
 </object>

Folgende Typen von Indizees sind möglich:

- ``DateIndex``
- ``DateRangeIndex``
- ``ExtendePathIndex``
- ``FieldIndex``
- ``KeywordIndex``
- ``PathIndex``
- ``TextIndex``
- ``TopicIndex``
- ``ZCTextIndex``

Hinzufügen von Index und Metadaten zum *ATCT Tool*
==================================================

Diese werden im ``portal_atct.xml``-Profil hinzugefügt::

 <?xml version="1.0"?>
 <atcttool>
     <topic_indexes>
         <index name="myfield"
                description="myfield's description"
                enabled="True"
                friendlyName="mytype's myfield">
             <criteria>ATSimpleStringCriterion</criteria>
         </index>
     </topic_indexes>
     <topic_metadata>
         <metadata  name="myfield"
                    description="myfield's description"
                    enabled="True"
                    friendlyName="mytype's myfield"/>
     </topic_metadata>
 </atcttool>

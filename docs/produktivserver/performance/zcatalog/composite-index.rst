===============
Composite Index
===============

CompositeIndex ist ein Index für den ZCatalog, der mehr als ein Attribut je Objekt enthalten kann.Solche Indizes sollten erstellt werden, wenn Anfragen mit mehreren Attributen in einer Suche zu erwarten ist und die kombinierte Suche deutlich weniger Ergebnisse erwarten lässt als die einzelnen Suchen mit nur einem Attribut. Hiervon profitieren vor allem große Sites mit mehr als 100.000 Objekten, bei denen die Anfragen zwei- bis dreimal schneller abgearbeitet werden können.

Viele Kataloganfragen basieren auf er Kombination indizierter Attribute. Üblicherweise arbeitet der ZCatalog jede dieser Anfragen sequentiell ab und berechnet die Schnittmenge zwischen jedem dieser Ergebnisse. Für große Sites mit vielen Objekten reduziert diese Strategie die Performance von Kataloganfragen deutlich. Der ``CompositeIndex`` von `unimr.compositeindex`_ hingegen kann jedoch bereits die Schnittmenge von Indizees der Typen ``FieldIndex`` und ``KeywordIndex`` bilden.

.. _`unimr.compositeindex`: http://pypi.python.org/pypi/unimr.compositeindex

Installation
============

Um ``unimr.compositeindex`` zu installieren, muss es einfach als Egg im ``[buildout]``-Abschnitt eingetragen werden::

 [buildout]
 ...
 eggs =
     ...
     unimr.compositeindex

Anschließend kann es in der ``configure.zcml``-Datei eines Produkts eingetragen werden::

 <include package="unimr.compositeindex" />

Alternativ kann es auch als Wert für ``zcml`` im Abschnitt der Zope-Instanz eingetragen werden::

 [instance]
 ...
 zcml =
     unimr.compositeindex

Verwendung
==========

Für das *Generic Setup*-Profil wird die ``catalog.xml``-Datei erstellt mit folgendem Inhalt::

 <?xml version="1.0"?>
 <object name="portal_catalog" meta_type="Plone Catalog Tool">
     <index name="comp01" meta_type="CompositeIndex">
         <indexed_attr value="is_default_page"/>
         <indexed_attr value="review_state"/>
         <indexed_attr value="portal_type"/>
         <indexed_attr value="allowedRolesAndUsers"/>
     </index>
     <column value="comp01"/>
 </object>


``index name``
 Eine gültige ID Ihrer Wahl.
``indexed_attr value``
 Name des Attributs eines Objekts, das in einer Anfrage verkettet werden soll.

Anschließend sollte im ZMI im *Indexes*-Reiter des Catalog Tools für diesen *CompositeIndex* noch *Reindex* angegeben werden. Jede Anfrage mit zwei oder mehr Komponenten des ``Composite key`` wird nun automatisch umgewandelt in eine Anfrage an den *CompositeIndex*.

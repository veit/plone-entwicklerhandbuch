===================
collective.indexing
===================

collective.indexing ersetzt die Standard-Indizierung des CMF durch einen asynchronen Mechanismus, der redundante Indizierungen vermeidet. Damit wird die Performance zur Aktualisierung der Indizes deutlich gesteigert.

Installation
============

Um `collective.indexing`_ zu installieren, muss es einfach als Egg im ``[buildout]``-Abschnitt eingetragen werden::

 [buildout]
 ...
 eggs =
     ...
     collective.indexing

Anschließend kann es in der ``configure.zcml``-Datei eines Produkts eingetragen werden::

 <include package="collective.indexing" />

Alternativ kann es auch als Wert für ``zcml`` im Abschnitt der Zope-Instanz eingetragen werden::

 [instance]
 ...
 zcml =
     collective.indexing

Anschließend kann ``collective.indexing`` für die Plone-Site installiert werden.

.. seealso::

    * `Clean and fast indexing in Plone`_

.. _`collective.indexing`: http://plone.org/products/collective.indexing/
.. _`Clean and fast indexing in Plone`: http://www.jarn.com/blog/plone-indexing-performance

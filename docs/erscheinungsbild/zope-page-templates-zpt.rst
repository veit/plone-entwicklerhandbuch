=========================
Zope Page Templates (ZPT)
=========================

*Zope Page Templates* verwenden TAL (Template Attribute Language), z.B.::

  <title tal:content="context/title">Page Title</title>

Dabei ist ``tal:content`` das TAL-Attribut wobei ``tal`` den XML-Namensraum angibt und ``content`` darauf hinweist, dass der Inhalt des ``title``-Tags gesetzt werden soll. Der Wert ``context/title`` schließlich ist ein Ausdruck, der den in den Tag einzufügenden Text liefert und dabei ``Page Title`` ersetzt.

Ausdrücke
=========

Der Text ``context/title`` ist ein einfacher Pfadausdruck der *TAL Expression Syntax* (TALES), der die Titel-Eigenschaft des Kontexts aufruft. Andere häufig verwendete Pfadausdrücke sind:

``request/URL``
 Die URL des aktuellen Web-Requests.
``user/getUserName``
 Der Login-Name des aktuell angemeldeten Nutzers.
``container/objectIds``
 Eine Liste aller IDs von Objekten im selben Ordner wie das Template.

Jeder Pfadausdruck startet mit einem Variablenname und kann, getrennt durch einen Schrägstrich (``/``), um den Namen eines Unterobjekts oder eine Eigenschaft spezifiziert werden.

Die Menge der verfügbaren Variablen, wie ``request`` oder ``user``, ist relativ gering und wird später noch vollständig beschrieben werden. Zudem werde ich zeigen, wie eigene Variablen definiert werden können.

Inhalte
=======

Angenommen unser Template hätte die ID ``my_page``, und wir wollten Text dynamisch einfügen, so könnten wir dies innerhalb eines ``span``-Tags machen::

 Die URL ist <span tal:replace="request/URL">URL</span>.

Beachten Sie, dass der gesamte Tag ersetzt wird durch das Ergebnis der TAL-Anweisung, also::

 Die URL ist http://localhost:8080/mysite/my_page.

Soll ein Tag erhalten bleiben, wird ``tal:content`` verwendet::

 <title tal:content="template/title">The Title</title>

Aufzählungen
============

Soll eine ganze Liste von Werten automatisch eingefügt werden, so kann dies mit ``tal:repeat`` erfolgen, z.B.::

 <table>
     <tr>
         <th>#</th><th>Id</th><th>Meta-Type</th><th>Title</th>
     </tr>
     <tr tal:repeat="item container/objectValues">
         <td tal:content="repeat/item/number">#</td>
         <td tal:content="item/id">Id</td>
         <td tal:content="item/meta_type">Meta-Type</td>
         <td tal:content="item/title">Title</td>
     </tr>
 </table>

Der ``tal:repeat``-Ausdruck auf einer Tabellenzeile bedeutet, dass diese Zeile für jeden Artikel in diese Container erstellt wird. Dabei wird für jede Zeile ein Artikel der Liste als ``item``-Variable verwendet und dessen Werte ausgelesen, wobei statt ``item`` auch jeder andere Name verwendet werden kann.

``repeat/item/number`` ist die fortlaufende Nummerierung der Artikel innerhalb der Aufzählung. Soll die Nummerierung mit ``0`` beginnen, muss statt ``number`` ``index`` verwendet werden, soll die fortlaufende Nummerierung alphabetisch sein, ist das Attribut ``letter``.

Selbstverständlich können auch mehrere Aufzählungen ineinander verschachtelt werden.

Bedingungen
===========

Um jeder zweiten Zeile der obigen Tabelle eine andere Hintergrundfarbe zu geben, können entsprechende Bedingungen angegeben werden::

 <table>
     <tr>
         <th>#</th><th>Id</th><th>Meta-Type</th><th>Title</th>
     </tr>
     <tbody tal:repeat="item container/objectValues">
         <tr bgcolor="#DDE0E8" tal:condition="repeat/item/even">
             <td tal:content="repeat/item/number">#</td>
             <td tal:content="item/id">Id</td>
             <td tal:content="item/meta_type">Meta-Type</td>
             <td tal:content="item/title">Title</td>
         </tr>
         <tr tal:condition="repeat/item/odd">
             <td tal:content="repeat/item/number">#</td>
             <td tal:content="item/id">Id</td>
             <td tal:content="item/meta_type">Meta-Type</td>
             <td tal:content="item/title">Title</td>
         </tr>
     </tbody>
 </table>

.. Zum Weiterlesen
.. ===============

.. - `ZPT - Zope Page Templates`_
.. - `Zope Page Templates: Getting Started`_
.. - `Zope Page Templates: Advanced Usage`_
.. - `Using Zope with Amaya, Dreamweaver, and Other WYSIWYG Tools`_
.. - `Using Zope Page Templates`_
.. - `Advanced Page Templates`_
.. - `Appendix C: Zope Page Templates Reference`_

.. _`ZPT - Zope Page Templates`: http://plone.org/documentation/tutorial/zpt
.. _`Zope Page Templates: Getting Started`: http://www.zope.org/Documentation/Articles/ZPT1
.. _`Zope Page Templates: Advanced Usage`: http://www.zope.org/Documentation/Articles/ZPT2
.. _`Using Zope with Amaya, Dreamweaver, and Other WYSIWYG Tools`: http://www.zope.org/Documentation/Articles/ZPT3
.. _`Using Zope Page Templates`: http://www.zope.org/Documentation/Books/ZopeBook/2_6Edition/ZPT.stx
.. _`Advanced Page Templates`: http://www.zope.org/Documentation/Books/ZopeBook/2_6Edition/AdvZPT.stx
.. _`Appendix C: Zope Page Templates Reference`: http://www.zope.org/Documentation/Books/ZopeBook/2_6Edition/AppendixC.stx

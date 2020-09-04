======
Felder
======

Die gebräuchlichsten Feldtypen und -eigenschaften, die in Dexterity verwendet werden.

Eine Anleitung zum Erstellen eines Schemas erhalten Sie in :doc:`../../../dexterity-artikeltypen/schema-interfaces`.

Feldeigenschaften
=================


+------------------------+------------------------+----------------+----------------------------------------------------------------+
| Interface              | Eigenschaft            | Typ            | Beschreibung                                                   |
+========================+========================+================+================================================================+
| ``IField``             | ``title``              | unicode        | Der Titel des Feldes, der im Widget verwendet wird.            |
|                        +------------------------+----------------+----------------------------------------------------------------+
|                        | ``description``        | unicode        | Die Beschreibung des Feldes, die im Widget verwendet wird.     |
|                        +------------------------+----------------+----------------------------------------------------------------+
|                        | ``required``           | bool           | Es wird überprüft, ob das Feld eine Angabe enthält.            |
|                        |                        |                | Der Standarwert ist ``True``.                                  |
|                        +------------------------+----------------+----------------------------------------------------------------+
|                        | ``readonly``           | bool           | Ist der Wert ``True``, so kann das Feld nur gelesen werden.    |
|                        |                        |                | Der Standarwert ist ``False``.                                 |
|                        +------------------------+----------------+----------------------------------------------------------------+
|                        | ``default``            |                | Der Standardwert eines Feldes. Dieser Wert kann ggf. auch als  |
|                        |                        |                | Fallback verwendet werden, falls keine Angabe gemacht wurde.   |
|                        |                        |                | Dieser Wert muss eine valide Angabe für dieses Feld sein.      |
|                        |                        |                | Der Standardwert ist ``None``.                                 |
|                        +------------------------+----------------+----------------------------------------------------------------+
|                        | ``missing_value``      |                | Ein wert, der verdeutlicht, dass dieses Feld nicht ausgefüllt  |
|                        |                        |                | wurde. Dieser Wert wird bei der Validierung des Formulars      |
|                        |                        |                | verwendet. Der Standarwert ist ``None``.                       |
|                        |                        |                | Für Listen und Tuples kann es gelegentlich nützlich sein, eine |
|                        |                        |                | leere Liste oder ein leeres Tuple zu setzen.                   |
+------------------------+------------------------+----------------+----------------------------------------------------------------+
| ``IMinMaxLen``         | ``min_length``         | int            | Die minimale Länge der Eingabe.                                |
|                        |                        |                | Wird für ``string``-Felder verwendet.                          |
|                        |                        |                | Der Standardwert ist ``0``.                                    |
|                        +------------------------+----------------+----------------------------------------------------------------+
|                        | ``max_length``         | int            | Die maximale Länge der Eingabe.                                |
|                        |                        |                | Wird für ``string``-Felder verwendet.                          |
|                        |                        |                | Der Standardwert ist ``0``.                                    |
+------------------------+------------------------+----------------+----------------------------------------------------------------+
| ``IMinMax``            | ``min``                |                | Der minimal erlaubte Wert. Dies muss ein valider Wert für      |
|                        |                        |                | dieses Feld sein. Der Standardwert ist ``None``.               |
|                        +------------------------+----------------+----------------------------------------------------------------+
|                        | ``max``                |                | Der maximal erlaubte Wert. Dies muss ein valider Wert für      |
|                        |                        |                | dieses Feld sein. Der Standardwert ist ``None``.               |
+------------------------+------------------------+----------------+----------------------------------------------------------------+
| ``ICollection``        | ``value_type``         |                | Erlaubte Werte einer Liste, eines Tuples oder einer anderen    |
|                        |                        |                | Sammlung. Muss für jedes ``collection``-Feld gesetzt werden.   |
|                        |                        |                | Häufig wird als Wert ``Choice`` angegeben um ein               |
|                        |                        |                | Multi-Selection-Feld mit einem Vokabular zu erstellen.         |
|                        +------------------------+----------------+----------------------------------------------------------------+
|                        | ``unique``             | ``bool``       | Ob die Werte in der Kollektion eindeutig sein müssen           |
|                        |                        |                | oder nicht. Wird meist nicht direkt gesetzt, sondern es wird   |
|                        |                        |                | ein ``Set`` oder ein ``Frozenset`` verwendet um die            |
|                        |                        |                | Eindeutigkeit zu garantieren.                                  |
+------------------------+------------------------+----------------+----------------------------------------------------------------+
| ``IDict``              | ``key_type``           |                | Beschreibt die erlaubten Schlüssel in einem Dictionary.        |
|                        |                        |                | Ähnlich dem ``value_type`` in Kollektionen.                    |
|                        |                        |                | Muss gesetzt werden.                                           |
|                        +------------------------+----------------+----------------------------------------------------------------+
|                        | ``value_type``         |                | Beschreibt die erlaubten Werte in einem Dictionary.            |
|                        |                        |                | Ähnlich ``value_type`` in Kollektionen.                        |
|                        |                        |                | Muss gesetzt werden.                                           |
+------------------------+------------------------+----------------+----------------------------------------------------------------+
| ``IObject``            | ``schema``             | ``Ìnterface``  | Ein Interface, das von jedem Objekt, das in diesem Feld        |
|                        |                        |                | gespeichert wird bereitgestellt werden muss.                   |
+------------------------+------------------------+----------------+----------------------------------------------------------------+
| ``IRichText``          | ``default_mime_type``  | ``str``        | Standard-MIME-Typ für den Eingabetext eines Rich Text-Felds.   |
|                        |                        |                | Der Standard ist ``text/html``.                                |
|                        +------------------------+----------------+----------------------------------------------------------------+
|                        | ``output_mime_type``   | ``str``        | Standard-MIME-Typ für den transformierten Text eines           |
|                        |                        |                | Rich Text-Felds.                                               |
|                        |                        |                | Der Standard ist ``text/x-html-safe``.                         |
|                        +------------------------+----------------+----------------------------------------------------------------+
|                        | ``allowed_mime_types`` | ``tuple``      | Eine Liste aller erlaubten MIME-Typen für die Eingabe.         |
|                        |                        |                | Der Standardwert ist ``None``, wobei den die Einstellungen     |
|                        |                        |                | für die gesamte Website übernommen werden.                     |
+------------------------+------------------------+----------------+----------------------------------------------------------------+

Feldtypen
=========

Die folgende Tabelle listet die am häufigsten verwendeten Feltypen auf, sortiert nach dem Modul, von dem sie importiert werden können.

Felder in ``zope.schema``
-------------------------

+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| Name                   | Typ                    | Beschreibung                                                   | Typ                            |
+========================+========================+================================================================+================================+
| ``Choice``             | ``N/A``                | Wird verwendet für die Auswahl aus einem Vokabular.            | Siehe `Vokabularien`_          ||                        |                        | Wird häufig verwendet als ``value_type`` eines Auswahlfeldes.  |                                |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``Bytes``              | ``str``                | Für binäre Daten                                               | ``IField``, ``IMinMaxLen``     |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``ASCII``              | ``str``                | ASCII-Text über mehrere Zeilen                                 | ``IField``, ``IMinMaxLen``     |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``BytesLine``          | ``str``                | Einzeiler mit Binärdaten                                       | ``IField``, ``IMinMaxLen``     |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``ASCIILine``          | ``str``                | Einzeiler mit ASCII-Text                                       | ``IField``, ``IMinMaxLen``     |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``Text``               | ``unicode``            | Mehrzeiliger Unicode-Text, der häufig zusammen mit dem         | ``IField``, ``IMinMaxLen``     |
|                        |                        | WYSIWYG-Widget verwendet wird.                                 |                                |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``TextLine``           | ``unicode``            | Einzeiler mit Unicode-Text.                                    | ``IField``, ``IMinMaxLen``     |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``Bool``               | ``bool``               | Wahr oder Falsch                                               | ``IField``, ``IMinMaxLen``     |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``Int``                | ``int``, ``long``      | Ganz Zahl. Sowohl ``ìnt`` als auch ``long`` sind zulässig.     | ``IField``, ``IMinMaxLen``     |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``Float``              | ``float``              | Fließkommazahl                                                 | ``IField``, ``IMinMaxLen``     |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``Tuple``              | ``tuple``              | Endliche Liste von Objekten                                    | ``IField``, ``Collection``,    |
|                        |                        |                                                                | ``IMinMaxLen``                 |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``List``               | ``List``               | Verkettete Liste                                               | ``IField``, ``Collection``,    |
|                        |                        |                                                                | ``IMinMaxLen``                 |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``Set``                | ``set``                | Set, eine ungeordnete Liste von Elementen                      | ``IField``, ``Collection``,    |
|                        |                        |                                                                | ``IMinMaxLen``                 |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``FrozensSet`          | ``frozenset``          | Unveränderliches und hashbares Set.                            | ``IField``, ``Collection``,    |
|                        |                        | Es kann daher als Dictionary key oder als ein Element eines    | ``IMinMaxLen``                 |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``Password``           | ``unicode``            | Einfache Zeichenkette, die jedoch das Password-Widget          | ``IField``, ``IMinMaxLen``     |
|                        |                        | impliziert.                                                    |                                |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``Dict``               | ``dict``               | Speichert ein Dictionary. Sowohl ``key_type``- als auch        | ``IField``, ``IMinMaxLen``     |
|                        |                        |                                                                | ``IDict``                      |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``Datetime``           | ``datetime``           | Speichert Python datetime, nicht Zope2 DateTime                | ``IField``, ``IMinMax``        |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``Date``               | ``date``               | Speichert Python date                                          | ``IField``, ``IMinMax``        |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``Timedelta``          | ``timedelta``          | Speichert Python timedelta                                     | ``IField``, ``IMinMax``        |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``SourceText``         | ``unicode``            | Ein Textfeld zum Speichern von Quellcode, z.B. HTML oder       | ``IField``, ``IMinMaxLen``     |
|                        |                        | Python-Skripte.                                                |                                |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``Object``             | ``N/A``                | Speichert ein Python-Objekt mit einem bestimmten Interface,    | ``IField``, ``IObject``        |
|                        |                        | das das Schema enthält.                                        |                                |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``URI``                | ``str``                | Eine URI-/URL)-Zeichenkette.                                   | ``IField``, ``IMinMaxLen``     |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``Id``                 | ``str``                | Ein Unique Identifier – entweder ein URI oder ein Dotted Name. | ``IField``, ``IMinMaxLen``     |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``DottedName``         | ``str``                | Eine Dotted Name-Zeichenkette.                                 | ``IField``, ``IMinMaxLen``     |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``InterfaceField``     | ``Interface``          | Eine Zope-Interface.                                           | ``IField``                     |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``Decimal``            | ``Decimal``            | Speichert ein `Python-Decimal`_. Erfordert zope.schema 3.4     | ``IField``, ``IMinMax``        |
|                        |                        | oder höher. Nicht verfügbar in Zope 2.10.                      |                                |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+

.. _`Vokabularien`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/dexterity-artikeltypen/standardwerte-vokabularien-und-autovervollstaendigung#vokabularien
.. _`Python-Decimal`: http://docs.python.org/library/decimal.html

Felder in ``plone.namedfile.field``
-----------------------------------

Weitere Informationen erhalten Sie unter `plone.namedfile`_ und  `plone.formwidget.namedfile`_.


.. _`plone.namedfile`: http://pypi.python.org/pypi/plone.namedfile
.. _`plone.formwidget.namedfile`: http://pypi.python.org/pypi/plone.formwidget.namedfile

+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| Name                   | Typ                    | Beschreibung                                                   | Typ                            |
+========================+========================+================================================================+================================+
| ``NamedFile``          | ``NamedFile``          | Eine hochzuladende Binärdatei. Üblicherweise wird das Widget   | ``IField``                     |
|                        |                        | aus ``plone.formwidget.namedfile`` verwendet.                  |                                |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``NamedImage``         | ``NamedImage``         | Ein hochzuladendeis Bild. Üblicherweise wird das Widget        | ``IField``                     |
|                        |                        | aus ``plone.formwidget.namedfile`` verwendet.                  |                                |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``NamedBlobFile``      | ``NamedBlobFile``      | Eine hochzuladende Binärdatei, die als ZODB-BLOB gespeichert   | ``IField``                     |
|                        |                        | wird. Üblicherweise wird das Widget aus                        |                                |
|                        |                        | ``plone.formwidget.namedfile`` verwendet.                      |                                |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``NamedBlobImage``     | ``NamedBlobImage``     | Ein hochzuladendes Bild, das als ZODB-BLOB gespeichert         | ``IField``                     |
|                        |                        | wird. Üblicherweise wird das Widget aus                        |                                |
|                        |                        | ``plone.formwidget.namedfile`` verwendet.                      |                                |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+

Felder in ``z3c.relationfield.schema``
--------------------------------------

Weitere Informationen erhalten Sie unter `z3c.relationfield`_.

.. _`z3c.relationfield`: http://pypi.python.org/pypi/z3c.relationfield

+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| Name                   | Typ                    | Beschreibung                                                   | Typ                            |
+========================+========================+================================================================+================================+
| ``Relation``           | ``RelationValue``      | Speichert den Wert einer einzelnen Relation.                   | ``IField``                     |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``RelationList``       | ``list``               | List-Feld für ``RelationValue``.                               | Siehe ``List``.                |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| ``RelationChoice``     | ``RelationValue``      | Choice-Feld für ``RelationValue``.                             | Siehe ``Choice``               |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+

Felder in ``plone.app.textfield``
---------------------------------

Weitere Informationen erhalten Sie unter `plone.app.textfield`_.

.. _`plone.app.textfield`: http://pypi.python.org/pypi/plone.app.textfield

+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+
| Name                   | Typ                    | Beschreibung                                                   | Typ                            |
+========================+========================+================================================================+================================+
| ``RichText``           | ``RichTextValue``      | Speichert einen ``RichTextValue``, der den Raw-Text, den       | ``IField``, ``IRichText``      |
|                        |                        | MIME-Typ und eine gecachte Version des in den Standard-MIME-   |                                |
|                        |                        | Typ konvertierten Textes enthält.                              |                                |
+------------------------+------------------------+----------------------------------------------------------------+--------------------------------+

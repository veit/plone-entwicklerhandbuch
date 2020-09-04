=======
Widgets
=======

Standard-Widgets und Third-Party-Widgets.

Die gebräuchlichsten Widgets werden von ``z3c.form`` bereitgestellt. Weitere Informationen zu diesen Widgets erhalten Sie in der `z3c.form-Dokumentation`_.

.. _`z3c.form-Dokumentation`: http://packages.python.org/z3c.form/widget.html

Die Tabelle führt die häufig verwendeten Widgets auf:

+----------------------------------------+----------------------------------------+------------------------+----------------------------------------------------------------+
| Widget                                 | Importiert von                         | Feld                   | Beschreibung                                                   |
+========================================+========================================+========================+================================================================+
| ``WysiwygFieldWidget``                 | ``plone.app.z3cform.wysiwyg``          | ``Text``               | Hiermit erhalten Sie den  Standard-WYSIWYG-Editor von Plone    |
|                                        |                                        |                        | für dieses Feld.                                               |
+----------------------------------------+----------------------------------------+------------------------+----------------------------------------------------------------+
| ``RichTextWidget``                     | ``plone.app.textfield.widget``         | ``RichText``           | Dieses Feld erlaubt neben dem Standard-WYSIWYG-Editor auch     |
|                                        |                                        |                        | Text-basiertes Markup wie bei reStructuredText.                |
+----------------------------------------+----------------------------------------+------------------------+----------------------------------------------------------------+
| ``AutocompleteFieldWidget``            | ``plone.formwidget.autocomplete``      | ``Choice``             | Autocpmplete-Widget, das auf jQuery-Autocomplete basiert.      |
|                                        |                                        |                        | Erfordert ein Choice-Feld mit Angabe von ``source``.           |
|                                        |                                        |                        | Siehe `Vokabularien`_.                                         |
+----------------------------------------+----------------------------------------+------------------------+----------------------------------------------------------------+
| ``AutocompleteMultiFieldWidget``       | ``plone.formwidget.autocomplete``      | ``Collection``         | Multi-Select-Version für Tuple, Listen,Sets oder Frozensets    |
|                                        |                                        |                        | mit dem WErtetyp ``Choice``.                                   |
+----------------------------------------+----------------------------------------+------------------------+----------------------------------------------------------------+
| ``ContentTreeFieldWidget``             | ``plone.formwidget.contenttree``       | ``RelationChoice``     | Content-Browser. Erfordert eine Quelle, die nach Objekten      |
|                                        |                                        |                        | angefragt werden kann.                                         |
+----------------------------------------+----------------------------------------+------------------------+----------------------------------------------------------------+
| ``MultiContentTreeFieldWidget``        | ``plone.formwidget.contenttree``       | ``RelationList``       | Content-Browser. Erfordert eine Quelle, die nach Objekten      |
|                                        |                                        |                        | angefragt werden kann.                                         |
+----------------------------------------+----------------------------------------+------------------------+----------------------------------------------------------------+
| ``NamedFileFieldWidget``               | ``plone.formwidget.namedfile``         | ``NamedFile``          | Ein Widget zum Hochladen von Dateien.                          |
+----------------------------------------+----------------------------------------+------------------------+----------------------------------------------------------------+
| ``NamedImageFieldWidget``              | ``plone.formwidget.namedimage``        | ``NamedImage``         | Ein Widget zum Hochladen von Bildern.                          |
+----------------------------------------+----------------------------------------+------------------------+----------------------------------------------------------------+
| ``TextLinesFieldWidget``               | ``plone.z3cform.textlines``            | `Collection``          | Listen-Eintrag für List, Tuple, Set oder Frozenset-Felder.     |
|                                        |                                        |                        | Erfordert als Wertetyp ``TextLine`` oder ``ASCIILine``.        |
+----------------------------------------+----------------------------------------+------------------------+----------------------------------------------------------------+
| ``SingleCheckBoxFieldWidget``          | ``z3c.form.browser.checkbox``          | ``Bool``               | Checkbox für wahr/falsch.                                      |
+----------------------------------------+----------------------------------------+------------------------+----------------------------------------------------------------+
| ``CheckBoxFieldWidget``                | ``z3c.form.browser.checkbox``          | ``Collection``         | Ein Set von Checkboxen. Wird verwendet für Set- oder           |
|                                        |                                        |                        | Frozenset-Felder mit ``Choice`` als WErtetyp und einem         |
|                                        |                                        |                        | Vokabular.                                                     |
+----------------------------------------+----------------------------------------+------------------------+----------------------------------------------------------------+

.. _`Vokabularien`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/dexterity-artikeltypen/standardwerte-vokabularien-und-autovervollstaendigung#vokabularien

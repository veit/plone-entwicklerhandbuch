===========
Validatoren
===========

Die einfachste Form der Validierung liefert bereits die ``z3c.form``-Bibliothek indem sie überprüft, ob die Eingaben dem Feldtyp entsprechen. Darüberhinaus können für jedes Feld die folgenden Eigenschaften angegeben werden, mit denen der Inhalt des Feldes überprüft wird:

``required``
  Als Werte sind hier ``True`` und ``False`` zulässig um den Wert eines Feldes
  als erforderlich oder optional zu kennzeichnen.
``min`` und ``max``
  wird verwendet für Felder vom Typ

  - ``Int``
  - ``Float``
  - ``Datetime``
  - ``Date``
  - ``Timedelta``

  Hiermit lassen sich die zulässigen Mindest- und Höchstwerte definieren.

``min_length`` und ``max_length``
  kann für folgende Felder angegeben werden:

  - Kollektionen

    - ``Tuple``
    - ``List``
    - ``Set``
    - ``Frozenset``
    - ``Dict``

  - Textfelder

    - ``Bytes``
    - ``BytesLine``
    - ``ASCII``
    - ``ASCIILine``
    - ``Text``
    - ``TextLine``

Bedingungen (Constraints)
=========================

Eine Constraint-Funktion sollte als Argument den Wert des Feldes erhalten und als Ergebnis ``True`` oder ``False`` liefern. Dabei sind Constraints zwar einfach zu schreiben, sie geben jedoch selten eine nutzerfreundliche Fehlermeldung aus. Mit ``z3c.form``-Error-View-Snippets lassen sich diese Fehlermeldungen jedoch anpassen. Weitere Informationen erhalten Sie in `Customizing Error Messages`_.

.. _`Customizing Error Messages`: http://packages.python.org/z3c.form/error.html#customizing-error-messages

Invarianten
===========

Während Constraints immer nur ein einzelnes Feld überprüfen können, lassen sich mit Invarianten mehrere Felder abgleichen.

Ein Beispiel hierfür ist der Vergleich von Start- und Enddatum::

 from zope.interface import invariant, Invalid

 class StartBeforeEnd(Invalid):
     __doc__ = _(u"The start or end date is invalid")

 class IRegistration(form.Schema):
     …
     start = schema.Datetime(
             title=_(u"Start date"),
             required=False,
         )

     end = schema.Datetime(
             title=_(u"End date"),
             required=False,
         )
     …
     @invariant
     def validateStartEnd(data):
         if data.start is not None and data.end is not None:
             if data.start > data.end:
                 raise StartBeforeEnd(_(u"The start date must be before the end date."))

 class StartBeforeEnd(Invalid):
     __doc__ = _(u"The start or end date is invalid")

Formular-Validatoren
====================

Mächtigere Validatoren können mit den ``z3c.form``-Widget-Validatoren geschrieben werden. Weitere Informationen hierzu erhalten Sie in der `z3c.form-Dokumentation`_.

.. _`z3c.form-Dokumentation`: http://packages.python.org/z3c.form/validator.html

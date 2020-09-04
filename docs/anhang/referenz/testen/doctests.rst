========
DocTests
========

DocTests bieten eine interessante Möglichkeit, um Python-Code zu testen indem die Geschichte einer Methode oder Klasse erzählt wird.
In Zope 3 sind DocTests weit verbreitet und werden oft für Unit Tests verwendet. Zudem sind DocTests oft eine gute Möglichkeit, gleichzeitig Dokumentationen und Tests zu schreiben.

Meist werden DocTests in eine einzige Datei geschrieben. Dabei ist jedoch zu beachten, dass nicht strikt zwischen den einzelnen Schritten getrennt wird und daher keine sauberen Unit Tests durchgeführt werden. Alternativ kann auch für jede Methode oder Klasse ein DocTest in deren docstring geschrieben werden. Die Syntax der DocTests ist zwar identisch, aber jeder docstring wird als eigene *Test Fixture* durchgeführt, die eine saubere Trennung der Tests erlaubt.

Hier nun ein einfaches Beispiel aus ``/Products/CMFPlone/PloneTool.py``::

 def normalizeString(self, text, relaxed=False):
     """Normalizes a title to an id.

     normalizeString() converts a whole string to a normalized form that
     should be safe to use as in a url, as a css id, etc.

     If relaxed=True, only those characters that are illegal as URLs and
     leading or trailing whitespace is stripped.

     >>> ptool = self.portal.plone_utils

     >>> ptool.normalizeString("Foo bar")
     'foo-bar'

     ...

     """
     return utils.normalizeString(text, context=self, relaxed=relaxed)

Dabei ist zu beachten, dass der docstring der Methode sowohl den einfachen Text enthält, der beschreibt, was die Methode tut, als auch Python-Statements, wie man sie aus einem interaktiven Python-Interpreter kennt.

Und tatsächlich führt der *DocTest Runner* jede Zeile, die mit ``>>>`` beginnt, im Python-Interpreter aus. Folgt diesem Statement eine Zeile, die genausoweit eingerückt ist, nicht leer ist und nicht mit ``>>>`` beginnt, so wird dies als Ergebnis des Statements erwartet. Stimmen sie nicht überein, gibt doctest eine Fehlermeldung aus.

Hinweis 1
 Wird kein Ausgabewert angegeben, wird von der Methode keine Ausgabe erwartet. Gibt die Methode dennoch etwas aus, wirft doctest eine Fehlermeldung aus.
Hinweis 2
 ``...`` bedeutet »beliebig viele Zeichen«. Dies ist sinnvoll für Werte, die nicht vorhergesagt werden können wie automatisch generierte IDs, die auf dem aktuellen Datum oder zufälligen Zahlen beruhen.

Testen mit DocTest
==================

`DocTests`_ sind ein Feature von Python 2 und daher kann Python’s ``unittest``-Library für einfache Doctests verwendet werden. Zope 3 erweitert die Funktionalität noch um das ``zope.testing``-Modul::

    import unittest
    from zope.testing import doctest

    def test_suite():
        return unittest.TestSuite((
            doctest.DocFileSuite('README.txt'),
            ))

    if __name__ == '__main__':
        unittest.main(defaultTest='test_suite')

.. _`DocTests`: http://docs.python.org/lib/module-doctest.html

Wird die Datei z.B. als ``test_doctests.py`` im ``tests``-Verzeichnis Ihres Produkts gespeichert, kann es mit den üblichen Aufrufen gestartet werden. Wenn Sie sich Zope3-DocTests anschauen, können Sie häufig feststellen, dass in den ersten Zeilen die Komponentenarchitektur oder einzelne Komponenten explizit geladen werden.

Um die Testumgebung für DocTests anzugeben, können Sie z.B. folgendes eingeben::

 import unittest
 import doctest

 from zope.testing import doctestunit
 from zope.component import testing, eventtesting

 from Testing import ZopeTestCase as ztc

 from vs.registration.tests import base

 def test_suite():
     return unittest.TestSuite([

         # Demonstrate the main content types
         ztc.ZopeDocFileSuite(
             'README.txt', package='vs.registration',
             test_class=base.RegistrationFunctionalTestCase,
             optionflags=doctest.REPORT_ONLY_FIRST_FAILURE | doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS),

         ])

 if __name__ == '__main__':
     unittest.main(defaultTest='test_suite')

Dieser Test ist aus ``vs.registration/tests/test_doctest.py`` entnommen. Er führt dabei die  ``README.txt``-Datei aus ``vs.registration/vs/registration/`` aus.

Hinweis 3
 Mit diesem Setup referenziert die Variable ``self`` auf eine PloneTestCase-Instanz. Demzufolge können Sie z.B. folgendes angeben::

   >>> self.portal.invokeFactory('Registration', 'my-first-registration')

 um ein Dokument im Wurzelverzeichnis Ihrer Site anzulegen. Auch alle anderen Methoden aus PloneTestCase und ZopeTestCase sollten innerhalb von DocTests laufen.

Hinweis 4
 In ``optionflags`` lassen sich Optionen und Anweisungen für ``docteststs`` angeben, u.a.:

 ``doctest.NORMALIZE_WHITESPACE``
  Wenn angegeben, werden alle Abfolgen von Leerzeichen und/oder Zeilenumbrüchen als gleich betrachtet.

 ``doctest.ELLIPSIS``
  Wenn angegeben, kann eine Ellipse ``...`` in der erwarteten Ausgabe auf jede beliebige Zeichenfolge passen.

 ``doctest.REPORT_ONLY_FIRST_FAILURE``
  Wenn angegeben, wird der erste fehlgeschlagene Test angezeigt, nicht jedoch der Ausgang der weiteren Tests. Hiermit wird verhindert, dass ``doctest`` fehlgeschlagene Tests aufgrund von vorangehend gescheiterten Tests ausgibt.

 Eine vollständige Übersicht über alle Optionen finden Sie in `Option Flags and Directives`_

DocTest Tipps & Tricks
======================

Dokumentation von DocTest lesen
 Das DocTest-Modul kommt mit einer umfangreichen `Dokumentation`_.
Ein Test ist eine Reihe von Python-Statements.
 Sie können z.B. auf Hilfsmethoden in Ihrem Produkt verweisen, angenommen Ihr Produkt enthält die Methode ``reset(self)`` in ``my.package.tests.utils``, so kann diese Methode mit DocTest aufgerufen werden::

  >>> from my.package.tests.utils import reset
  >>> reset()

Die Testsuite kann zusätzliche Funktionen einführen
 Möchten Sie z.B. ein Produkt in obigem Beispiel verfügbar machen, müssen Sie nur ``ZopeTestCase.installProduct()`` in der testsuit-Datei Ihres Produkts aufrufen.

Debugging
 Wenn Sie ``import pdb; pdb.set_trace()`` in Ihren DocTest einfügen, können Sie zwar nicht schrittweise durch Ihren Kode gehen, aber Variablen und der Status der *Test Fixture* kann mit ``print`` ausgegeben werden.

 Dabei sollten Sie jedoch beachten, dass sich ``locals`` auf Interna von ``doctest`` bezieht::

  (Pdb) locals()
  {'__return__': None, 'self': <zope.testing.doctest._OutputRedirectingPdb instance at 0x5a7c8f0>}

 Das gewohnte Verhalten von ``pdb`` erhalten Sie indem Sie im Stack eine Ebene nach oben gehen::

  (Pdb) up
  > /Users/veit/vs_buildout/src/Products.PloneGetPaid/Products/PloneGetPaid/notifications.py(22)__call__()
  -> import pdb ; pdb.seT_trace()
  (Pdb) locals()
  {'settings': <Products.PloneGetPaid.preferences.StoreSettings object at 0x5f631b0>, 'store_url': 'http://nohost/plone', 'self': <Products.PloneGetPaid.notifications.MerchantOrderNotificationMessage object at 0x56c30d0>, 'order_contents': u'11 pz @84.00 total: US$924.00\n22 ph @59.00 total: US$1298.00\n12 pf @98.00 total: US$1176.00\n23 pX @95.00 total: US$2185.00\n3 pM @89.00 total: US$267.00\n22 po @60.00 total: US$1320.00\n23 pj @39.00 total: US$897.00\n15 po @34.00 total: US$510.00\n5 pS @76.00 total: US$380.00\n1 pm @70.00 total: US$70.00', 'template': u'To: ${to_email}\nFrom: "${from_name}" <${from_email}>\nSubject: New Order Notification\n\nA New Order has been created\n\nTotal Cost: ${total_price}\n\nTo continue processing the order follow this link:\n${store_url}/@@admin-manage-order/${order_id}/@@admin\n\nOrder Contents\n\n${order_contents}\n\nShipping Cost: ${shipping_cost}\n\n', 'pdb': <module 'pdb' from '/Users/moo/code/python-macosx/parts/opt/lib/python2.4/pdb.pyc'>}
  (Pdb)

 Weitere Informationen zum Debugging erhalten Sie in der `Python Dokumentation`_.

 `Interlude <https://pypi.python.org/pypi/interlude>`_ erlaubt die Verwendung einer interaktiven Shell innerhalb von Doctests, wobei die oben beschriebene Besonderheit nicht auftritt::

  >>> from interlude import interact
  >>> interact(locals())

 Wenn der ``testrunner`` nun ``interact`` durchläuft, erhalten Sie eine interaktive Python-Konsole.

Exceptions (Ausnahmen) ausgeben
 Folgender Code gibt Exceptions aus::

  >>> try:
  ...     someOperation()
  ... except:
  ...     import pdb; pdb.set_trace()
  >>> # continue as normal

.. _`Dokumentation`: http://docs.python.org/lib/module-doctest.html
.. _`Option Flags and Directives`: http://docs.python.org/library/doctest.html#doctest-options
.. _`Python Dokumentation`: http://docs.python.org/library/doctest.html#debugging

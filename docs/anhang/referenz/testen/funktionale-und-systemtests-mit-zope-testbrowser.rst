================================================
Funktionale und Systemtests mit zope.testbrowser
================================================

Während unit tests und DocTests die Gültigkeit von einzelnen Methoden und
Modulen überprüfen, überprüfen funktionale Tests die Anwendungen als Ganzes.
Häufig nehmen sie dabei die Sicht des Nutzers ein und üblicherweise orientieren
sie sich an den Nutzungsfällen (Use cases) der Anwendung. Systemtests hingegen
testen die Anwendung als Blackbox.

Mit Zope 3 kommt die Bibliothek ``zope.testbrowser``, die es ermöglicht,
DocTests zu schreiben, die sich wie ein Webbrowser verhalten. Sie können URLs
öffnen, Links anklicken, Formularfelder ausfüllen und abschicken und dann die
zurückgelieferten HTTP headers, URLs und Seiteninhalte überprüfen.

.. note::
   Da der ``testbrowser`` momentan kein JavaScript unterstützt, empfiehlt sich
   zum Testen dynamischer User Interfaces `selenium
   <https://selenium.dev/>`_. Selenium wird auch vom
   `Robot Test Automatisation Framework <http://robotframework.org/>`_
   verwendet.

Funktionale Tests sind kein Ersatz für Unit tests sondern überprüfen den
funktionalen Ablauf, wie ihn der Nutzer wahrnimmt. Ein funktionaler Test
überprüft z.B., ob ein Delete-Button vorhanden ist und wie erwartet
funktioniert. Um die Tests überschaubar zu halten, wird meist nur überprüft, ob
die entsprechenden Templates vorhanden sind und für Nutzer mit verschiedenen
Rollen und Rechten wie erwartet funktioniert.

Im folgenden nun ein Auszug aus einem ``zope.testbrowser``-Test aus
``vs.registration``::

    Setting up and logging in
    -------------------------

        >>> from Products.Five.testbrowser import Browser
        >>> browser = Browser()
        >>> portal_url = self.portal.absolute_url()
        [...
        >>> from Products.PloneTestCase.setup import portal_owner, default_password

        >>> browser.open(portal_url + '/login_form?came_from=' + portal_url)
        >>> browser.getControl(name='__ac_name').value = portal_owner
        >>> browser.getControl(name='__ac_password').value = default_password
        >>> browser.getControl(name='submit').click()

``zope.testbrowser`` wird verwendet um die Interaktion mit einem Browser zu
simulieren. Dies sind keine reinen funktionalen Tests, da auch der Zustand der
ZODB überprüft und verändert wird.

Anschließend meldet sich der Test als Eigentümer des Portals im ``login_form``-
Formular an.

Alle Aktionen finden im ``browser``-Objekt statt. Dies simuliert einen
Webbrowser mit einer Schnittstelle zum Finden und Ausführen von Form controls
und Links. Mit den Variablen ``browser.url`` und ``browser.contents`` lassen
sich sowohl die URL als auch die Inhalte überprüfen. ``zope.testbrowser`` bietet
eine umfangreiche Dokumentation in seiner `README.txt
<http://svn.zope.org/Zope3/trunk/src/zope/testbrowser/README.txt?view=auto>`-Datei. Die bedeutendsten Methoden des `IBrowser interface
<https://github.com/zopefoundation/zope.testbrowser/blob/master/src/zope/testbrowser/interfaces.py>`_ sind:

``open(url)``
    öffnet eine gegebene URL.
``reload()``
    lädt die aktuelle Seite erneut.
``goBack(count=1)``
    simuliert, wie häufig der zurück-Button gedrückt wird.
``getLink(text=None, url=None, id=None)``
    sucht nach einen Link entweder mit dem in ``<a>``-Tags angegebenen Inhalt,
    der URL im ``href``-Attribut oder der ID des Links.

    Mit ``click()`` kann dieser Link ausgeführt werden.

``getControl(label=None, name=None, index=None)``
    gibt den inhalt eines Formularfeldes aus, das entweder durch sein Label oder
    seinen Namen gefunden wird. Das ``index``-Argument wird verwendet, wenn
    mehrere form controls vorliegen (``index=0`` ist z.B. die erste form
    control).

    Und auch hier kann mit ``click()`` das Klicken auf das Kontroll-Objekt
    ausgeführt werden.

Das IBrowser-Interface bietet einige Eigenschaften (Properties), die zum
Abfragen des Zustands der aktuellen Seite verwendet werden können:

``url``
    die vollständige URL der aktuellen Seite.
``contents``
    Den vollständigen Inhalt der aktuellen Seite als string (normalerweise mit
    HTML-Tags).
``headers``
    die HTTP headers.

Detailliertere Angaben zu weiteren Methoden, Attributen, Schnittstellen und
Beispielen für die verschiedenen Arten von Links und Controls erhalten Sie in `Interfaces
<https://github.com/zopefoundation/zope.testbrowser/blob/master/src/zope/testbrowser/interfaces.py>`_
und der README.txt-Datei.

Funktionale Tests ablaufen lassen
=================================

Da ein Test mit dem ``testbrowser`` ein normaler DocTest ist, kann er mit
üblichem testrunner und Testsuite-Setup laufen.

.. note::
   Die Site mit dem ``zope.testbrowser`` aufzusetzen wäre unnötig kompliziert,
   zumal damit nur Plone getestet würde und nicht ``vs.registration``.

Funktionale Tests debuggen
==========================

Wenn der ``testbrowser`` zu einer Zope-Fehlermeldung führt, kann es schwierig
werden, die Ursache zu ermitteln. Zwei Änderungen vereinfachen dies deutlich.

Zunächst sollten Sie sicherstellen, dass die Fehler auch angezeigt werden::

    >>> browser.handleErrors = False

Damit werdenIhnen die vollständigen Zope-Exceptions angezeigt.

Und wenn PloneTestCase verwendet wird, kann auch Plone’s Error log verwendet
werden::

    >>> self.portal.error_log._ignored_exceptions = ()

Damit werden Fehler wie *NotFound* und *Unauthorized* im Error log angezeigt werden. Zudem kann es sinnvoll sein, *Verbose Security* zu aktivieren.

Anschließend kann statt einer Zeile, die zu einem Fehler führte, z.B. folgender Kode eingegeben werden::

    >>> try:
    ...     browser.getControl('Save').click()
    ... except:
    ...     print self.portal.error_log.getLogEntries()[0]['tb_text']
    ...     import pdb; pdb.set_trace()
    >>> # continue as normal

Damit wird der letzte Eintrag in das Error log ausgegeben und ein PDB break
point gestzt.

Funktionale Tests vs. Systemtests
=================================

Ein Systemtest überprüft ein System als sog. Blackbox. Ein funktionaler Test
konzentriert sich auf die geforderten Funktionsabläufe, die meist in
Nutzungsfällen (Use Cases) beschrieben sind.

Für einen funktionalen Test mag es akzeptabel sein, Annahmen auf einem
festgelegten Status einer Site, der Testsuite, zu machen. Der Systemtest macht
hingegen keine solchen Annahmen. Daher benötigt ein ``zope.testbrowser``-Test
idealerweise nicht das PloneTestCase-Test fixture::


    import unittest
    from zope.testing import doctest

    def test_suite():
        return unittest.TestSuite((
            doctest.DocFileSuite('TestSystem.txt'),
            ))

    if __name__ == '__main__':
        unittest.main(defaultTest='test_suite')

Abgesehen davon bleiben die verwendeten Methoden für einen Systemtest dieselben.

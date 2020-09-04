========================
Einführung in Unit tests
========================

Unit Tests sind kleine, sich selbst enthaltende Testmethoden, die unabhängig von anderen Methoden ausgeführt werden und sich nicht gegenseitig beeinflussen.

Folgende Regeln für unit tests sind zu beachten:

- Schreiben Sie mindestens einen Test für jede Methode.
- Schreiben Sie zunächst die Interface- und/oder stub-Methoden, dann die Tests. Vergewissern Sie sich, dass die Tests nicht bestanden werden (da der Code ja noch nicht geschrieben ist).
- Erst jetzt sollte das neue Feature implementiert werden mit dem Ziel, den Test zu bestehen.
- Wenn Sie nach einem Release einen Bug entdecken, beheben Sie ihn nicht einfach, sondern

  - schreiben Sie zunächst einen Test, der den Fehler demonstriert,
  - dann erst beseitigen Sie den Bug.

Unit tests erlauben Ihnen,

- Ihre Software auch in entfernten Umgebungen überprüfen zu können;
- beim Implementieren neuer Features nicht bereits bestehende zu kompromitieren;
- bereits behobene Bugs nicht wieder einzuführen;
- Zeit bei der Entwicklung einzusparen, da die Chancen fehlerhaften Code schnell zu erkennen, deutlich steigen;
- Code schreiben und testen in derselben Umgebung auszuführen;
- die Test-Abdeckung immer weiter zu erhöhen.

Unit Tests in Zope und Plone
============================

Unit Tests im Zope-2/Plone-Kontext basieren meist auf `ZopeTestCase`, der das `Python unittest-Modul`_ verwendet. Dabei laufen die Unit Tests meistens in einer *Sandbox* (auch *Test-Fixture* genannt) ab.

`PloneTestCase` basiert auf `ZopeTestCase`, ist jedoch eher ein Integrationstest, der die Integration Ihrer und der zugrundeliegenden Komponenten wie ZODB und ZPublisher überprüft. `PloneTestCase` erstellt eine leere Zope-Instanz mit einer einzelnen Plone Site, einem Nutzer und dem Standard Mitglieder-Ordner. Ist der Test beendet, wird die Transaktion abgebrochen, so dass keine der durch den Test vorgenommenen Änderungen der Plone-Site erhalten bleibt.

Links
=====

- `Dive Into Python, Chapter on Unit Testing`_
- `PyUnit Documentation`_
- `How to run Zope Unit Tests`_
- `ZopeTestCase ZopeTestCaseWiki`_
- `Plone Testing Tutorial`_

Produkte
--------

- `ZopeTestCase`_
- `CMFTestCase`_
- `PloneTestCase`_

.. _`Python unittest-Modul`: http://docs.python.org/lib/module-unittest.html
.. _`Dive Into Python, Chapter on Unit Testing`: https://diveintopython3.problemsolving.io/unit-testing.html
.. _`PyUnit Documentation`: http://docs.python.org/library/unittest.html
.. _`How to run Zope Unit Tests`: http://wiki.zope.org/zope2/HowToRunZopeUnitTests
.. _`ZopeTestCase ZopeTestCaseWiki`: http://www.zope.org/Members/shh/ZopeTestCaseWiki/ZopeTestCaseWiki
.. _`Plone Testing Tutorial`: http://plone.org/documentation/tutorial/testing
.. _`ZopeTestCase`: http://wiki.zope.org/zope2/ZopeTestCase
.. _`CMFTestCase`: https://pypi.python.org/pypi/Products.CMFTestCase
.. _`PloneTestCase`: https://pypi.python.org/pypi/Products.PloneTestCase/

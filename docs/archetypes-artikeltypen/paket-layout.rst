Paket-Layout
============

Der neue Artikeltyp soll als neues Paket erstellt werden. Entsprechend unserer Anforderung nennen wir es ``vs.registration``. Um dieses Paket zu erstellen verwenden wir wieder PasteScript::

 $ cd src
 $ ../bin/zopeskel archetype vs.registration

Antworten Sie dabei auf die Frage *Are you creating a Zope 2 Product?* mit *True*.

Anschließend informieren wir die Buildout-Umgebung von unserem neuen Paket. Hierzu ändern wir ``buildout.cfg``::

 [buildout]
 ...
 develop
     src/vs.policy
     src/vs.theme
     src/vs.registration
 ...
 eggs =
     elementtree
     vs.policy
     vs.theme
     vs.registration
 ...

Nun wird das Buildout-Skript erneut aufgerufen::

 $ ./bin/buildout -o

Entgegen dem Policy-Produkt fügen wir keinen neuen *zcml-slug* hinzu, sondern definieren es als Abhängigkeit in ``vs.policy``. Deshalb fügen wir in ``vs.policy/configure.zcml`` folgendes hinzu::

 <configure
     xmlns="http://namespaces.zope.org/zope"
     xmlns:five="http://namespaces.zope.org/five"
     xmlns:genericsetup="http://namespaces.zope.org/genericsetup"
     i18n_domain="vs.policy">

     <include package="vs.registration" />
     ...
 </configure>

.. In diesem Kapitel werden nun nicht mehr alle Code-Schnipsel explizit beschrieben. Sie können sich jedoch die für das Buildout-Projekt relevanten Dateien, wie es am Ende dieses Kapitels aussehen sollte, hier herunterladen: `artikeltypen.tgz`_ Das Layout des fertiggestellten Pakets mit seinen Dateien und Verzeichnissen entspricht den üblichen Konventionen:

.. ``__init__.py``
 Initialisiert das Zope2-Produkt.

.. ``browser/``
 Enthält die Zope3-Views, Page Templates und Icons für jeden Artikeltyp. Zudem ist hier auch die CSS-Datei für die Artikeltypen zu finden.

.. ``config.py``
 enthält globale Konstanten wie *project name* und die Namen der verschiedenen Berechtigungen.

.. ``configure.zcml``
 registriert die Komponenten. ``browser``, ``content`` und
.. ``portlets`` haben ihre eigenen ``configure.zcml``-Dateien, die hier eingeschlossen werden.

.. ``content/``
 enthält die Definitionen der Artikeltypen. Einige Typen hängen von zusätzlichen Adaptern und Event-Handlern ab, die ebenfalls in diesem Verzeichnis zu finden sind.

.. ``interface.py``
 enthält die Interfaces, die die jeweiligen Artikeltypen und ihre Komponenten beschreibt.

.. ``portlets/``
 enthält die Definitionen und Registrierungen von Portlets (s.a. ``plone.qpp.portlets.portlets``).

.. ``profiles/``
 enthält das Extension-Profil des Generic Setup Tools.

.. ``README.txt``
 beschreibt das Paket in Form eines Doctests, das die Artikeltypen und ihre Funktionalitäten untersucht.

.. ``tests/``
 enthält die Testsuite.

.. ``version.txt``
 Versionsnummer, die von Plone ausgelesen wird.

.. _`artikeltypen.tgz`: artikeltypen.tgz

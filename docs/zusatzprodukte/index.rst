==============
Zusatzprodukte
==============

Finden, evaluieren und installieren von Zusatzprodukten.

Finden
======

.. Die meisten Zusatzprodukte für Plone sind im *Products*-Abschnitt auf der Plone-
   Website aufgeführt: http://plone.org/products. Dabei kann für jedes Produkt
   angegeben werden, zu welchen Plone-Versionen sie kompatibel sind. Darüberhinaus
   können noch weitere Angaben gemacht werden wie Dokumentation, Issue tracker und
   Roadmap.

   Viele dieser Produkte und auch einige weitere sind im *Collective*-Subversion-
   Repository unter ``http://svn.plone.org/svn/collective`` zu finden. Dieses
   Repository kann auch mit einem Web-Browser unter der Adresse
   http://dev.plone.org/collective/browser durchsucht werden.

Die meisten Produkte befinden sich mittlerweile auf Github: https://github.com/collective.

.. Eine Liste von Plone-Paketen nach Kategorien unterteilt erhalten Sie auch auf
   der `OpenComparison <http://plone.opencomparison.org/>`_-Site.

Evaluieren
==========

Um nun zu überprüfen, ob das Produkt wirklich passend ist, können Sie
verschiedene Schritte durchführen:

#. Zunächst sollten Sie überprüfen, wie sich das Produkt selbst präsentiert:

   - Ist es hinreichend gut dokumentiert?
   - Gibt es einen Bug Tracker?

     Wie viele offene und geschlossene Bugs gibt es?

     Wie schnell wurden die Bugs behoben?

   - In welcher Version liegt das Produkt vor?

     Eine 0.* oder alpha-Version ist voraussichtlich weniger stabil als ein
     *final release*.

   - Gibt es eine Roadmap?

     Sie gibt Ihnen Hinweise, wie die Planung für die weitere Entwicklung
     aussieht und wie zukunftssicher das Produkt ist.

#. Wie umfangreich und mit welchen Erfahrungen wird das Produkt eingesetzt?

   Fragen Sie in einer Mailingliste nach, welche Erfahrungen mit dem Produkt
   gemacht wurden.

#. Dann sollten Sie das Produkt ausführlich in einer Testumgebung testen.

   - Kopieren Sie gegebenenfalls die ZODB aus Ihrem Produktivsystem in Ihr
     Testsystem.

     Achten Sie darauf, dass die Buildout-Konfigurationen beider Systeme
     identisch sind.

   - Wie hoch ist die Testabdeckung des Produkts?

     In `Testabdeckung (Code Coverage) <testabdeckung-code-coverage>`_ erhalten
     Sie weitergehende Informationen.

   - Durchlaufen Sie die automatisierten Tests sowohl Ihrer eigenen als auch des
     neuen Produkts.
   - Schließlich sollten Sie die Funktionalität und das User Interface auch in
     Ihrem Browser testen.

Allgemeinere und umfassendere Informationen zur Evaluation von OpenSource-
Software erhalten Sie im Artikel `Software-Evaluation
<http://www.veit-schiele.de/profil/artikel/software-evaluierung/software-evaluierung>`_.

Installation und Aktivierung
============================

#. Zusatzprodukte können unter ``install_requires`` in der setup.py``-Datei
   angegeben werden, also z.B.::

    install_requires=[
        'setuptools',
        'Plone',
        'vs.event',
    ],

#. Anschließend wird das Zusatzprodukt noch in der Instanz registriert in der
   ``configure.zcml``-Datei::

    <configure
        xmlns="http://namespaces.zope.org/zope"
        xmlns:five="http://namespaces.zope.org/five"
        xmlns:i18n="http://namespaces.zope.org/i18n"
        xmlns:genericsetup="http://namespaces.zope.org/genericsetup"
        i18n_domain="vs.policy">
        <includeDependencies package="." />
        …
    </configure>

   ``<includeDependencies package="." />``
    fügt alle Pakete der ``install_requires``-Liste einer Site hinzu.

   Sollen die Pakete explizit angegeben werden, kann dies z.B. erfolgen mit::

    <include package="vs.event" />

#. Damit unser Zusatzprodukt beim Aufsetzen einer neuen Plone-Site mit unserem
   ``vs.policy``-Produkt automatisch aktiviert wird, sollten wir es noch in der
   ``metadata.xml``-Datei eintragen::

    <?xml version="1.0"?>
    <metadata>
      <version>1.0</version>
      <dependencies>
        <dependency>profile-vs.event:default</dependency>
      </dependencies>
    </metadata>

#. Schließlich sollten diese Änderungen noch in unserem Buildout-Projekt
   übernommen werden. Hierzu wird das Buildout-Skript erneut aufgerufen::

    $ bin/buildout

Tests
=====

#. Zunächst müssen wir sicherstellen, dass ``vs.event´´ in unseren Tests zur
   Verfügung steht::

    class VsPolicy(PloneSandboxLayer):
        defaultBases = (PLONE_FIXTURE,)
        def setUpZope(self, app, configurationContext):
            # Load ZCML
            import vs.policy
            xmlconfig.file(
                'configure.zcml',
                vs.policy,
                context=configurationContext
            )
            # Install products that use an old-style initialize()
            # function
            z2.installProduct(app, 'vs.event')

    def tearDownZope(self, app):
        # Uninstall products installed above
        z2.uninstallProduct(app, 'vs.event')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'vs.policy:default')

#. Nun fügen wir den eigentlichen Test hinzu::

    def test_vs_event_installed(self):
        portal = self.layer['portal']
        portal_types = getToolByName(portal, 'portal_types')
        self.assertTrue("VSEvent" in portal_types)

#. Schließlich führen wir diesen Test aus::

    $ ./bin/test

.. toctree::
    :titlesonly:
    :maxdepth: 0
    :hidden:

    haeufig-verwendete-zusatzprodukte
    linguaplone

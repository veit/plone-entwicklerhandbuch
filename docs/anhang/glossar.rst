=======
Glossar
=======

.. glossary::

    Acquisition
        Acquisition ist ein Mechanismus, der es Objekten erlaubt, Attribute aus ihrer Umgebung zu erhalten. Eine ausführliche Beschreibung, wie in Zope Acquisition verwendet werden kann, finden Sie im Zope Book.

    Adapter
        In der `Zope Component Architecture (ZCA) <zope-component-architecture>`_ sind Adapter Komponenten, die aus anderen Komponenten erstellt werden um sie einem bestimmten Interface zur Verfügung zu stellen::

         >>> class IPerson(interface.Interface):
         ...     name = interface.Attribute("Name")
         >>> class PersonGreeter:
         ...
         ...     component.adapts(IPerson)
         ...     interface.implements(IGreeter)
         ...
         ...     def __init__(self, person):
         ...         self.person = person
         ...
         ...     def greet(self):
         ...         print "Hello", self.person.name

        Die Klasse definiert einen Constructor, der ein Argument für jedes adaptierte Objekt nimmt.

        ``component.adapts``
         deklariert, was angepasst werden soll.
        ``adaptedBy``
         gibt eine Liste der Objekte aus, die adaptiert werden::

          >>> list(component.adaptedBy(PersonGreeter)) == [IPerson]
          True

        ``provideAdapter``
         Sofern nur ein Interface angeboten wird, kann dieses einfach bereitgestellt
         werden mit::

          >>> component.provideAdapter(PersonGreeter)

         Ebenso können spezifische Argumente zum Registrieren eines Adapters angegeben werden::

          >>> class VeitPersonGreeter(PersonGreeter):
          ...     name = 'Veit'
          ...     def greet(self):
          ...         print "Hello", self.person.name, "my name is", self.name
          >>> component.provideAdapter(
          ...                        VeitPersonGreeter, [IPerson], IGreeter, 'veit')


         oder als *keyword arguments*::

          >>> class ChrisPersonGreeter(VeitPersonGreeter):
          ...     name = "Chris"
          >>> component.provideAdapter(
          ...     factory=ChrisPersonGreeter, adapts=[IPerson],
          ...     provides=IGreeter, name='chris')

        ``queryAdapter`` oder ``getAdapter``
         kann für For *named adapters* verwendet werden::

          >>> component.queryAdapter(Person("Chris"), IGreeter, 'veit').greet()
          Hello Chris my name is Veit
          >>> component.getAdapter(Person("Chris"), IGreeter, 'veit').greet()
          Hello Chris my name is Veit

         Falls kein Adapter vorhanden ist, gibt ``queryAdapter`` einen Standardwert zurück wohingegen ``getAdapter`` eine Fehlermeldung ausgibt::

          >>> component.queryAdapter(Person("Chris"), IGreeter, 'daniel')
          >>> component.getAdapter(Person("Chris"), IGreeter, 'daniel')
          ... # doctest: +ELLIPSIS
          Traceback (most recent call last):
          ...
          ComponentLookupError: (...Person...>, <...IGreeter>, 'daniel')

        ``queryMultiAdapter`` oder ``getMultiAdapter``
         gibt die Adapter mehrerer Objekte zurück.

         Wenn wir z.B. einen Adapter mit mehreren Objekten erstellen::

          >>> class TwoPersonGreeter:
          ...
          ...     component.adapts(IPerson, IPerson)
          ...     interface.implements(IGreeter)
          ...
          ...     def __init__(self, person, greeter):
          ...         self.person = person
          ...         self.greeter = greeter
          ...
          ...     def greet(self):
          ...         print "Hello", self.person.name
          ...         print "my name is", self.greeter.name


         können wir diesen Multi-Adapter anfragen mit ``queryMultiAdapter`` oder
         ``getMultiAdapter``::

          >>> component.queryMultiAdapter((Person("Chris"), Person("Veit")),
          ...                                  IGreeter).greet()
          Hello Chris
          my name is Veit

    AJAX
        Asynchronous JavaScript and XML.

    API
        Application Programming Interface.

        Schnittstelle, die Funktionen eines Programms zugänglich macht.

    Archetypes
        Archetypes ist ein Framework um neue Artikeltypen in Plone aus Schemadefinitionen zu erstellen. Die Seiten zur Ansicht und zum Editieren lassen sich dabei automatisch generieren.

    ATCT
        Mit Archetypes geschriebene Artikeltypen, die zusammen mit Plone ausgeliefert werden.

    Browserlayer
        Browserlayer vereinfachen die Registrierung visueller Elemente wie Views, Viewlets etc. sodass diese Elemente nur in den Sites erscheinen, in denen sie explizit installiert wurden.

        Verwendung
        ==========

        #. Zunächst wird ein Marker-Interface z.B. in ``vs.theme/vs/theme/browser/interfaces.py`` erstellt::

            from plone.theme.interfaces import IDefaultPloneLayer

            class IThemeSpecific(IDefaultPloneLayer):
                """Marker interface that defines a Zope 3 browser layer.
                   If you need to register a viewlet only for the
                   "vs.theme" theme, this interface must be its layer.
                """

        #. Anschließend kann dieses Marker-Interface regsitriert werden in ``vs.theme/vs/theme/profiles/default/browserlayer.xml``, z.B.::

            <layers>
                <layer name="vs.theme"
                       interface="vs.theme.interfaces.IThemeSpecific" />
            </layers>

        #. Schließlich können visuelle Komponenten für diesen Browserlayer registriert werden in ``vs.theme/vs/theme/browser/configure.zcml``, z.B.::

            <browser:page
                for="Products.CMFCore.interfaces.ISiteRoot"
                name="dashboard"
                permission="plone.app.portlets.ManageOwnPortlets"
                class="plone.app.layout.dashboard.dashboard.DashboardView"
                template="templates/dashboard.pt"
                layer=".interfaces.IThemeSpecific"
                />

    Buildout
        `Buildout <https://pypi.python.org/pypi/zc.buildout/>`_ erlaubt, identische Entwicklungsumgebungen einfach aufzusetzen. Hierzu nutzt buildout die Fähigkeit der `setuptools <http://peak.telecommunity.com/DevCenter/setuptools>`_, automatisch Abhängigkeiten aufzulösen und Aktualisierungen durchzuführen  (s.a.: `Buildout’s documentation <http://www.buildout.org/en/latest/contents.html>`_).

    Catalog
        Der Katalog ist ein interner Index der Inhalte einer Plone-Site. Dabei kann auf den Catalog  auch über das ZMI als ``portal_catalog`` zugegriffen werden.

    Collective
        `Collective`_ ist ein Subversion-Repository für die Plone-Community um Zusatzprodukte bereitzustellen.

        .. _`Collective`: http://dev.plone.org/collective

    CSS
        CSS ist ein Web-Standard zur Darstellung von Inhalten. Der Standard ist beschreiben auf der `W3C-Website`_. Eine Einführung in CSS finden Sie unter

        Siehe auch: `Einführung in Cascading Style Sheets (CSS)`_

        .. _`W3C-Website`: http://www.w3.org/Style/CSS/
        .. _`Einführung in Cascading Style Sheets (CSS)`: http://www.veit-schiele.de/dienstleistungen/schulungen/css/einfuhrung

    Decorator
        Ein sog. Wrapper um eine Python-Funktion oder -Klasse, die die Funktion oder Klasse als sein erstes Argument nimmt und ein beliebiges Objekt zurückgibt. In Plone werden verschiedene Decorator verwendet, so z.B. `memoize`_ zum Caching der Werte von Funktionen und Methoden und `profilehooks`_ für das Erstellen von Profilen einzelner Funktionen

        Sehen Sie auch `PEP 318`_.

        .. _`memoize`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/produktivserver/caching/memoize.html
        .. _`profilehooks`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/produktivserver/profiling.html
        .. _`PEP 318`: http://www.python.org/dev/peps/pep-0318/

    Distribution
        Eine Distribution besteht in Python aus einem Verzeichnis mit einer
        ``setup.py``-Datei und anderen Ressourcen. Die Metaangaben in der
        ``setup.py``-Datei können u.a. die Versionsnummer, Abhängigkeiten und
        Lizenzinformationen enthalten.

        Werkzeuge wie `Setuptools <https://pypi.python.org/pypi/setuptools>`_,
        `Distribute <https://pypi.python.org/pypi/distribute>`_ oder auch `Buildout
        <https://pypi.python.org/pypi/zc.buildout>`_ können die Metainformationen
        verwenden um
        Installationen in verschiedenen Versionen zu erhalten, Abhängigkeiten aufzulösen
        etc.

    DocFinderTab
        `DocFinderTab`_ ist ein Produkt, das alle Klassen und Methoden eines Objekts im Zope Management Interface (ZMI) auflistet.

        .. _`DocFinderTab`: http://www.zope.org/Members/shh/DocFinderTab

    Doctest
        Eine spezielle Syntax zum Schreiben von Tests. Ein Vorteil von Doctests ist,
        dass sie mit dem Test auch gleich die Dokumentation mitliefern. Als Nachteilig
        hat sich herausgestellt, dass nicht eine Untermenge der Doctests durchlaufen
        werden kann. Zudem werden beim Fehlschlagen eines Tests die weiteren Tests nicht
        mehr durchlaufen. Schließlich wird der Code auf eine besondere Weise ausgeführt,
        die schwieriger nachzuvollziehen und zu analysieren sind.

    DTML
        DTML ist eine serverseitige Template-Sprache, mit der sich dynamische Inhalte erstellen lassen. Plone verwendet für die Erstellung von HTML jedoch ZPT, sodass DTML nur noch für nicht XML-konforme Inhalte wie SQL-Anfragen, Mail- und CSS-Generierung verwendet wird.

    Easy Install
        `Easy Install <http://peak.telecommunity.com/DevCenter/EasyInstall>`_ ist ein
        Python-Modul mit dem der `Python Package Index <python-package-index>`_
        durchsucht werden kann und das die Pakete in die globale Python-Umgebung
        installiert. Neben Buildout werden wir nur noch ZopeSkel mit ``easy_install``
        installieren, alle weiteren Eggs werden von Buildout in das lokale
        Buildout-Projekt heruntergeladen, unter anderem um Versionskonflikte zu
        vermeiden.

    Egg
        Ein binäres Distributionsformat, das von den Setuptools und Distribute verwendet wird. Dabei wird ür jede Plattform und jede Python-Version ein spezifisches Egg erstellt.

        Daher können Source-Distributionen, die meist nur ein komprimiertes Archiv des Codes und der Metaangaben sind, flexibler eingesetzt werden. Umgekehrt muss für Paketen, die binäre Abhängigkeiten besitzen (wie z.B. in C geschriebene Erweiterungen) die notwendigen Compiler und Bibliotheken verfügbar sein, um die Source-Distribution installieren zu können.

    Event
        Die `Zope Component Architecture (ZCA) <zope-component-architecture>`_ ermöglicht, *Events* an bestimmte `Handler <handler>`_ zu schicken.

        Events erstellen
        =================

        #. Im Folgenden erstellen wir zwei Beispielklassen, die ``zope.component.event`` für das Dispatching benötigen::

            >>> import zope.component.event

            >>> class Event1(object):
            ...     pass
            >>> class Event2(Event1):
            ...     pass

        #. Anschließend werden zwei *Handler* für diese Event-Klassen erstellt::

            >>> called = []
            >>> import zope.component
            >>> @zope.component.adapter(Event1)
            ... def handler1(event):
            ...     called.append(1)
            >>> @zope.component.adapter(Event2)
            ... def handler2(event):
            ...     called.append(2)

        #. Diese Handler werden nun registriert mit::

            >>> zope.component.provideHandler(handler1)
            >>> zope.component.provideHandler(handler2)

        #. Nun Überprüfen wir, ob die *Handler* auch tatsächlich aufgerufen wurden::

            >>> from zope.event import notify
            >>> notify(Event1())
            >>> called
            [1]
            >>> del called[:]
            >>> notify(Event2())
            >>> called.sort()
            >>> called
            [1, 2]

        .. seealso::
            - `Events <http://pypi.python.org/pypi/zope.component#events>`_
            - `Object events <http://pypi.python.org/pypi/zope.component#object-events>`_

    File descriptor
        Ein *file descriptor* ist ein abstrakter Indikator für den Zugriff auf eine Datei.

        Dabei verwendet ein ZEO-Server für jeden Storage je Client-Verbindung 3 dieser Deskriptoren. Bei einem ZEO-Server mit zehn Storages und 36 ZEO-Clients würden also 10×36×3 *file sescriptors* benötigt. Üblicherweise verwendet der ZEO-Server jedoch nicht die erforderlichen 1080 *file descriptors* sondern nur 1025. Dies führt dann dazu, dass ZEO-Clients mit der Zeit keine Seiten mehr ausliefern und in deren Log-Dateien ``ECONNREFUSED``-Meldungen erscheinen.

        Die Ursache hierfür ist, dass Python üblicherweise kompiliert wird mit einer maximalen Anzahl von 1024 *file descriptors* je Prozess. Dies lässt sich ändern indem in ``/usr/include/bits/typesizes.h`` der Wert für ``define __FD_SETSIZE`` hochgesetzt wird, z.B. auf 2048. Nach einem Neukompilieren von Python kann der ZEO-Server dann auch alle 1080 *file descriptors* verwenden.

        Andreas Gabriel hat ein Skript geschrieben, mit dem sich die maximale Anzahl der Verbindungen testen lässt: `zeo-check-max-connections.py`_

        .. _`zeo-check-max-connections.py`: zeo-check-max-connections.py/view

    Handler
        Handler sind eine spezifische Form von `Subscribern
        <subscriber>`_, die nichts bereitstellen und meistens von
        `Events <event>`_ aufgerufen werden.

        Beim Aufruf eines *Handlers* wird kein Rückgabewert erwartet. Auch bieten *Handler* keine API an. Daher werden *Handler* meist als Funktion und nicht als Klasse implementiert. Zum Beispiel::

         >>> import datetime
         >>> def documentCreated(event):
         ...     event.doc.created = datetime.datetime.utcnow()
         >>> documentCreated = component.adapter(IDocumentCreated)(documentCreated)

        Die letzte Zeile markiert den *Handler* als Adapter von ``IDocumentCreated``-Events. Nun wird der *Handler* noch registriert mit::

         >>> component.provideHandler(documentCreated)

        Schließlich kann die ``handle``-Funktion verwendet werden um *Handlers*, die für einen *Event* registriert sind, aufzurufen::

         >>> component.handle(DocumentCreated(doc))
         >>> doc.created.__class__.__name__
         'datetime'

        .. seealso::
            - `Handlers <http://pypi.python.org/pypi/zope.component#handlers>`_

    i18n
        Präparierung des Quellcodes, sodass er ohne weitere Änderung in verschiedene Sprachen übersetzt werden kann. i18n wird durch den ersten und letzten Buchstaben von *Internationalization* und die Anzahl der dazwischenliegenden Zeichen gebildet.

        Die Übersetzungsarbeit selbst wird dann `l10n`_ genannt.

        .. _`l10n`: l10n

    Integrationstest
        Ein Test, ob eine Komponente mit anderen Komponenten zusammen läuft. Die meisten Tests, die für Plone-Produkte geschrieben werden, sind Integrationstests da das gesamte Plone-Framework benötigt wird, um die gewünschten Testergebnisse zu erhalten. Ein Beispiel für einen Integrationstest ist der Test, ob ein Objekt eines neuen Artikeltyps erstellt werden kann nachdem dieses Produkt in einer Plone-Site installiert wurde.

    Interface
        Zope-Interfaces sind Objekte, die das externe Verhalten desjenigen Objekts
        spezifizieren, das sie bereitstellt. Dies geschieht durch:

        - Informelle Dokumentationen in Doc-Strings.
        - Attribut-Definitionen
        - Invarianten, also Bedingungen für Objekte, die dieses Interface
          bereitstellen.

        Dabei spezifiziert ein Interface die Charakteristiken eines Objekts, sein
        Verhalten und seine Fähigkeiten.

        Interfaces machen Angaben, *was* ein Objekt bereitstellt, nicht *wie* es bereitgestellt wird. Sie beruhen auf dem `Design By
        Contract <http://en.wikipedia.org/wiki/Design_by_contract>`_-Modell.

        Während in einigen anderen Programmiersprachen Interfaces ein Bestandteil der Sprache selbst sind, werden in Python mit der `ZCA <zope-component-architecture>`_ Interfaces als Meta-Klasse implementiert, die ererbt werden kann.

        Interfaces erstellen
        ====================

        Für eine Komponente wird zunächst dessen Interface erstellt. Interface-
        Objekte werden üblicherweise mit *Python Class Statements* erstellt, sind
        jedoch selbst keine Klassen sondern Objekte. Ein Interface-Objekt wird nun
        als *Subclass* von ``zope.interface.Interface`` erstellt::

         from zope.interface import Interface

         class IHello(Interface):

             def hello(name):
                 """Say hello to somebody"""

        Durch das Subclassing von ``zope.interface.Interface`` wird nun das Interface-Objekt ``IHello`` erstellt::

         >>> IHello
         <InterfaceClass __main__.IHello>

        Marker-Interfaces
        -----------------

        Interfaces können auch verwendet werden um ein bestimmtes Objekt zu einem
        spezifischen Typ gehört. Ein solches Interface ohne Attribute und Methoden
        wird Marker-Interface genannt. Ein solches Interface kann z.B. so aussehen::

         >>> from zope.interface import Interface

         >>> class ISpecialGreeting(Interface):
         ...     """A special greeting"""

        Invarianten
        -----------

        Gelegentlich sind Regeln mit einem oder mehreren Attributen für das Interface einer Komponente erforderlich. Solche Regeln werden Invarianten genannt und können mit ``zope.interface.invariant`` erstellt werden.

        So kann z.B. für ein ``person``-Objekt mit den Attributen ``name``,  ``email`` und  ``phone`` ein Validator erstellt werden, der überprüft ob entweder ``email`` und  ``phone`` angegeben wurden.

        #. Zunächst wird nun ein aufrufbares Objekt entweder als Funktion oder Instanz erstellt::

            >>> def contacts_invariant(obj):
            ...
            ...     if not (obj.email or obj.phone):
            ...         raise Exception(
            ...             "At least one contact info is required")

        #. Anschließend wird das Interface des ``person``-Objekts mit der
        ``zope.interface.invariant``-Funktion definiert::

            >>> from zope.interface import Interface
            >>> from zope.interface import Attribute
            >>> from zope.interface import invariant

            >>> class IPerson(Interface):
            ...
            ...     name = Attribute("Name")
            ...     email = Attribute("Email Address")
            ...     phone = Attribute("Phone Number")
            ...
            ...     invariant(contacts_invariant)

        #. Schließlich kann die ``validateInvariants``-Methode verwendet werden::

            >>> from zope.interface import implements

            >>> class Person(object):
            ...     implements(IPerson)
            ...
            ...     name = None
            ...     email = None
            ...     phone = None

            >>> veit = Person()
            >>> veit.email = u"veit@example.org"
            >>> IPerson.validateInvariants(veit)
            >>> chris = Person()
            >>> IPerson.validateInvariants(jill)
            Traceback (most recent call last):
            ...
            Exception: At least one contact info is required

        Interfaces implementieren
        =========================

        Dieses ``Hello``-Interface kann nun assoziiert werden mit einer konkreten
        Klasse, in der das Verhalten definiert wird. In unserem Beispiel::

         class HelloComponent:

             implements(IHello)

             def hello(self, name):
                 return "Hello %s!" % name

        Die neue Klasse ``HelloComponent`` implementiert das ``Hello``-Interface.

        Dabei kann eine solche Klasse auch mehrere Interfaces implementieren. Sollen also Instanzen unserer ``HelloComponent`` zusätzlich ein ``Other``-Interface implementieren, wird einfach eine Sequenz der Interface-Objekte in der ``HelloComponent``-Klasse bereitgestellt::

         class HelloComponent:

             implements(IHello, IOther)
             ...

        Überprüfen der Implementierung
        ------------------------------

        Mit ``implementedBy`` kann ein Interface gefragt werden, ob eine bestimmte Klasse oder Instanz dieses Interface implementiert. So sollte  z.B. die Überprüfung, ob eine Instanz der ``HelloComponent``-Klasse ``Hello``implementiert den Wert ``true`` zurückliefern::

         IHello.implementedBy(HelloComponent)

        Interfaces erweitern
        ====================

        Interfaces können einfach erweitert werden, so kann z.B. unser ``IHello``-Interface  um eine Methode ``lastGreeted`` erweitert werden::

         class ISmartHello(IHello):
             """A Hello object that remembers who is greeted"""

             def lastGreeted(self):
                 """Returns the name of the last person greeted."""

        ``getBases``
         gibt eine Liste der Interfaces aus, die durch dieses Interface erweitert wurden, z.B.::

            >>> ISmartHello.getBases()
            (<InterfaceClass __main__.IHello>,)

        ``extends``
         gibt ``true`` oder `false``, je nachdem, ob ein Interface ein anderes erweitert oder nicht, z.B.::

            >>> ISmartHello.extends(IHello)
            True
            >>> IOther(Interface):
            ...     pass
            >>> ISmartHello.extends(IOther)
            False

        Interfaces abfragen (querying)
        ==============================

        ``names``
         gibt eine Liste der Namen aller Items aus, die durch das Interface beschrieben werden, z.B.::

            >>> IUser.names()
            ['getUserName', 'getPassword']

        ``namesAndDescriptions``
         gibt eine Liste von Tuples ``(name, description)`` aus, z.B.::

            >>> IUser.namesAndDescriptions()
            [('getUserName', <zope.interface.interface.Method.Method object at 80f38f0>),
            ('getPassword', <zope.interface.interface.Method.Method object at 80fded8>)]

        Marker interfaces
        =================

        Zum Weiterlesen
        ===============

        - `zope.interface <http://pypi.python.org/pypi/zope.interface>`_
        - `Components and Interfaces <http://docs.zope.org/zope2/zdgbook/ComponentsAndInterfaces.html>`_

    jQuery
        JavaScript-Bibliothek, die die Traversierung und das Event-Handling von HTML-Dokumenten vereinfacht. So lässt sich z.B. in einem Einzeiler angeben, dass alle PDFs in einem neuen Fenster geöffnet werden sollen::

         jQuery("#content a[ @href $= '.pdf']").attr('target', '_blank');

        Weitere Informationen zu jQuery erhalten Sie unter:

        - http://jquery.com/
        - http://docs.jquery.com

        Und mit `FireQuery`_ gibt es eine Firefox-Extension, die in Firebug integriert ist.

        .. _`FireQuery`: http://firequery.binaryage.com/

    Kinetic Style Sheet
        In Plone 3 verwendetes `AJAX`_-Framework.

        .. _`AJAX`: ajax

    Kupu
        Kupu ist ein graphischer HTML-Editor, der mit Plone zusammen ausgeliefert wird.

    l10n
        l10n ist die Übersetzung in eine oder mehrere spezifische Sprachen. l10n wird durch den ersten und letzten Buchstaben von *Localization* und die Anzahl der dazwischenliegenden Zeichen gebildet.

    Layer
        Ein Layer ist eine Sammlung von Templates und Skripten. Dabei bildet ein Stapel von Layern einen Skin. Im ZMI können Sie im *Properties*-Reiter des ``portal_skins``-Tool die Definition von Skins über Layer sehen und im *Content*-Reiter sehen Sie diese Layer als *Filesystem Directory View* oder *Folder*.

    LDAP
        LDAP beschreibt die Kommunikation zwischen einem sog. LDAP-Client und einem Verzeichnisdienst. EIn solches Verzeichnis kann z.B. ein Adressbuch sein, das Personendaten enthält. Der LDAP-Client kann dann ein E-Mail-Programm sein, das bei der Suche nach einer Adresse eine Anfrage an den LDAP-Server, der diese Adressinformationen bereitstellt, stellt.

        LDAP ist spezifiziert in `RFC 4511`_.

        .. _`RFC 4511`: http://tools.ietf.org/html/rfc4511

    Logging
        Für des Entwickelns stellt Plone einen eigenen Logger bereit: `plone_log`_::

         from logging import getLogger
         log = getLogger('Plone')
         log.info('Debug: %s \n%s', summary, text)

        .. _`plone_log`: http://dev.plone.org/plone/browser/Products.CMFPlone/trunk/Products/CMFPlone/skins/plone_scripts/plone_log.py

        Wie ``plone_log`` verwendet werden kann, finden Sie z.B. in `setConstrainTypes.cpy`_::

         ...
         plone_log=context.plone_log
         constrainTypesMode = context.REQUEST.get('constrainTypesMode', [])
         currentPrefer = context.REQUEST.get('currentPrefer', [])
         currentAllow = context.REQUEST.get('currentAllow', [])
         plone_log( "SET: currentAllow=%s, currentPrefer=%s" % ( currentAllow, currentPrefer ) )
         ...

        .. _`setConstrainTypes.cpy`: http://dev.plone.org/plone/browser/Products.CMFPlone/trunk/Products/CMFPlone/skins/plone_form_scripts/setConstrainTypes.cpy

    Manager
        Rolle, die in Zope alle Berechtigungen erhält bis auf *Take Ownership*.

    METAL
        Macro Expansion Tag Attribute Language

        *METAL* kann für das Verarbeitung von Macros für HTML und XML verwendet werden. Sie kann zusammen mit TAL und TALES verwendet werden.

        Macros erlauben Definitionen in einer Datei, die von einer oder mehreren anderen Dateien verwendet werden können. Dabei werden macros immer in vollem Umfang verwendet.

        METAL-Statements
        ================

        ``metal:define-macro``
         Definieren eines Macros als Element und dessen Teilbaum.

        ``metal:use-macro``
         Verwenden eines Macros wobei der Ausdruck in Zope immer die Angabe des Pfads ist, der auf ein Macro in einem anderen Template verweist.

        ``metal:define-slot``
         Definieren eines Slots, der angepasst werden kann.

         Wird ein Macro verwendet, so können dessen Slots ersetzt werden um das Macro anzupassen. Slot-Definitionen liefern dann den Standard-Inhalt für diesen Slot, der verwendet wird, sofern das Macro nicht angepasst wird.

         Die Anweisung ``metal:define-slot`` muss innerhalb von ``metal:define-macro`` verwendet werden. Darüberhinaus müssen die Slot-Namen innerhalb eines Macros einheitlich sein.

        ``metal:fill-slot``
         Anpassen eines Macros indem ein Slot dieses Macros ersetzt wird.

         Die Anweisung ``metal:fill-slot``muss innerhalb von ``metal:use-macro`` verwendet werden. Darüberhinaus müssen die Slot-Namen innerhalb eines Macros einheitlich sein.

        If the named slot does not exist within the macro, the slot contents will be silently dropped.

        Zum Weiterlesen
        ===============

        - `The Zope2 Book: METAL Overview`_

        .. _`The Zope2 Book: METAL Overview`: http://docs.zope.org/zope2/zope2book/AppendixC.html#metal-overview

    Monkey Patch
        Ein Monkey Patch erlaubt die Änderung des Verhaltens von Zope oder eines Produkts ohne den Original-Code verändern zu müssen.

        Ein Monkey Patch lässt sich einfach mit `collective.monkeypatcher`_ erstellen. Hierzu tragen wir in die ``configure.zcml``-Datei folgendes ein::

         <configure
             ...
             xmlns:monkey="http://namespaces.plone.org/monkey">
             ...
             <monkey:patch
                 description="TinyMCE JSON Folder listing should ignore INavigationRoot"
                 class="Products.TinyMCE.adapters.JSONFolderListing.JSONFolderListing"
                 original="getListing"
                 replacement=".patches.getListing"
                 />

        Nun erstellen wir unseren Pach, indem wir aus ``Products.TinyMCE.adapters.JSONFolderListing.JSONFolderListing`` die Methode ``getListing`` in die Datei ``patches.py`` kopieren und entsprechend anpassen.

        **Anmerkung:** Mit `collective.monkeypatcherpanel`_ wird ein Zope2-Control-Panel angelegt, das die mit ``collective.monkeypatcher`` erstellten Monkey Patches anzeigt.

        .. _`collective.monkeypatcher`: http://pypi.python.org/pypi/collective.monkeypatcher
        .. _`collective.monkeypatcherpanel`: http://pypi.python.org/pypi/collective.monkeypatcherpanel/1.0.2

    mr.bob
        `mr.bob <https://pypi.python.org/pypi/mr.bob/>`_ ist ein Dateisystem-Template-
        Renderer. Er ermöglicht, aus einer Vorlage eine Verzeichnisstruktur zu erstellen,
        die das Erstellen von Python-Paketen deutlich vereinfacht.

        Weitere Informationen zur Installation, den Vorlagen und Standardeinstellungen
        erhalten Sie im Abschnitt `Referenzen <../../anhang/referenz/mr.bob/>`_ des Plone-
        Entwicklerhandbuchs.

        .. seealso::
            * `mr.bob’s documentation <http://mrbob.readthedocs.org/en/latest/>`_
            * `Git repository <https://github.com/domenkozar/mr.bob>`_

    Namensraum
        Plone verwendet verschachtelte Pakete um Namensräume zu bilden, die durch Pfadnamen eindeutig angesprochen werden können und so Kollisionen mit anderen Paketen vermeiden helfen. Dabei nutzt Plone eine Funktion der Setuptools, womit mehrere getrennte Python Packages ausgeliefert werden können, die einen gemeinsamen Top-level-Namespace teilen, z.B. ``plone.theme`` und ``plone.portlets``.

    PAS
        PAS ist ein Framework zur Authentifizierung in Zope. PAS ist ein Zope-``acl_users``-Ordner, das Plugins verwendet um verschiedene Authentifizierungsschnittstellen bereitzustellen.

    Paste
        `Paste`_ ist ein WSGI-Entwicklungs- und Deployment-System, das von Ian Bicking entwickelt wurde.

        .. _`Paste`: http://pythonpaste.org/

    PDB
        PDB ist ein interaktiver Debugger, mit dem schrittweise durch den Code gegangen werden kann um Probleme aufzufinden.

        Um einen einfachen *Breakpoint* zusetzen, kann folgendes angegeben werden::

            import pdb; pdb.set_trace()

        Anschließend sollte Zope neu im Vordergrund gestartet werden mit::

            $ ./bin/instance fg

        Anschließend sollte der Code ausgeführt werden, für den der Breakpoint gesetzt wurde. Das Terminal, in dem die Instanz gestartet wurde, sollte dann eine Debug-Session öffnen mit folgender Angabe::

            -> Pdb().set_trace()
            (Pdb)

        Sie können nun mit ``r`` (*Return*) den ``set_trace()``-Aufruf verlassen und so schrittweise den Code untersuchen.

        Wenn ein Fehler in einer Methode auftritt, die häufig ausgeführt wird, ist es jedoch nur lästig, sehr häufig *Return* angeben zu müssen. Daher empfiehlt sich, das sog. *post-mortem*-Idiom zu verwenden::

            try:
                [YOUR CODE HERE]
            except:
                import pdb, sys
                e, m, tb = sys.exc_info()
                pdb.post_mortem(tb)

        Anschließend sollte die Zope-Instanz wieder im Vordergrund gestartet werden. Nun wird ``pdb`` nur noch aufgerufen, wenn ein Fehler im Abschnitt ``[YOUR CODE HERE]`` auftritt.

        Um zu gewährleisten, dass derselbe pdb-Breakpoint in einer Deubug-Session nicht mehrfach eine Exception ausgibt, kann die Variable ``PDB_ACTIVE`` auf ``1`` gesetzt werden::

            if not globals().get( 'PDB_ACTIVE', 0 ):
                globals()['PDB_ACTIVE'] = 1
                import pdb; pdb.set_trace()

        **Anmerkung:** Entfernen Sie bitte wieder die *debugging hooks* bevor der Code in das Repository eingecheckt wird.

        ``~/.pdbrc``
        ============

        Eine ``~/.pdbrc``-Konfigurationsdatei kann verwendet werden um sich einige Shortcuts zum Debuggen zu erstellen, z.B.::

            # Print a sorted dictionary.
            # %1 is the dict
            # %2 is the prefix for the names.
            alias p_ for k in sorted(%1.keys()): print "%s%-15s= %-80.80s" % ("%2",k,repr(%1[k]))

            # Print the member variables of something
            alias pi p_ %1.__dict__ %1.

            # Print the member variables of self
            alias ps pi self

            # Print locals
            alias pl p_ locals() local:

            # Next list and step list
            alias nl n;;l
            alias sl s;;l

        Um weitere Hilfsfunktionen in pdb nutzen zu können, lassen sich auch externe
        Python-Dateien in die ``~/.pdbrc``-Datei einbinden – siehe hierzu `PdbRcIdea
        <http://wiki.python.org/moin/PdbRcIdea>`_.

        Zum Weiterlesen
        ===============

        `Python Documentation: Debugger Commands`_
         Verwendung von pdb
        `Ken Manheimer: Conversing With Zope`_
         Ausführliche Anleitung für die Verwendung von pdb mit Zope
        `Stephen Ferg: Debugging in Python <http://pythonconquerstheuniverse.wordpress.com/category/python-debugger/>`_
         Eine kurze praktische Einführung in ``pdb``
        `Jeremy Jones: Interactive Debugging in Python`_
         Eine ausführliche Anleitung mit fortgeschrittenen Beispielen

        .. _`Python Documentation: Debugger Commands`: http://docs.python.org/library/pdb.html#debugger-commands
        .. _`Ken Manheimer: Conversing With Zope`: http://www.zope.org/Members/klm/ZopeDebugging/ConversingWithZope
        .. _`Jeremy Jones: Interactive Debugging in Python`: http://www.onlamp.com/pub/a/python/2005/09/01/debugger.html

    PLIP
        Vergleichbar mit Pythons PEPs (Python Enhancement Proposals).

        Das Plone-Team strukturiert und organisiert mit PLIPs den Entwicklungsprozess von Plone.

    Plone
        `Plone`_ ist ein, auf dem freien Webanwendungsserver `Zope`_ aufbauendes Enterprise-Content-Management-System, das in der Programmiersprache Python geschrieben ist.

        Es kann für Intranet- und Extranet-Anwendungen, als Dokumentenmanagementsystem und als Groupware eingesetzt werden. Zahlreiche Erweiterungen ermöglichen den Einsatz für weitere Aufgaben, z.B. im eLearning, Webshop oder Bilddatenbank.

        .. _`Plone`: http://plone.org/
        .. _`Zope`: zope

    Portlet
        Portlets sind frei konfigurierbare Ansichten, die sich an beliebigen Stellen der Website hinzufügen lassen.

        Folgende Portets werden mit Plone mitgeliefert:

        - Calendar portlet
        - Classic portlet
        - Collection portlet
        - Termine
        - Login
        - Navigation
        - Nachrichten
        - RSS feed
        - Aktuelle Änderungen
        - Revisionsliste
        - Suche
        - Static text portlet

        Die Zuweisung kann über folgende Kategorien erfolgen:

        Kontextabhängige Portlets
         ``context``
        Artikelspezifische Portlets
         ``content_type``
        Gruppenportlets
         ``group``

         Beachten Sie bitte, dass gruppenspezifische Portlets normalerweise unterhalb von kontextabhängigen Portlets angezeigt werden.

        Nutzerportlets
         ``user``

         Diese Angabe ist vermutlich nur für die Dashboard-Portlet-Manager sinnvoll.

    Portlet Manager
        Plone wird mit folgenden Portlet Managern ausgeliefert:

        ``plone.leftcolumn`` und ``plone.rightcolumn``
         für die linke und rechte Spalte
        ``plone.dashboard1`` bis ``plone.dashboard4``
         für die vier Spalten des Dashboard.

    Python
        Python ist die Programmiersprache, die von Zope und Plone verwendet wird.

        Tutorials
        =========

        The Python Tutorial
            http://docs.python.org/tutorial/
        Google Python classes
            http://code.google.com/edu/languages/google-python-class/

        Installation
        ============

        Es wird nicht empfohlen, die systemweite Python-Installation zu verwenden da für Plone häufig Python-Pakete benötigt werden, die nicht oder nicht in der gewünschten Version vorliegen.

        Wie Python aus den Sourcen installiert werden kann, ist im Kapitel `Entwicklungsumgebung`_ beschrieben.

        .. _`Entwicklungsumgebung`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/entwicklungsumgebung#installation

    Python Egg
        `Python Eggs`_ sind ein Deploymentformat für Python-Packages. Sie enthalten ein ``setup.py``-Skript mit Metainformationen (Lizenz, Abhängigkeiten, etc.) Mit der Python-Bibliothek *Setuptools* können solche Abhängigkeiten automatisch nachgeladen werden, wobei in Eggs spezifische Versionen angegeben werden können.

        .. _`Python Eggs`: http://peak.telecommunity.com/DevCenter/PythonEggs

    Python Package
        Python-Pakete strukturieren den Namensraum von Python-Modulen so, dass sog. *dotted module names* verwendet werden können.

        Sehen Sie auch in der Python Dokumentation: `Packages`_

        .. _`Packages`: http://docs.python.org/tutorial/modules.html#packages

    Python Package Index
        Der `Python Package Index PyPI unter `pypi.python.org
        <https://pypi.python.org/pypi/>`_ ist ein Index mit tausenden von
        Python-Paketen. Setuptools, `easy_install <easyinstall>`_ und `buildout
        <buildout>`_ nutzen diesen Index, um Python Eggs automatisch zu installieren.

        Er ist momentan noch der Standardhost zum Herunterladen von Paketen. Zukünftig
        wird `pypi.org <https://pypi.org/>`_ der Standard-Host werden; momentan ist er
        jedoch noch nicht voll funktionsfähig.

    PYTHONPATH
        Suchpfad für die Dateien von Modulen eines Python-Interpreters. Das Format entspricht demjenigen von ``PATH``. Innerhalb von Python ist der PYTHONPATH mit ``sys.path`` verfügbar. So kann z.B. beim Aufruf des ``bootstrap.py`` ein Skript ``bin/buildout`` erzeugt werden mit folgendem Inhalt::

         #!/opt/python/2.4.6/bin/python

         import sys
         sys.path[0:0] = [
           '/opt/plone/3.3/eggs/zc.buildout-1.3.1-py2.4.egg',
           '/opt/plone/3.3/eggs/setuptools-0.6c9-py2.4.egg',
           ]

    PyUnit
        Ein Standard-Unit-Testing-Framework für Python.

    Repoze
        `Repoze`_ ist eine Sammlung von Technologien um den Webanwendungsserver `Zope`_ mit `WSGI`_-Anwendungen zu verbinden.

        .. _`Repoze`: http://repoze.org
        .. _`Zope`: zope
        .. _`WSGI`: wsgi

    Request
        Um die Ansicht einer Seite in der Plone-Site zu erhalten, wird ein Request an die Plone-Site gestellt. Diese Anfrage wird in Zope in ein request-Objekt gekapselt, i.a. ``REQUEST`` genannt (oder ``request`` in ZPT).

    Resource Registries
        Plone-Infrastruktur, das CSS- und Javascript-Deklarationen in getrennten Dateien erlaubt. Erst für der Auslieferung werden diese Dateien zusammengeschrieben. Auch muss für das Einbinden einer neuen Datei nicht jedesmal in Zope Page Templates geändert werden um die Datei zu importieren oder auf sie zu verweisen. Die *Resource Registries* sind im ZMI zu finden unter ``portal_css``, ``portal_javascript`` und ``portal_kss``.

    roadrunner
        `roadrunner`_ ist ein Testrunner, der die testgetriebene Entwicklung deutlich beschleunigen kann indem er vorab das Standard-Zope- und Plone-Environment für PloneTestCase läd.

        .. _`roadrunner`: http://pypi.python.org/pypi/roadrunner

    Round-Robin
        Round-Robin wird bei der Lastverteilung (load balancing) von `Varnish`_ verwendet, wobei die Resourcen möglichst gleichmäßig beansprucht werden sollen. Dabei werden die Prozesse in einer Warteschlange verwaltet und der vorderste Prozess erhält eine bestimmte Zeit lang Zugang zu den Resourcen bevor er sich wieder am Ende der Warteschlange einreiht.

        .. _`Varnish`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/produktivserver/caching/varnish

    Skin
        Ein Stapel von Layer, die als Suchpfad verwendet werden wenn eine Seite gerendert wird. Skins werden im ``portal_skins``-Tool definiert, das auch durch das ZMI erreichbar ist.

    Subscriber
        Subscriber sind eine spezifische Form von `Adaptern <adapter>`_, die Verwendung findet, wenn alle Adapter eines Objekts zu einem Adapter zusammengefasst werden sollen.

        Subscriber registrieren
        =======================

        Subscriber lassen sich registrieren mit ``registerSubscriptionAdapter``::

         >>> components.registerSubscriptionAdapter(tests.A1_2)
         ... # doctest: +NORMALIZE_WHITESPACE
         Registered event:
         SubscriptionRegistration(<Components comps>, [I1], IA2, u'', A1_2, u'')

        Subscriber bereitstellen
        ========================

        Subscriber können bereitgestellt werden mit ``provideSubscriptionAdapter``.

        ::

         >>> component.provideSubscriptionAdapter(SingleLineSummary)
         >>> component.provideSubscriptionAdapter(AdequateLength)

         >>> doc = Document("A\nDocument", "blah")
         >>> [adapter.validate()
         ...  for adapter in component.subscribers([doc], IValidate)
         ...  if adapter.validate()]
         ['Summary should only have one line', 'too short']

        Subscriber verwenden
        ====================

        Mit ``subscribers`` erhalten Sie die Subscriber der jeweiligen Komponente::

         >>> doc = Document("A\nDocument", "blah")
         >>> [adapter.validate()
         ...  for adapter in component.subscribers([doc], IValidate)
         ...  if adapter.validate()]
         ['Summary should only have one line', 'too short']

        Informationen zu Subscribern erhalten
        =====================================

        Der Name und die Factory-Methode eines Subscribers sowie die
        Angabe, ob der Subscriber erforderlich ist, erhalten Sie mit
        ``provided``, ``factory`` und ``required`` aus
        ``registeredSubscriptionAdapters``::

         >>> for registration in sorted(
         ...     components.registeredSubscriptionAdapters()):
         ...     print registration.required
         ...     print registration.provided, registration.name
         ...     print registration.factory, registration.info


        Subscriber löschen
        ==================

        Subscriber lassen sich löschen mit
        ``unregisterSubscriptionAdapter``::

         >>> components.unregisterSubscriptionAdapter(tests.A1_2)
         ... # doctest: +NORMALIZE_WHITESPACE
         Unregistered event:
         SubscriptionRegistration(<Components comps>, [I1], IA2, u'', A1_2, '')
         True

        Zum Weiterlesen
        ===============

        - `Subscription Adapters <http://pypi.python.org/pypi/zope.component#subscription-adapters>`_
        - `Subscribers <http://pypi.python.org/pypi/zope.component#subscribers>`_.

    Supervisor
        Supervisor ist ein Client/Server-System, das die Prozessüberwachung und -kontrolle auf Unix-Betriebssystemen erlaubt.

        Dieses Python-Programm erlaubt ``start``, ``stop`` und ``restart`` anderer Programme auf UNIX-Systemen wobei es auch abgestürzte Prozesse erneut starten kann.

    TAL
        *TAL* ist eine Template-Sprache, die zur Generierung von XML-Dokumenten verwendet werden kann und abstrahiert dabei völlig von der eingesetzten Programmiersprache. Erst mit TALES, die die Syntax der Ausdrücke von *TAL* bescreibt, werden implementierungsabhängige Ausdrücke in Python erlaubt.

        Im Folgenden alle *TAL*-Ausdrücke:

        ``tal:attributes``
         erlaubt das dynamische Ändern der Attribute eines Elements.
        ``tal:define``
         definiert Variablen.
        ``tal:condition``
         testet, ob die angegebenen Bedingungen erfüllt werden.
        ``tal:content``
         ersetzt den Inhalt eines Elements.
        ``tal:omit-tag``
         entfernt ein Element.
        ``tal:on-error``
         beschreibt den Umgang bei einem Fehler.
        ``tal:repeat``
         wiederholt ein Element.

         Die ``tal:repeat``-Variable hält folgende Informationen:
          ``index``
           Fortlaufende Zahlen, mit Null beginnend
          ``number``
           Fortlaufende Zahlen, mit Eins beginnend
          ``even``
           wahr für mit even-indexierte Wiederholungen (0, 2, 4, ...)
          ``odd``
           wahr für odd-indexierte Wiederholungen (1, 3, 5, ...)
          ``start``
           wahr für die erste Wiederholung
          ``end``
           wahr für die letzte Wiederholung
          ``first``
           wahr für den ersten Eintrag der Wiederholung
          ``last``
           wahr fpr den letzten Eintrag der Wiederholung
          ``length``
           Länge der Sequenz, d.h. die Gesamtzahl der Einträge einer Wiederholung
          ``letter``
           Position des Eintrags als Kleinbuchstagen: ``a-z``, ``aa-az``, ``ba-bz``, ... ``za-zz``, ``aaa-aaz`` etc.
          ``Letter``
           Position des Eintrags als Versalien
          ``roman``
           Position des Eintrags als römische Zahl in Kleinbuchstaben:  ``i``, ``ii``, ``iii``, ``iv``, ``v`` etc.
          ``Roman``
           Position des Eintrags als römische Zahl in Versalien.

        ``tal:replace``
         ersetzt den Inhalt eines Elements.

        Erhält ein Element mehrere *TAL*-Anweisungen, so werden diese in folgender Reihenfolge ausgeführt:

        #. ``tal:define``
        #. ``tal:condition``
        #. ``tal:repeat``
        #. ``tal:content`` oder ``tal:replace``
        #. ``tal:attributes``
        #. ``tal:omit-tag``

    TALES
        *TALES* beschreibt die Syntax der Ausdrücke der Template Attribute Language (TAL) und der Macro Expansion Template Attribute Language (METAL).

        *TALES* stellt mehrere Methoden für Ausdrücke zur Verfügung, die in TAL- und METAL-Attributen  durch ein Präfix unterschieden werden können.

        Ausdruckstypen
        ==============

        ``path:``
         Der Präfix ist optional, d.h., wird kein Präfix angegeben, so wird ein Pfad-Ausdruck erwartet.

         Solche Ausdrücke referenzieren Objekte, um deren Methoden oder Attribute aufzurufen.

        ``string:``
         Präfix, der beliebige Zeichenketten erlaubt und damit z.B. auch aus Variablen generierte Pfadausdrücke mit ``${...)
          ``odd``
           wahr für odd-indexierte Wiederholungen (1, 3, 5, ...)
          ``start``
           wahr für die erste Wiederholung
          ``end``
           wahr für die letzte Wiederholung
          ``first``
           wahr für den ersten Eintrag der Wiederholung
          ``last``
           wahr fpr den letzten Eintrag der Wiederholung
          ``length``
           Länge der Sequenz, d.h. die Gesamtzahl der Einträge einer Wiederholung
          ``letter``
           Position des Eintrags als Kleinbuchstagen: ``a-z``, ``aa-az``, ``ba-bz``, ... ``za-zz``, ``aaa-aaz`` etc.
          ``Letter``
           Position des Eintrags als Versalien
          ``roman``
           Position des Eintrags als römische Zahl in Kleinbuchstaben:  ``i``, ``ii``, ``iii``, ``iv``, ``v`` etc.
          ``Roman``
           Position des Eintrags als römische Zahl in Versalien.

        ``tal:replace``
         ersetzt den Inhalt eines Elements.

        Erhält ein Element mehrere *TAL*-Anweisungen, so werden diese in folgender Reihenfolge ausgeführt:

        #. ``tal:define``
        #. ``tal:condition``
        #. ``tal:repeat``
        #. ``tal:content`` oder ``tal:replace``
        #. ``tal:attributes``
        #. ``tal:omit-tag``

    TALES
        *TALES* beschreibt die Syntax der Ausdrücke der Template Attribute Language (TAL) und der Macro Expansion Template Attribute Language (METAL).

        *TALES* stellt mehrere Methoden für Ausdrücke zur Verfügung, die in TAL- und METAL-Attributen  durch ein Präfix unterschieden werden können.

        Ausdruckstypen
        ==============

        ``path:``
         Der Präfix ist optional, d.h., wird kein Präfix angegeben, so wird ein Pfad-Ausdruck erwartet.

         Solche Ausdrücke referenzieren Objekte, um deren Methoden oder Attribute aufzurufen.

        ``string:``
         Präfix, der beliebige Zeichenketten erlaubt und damit z.B. auch aus Variablen generierte Pfadausdrücke mit ``${...}``.
        Logische Negation ``not:``
         Präfix, der den folgenden Ausdruck auswertete und seine logische Negation zurückgibt.
        Python ``python:``
         Präfix, der den Wert des folgenden Python-Skripts ausgibt.

         Ein Zugriff dieser Python-Skripte auf sicherheitsrelevante Objekte wird jedoch unterbunden.

        Unterdrückung des Quotings ``structure``
         Ein vorangestelltes ``structure`` unterdrückt das HTML-Quoting. Damit kann z.B. ein komplettes HTML-Element erzeugt werden.

        Eingebaute Namen
        ================

        ``nothing``
         Einzelner Wert, der von TAL verwendet wird um einen *Nicht-Werte* anzugeben, z.B. ``void``, ``None``, ``Nil``, ``NULL``.
        ``default``
         Einzelnder Wert, der in TAL spezifiziert, dass existierender Text nicht ersetzt werden ``options``
         Im Template zulässige Keyword-Argumente
        ``repeat``
         Schleifenvariablen, s.a. `The Zope2 Book: Repeat an element`_
        ``attrs``
         Ein Dictionary, das die zulässigen Werte des aktuellen Tags enthält.
        ``CONTEXTS``
         Liste der Standardnamen. Dies kann verwendet werden um auf eine eingebaute Variable zuzugreifen, die von einer lokalen oder globalen Variable desselben Namens verborgen wird.

        Zum Weiterlesen
        ===============

        - `TALES-Spezifikation, Version 1.3`_
        - `The Zope2 Book: TALES Overview`_

        .. _`The Zope2 Book: Repeat an element`: http://docs.zope.org/zope2/zope2book/AppendixC.html#repeat-repeat-an-element
        .. _`TALES-Spezifikation, Version 1.3`: http://wiki.zope.org/ZPT/TALESSpecification13
        .. _`The Zope2 Book: TALES Overview`: http://docs.zope.org/zope2/zope2book/AppendixC.html#tales-overview

    Test, funktionaler
        Test vom Standpunkt eines Endnutzers. Üblicherweise wird ein Use Case oder eine User Story getestet. Ein Beispiel für einen funktionalen Test ist, ob eine bestimmte Nachricht angezeigt wird nachdem ein Formular ohne erforderliche Daten abgeschickt wurde.

    Test-Suite
        Eine Sammlung von `Testfällen`_, die zusammen durchlaufen werden.

        .. _`Testfällen`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/anhang/glossar/testfall

    Testfall
        Eine Sammlung von Tests.

    Traceback
        Ein Python Traceback ist eine detaillierte Fehlermeldung, die ausgegeben wird wenn ein Fehler beim Ausführen von Python-Coder auftritt. Um sich einen solchen Traceback anzuschauen, können Sie entweder in die *event log*-Datei in ``var/log/instance`` schauen oder im ZMI Ihrer Plone-Site in ``error_log``. Ein Traceback beginnt mit ``Traceback (innermost last):`` oder ``Traceback (most recent call last):``. Meist ist die bedeutendste Information am Ende eines Tracebacks angegeben.

    Unit-Test
        Ein Test für kleine Code-Einheiten, z.B. das Setzen und Erhalten von Attributen einer Klasse.

    Utility
        *Utilities* sind Komponenten mit einem Interface und die mit einem Interface und einem Namen aufgerufen werden können.

        Utilities erstellen
        ===================

        Solche *Utilities* können erstellt werden mit::

         >>> from zope import interface
         >>> class IGreeter(interface.Interface):
         ...     def greet():
         ...         "say hello"
         >>> class Greeter:
         ...     interface.implements(IGreeter)
         ...
         ...     def __init__(self, other="world"):
         ...         self.other = other
         ...
         ...     def greet(self):
         ...         print "Hello", self.other

        ``queryUtility`` oder ``getUtility``
         fragen das Utility nach ihrem Interface::

          >>> component.queryUtility(IGreeter, 'christian').greet()
          Hello chris
          >>> component.getUtility(IGreeter, 'christian').greet()
          Hello chris

         ``queryUtility`` und ``getUtility`` unterscheiden sich jedoch in ihrer Fehlerbehandlung::

          >>> component.queryUtility(IGreeter, 'veit')
          >>> component.getUtility(IGreeter, 'veit')
          ... # doctest: +ELLIPSIS
          Traceback (most recent call last):
          ...
          ComponentLookupError: (<InterfaceClass ...IGreeter>, 'veit')

        ``provideUtility``
         registriert eine Instanz einer Utility-Klasse, z.B.::

          >>> from zope import component
          >>> greet = Greeter('chris')
          >>> component.provideUtility(greet, IGreeter, 'christian')

    View
        Ein View ist eine bestimmte Ansicht eines Objektes.

        Genauer betrachtet ist ein View eine Funktion zur Berechnung der Darstellung eines Objekts.

    Viewlet
        Ansicht zusätzlicher Informationen, die nicht der Inhalt eines Objekts sind. Dabei werden Viewlets meist durch `Viewlet Manager`_ verwaltet. Viewlets und Viewlet Manager ermöglichen die Erstellung von *pluggable user interfaces*.

        .. _`Viewlet Manager`: viewlet-manager

    Viewlet Manager
        Viewlet Manager verwalten die für sie registrierten `Viewlets`_.

        .. _`Viewlets`: viewlet

    virtualenv
        `virtualenv`_ erlaubt die Erstellung einer virtuellen Python-Umgebung. Damit lassen sich andere Abhängigkeiten, Versionen und Berechtigungen verwenden als in einer systemweiten Installation.

        .. _`virtualenv`: http://www.virtualenv.org/

        Installation
        ============

        ::

         $ easy_install-2.7 virtualenv
         $ virtualenv my_virtualenv

        Verzeichnisübersicht
        ====================

        ``bin``
         Das Verzeichnis enthält die Skripte zum Aktivieren und Deaktivieren des virtualenv, außerdem ``easy_install``, ``pip`` und ``python`` (Dabei ist ``python`` eine Kopie desjenigen Python, mit dem das ``virtualenv`` erstellt wurde.
        ``include``
         Das Verzeichnis enthält nur einen Symlink zum ``include``-Verzeichnis derjenigen Python-Installation, aus dem das ``virtualenv`` erstelt wurde.
        ``lib``
         Das Verzeichnis enthält einen Symlink zum ``include``-Verzeichnis derjenigen Python-Installation, aus dem das ``virtualenv`` erstellt wurde.

        Alternativen
        ============

        Ab Python 2.6 kann ein Nutzer auch einfach seine Python-Umgebung erstellen mit::

         $ pip install --user foo

        Siehe auch:

        - `Compare & Contrast with Alternatives`_
        - `PEP 370: Per user site-packages directory`_
        - `PEP 370-Documentation`_

        .. _`Compare & Contrast with Alternatives`: http://www.virtualenv.org/en/latest/index.html#compare-contrast-with-alternatives
        .. _`PEP 370: Per user site-packages directory`: http://www.python.org/dev/peps/pep-0370
        .. _`PEP 370-Documentation`: http://docs.python.org/whatsnew/2.6.html#pep-370-per-user-site-packages-directory

    WebDAV
        `WebDAV`_ steht für *Web-based Distributed Authoring and Versioning* und ist eine Erweiterung des Protokolls ``HTTP/1.1``, die in `RFC 2518`_ spezifiziert ist. Sie erlaubt, ganze Verzeichnisse zu übertragen. Zudem können Ressourcen bei der Bearbeitung gesperrt werden um ein konkurrierendes Schreiben zu verhindern.

        .. _`WebDAV`: http://www.webdav.org/
        .. _`RFC 2518`: http://tools.ietf.org/html/rfc2518

        Wie Zope als WebDAV-Server eingerichtet werden kann, ist in `WebDAV-Server`_ beschrieben.

        .. _`WebDAV-Server`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/produktivserver/webdav-server

        Eine Übersicht über diverse WebDAV-Clients finden Sie im `Plone-Nutzerhandbuch`_.

        .. _`Plone-Nutzerhandbuch`: http://www.plone-nutzerhandbuch.de/plone-nutzerhandbuch/webdav

        Zum Weiterlesen
        ===============

        - `Dexterity WebDAV notes`_

        .. _`Dexterity WebDAV notes`: http://svn.plone.org/svn/plone/plone.dexterity/trunk/docs/WebDAV.txt

    Workflow
        Workflows sind eine einfache Möglichkeit, Geschäftsprozesse abzubilden. Folgende Probleme lassen sich hiermit lösen:

        - Artikel können unterschiedliche Zustände (Stadien) annehmen
        - Artikel können je nach Stadium unterschiedliche Berechtigungen haben
        - Benutzer können bestimmte Ereignisse beim Ändern eines Status auslösen
        - Es lassen sich Abnahmen und Übergaben damit realisieren

        Home: http://pypi.python.org/pypi/Products.DCWorkflow

    WSGI
        Python-Standard-Interface zwischen Webanendungen mit dem Ziel, die Portabilität von Webanwendungen zu fördern.

        WSGI ist in `PEP 333`_ definiert.

        .. _`PEP 333`: http://www.python.org/dev/peps/pep-0333

    XML-RPC
        XML-RPC ist eine Definition zum Aufruf von Methoden und Funktionen durch entfernte Systeme.

        Zope unterstützt XML-RPC für jedes traversierbare Objekt, z.B.::

         target = 'http://localhost:8080/plone'
         path = xmlrpclib.ServerProxy(target).getPhysicalPath()

        Authentifizierung
        =================

        Eine einfache Möglichkeit, einen Nutzer für XML-RPC zu authentifizieren, ist das Einbinden von *HTTP Basic Auth* in eine URL::

         target = 'http://admin:secret@localhost:8080/plone'
         path = xmlrpclib.ServerProxy(target).getPhysicalPath()

        Marshalling
        ===========

        XML-RPC kann Objekte nicht zuverlässig an andere Aufrufe übergeben. Um an das entfernte Objekt zu gelangen, kann ``ZPublisher.Client.Object`` verwendet werden.

        Sehen Sie auch `Zope2.utilities.load_site`_

        .. _`Zope2.utilities.load_site`: http://svn.zope.org/Zope/trunk/src/Zope2/utilities/load_site.py?view=markup

        Web Services API for Plone (wsapi4plone)
        ========================================

        `wsapi4plone.core`_ stellt zusätzliche Methoden für Zopes XML-PRC-Api zur Verfügung.
        This is an add-on product exposes more methods available through Zope's XML-RPC api.

        .. _`wsapi4plone.core`: http://pypi.python.org/pypi/wsapi4plone.core

        Im Folgenden ein Beispiel, wie aus einem ``pictures``-Ordner ein Bild mit der ID ``portrait.jpg`` in einen Ordner ``portraits`` geladen und in ``veit.jpg`` umbenannt wird::

         import os
         from xmlrpclib import ServerProxy
         from xmlrpclib import Binary

         client = ServerProxy("http://admin:secret@localhost:8080/plone")
         data = open(os.path.join('pictures', 'portrait.jpg')).read()
         myimage = {'portraits/veit.jpg': [{'title': 'a Portrait of Veit', 'image':Binary(data)},'Image']}
         output = client.get_object(client.post_object(myimage))

        **Anmerkung:** `transmogrify.ploneremote`_ nutzt XML-RPC um Inhalte in eine Plone-Site zu importieren.

        .. _`transmogrify.ploneremote`: http://pypi.python.org/pypi/transmogrify.ploneremote

        Zum Weiterlesen
        ===============

        - `XML-RPC How To`_

        .. _`XML-RPC How To`: http://www.zope.org/Members/Amos/XML-RPC

    XPath
        XPath ist eine vom W3C entwickelte Abfragesprache, um Teile eines XML-Dokumentes zu adressieren. Auf ihr basieren weitere Standards wie ``XSLT``, ``XPointer`` und ``XQuery``.

        Ein XPath-Ausdruck setzt sich zusammen aus:

        - einem oder mehreren Lokalisierungsschritten,

          sie werden mit dem Zeichen ``/`` getrennt.

        - optional gefolgt von einem oder mehreren Prädikaten.

        Lokalisierungsschritte bestehen aus einer Achse und einem Knotentest, die *Achse::Knotentest* geschrieben werden.

        Achsen
        ======

        Hier die gebräuchlichsten Achsen:

        ``child``
         Direkt untergeordneter Knoten
         ``./``
        ``parent``
         Direkt übergeordneter Elternknoten
         ``./..``
        ``self``
         Der Kontextknoten selbst, der für zusätzliche Bedingungen ausgewählt wird
         ``.``
        ``descendant``
         Untergeordnete Knoten
         ``.//``
        ``attribute``
         Attributknoten
         ``@``

        Knotentests
        ===========

        Knotentests schränken die Elementauswahl einer Achse ein:

        Elementname
         Beispiel: ``.//Foo`` wählt alle Elemente des untergeordneten Knotens mit dem Namen `Foo`.
        ``*``
         Auswahl aller Elemente eines Knotens
        ``text()``, ``comment()`` und ``processing-instruction()``
         Auswahl von Knoten eines bestimmten Typs

        Zum Weiterlesen:
        ================

        - `XML Path Language (XPath) 2.0`_

        .. _`XML Path Language (XPath) 2.0`: http://www.w3.org/TR/xpath20/

    ZCatalog
        ZCatalog ist die Zope Suchmaschine, die die Kategorisierung von und die Suche nach allen Zope-Pbjekten erlaubt. Dabei wird auch die Suche in externen Daten, die z.B. in einer relationalen Datenbank liegen, unterstützt. Darüber hinaus kann der ZCatalog auch zur Erstellung von Sammlungen von Objekten verwendet werden.

        Volltextsuche und die gleichzeitige Suche in mehreren Indexen sowie das Gewichten der Felder in den Suchergebnissen werden unterstützt.

        Weitere Informationen über den ZCatalog erhalten Sie im `Zope Book`_

        .. _`Zope Book`: http://docs.zope.org/zope2/zope2book/source/SearchingZCatalog.html

    ZCML
        XML-Dialekt, der die verschiedenen Zope-Komponenten verbindet.

        Von Zope wird initial die in ``site-definition`` angegebene Datei abgearbeitet, meist ``$INSTANCE/etc/site.zcml``. Diese bindet dann über ``<includes>-``-Tags alle weiteren ZCML-Konfigurationsdateien ein::

          <!-- Load the meta -->
          <include files="package-includes/*-meta.zcml" />
          <five:loadProducts file="meta.zcml"/>

          <!-- Load the configuration -->
          <include files="package-includes/*-configure.zcml" />
          <five:loadProducts />

          <!-- Load the configuration overrides-->
          <includeOverrides files="package-includes/*-overrides.zcml" />
          <five:loadProductsOverrides />

          <securityPolicy
              component="Products.Five.security.FiveSecurityPolicy" />

        ``*-meta.zcml``
         Diese Dateien gewährleisten, dass die ZCML-Anweisungen der eingebundenen Pakete bei der Abarbeitung der ZCML-Anweisungen vollständig zur Verfügung stehen.
        ``*-configure.zcml``
         Hiermit werden ZCML-Dateien innerhalb der installierten Pakete abgearbeitet.
        ``*-overrides.zcml``
         Damit können Konfigurationen von Paketen überschreiben werden.
        ``securitypolicy.zcml``
         Hiermit wird die Security-Policy festgelegt

        Bedingungen
        ===========

        Pakete als Bedingungen
        ----------------------

        Das Starten der Instanz bricht ab, wenn in einer ``zcml``-Datei ``include package`` angegeben wird, dieses Paket jedoch nicht installiert ist. Um dies zu vermeiden, kann ``include`` an die Bedingung geknüpft werden, dass das Paket installiert ist, z.B.::

         <include
             zcml:condition="installed zope.app.zcmlfiles"
             package="zope.app.zcmlfiles"
             />
         <include
             zcml:condition="not-installed zope.app.zcmlfiles"
             package="zope.app"
             />
         <include zcml:condition="installed some.package"
             package="some.package" />
         <include zcml:condition="not-installed some.package"
             package=".otherpackage" />

        Funktionen als Bedingungen
        --------------------------

        Es können auch bestimmte Funktionen als Bedingung genannt werden. Diese Bedingungen können mit ``have`` oder deren Abwesenheit mit ``not-have``  angegeben werden, z.B.::

         <include
             package="Products.CMFCore" file="permissions.zcml"
             xmlns:zcml="http://namespaces.zope.org/zcml"
             zcml:condition="have plone-41" />
         <configure
             zcml:condition="not-have plone-4">
            <!-- only when the Plone 4 feature has not been provided -->
         </configure>
         <configure
             zcml:condition="not-have plone-5">
            <!-- only when the Plone 5 feature has not been provided -->
         </configure>

        Zum Weiterlesen
        ===============

        - `Zope Toolkit ZCML Documentation <http://docs.zope.org/zopetoolkit/codingstyle/zcml-style.html>`_

    ZEO
        Mittels ZEO greift eine Zope-Instanz nicht unmittelbar auf einen Datenspeicher zu sondern per TCP/IP auf einen sog. ZEO-Server. Durch die Verwendung mehrerer Zope-Instanzen, die auf denselben ZEO-Server zugreifen, lässt sich die Last besser verteilen.

        Weitere Informationen zu ZEO erhalten Sie im `Zope Book`_

        .. _`Zope Book`: http://docs.zope.org/zope2/zope2book/ZEO.html

    ZMI
        Erlaubt die Verwaltung des Zope-Servers durch das Web.

        Das *Zope Management Interface* lässt sich für die meisten vom Zope-Server ausgelieferten Objekte anzeigen, indem an die URL ``manage_workspace`` angehängt wird.

    ZODB
        Die ZODB bietet eine einfache Persistenz für Python-Objekte. Sie wird von Zope verwendet um Inhalte, Skripte und Konfigurationen zu speichern.

        Das `ZMI`_ ist ein Web-Interface zum Verwalten der Inhalte der ZODB.

        .. _`ZMI`: zmi

        Zum Weiterlesen:

        - `Welcome to the ZODB Book`_
        - `ZODB tutorial`_
        - `ZODB/ZEO programming guide`_
        - `ZODB articles`_

        .. _`Welcome to the ZODB Book`: http://zodb.readthedocs.org/
        .. _`ZODB tutorial`: http://www.zodb.org/documentation/tutorial.html
        .. _`ZODB/ZEO programming guide`: http://www.zodb.org/documentation/guide
        .. _`ZODB articles`: http://www.zodb.org/documentation/articles

    Zope
        `Zope`_ ist ein objektorientierter, in der Programmiersprache Python geschriebener, freier Webanwendungsserver.

        .. _`Zope`: http://www.zope.org/

    Zope Component Architecture
        *ZCA* ist ein Python-Framework zur einfachen Erstellung eines komponentenbasierten Designs. Dabei sind Komponenten wiederverwendbare Objekte mit einem Interface, das beschreibt, wie dieses Objekt angesprochen werden kann. *ZCA* vereinfacht die Erstellung von zwei Basiskomponenten:

        `Adapter <adapter>`_
         Komponenten, die aus anderen Komponenten erstellt werden um sie einem bestimmten Interface zur Verfügung zu stellen. Dabei sind `Subscribers <subscriber>`_ und `Handlers <handler>`_ zwei spezielle Typen von Adaptern.
        `Utilities <utility>`_
         Komponenten, die ein Interface anbieten und von einem Interface und einem Namen aufgerufen werden.

        Installation
        ============

        Zur *ZCA* gehören im wesentlichen drei Pakete:

        `zope.interface <zope.interface>`_
         wird verwendet um die Interfaces einer Komponente zu definieren.
        `zope.event <http://pypi.python.org/pypi/zope.event>`_
          bietet ein einfaches Event-System, siehe `Event <event>`_.
        `zope.component <http://pypi.python.org/pypi/zope.component>`_
         erleichtert die Erstellung, Registrierung und Retrieval der Komponenten.

        Die Installation beider Paktete kann einfach erfolgen mit `easy_install <http://peak.telecommunity.com/DevCenter/EasyInstall>`_::

         $ easy_install zope.component

    ZopeSkel
        `ZopeSkel <http://pypi.python.org/pypi/ZopeSkel>`_ ist eine Sammlung von Vorlagen, mit denen sich schnell Zope-Projekte erstellen lassen.

        Um solche Projekte zu erstellen verwendet ZopeSkel intern die `Paste Script <http://pythonpaste.org/script/>`_-Bibliothek.

        Weitere Informationen zur Installation, den Vorlagen und Standardeinstellungen erhalten Sie in `ZopeSkel. <http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/anhang/referenz/zopeskel/>`_.

    ZPT
        *Zope Page Templates* ist eine Template-Sprache um XML-konforme Dokumente zu erstellen.  Sie ist nahezu vollständig in `TAL`_, `TALES`_ und `METAL`_ beschrieben.

        Darüberhinaus hat *ZPT* jedoch einige zusätzliche Funktionen: Wird als Content-Type ``text/html`` angegeben, müssen die Namensräume für TAL und METAL nicht angegeben werden. Auch werden HTML-Dokumente mit dem non-XML-Parser analysiert, der nachlässiger mit fehlerhaftem Markup umgeht.

        Zum Weiterlesen
        ===============

        - `ZPT-specific Behaviors`_


        .. _`TAL`: tal
        .. _`TALES`: tales
        .. _`METAL`: metal
        .. _`ZPT-specific Behaviors`: http://docs.zope.org/zope2/zope2book/AppendixC.html#zpt-specific-behaviors

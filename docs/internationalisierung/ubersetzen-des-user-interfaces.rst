==============================
Übersetzen des User-Interfaces
==============================

Übersetzungen können nicht nur zur Übersetzung in völlig andere Sprachen verwendet werden, sondern auch z.B. zur Unterscheidung von österreichischen und deutschen Redewendungen. Desweiteren ermöglichen sie auch eine standardisierte Terminologie bei der Verwendung von Zusatzprodukten.

Zope und Plone nutzen `GNU gettext`_ und dessen *message catalogs*, eine Liste übersetzter Texte.

#. Wie eine sprachspezifische ``.po``-Datei erstellt wird ist bereits in `Erstellen der *.po-Datei`_ beschrieben.

#. Als Werkzeug zum Übersetzen können Sie `poEdit`_ oder einen einfachen Texteditor verwenden. Bei einem Texteditor sollte ``utf-8`` als Zeichenkodierung verwendet werden.
#. Jeder Abschnitt gliedert sich üblicherweise in folgende Angaben:

   ``#:``
    Eine Zeile, die mit diesen Zeichen beginnt, gibt das Template an, in dem die Zeichenkette verwendet wird. Kommt eine Zeichenkette in mehreren Templates vor, wird erhält jedes Template eine eigene Zeile.
   ``#.``
    Zeilen, die mit diesen Zeichen beginnen, geben den Abschnitt an, dem die Zeichenkette entstammt.
   ``msgid``
    Diese Zeile gibt die exakte Zeichenkette des zu übersetzenden Textes an. Variablen wie ``${foo}`` sind in die Übersetzung ohne Veränderung zu übernehmen.
   ``msgstr``
    Diese Zeile enthält den übersetzten Text.

Bevor sie nun mit dem Übersetzen beginnen, sollten sie sich noch die grundlegenden Begriffe anschauen, die Plone in den Language Specific Terms festlegt. Produkte, die auf Plone aufsetzen, sollten diese Begriffe übernehmen um konsistente Bezeichnungen zu gewährleisten. Daher empfiehlt sich auch für Ihr Produkt eine solche Liste spezifischer Begriffe.

Datum und Urzeit
================

Datum und Zeit werden im ``strftime``-Format lokalisiert, z.B.::

 msgid "date_format_long"
 msgstr "${Y}-${m}-${d} ${H}:${M}"

 msgid "date_format_short"
 msgstr "${Y}-${m}-${d}"

+-----------+---------------------------------------------------------+
| Anweisung | Beschreibung                                            |
+===========+=========================================================+
| ``%a``    | Lokalisierter abgeküzter Name des Wochentags.           |
+-----------+---------------------------------------------------------+
| ``%A``    | Lokalisierter Wochentag.                                |
+-----------+---------------------------------------------------------+
| ``%b``    | Lokalisierter abgekürzter Name des Monats.              |
+-----------+---------------------------------------------------------+
| ``%B``    | Lokalisierter Monatsname                                |
+-----------+---------------------------------------------------------+
| ``%c``    | Lokalisierte entsprechende Datums- und Zeitdarstellung. |
+-----------+---------------------------------------------------------+
| ``%d``    | Tag des Monats als Dezimalzahl ``01`` – ``31``.         |
+-----------+---------------------------------------------------------+
| ``%H``    | Stunde als Dezimalzahl ``00`` – ``23``.                 |
+-----------+---------------------------------------------------------+
| ``%I``    | Stunde als Dezimalzahl ``01`` – ``12``.                 |
+-----------+---------------------------------------------------------+
| ``%j``    | Tag des Jahres als Dezimalzahl. ``001`` – ``366``.      |
+-----------+---------------------------------------------------------+
| ``%m``    | Monat als Dezimalzahl ``01`` – ``12``.                  |
+-----------+---------------------------------------------------------+
| ``%M``    | Minute als Dezimalzahl ``00`` – ``59``.                 |
+-----------+---------------------------------------------------------+
| ``%p``    | Lokalisiertes Äquivalent von AM oder PM. [#]_           |
+-----------+---------------------------------------------------------+
| ``%S``    | Sekunde als Dezimalzahl ``00`` – ``61``. [#]_           |
+-----------+---------------------------------------------------------+
| ``%U``    | Wochenzahl eines Jahres als Dezimalzahl  ``00`` – ``53``|
|           | (Sonntag als erster Tag der Woche).                     |
|           | Alle Tage eines Jahres vor dem ersten Sonntag werden    |
|           | der Woche 0 zugerechnet. [#]_                           |
+-----------+---------------------------------------------------------+
| ``%w``    | Wochentag als Dezimalzahl ``0`` (Sonntag) – ``6``.      |
+-----------+---------------------------------------------------------+
| ``%W``    | Wochenzahl eines Jahres als Dezimalzahl ``00`` – ``53`` |
|           | (Montag als erster Tag der Woche)                       |
|           | Alle Tage eines Jahres vor dem ersten Montag werden der |
|           | Woche 0 zugerechnet. [3]_                               |
+-----------+---------------------------------------------------------+
| ``%x``    | Lokalisierte angemessene Datumsdarstellung.             |
+-----------+---------------------------------------------------------+
| ``%X``    | Lokalisierte angemessene Zeitdarstellung.               |
+-----------+---------------------------------------------------------+
| ``%y``    | Jahr ohne Jahrhundert als Dezimalzahl ``00`` – ``99``.  |
+-----------+---------------------------------------------------------+
| ``%Y``    | Jahr mit Jahrhundert als Dezimalzahl.                   |
+-----------+---------------------------------------------------------+
| ``%Z``    | Name der Zeitzone                                       |
|           | (keine Zeichen, wenn keine Zeitzone existiert.          |
+-----------+---------------------------------------------------------+
| ``%%``    | Das Zeichen ``%``.                                      |
+-----------+---------------------------------------------------------+

Übersetzungen für Pakete
========================

#. Fügen sie in ihr Paket folgende Unterverzeichnisse für jede gewünschte Sprache ein: ``locales/<locale>/LC_MESSAGES/``, z.B.::

    locales/de/LC_MESSAGES/
    locales/en/LC_MESSAGES/

#. Erstellen Sie die entsprechenden ``vs.theme.po``-Dateien  in den ``LC_MESSAGES``-Ordnern und editieren diese z.B. mit `poEdit`_.
#. Registrieren sie die Übersetzungen in der ``configure.zcml``-Datei mit folgenden Anweisungen::

    <configure
        ...
        xmlns:i18n="http://namespaces.zope.org/i18n"
        i18n_domain="vs.theme">
        ...
        <i18n:registerTranslations directory="locales" />
    </configure>

#. Normalerweise werden die ``.po``-Dateien beim Starten des Zope-Servers vom PlacelessTranslationService kompiliert, d.h. ``.mo``-Dateien erzeugt.
#. Gegebenenfalls können auch mit folgendem Skript die ``.po``-Dateien kompiliert werden::

    # Compile po files
    for lang in $(find locales -mindepth 1 -maxdepth 1 -type d); do
        if test -d $lang/LC_MESSAGES; then
            msgfmt -o $lang/LC_MESSAGES/${PRODUCT_NAME}.mo $lang/LC_MESSAGES/${PRODUCT_NAME}.po
        fi
    done

Plone 4
=======

In Plone 4 nutzt der ``PlacelessTranslationService`` ``zope.i18n``. Die Ordner ``i18n`` und ``locales`` verwenden dieselbe Katalog-Engine.

In Plone 3 kompilierte der ``PlacelessTranslationService`` die ``*.po``-Dateien erneut. In Plone 4 jedoch nutzt er das ``zope.i18n``-Modul, für das explizit angegeben werden muss, dass es ``*.po``-Dateien kompilieren soll. Hierzu wird in der Buildout-Konfiguration dann folgendes angegeben::

 [instance]
 ...
 environment-vars =
     zope_i18n_compile_mo_files = true

Einschränken der verwendeten Sprachen
=====================================

Um den Startprozess von der Zope-Instanzen zu beschleunigen und weniger Speicher zu verbrauchen, kann eine Umgebungsvariable gesetzt werden, die das Kompilieren und Laden von ``*.po``-Dateien einschränkt. Um die Sprachen z.B. auf Englisch und Deutsch zu beschränken, kann in der ``buildout.cfg``-Datei folgendes angegeben werden::

 [instance]
 ...
 environment-vars =
     ...
     PTS_LANGUAGES en de
     zope_i18n_allowed_languages en de

``PTS_LANGUAGES``
 In Plone 3 beeinflusst diese Angabe sowohl das Kompilieren der Übersetzungsdateien in ``i18n``- und ``locales``-Ordnern.

 In Plone 4 wird hierdurch nur noch das Kompilieren der Übersetzungsdateien in ``i18n``-Ordnern.

``zope_i18n_allowed_languages``
 In Plone 4 wird hierdurch das Kompilieren der Übersetzungsdateien in ``locales``-Ordnern gesteuert.

.. seealso::
    * `Internationalizing a Package`_.

.. _`GNU gettext`: http://www.gnu.org/software/gettext
.. _`Erstellen der *.po-Datei`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/internationalisierung/erstellen-der-ubersetzungsdateien.html#erstellen-der-po-datei
.. _`poEdit`: http://poedit.net/

----

.. [#] In der ``strftime`` -Funktion ändert die ``%p`` -Anweisung nur die Ausgabe, wenn ``%I`` verwendet wird.
.. [#] Der Umfang ist tatsächlich ``00`` – ``61`` um Schaltsekunden («leap seconds» und «double leap seconds») berücksichtigen zu können.
.. [#] In ``strftime`` -Funktionen wird ``%U`` und ``%W`` nur berechnet, wenn Tag, Woche und Jahr angegeben sind.
.. _`Internationalizing a Package`: http://wiki.zope.org/zope3/i18n.html

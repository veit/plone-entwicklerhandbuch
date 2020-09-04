=================================
Erstellen der Übersetzungsdateien
=================================

Zum Erstellen des `GNU gettext`_-*message catalogs* verwenden wir `i18ndude`_.

``i18ndude``-Installation
=========================

``i18ndude`` lässt sich am einfachsten als eigenständiges Buildout-Projekt installieren um Versionskonflikte in den Abhängigkeiten zu vermeiden. Hierzu erhält die ``buildout.cfg``-Datei ausschließlich den Abschnitt ``scripts``::

 [buildout]
 parts =
     scripts

 eggs =
     i18ndude

 [scripts]
 recipe = zc.recipe.egg
 eggs = i18ndude

.. $ easy_install -N i18ndude

.. Sofern die erforderlichen Berechtigungen für das Pythonverzeichnis vorliegen wird das Paket damit installiert.

.. Die Option ``-N`` sorgt dafür, dass die Abhängigkeiten von ``i18ndude``, dies sind etliche Zope-Pakete, nicht mitinstalliert werden. Stattdessen wird anschließend der ``PYTHONPATH`` auf die entsprechenden *fake-eggs* der Zope-Installation gesetzt::

..  $ export PYTHONPATH="/home/veit/myproject/fake-eggs:$PYTHONPATH"

Erstellen der ``.pot``-Datei
============================

Die ``.pot``-Datei ist ein Template, aus dem die sprachspezifischen Übersetzungsdateien abgeleitet werden. Im Template tragen üblicherweise die ``msgid``-Zeilen Strings aus Page Templates (``*.pt``) und Python-Dateien (``*.py``), die ``msgstr`` sind leer. Strings aus ``.xml``-Dateien werden über die passende Angabe ``i18n:domain`` im Header erfasst.
Um Fehlermeldungen zu vermeiden erstellen wir zuerst die benötigten Verzeichnisse.

::

 $ mkdir -p src/vs.registration/vs/registration/locales/de/LC_MESSAGES
 $ cd /home/veit/i18ndude_buildout
 $ ./bin/i18ndude rebuild-pot --pot /home/veit/myproject/src/vs.registration/vs/registration/locales/vs.registration.pot --create vs.registration /home/veit/myproject/src/vs.registration/vs/registration

Mit der Option ``rebuild-pot --pot`` gibt man die Datei an, in die das neue Template geschrieben wird. Mit dem zweiten Parameter ``--create`` gibt man zuerst die Domäne und danach das Verzeichnis an, das rekursiv nach relevanten Dateien durchsucht wird.

Weitere Optionen liefert der Aufruf von ``./bin/i18ndude --help``.

Erstellen der ``.po``-Datei
===========================

Die ``.po``-Dateien enthalten die Übersetzungen in den ``msgstr``-Zeilen. Diese werden für die Anzeige der Übersetzung verwendet. Mit dem folgenden Befehl werden sie erstellt und in ``src/vs.registration/vs/registration/locales/de/LC_MESSAGES/`` abgelegt. Um Fehlermeldungen zu vermeiden erstellen wir zuerst eine leere ``.po``-Datei.

::

 $  touch src/vs.registration/vs/registration/locales/de/LC_MESSAGES/vs.registration.po
 $ ./bin/i18ndude sync --pot src/vs.registration/vs/registration/locales/vs.registration.pot src/vs.registration/vs/registration/locales/de/LC_MESSAGES/vs.registration.po

Der Befehl liefert beim ersten Durchlauf eine Rückmeldung wie z.B. diese::

 src/vs.registration/vs/registration/locales/de/LC_MESSAGES/vs.registration.po: 31 added, 0 removed

Sollte eine Fehlermeldung besagen, dass die Zieldatei nicht existiert, dann wurde womöglich der XML-Namespace ``i18n`` nicht verwendet oder die Eigenschaft ``i18n:translate`` nicht korrekt verwendet.

**Anmerkung 1:** Werden die Dateien erneut synchronisiert, werden auch die Kommentare verglichen. Dabei wird ein ``fuzzy``-Kommentar hinzugefügt sofern sich die ``msgid`` geändert hat. Diese Angaben sollten dann überprüft werden.

**Anmerkung 2:** Kommen in einer ``msgid`` URLs vor, die in Anführungszeichen (``"``) gesetzt sind, so müssen diese *escaped* werden mit ``\``, also z.B. ``<a href=\"http://www.veit-schiele.de\">www.veit-schiele.de</a>``.

Aktualisieren bestehender Übersetzungen
=======================================

Um die Übersetzungen zu aktualisieren, etwa wenn sich die Zahl der Strings verändert hat, wird zunächst die ``.pot``-Datei wie oben beschrieben aktualisiert. Anschließend wird die deutsche Übersetzungsdatei mit diesem Befehl aktualisiert::

 $ ./bin/i18ndude sync --pot src/vs.registration/vs/registration/locales/vs.registration.pot src/vs.registration/vs/registration/locales/de/LC_MESSAGES/vs.registration.po

Skripte zum Aktualisieren der Übersetzungen
===========================================

Um nicht bei jeder Aktualisierung erneut die obigen Shell-Kommandos eingegeben werden müssen, kann auch ein Shell-Skript angelegt werden, z.B. ``rebuild.sh`` mit folgendem Inhalt::

 #!/usr/bin/env bash
 ./bin/i18ndude rebuild-pot --pot src/vs.policy/vs/policy/locales/vs.policy.pot --create "vs.policy" --merge src/vs.policy/vs/policy/locales/vs.policy-manual.pot src/vs.policy*
 ./bin/i18ndude rebuild-pot --pot src/vs.policy/vs/policy/locales/plone.pot --create "plone" --merge src/vs.policy/vs/policy/locales/plone-manual.pot src/vs.policy/vs/policy/profiles/
 ./bin/i18ndude sync --pot src/vs.policy/vs/policy/locales/vs.policy.pot src/vs.policy/vs/policy/locales/de/LC_MESSAGES/vs.policy.po
 msgfmt --no-hash -o src/vs.policy/vs/policy/locales/de/LC_MESSAGES/vs.policy.mo src/vs.policy/vs/policy/locales/de/LC_MESSAGES/vs.policy.po
 ./bin/i18ndude sync --pot src/vs.policy/vs/policy/locales/plone.pot src/vs.policy/vs/policy/locales/de/LC_MESSAGES/plone.po
 msgfmt --no-hash -o src/vs.policy/vs/policy/locales/de/LC_MESSAGES/plone.mo src/vs.policy/vs/policy/locales/de/LC_MESSAGES/plone.po

Sortierung der Einträge in ``.po``-Dateien
==========================================

``i18ndude`` sortiert die Übersetzungen alphabetisch nach der ``msgid``. Bei umfangreichen Übersetzungen, die sich bezüglich der Anzahl der Strings nicht mehr ändern, kann es sinnvoll sein diese nach der Herkunftsdatei zu sortieren, wie von gettext empfohlen. Fertige ``.po``-Dateien lassen sich mit ``gettext`` entsprechend bearbeiten, das Paket stellt hierfür den Befehl ``msgcat`` und den Parameter ``--sort-by-file`` zur Verfügung. Siehe die Dokumentation von `GNU gettext`_.

.. _`GNU gettext`: http://www.gnu.org/software/gettext
.. _`i18ndude`: http://pypi.python.org/pypi/i18ndude

.. `How to internationalize your application`_
.. `i18n, locales and Plone 3.0`_

.. _`How to internationalize your application`: http://grok.zope.org/documentation/how-to/how-to-internationalize-your-application
.. _`i18n, locales and Plone 3.0`: http://maurits.vanrees.org/weblog/archive/2007/09/i18n-locales-and-plone-3.0

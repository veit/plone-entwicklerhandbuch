====================
Erstellen eines Jobs
====================

Verwenden Sie in Jenkins die *Free Style*-Vorlage um einen neuen Job zu erstellen.

#. Alte Builds verwerfen

   Wie lange sollen *Builds* aufbewahrt werden? Hiermit lässt sich der Festplattenverbrauch von Jenkins steuern. Jenkins bietet hierzu zwei Strategien an:

   Nach Alter
    Jenkins löscht Aufzeichnungen, sobald sie ein bestimmtes Alter erreichen, z.B. 7 Tage alt sind.
   Nach Anzahl
    Jenkins bewahrt nur die ``N`` neuesten *Builds* auf. Wenn ein neuer Build gestartet wird, löscht Jenkins den ältesten.

   Jenkins erlaubt darüberhinaus, dass einzelne *Builds* markiert werden mit*Dieses Protokoll für immer aufbewahren*, sodass wichtige *Builds* von der automatischen Löschung ausgeschlossen werden.

#. Erweiterte Projekteinstellungen

   Hier können Sie die Anzahl der Wiederholungen bei fehlgeschlagenen Checkouts angeben.

#. Source-Code-Management (SCM)

   Hier können Sie z.B. die URL Ihres Subversion-Repository, die Check-Out-Strategie und den Repository-Browser angeben.

#. Build-Auslöser

   Hier können Sie die Zeitpläne angeben, zu denen die Builds gestartet werden sollen.

#. Buildverfahren

   Als Buildverfahren wählen Sie ein Shell-Skript, das z.B. folgenden Inhalte haben kann::

    cd /home/veit/my_buildout
    ./bin/develop up
    ./bin/buildout
    ./bin/test --xml -s vs.registration

   ``./bin/develop up``
     aktualisiert die Quellen von ``mr.developer``.
   ``./bin/test --xml -s vs.registration``
     Das Buildout hat einen ``[test]``-Abschnitt, der folgendermaßen aussieht::

      [test]
      recipe = collective.xmltestreport
      eggs =
          vs.registration
      extra-paths = ${zope2:location}/lib/python
      defaults = ['--exit-with-status', '--auto-color', '--auto-progress']

     Das Rezept ``collective.xmltestreport`` ist eine spezielle Version von ``zc.recipe.testrunner`` um Testreports im XML-Format zu schreiben wie es von JUnit/Ant verwendet wird. Dies erlaubt es Jenkins, die Testergebnisse zu analysieren.

#. Post-Build-Aktionen

   Veröffentliche JUnit-Testergebnisse
    Es sind reguläre Ausdrücke wie z.B. ``parts/test-jenkins/testreports/*.xml`` erlaubt. Das Ausgangsverzeichnis ist der Arbeitsbereich.
   Plot build data
    Mit dem `Plot plugin`_ können Sie sich Trends grafisch darstellen lassen.
   E-Mail-Benachrichtigung
    Hier können Sie eine Liste der Empfänger angeben, die bei jedem fehlgeschlagenen Build informiert werden sollen.

    Darüberhinaus können auch diejenigen informiert werden, die einen Build fehlschlagen ließen.

.. _`Plot plugin`: http://wiki.jenkins-ci.org/display/JENKINS/Plot+Plugin

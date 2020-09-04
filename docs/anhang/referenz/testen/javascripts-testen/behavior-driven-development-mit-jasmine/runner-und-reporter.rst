===================
Runner und Reporter
===================

Jasmine ist in JavaScript geschrieben und muss daher
in eine JS-Umgebung eingebunden werden.

#. Hierfür wird eine HTML-Seite geschrieben, die die
   Javascript-Dateien mit dem ``<script>``-Tag
   einbindet sodass alle *Specs* mit Jasmine
   durchlaufen und aufgezeichnet werden.  Daher ist
   diese HTML-Seite der *Test-Runner*. Sehen Sie
   hierzu `SpecRunner.html
   <https://github.com/pivotal/jasmine/blob/master/lib/jasmine-core/example/SpecRunner.html>`_.

   Dabei werden folgende Schritte durchlaufen:

   #. Zunächst wird ein ``HTMLReporter`` erstellt um
      die Ergebnisse jeder *Spec* und jeder Test-Suite
      aufzuzeichnen. Der Reporter ist auch für die
      spätere Darstellung der Ergebnisse zuständig.
   #. Auswählen einzelner Test-Suites oder *Specs*,
      die Durchlaufen werden sollen.
   #. Durchlaufen aller ausgewählten Tests.

   Diese Seite sollte im ``tests``-Modul unseres Pakets unter dem Namen ``testRunner.html`` abgespeichert werden.

#. Anschließend passen wir die Verweise auf die
   Quelldateien an, da die von uns zu testenden
   Javascript-Dateien nicht im ``tests``-Modul selbst
   sondern im ``browser``- oder ``skins``-Modul liegen
   werden.
#. Nun kopieren wir noch die folgenden Dateien in
   ``tests/jasmine`` und passen die Pfade in
   ``testRunner.html`` entsprechend an:

   - `jasmine-html.js <https://github.com/pivotal/jasmine/blob/master/lib/jasmine-core/jasmine-html.js>`_
   - `jasmine.css <https://github.com/pivotal/jasmine/blob/master/lib/jasmine-core/jasmine.css>`_
   - `jasmine.js <https://github.com/pivotal/jasmine/blob/master/lib/jasmine-core/jasmine.js>`_
   - `jasmine_favicon.png <https://github.com/pivotal/jasmine/blob/master/images/jasmine_favicon.png>`_

#. Schließlich können wir noch unsere *Specs*
   schreiben wobei sich bewährt hat, die Javascript-
   Dateinamen im ``tests``-Modul beizubehalten.

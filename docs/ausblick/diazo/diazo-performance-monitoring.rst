============================
Diazo Performance-Monitoring
============================

Das Ausführen von XSLT für ein Diazo-Theme ist gewöhnlich deutlich schneller als
die Auslieferung einer Plone-Seite selbst. Dabei sollte eine Anfrage weniger als eine Sekunde benötigen. 10–50ms je Anfrage an Diazo, je nach Komplexität des
Themes sind dabei vollkommen normal. Wenn Sie jedoch feststellen, dass das
Rendering von XSLT viel mehr Zeit verbraucht, haben Sie folgende Möglichkeiten
um den Fehler genauer analysieren zu können:

#. Einfache binäre Suche

   Entfernen Sie Schritt für Schritt eine weitere Hälfte Ihres Themes und
   wiederholen anschließend Ihre Messung. So können Sie ggf. den
   zeitaufwendigen XSLT-Anweisungen auf die Spur kommen.


   Dabei werden Sie entdecken, dass Regeln wie z.B. die folgende sehr aufwändig
   sind::

       <before css:content="head link" css:theme="head link" />

   Diese Diazo-Regel trifft auf mehrere Knoten in einem Dokument zu. Diese Regel
   fügt eine Kopie aller ``link``-Tags aus ``content`` vor jeden ``link``-Tag im
   Theme. Stattdessen wird jedoch vermutlich das Folgende benötigt::

       <before css:content="head link" theme="/head/link[1]" />

#. Kompilieren Sie Ihr Theme mit dem Diazo-Server

   Anschließend können Sie folgende Messungen durchführen::

       $ bin/diazocompiler -r rules.xml -o compiled.xsl
       $ xsltproc --timing --repeat --html --noout compiled.xsl mypage.html
       Parsing stylesheet compiled.xsl took 1 ms
       Parsing document mypage.html took 26 ms
       Applying stylesheet 20 times took 197 ms

   Dabei erhalten wir mit ``xsltproc --profile`` jedoch nur Statistiken über
   einzelne Templates. Dies führt leider nicht immer zum gewünschten Ergebnis.


.. `huge performance issues using Diazo
   <http://plone.293351.n2.nabble.com/huge-performance-issues-using-Diazo-tp7372056p7380644.html>`_

=========
Profiling
=========

Die Steigerung der Performance kann sehr schwierig sein. Es gibt jedoch eine Reihe von Werkzeugen, mit denen sich die Performance messen und die Flaschenhälse auffinden lassen.

`Python Profilers <http://docs.python.org/library/profile.html>`_
 erstellt Zope-Publisher-Profile, die im ZMI unter ``http://127.0.0.1:8080/Control_Panel/DebugInfo/manage_profile`` angezeigt werden:

 .. figure:: profile.png
    :alt: Publisher Profile

 Die Installation erfolgt mit::

  [instance]
  ...
  zope-conf-additional =
      publisher-profile-file ${buildout:directory}/var/instance/profile.dat
  environment-vars =
      PROFILE_PUBLISHER 1

`PTProfiler`_
 erstellt Profile für Page Templates in Zope2. Für jeden TAL-Ausdruck wird die Zeit gemessen und eine Tabelle sortiert nach den benötigten Zeiten erstellt.

 Um ``PTProfiler`` zu installieren können Sie einfach folgendes in Ihre ``buildout.cfg``-Datei schreiben::

  eggs =
      ...
      Products.PTProfiler

 Nachdem Sie das Buildout-Skript aufgerufen und die Instanz neu gestartet haben, können Sie an jeder Stelle Ihrer Instanz ein *PTProfiler Viewer*-Objekt hinzufügen und anschließend auf *Enable* klicken. Nun erhalten Sie eine Liste der Pfade aller aufgerufenen Page Templates und beim Klicken auf einen der Pfade auch die Zeiten für alle Aufrufe.

`Call Profiler`_
 zeigt den Ablauf von DTML, ZSQL, ZPT, Python-Methoden und -Skripten an, wobei sowohl die absoluten als auch die relativen Zeiten ermittelt werden. Zum Installieren lässt sich in der ``buildout.cfg``-Datei im Abschnitt ``[productdistros]`` als URL folgendes angegeben::

  http://plone.org/products/callprofiler/releases/1.4-fixed/CallProfiler-1.4-fixed.tar.gz

 .. figure:: callprofiler.png
    :alt: CallProfiler

 Anschließend kann in ``/Control_Panel/CallProfiler`` angegeben werden, für welche Aufrufe ein Profil erstellt werden soll.

`ZopeProfiler`_
 liefert sowohl *Zope object call level*- als auch *Python function call level*-Statistiken, z.B.::

        167 function calls (160 primitive calls) in 5.229 CPU seconds

  Ordered by: internal time

  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       1    2.927    2.927    2.960    2.960 document_view:0(__call__)
       1    0.754    0.754    3.715    3.715 mysite:0(Request)
       1    0.186    0.186    0.187    0.187 search_icon.gif:0(Request)
       1    0.132    0.132    0.132    0.132 folder_icon.gif:0(Request)
       1    0.080    0.080    0.080    0.080 file_icon.gif:0(Request)
       1    0.076    0.076    0.076    0.076 member-cachekey9666.css:0(Request)
       1    0.071    0.071    0.073    0.073 document_icon.gif:0(Request)
  ...

 Installieren lässt sich der ZopeProfiler durch die Angabe der URL im Abschnitt ``[productdistros]`` der ``buildout.cfg``-Datei::

  http://www.dieter.handshake.de/pyprojects/zope/ZopeProfiler.tgz

 Eine Erläuterung der Tabelle finden Sie in `The Python Profilers`_.

`hotshot`_
 Python-Profiler, der für jede einzelne Funktion ein Profil ausgibt. Er kann einfach aufgerufen werden, z.B. mit::

  ./bin/instance test -pvvv --profile -m vs.registration

 Dabei wird eine Liste der 50 zeitaufwendigsten Funktionen ausgegeben und eine Datei geschrieben wie z.B. ``myproject/tests_profile.bMAEin.prof``. Diese Datei lässt sich editieren, z.B. mit::

  $ python
  >>> from hotshot.stats import load
  >>> s = load('tests_profile.bMAEin.prof')
  s.print_stats('.*some_function.*')

`profilehooks`_
 Decorator für das Profiling einzelner Funktionen::

  from profilehooks import profile

    @profile
    def my_function(args, etc):
        pass

 Die  Installation erfolgt einfach mit ``easy_install profilehooks``.

 Mit ``pydoc profilehooks`` erhalten Sie eine Liste aller verfügbaren Decorator-Optionen.

 Weitere Informationen erhalten Sie in der `profilehooks-Dokumentation`_

`collective.stats`_
 gibt low level ZODB-Statistiken aus.

 Installation::

  [instance]
  ...
  eggs =
      ...
      collective.stats

 Beim Starten der Instanz im Vordergrung mit ``./bin/instance fg`` erhalten Sie
 dann z.B. folgende Ausgabe auf der Konsole::

  2014-02-17 12:25:30 INFO Zope Ready to handle requests
  2014-02-17 12:25:50 INFO collective.stats | 0.0021 0.0014 0.0018 0.0004 0.0000 0000 0000 0000 | GET:/favicon.ico | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 116708 - 116744
  2014-02-17 12:25:55 INFO collective.stats | 0.1783 0.0021 0.1779 0.0004 0.0000 0000 0000 0000 | GET:/manage_main | t: 0.0000, t_c: 0.0000, t_nc: 0.0000 | RSS: 116756 - 116948

 Die Werte bedeuten dann im Einzelnen:

 ``Header``
  Detail
 ``time``
  Dauer innerhalb des Zope Publisher
 ``t traverse``
  Zeit, zu dem der Zope Publisher
 ``t commit``
  Dauer für ``transaction.commit()``
 ``t transchain``
  Dauer für ``plone.transformchain.applyTransform``
 ``setstate``
  Dauer in ``Connection.setstate``
 ``total``
  Anzahl der *zodb object loads*
 ``total cached``
  Anzahl der Cache loads
 ``modified``
  Anzahl modifizierter Objekte
 ``rss before``
  RAM-Verbrauch vor dem Request
 ``rss after``
  RAM-Verbrauch nach dem Request

`Products.LongRequestLogger`_
 Sog. *stack traces* lang laufender Requests an eine Zope2-Instanz werden periodisch in eine Log-Datei geschrieben. Die Konfiguration des ``Products.LongRequestLogger`` erfolgt über Umgebungsvariablen für diese Instanz::

  [instance]
  ...
  eggs =
      ...
      Products.LongRequestLogger

  environment-vars =
      longrequestlogger_file = ${buildout:directory}/var/log/${:_buildout_section_name_}-longrequest.log
      longrequestlogger_timeout = 4
      longrequestlogger_interval = 2

 ``longrequestlogger_file``
  Erforderliche Pfadangabe zu der Datei, in die das Log geschrieben werden soll.
 ``longrequestlogger_timeout``
  Die Anzahl in Sekunden als Fließkommazahl, nachdem das Logging beginnen soll.

  Der Standardwert ist``2``.
 ``longrequestlogger_interval``
  Die Frequenz, mit der der *stack trace* geschrieben werden soll.

  Der Standardwert ist ``1``.

`HAProxy <http://www.haproxy.org/>`_
    * `Debugging web application performance with HAProxy
      <http://blog.flyingcircus.io/2015/11/26/debugging-web-application-performance-with-haproxy/>`_
    * `Debugging web application performance with HAProxy – Part 2
      <http://blog.flyingcircus.io/2015/12/17/debugging-web-application-performance-with-haproxy-part-2/>`_
`ab`_
 Apache HTTP-Server-Benchmarking-Werkzeug, das einfache Performance-Tests erlaubt.

 Unter Debian und Ubuntu lässt sich ``ab`` installieren mit::

  $ apt-get install apache2-utils

 Anschließend kann es z.B. mit folgenden Optionen aufgerufen werden::

   $ ab -n 100 -c 3 http://www.veit-schiele.de/

 Damit wird 100-mal die Seite angefragt, wobei immer je 3 Anfragen gleichzeitig gestellt werden.

 Um die jeweiligen Einstellungen zu testen, empfiehlt es sich, zunächst die einfache Plone-Site, dann mit CacheFu und schließlich   mit Varnish zu testen.

 Mehr über Apache Benchmark erfahren Sie mit::

  $ ab -h

 Beachten Sie, dass Apache Benchmark nur die angegebene URL prüft, nicht die gesamte Seite mit Bildern und CSS-Dateien.

`TinyLogAnalyzer`_
 Mit TinyLogAnalyzer lassen sich die Antowrtzeiten des HTTP-Access-Log auswerten. Hierzu muss zunächst die Log-Datei so konfiguriert werden, dass sie auch die Antwortzeiten protokolliert::

  LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\" %T/%D" combined

 ergibt z.B. folgende Ausgabe::

  [31/Oct/2011:13:36:07 +0000] "GET / HTTP/1.1" 200 7918 "" "..." 0/95491

 Dabei ist ``0/95491`` die Zeit in Sekunden und Mikrosekunden, die de Beantwortung des Requests dauerte.

 Eine solche Log-Datei kann nun von TinyLogAnalyzer ausgewertet werden.

`Apache JMeter`_
 Apache JMeter wurde entwickelt um Last und Performance von funktionalen Tests zu messen.

`FunkLoad`_
 Mit FunkLoad lassen sich ebenfalls Lasttests auf Basis von funktionalen Tests erstellen

`Firebug <http://www.getfirebug.com/>`_
 Mit Firebug lässt sich der Traffic zwischen Ihrem Browser und der Website beobachten:

 .. figure:: firebug-net.png
    :alt: Firebug

 Dabei werden alle Requests zum Darstellen der gesamten Seite analysiert. Zudem kann man sich die *Response Headers* für jedes Objekt anzeigen lassen und so herausfinden, ob, von wem und in welchem Umfang tatsächlich gecached wird.

`YSlow <http://www.yahooapis.com/yslow/>`_
 analysiert Webseiten und teilt Ihnen mit, warum Ihre Seiten langsam dargestellt werden. YSlow ist ein Firefox Add-on, das in Firebug integriert ist.
`GTmetrix <http://gtmetrix.com/>`_
 Website, die die Ergebnisse der Messungen mit `PageSpeed <https://developers.google.com/speed/pagespeed/>`_ und `YSlow <http://www.yahooapis.com/yslow/>`_
 anzeigt, ohne dass diese Plugins installiert sein müssten. Darüberhinaus lassen sich auch *Timeline* und *History* anzeigen.

varnishstat
 Varnishstat erstellt kontinuierlich aktualisierte Statistiken einer laufenden ``varnishd``-Instanz, wobei zwischen ``Hit`` und ``MISS`` unterschieden wird.

.. _`PTProfiler`: http://pypi.python.org/pypi/Products.PTProfiler/
.. _`Call Profiler`: http://plone.org/products/callprofiler
.. _`ZopeProfiler`: http://www.dieter.handshake.de/pyprojects/zope/#bct_sec_4.8
.. _`The Python Profilers`: http://docs.python.org/library/profile.html#module-pstats
.. _`hotshot`: http://docs.python.org/lib/module-hotshot.html
.. _`profilehooks`: http://pypi.python.org/pypi/profilehooks/
.. _`profilehooks-Dokumentation`: http://mg.pov.lt/profilehooks/
.. _`TinyLogAnalyzer`: http://pypi.python.org/pypi/TinyLogAnalyzer
.. _`Products.LongRequestLogger`: http://pypi.python.org/pypi/Products.LongRequestLogger
.. _`collective.stats`: https://pypi.python.org/pypi/collective.stats
.. _`ab`: http://httpd.apache.org/docs/2.0/programs/ab.html
.. _`Apache JMeter`: http://jakarta.apache.org/jmeter/
.. _`FunkLoad`: http://funkload.nuxeo.org/

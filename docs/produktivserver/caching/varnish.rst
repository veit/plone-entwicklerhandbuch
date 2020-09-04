=======
Varnish
=======

Varnish ist ein sog. Caching Reverse Proxy, d.h. er sitzt unmittelbar nach dem Web-Server und bildet einen Zwischenspeicher für ausgehende Inhalte.

Einführung
==========

Diese Seite beschreibt, wie der `Varnish <http://varnish-cache.org/>`_ caching
Proxy mit Plone verwendet werden kann.

Installation
============

Zur Installation von Varnish empfehlen wir denPaket-Manager der jeweiligen
Distribution.

* Für Debian/Ubuntu::

      $ sudo apt-get install varnish

* Für CentOS/Fedora::

      $ yum install varnish

* Für Mac OS X::

      $ sudo port install varnish

  oder::

      $ brew install varnish

Administrieren
==============

zum Überprüfen einer Varnish-Instanz steht Ihnen ``varnishadm`` zur Verfügung::

    # varnishadm -T localhost:6082 -S /etc/varnish/secret
    200
    -----------------------------
    Varnish Cache CLI 1.0
    -----------------------------
    Linux,4.4.0-92-generic,x86_64,-junix,-smalloc,-smalloc,-hcritbit
    varnish-4.1.1 revision 66bb824

    Type 'help' for command list.
    Type 'quit' to close CLI session.

    varnish>

Beenden der Konsole
-------------------

::

    quit

Cache löschen
-------------

Cache vollständig löschen::

        # varnishadm "ban req.url ~".

Alle ``.jpg``-Dateien aus dem Cache löschen::

        # varnishadm "ban req.url ~ .jpg"

Konfiguration
=============

Eine neue ``*.vcl``-Datei kann geladen werden mit::

    # vcl.load <name> <file>

also z.B. mit::

    # vcl.load ploneconf /etc/varnish/plone.vcl

Anschließend kann sie aktiviert werden mit::

    # vcl.use ploneconf

Anschließend kann Varnish mit Buildout konfiguriert werden. Hierzu tragen Sie
folgendes in Ihre ``deploy.cfg``-Datei ein::

    [buildout]
    parts =
    ...
    varnish-config
    ...
    [varnish-config]
    recipe = collective.recipe.template
    input = templates/plone.vcl.in
    output = ${buildout:directory}/etc/plone.vcl
    backend-host = 127.0.0.1
    backend-port = 8010

Eine examplarische Varnish-Konfigurationsdatei finden Sie hier: `plone.vcl.in
<https://github.com/veit/vs_buildout/blob/master/templates/plone.vcl.in>`_.
In ihr wird das Backend spezifiziert, das auf ``localhost`` an Port ``8080``
läuft und erlaubt Anfragen via HTTP-Basic Authentication oder Cookie-basierte
Authentifizierung.

Weitere Informationen zur Varnish-Konfiguration erhalten Sie in `Varnish
Configuration Language - VCL
<http://www.varnish-cache.org/docs/2.1/tutorial/vcl.html>`_.

Log-Dateien
===========

Um einen Einträge in den Log-Dateien in Echtzeit zu sehen, können Sie folgendes
eingeben::

       # varnishlog

Statistiken
===========

Um sich in Echtzeit die Varnish-Statistik anzuzeigen ähnlich ``top``, rufen Sie
``varnishstat`` auf::

       # varnishstat
       Uptime mgt:     1+23:43:52
       Hitrate n:       10       46       46
       Uptime child:   1+23:43:53                                                       avg(n):   0.0000   0.0000   0.0000
           NAME                             CURRENT        CHANGE       AVERAGE        AVG_10       AVG_100      AVG_1000
       MAIN.uptime                       1+23:43:53
       MAIN.sess_conn                         53834          0.00           .            0.07          0.07          0.07
       MAIN.client_req                        53834          0.00           .            0.07          0.07          0.07
       MAIN.cache_hit                         14119          0.00           .            0.00          0.00          0.00
       MAIN.cache_miss                        39568          0.00           .            0.07          0.07          0.07
       MAIN.backend_reuse                     38602          0.00           .            0.07          0.07          0.07
       ...

Üblicherweise schreibt Varnish keine Log-Datei sondern hält die Informationen
nur im Arbeitsspeicher. Wenn Apache-ähnliche Protokolle aus Varnish geschrieben werden sollen, kann dies mit ``varnishncsa`` geschehen.

.. Anschließend können Sie Varnish mit dieser Konfigurationsdatei und 1 GB Cache am
   Port ``8100`` starten mit::

       $ ./bin/varnish-instance

   Dies startet den Varnish-Daemon in ``{buildout:directory}/parts/varnish-
   build/sbin/varnishd`` unter Verwendung der Konfigurationsdatei
   ``{buildout:directory}/etc/plone.vcl``.

   Auf manchen Systemen muss ``ulimit`` erhöht werden, z.B. mit::

       $ ulimit -n ${NFILES:-131072}
       $ ulimit -l ${MEMLOCK:-82000}

   Um zu überprüfen, ob der Varnish auch tatsächlich die gewünschten Dateien
   cached, stehen Ihnen diverse Werkzeuge in
   ``{buildout:directory}parts/varnish-build/bin``
   zur Verfügung:

   ``varnishtop``
       gibt die Memory-Log-Dateien in einer regelmäßig aktualisierten Liste der
       häufigsten Log-Einträge aus.
   ``varnishhist``
       gibt die Memory-Log-Dateien als regelmäßig aktualisierte Histogramme der
       Lastverteilung der letzten ``N`` Anfragen aus.
   ``varnishsizes``
       macht dasselbe wie ``varnishhist``, zeigt jedoch die Größe der Objekte und
       nicht die Zeit zum Abarbeiten der Anfragen. Dies gibt Ihnen einen guten
       Überblick über die Größe der ausgelieferten Objekte.
   ``varnishstat``
       gibt Ihnen eine detaillierte Angabe über die Anzahl der ``misses``,
       ``hits``, den verwendeten Storage, erstellte Threads und gelöschte Objekte.

   Weitere Informationen zu den statistischen Auswertungsmöglichkeiten von Varnish
   erhalten Sie in `Statistics
   <http://www.varnish-cache.org/docs/2.1/tutorial/statistics.html>`_.

Lastverteilung
==============

Mit der Verteilung der Last auf verschiedene Applikationsserver können die
angefragten Objekte schneller ausgeliefert werden.Das ``vmod_directors``-Modul
ermöglicht diese Lastverteilung auf verschiedene Weisen:

``round-robin`` (Rundlauf-Verfahren)
    greift nacheinander auf die einzelnen Instanzen zu.
``fallback``
    versucht jede Instanz aus und wählt die erste, die antwortet.
``hash``
    wählt die Instanz durch Berechnen des Hash eines Strings.

    Dies wird häufig verwendet mit ``client.ip``oder einem Session-Cookie, um
    sog. *sticky sessions* zu bekommen.

``random``
    verteilt die Last über die Instanzen mit einer gewichteten zufälligen
    Wahrscheinlichkeitsverteilung.

Das folgende Beispiel zeigt, wie Sie die Round-Robin-Lastverteilung von zwei
Plone-Instanzen konfigurieren können::

    backend instance1 {
        .host = "127.0.0.1";
        .port = "8081";
        .connect_timeout = 0.4s;
        .first_byte_timeout = 300s;
        .between_bytes_timeout  = 60s;
        .probe = {
            .url = "/";
            .timeout = 5s;
            .interval = 15s;
            .window = 10;
            .threshold = 8;
        }
    }

    backend instance2 {
        .host = "127.0.0.1";
        .port = "8082";
        .connect_timeout = 0.4s;
        .first_byte_timeout = 300s;
        .between_bytes_timeout  = 60s;
        .probe = {
            .url = "/";
            .timeout = 5s;
            .interval = 15s;
            .window = 10;
            .threshold = 8;
        }
    }

    ...

    import directors;

    sub vcl_init {
        new vdir = directors.fallback();
        vdir.add_backend(instance1);
        vdir.add_backend(instance1);
    }

    ...

    import std;

    sub vcl_recv {

        set req.backend_hint = vdir.backend();
        ...
        if (! std.healthy(req.backend_hint))  {
            set req.backend_hint = sorryserver();
            return(pass);
        }
        ...
    }

``probe``
    gibt in unserem Fall an, dass Varnish das ``/``-Objekt alle 5 Sekunden
    aufruft. Falls die Antwort länger als eine Sekunde ausbleibt, nimmt Varnish
    an, dass das Backend nicht erreichbar ist. Umgekehrt nimmt Varnish an, dass
    das Backend erreichbar ist wenn drei der letzten fünf Verbindungsversuche
    erfolgreich waren. Weitere Informationen hierzu erhalten sie in `backend
    health polling <http://varnish-cache.org/wiki/BackendPolling>`_.

.. note::
   Allgemeine Informationen zur Lastverteilung mit Varnish erhalten Sie unter
   `Backend servers
   <https://www.varnish-cache.org/docs/trunk/users-guide/vcl-backends.html>`_
   und `vmod_directors
   <https://www.varnish-cache.org/docs/trunk/reference/vmod_directors.generated.html>`_.

Migration zu Varnish 4.x
========================

* `Plone Documentation: Varnish 4.x <https://docs.plone.org/manage/deploying/caching/varnish4.html>`_
* `What’s new in Varnish 4.0 <https://varnish-cache.org/docs/4.0/whats-new/upgrading.html#changes-to-vcl>`_
* `github.com/fgsch/varnish3to4 <https://github.com/fgsch/varnish3to4>`_

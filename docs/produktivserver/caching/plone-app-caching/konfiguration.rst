================================
plone.app.caching: Konfiguration
================================

Nach dem Aktivieren finden Sie ein Caching-Kontrollfeld in der Plone-Konfiguration. Dieses Kontrollfeld enthält die folgenden Reiter:

Change Settings
===============

Global settings
---------------

Enable caching
 Falls diese Option nicht aktiviert ist, wird nicht gecacht.
Enable GZip compression
 Ist diese Option aktiv, werden die Inhalte momprimiert bevor sie zum Browser gesendet werden.

Caching proxies
---------------

Enable purging
 Ist diese Option aktiviert, schickt Plone ggf. HTTP-PURGE-Anfragen an den Caching-Proxy. Dieser muss PURGE erlauben, damit der Cache ggf. geleert werden kann.
Caching proxies
 Geben Sie hier den Domain-Namen jedes Caching Proxy an, einen je Zeile.

Content types to purge
 Ist diese Option aktiviert, kann Plone die Views von Artikeln löschen wenn sie verändert oder gelöscht wurden.
Virtual host rewriting takes place front of the caching proxy
 Aktivieren Sie diese Option, wenn Sie virtuelle Hosts mit Rewriting vor dem Caching Proxy verwenden.

Externally facing domains
 Falls Sie Rewriting mit virtuellen Hosts konfiguriert haben und Ihre Site über mehrere Domains erreichbar ist (z.B. ``http://veit-schiele.de`` und ``http://www.veit-schiele.de``), sollten alle verfügbaren Domains eingetragen werden, eine je Zeile. Dies gewährleistet, dass die PURGE-Anfragen für alle Domains gesendet werden.

In-memory cache
---------------

Maximum entries in the cache
 Wie viele Artikel sollen im Cache gespeichert werden?
Maximum age of entries in the cache
 Die maximale Zeit in Sekunden, die ein Artikel im Cache gespeichert wird bevor es gelöscht wird.
Cleanup interval
 Zeit in Sekunden, bevor der Cache gereinigt werden soll. Geringere WErte verringern den Speicherverbrauch, erhöhen jedoch die Last.

Caching operations
------------------

Ruleset mappings
````````````````

Regelsätze zur Verknüpfung von Views, PageTemplates und Ressourcen mit Caching-Operatoren. ``plone.app.caching`` enthält sechs verschiedene Regelsätze, die zusammen mit den Beschreibungen im Kontrollfeld ausgewählt werden können:

Content Feed (``plone.content.feed``)
 Regelsatz für Feeds, z.B. RSS oder ATOM.
Content files and images (``plone.content.file``)
 Regelsatz für Dateien und Bilder im Inhaltsbereich.
Content folder view (``plone.content.folderView``)
 Öffentliche Ansicht eines Artikels, der andere Artikel enthalten kann.
Content item view (``plone.content.itemView``)
 Öffentliche Ansicht eines Artikels, der keine anderen Artikel enthalten kann.
File and image resources (``plone.resource``)
 Bilder und Dateien, die enweder über das *Portal Skin Tool* ausgeliefert werden oder in registrierten Verzeichnissen im Dateisystem bereitgestellt werden.
Stable file and image resources (``plone.stableResource``)
 Über die *Resource Registries* verwaltete Ressourcen wie CSS-, Javascript- und KSS-Dateien. Dies sind Dateien, die dauerhaft gespeichert werden können, da sich die URL ändert sobald sich das Objekt selbst ändert.

Legacy template mappings
````````````````````````

Für jeden dieser Regelsätze können Sie einen der Operatoren auswählen, der mit ``plone.app.caching`` geliefert wird:

Strong caching (``plone.app.caching.strongCaching``)
 cacht im Browser und Proxy für 24 Stunden und setzt folgende Header::

  Last-Modified: <last-modified-date>
  Cache-Control: max-age=<seconds>, proxy-revalidate, public

 **Achtung:** Dies sollte nur für *Stable Ressources** verwendet werden, die sich nie ändern ohne dass sich auch ihrre URL ändert.

Moderate caching (``plone.app.caching.moderateCaching``)
 cacht im Browser, aber läuft sofort ab und cacht im Proxy für 24 Stunden.

 Der Operator wird verwendet für die Regelsätze ``plone.content.feed`` und ``plone.content.file``. Für Feeds wird dann z.B. folgender Header ausgeliefert::

  ETag: <etag-value>
  Cache-Control: max-age=0, s-maxage=<seconds>, must-revalidate

 Und für Dateien wird folgender Header gesetzt::

  Last-Modified: <last-modified-date>
  Cache-Control: max-age=0, s-maxage=<seconds>, must-revalidate

 **Achtung:** Wird ein Proxy verwendet, dessen Cache nicht zuverlässig geleert werden kann, können veraltete Inhalte ausgeliefert werden.

Weak caching (``plone.app.caching.weakCaching``)
 cacht im Browser aber läuft sofort ab und gibt anschließend den HTTP-Status-Code ``304 Not Modified`` aus.

 Im Caching-Profil ``with-caching-proxy`` wird der operator verwendet für die Regelsätze ``plone.content.itemView`` und ``plone.content.folderView``.

No caching (``plone.app.caching.noCaching``)
 die Antwort verfällt sofort im Browser und verhindert die Validierung.
Chain (``plone.caching.operations.chain``)
 erlaubt die Verwendung mehrerer Operatoren zusammen.

Standard-Mapping  von ``plone.app.caching``:

+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| Regelsatz                      | Profile                                                                                          |
+                                +--------------------------------+--------------------------------+--------------------------------+
|                                | without-caching-proxy          | with-caching-proxy             | with-caching-proxy-splitviews  |
+================================+================================+================================+================================+
| Content Feed                   | weakCaching                    | moderateCaching                | moderateCaching                |
+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| Content files and images       | weakCaching                    | moderateCaching                | moderateCaching                |
+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| Content folder view            | weakCaching                    | weakCaching                    | moderateCaching                |
+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| Content item view              | weakCaching                    | weakCaching                    | moderateCaching                |
+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| File and image resources       | strongCaching                  | strongCaching                  | strongCaching                  |
+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| Stable file and image resources| strongCaching                  | strongCaching                  | strongCaching                  |
+--------------------------------+--------------------------------+--------------------------------+--------------------------------+

Detailed settings
-----------------

Hier können Sie Parameter für individuelle Caching-Operatoren angeben:

Maximum age (``maxage``)
 Zeit in Sekunden, die die Antwort im Browser oder Caching-Proxy gespeichert werden soll.

 Fügt der Antwort einen ``Cache-Control: max-age=<value>``-Header und einen passenden ``Expires``-Header hinzu.

Shared maximum age (``smaxage``)
 Zeit in Sekunden, die die Antwort im Caching-Proxy gespeichert wird.

 Fügt der Antwort einen ``Cache-Control: s-maxage=<value>``-Header hinzu.

ETags (``etags``)
 Eine Liste der ETag-Komponenten, die mit dem ETag-Header ausgegeben werden sollen.

 Darüberhinaus wird eine ``304 Not Modified``-Antwort generiert für Antworten auf ``If-None-Match``-Anfragen.

Last-modified validation (``lastModified``)
 Fügt der Antwort einen ``Last-Modified``-Header hinzu und ``304 Not Modified``-Antworten auf ``If-Modified-Since``-Anfragen.

RAM cache (``ramCache``)
 cacht im Zope-RAM-Cache. Ist die URL nicht eindeutig, können entweder ETags oder Last-Modified der Liste der Parameter hinzugefügt werden um einen Unique Cache Key zu erzeugen.

Vary (``vary``)
 Namen der HTTP-Headers in der Anfrage einer URL, die der Caching Proxy für das Ausliefern einer gecachten Antwort benötigt.

Anonymous only (``anonOnly``)
 Wird der Wert auf ``True`` gesetzt, so erhalten angemeldete Nutzer immer die aktuellen Inhalte.

 Dies funktioniert am besten zusammen mit dem *moderate caching*-Operator.

 Beachten Sie bitte, dass im Caching Proxy der Vary-Header für ``X-Anonymous`` gesetzt ist.

Request variables that prevent caching (``cacheStopRequestVariables``)
 Eine Liste von Variablen in der Anfrage (einschließlich Cookies), die das Caching verhindern sollen.

Import settings
===============

Hier können vordefinierte Profile mit Caching-Einstellungen importiert werden.

``plone.app.caching`` kommt mit drei Standard-Caching-Profilen:

- Ohne Caching Proxy

  Diese Einstellungen sind hilfreich, wenn kein Caching Proxy verwendet wird.

- Mit Caching Proxy

  Diese Einstellungen sind hilfreich wenn ein Caching Proxy wie Squid oder Varnish verwendet wird. Dieses Profil unterscheidet sich im wesentlichen dadurch vom Profil *Ohne Caching Proxy*, dass Dateien und Bilder im Proxy Cache gespeichert werden können.

- Mit Caching Proxy (und Split-View-Caching)

  Ein Beispiel für ein Profil, das unterschiedliche Ansichten bereitstellt.

Purge Caching-Proxy
===================

Hier können manuell Inhalte des Caching-Proxy gelöscht werden.

Dieser Reiter wird nur angezeigt, wenn Sie in *Change Settings* Purging erlaubt haben.

RAM-Cache
=========

Hier können Sie Statistiken zu Purging und RAM-Cache betrachten.

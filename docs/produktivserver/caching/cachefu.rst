=======
CacheFu
=======

CacheFu ist eine Sammlung von Produkten, die die Darstellung von Seiten einer Plone-Site deutlich beschleunigen kann, wobei auch Caching-Proxies wie Squid und Varnish unterstützt werden.

CacheFu lässt sich einfach mit Buildout installieren indem unter ``eggs`` im ``[buildout]``-Abschnitt ``Products.CacheSetup`` angegeben wird.

Nachdem ``./bin/buildout`` aufgerufen und die Instanz neu gestartet wurde, lässt sich *CacheSetup* in der Website-Konfiguration unter Zusatzprodukte für die Plone-Site installieren. Anschließend finden Sie in der Konfiguration von Zusatzprodukten *Cache Configuration*.

- Im *Main*-Reiter kann CacheFu eingeschaltet und die verwendete Cache Policy angegeben werden. Außerdem kann zwischen verschiedenen Server-Konfigurationen gewählt werden.
- Im *Policy*-Reiter kann zwischen verschiedenen Policies gewählt oder neue erstellt werden.
- Im *Rules*-Reiter können Regeln angegeben werden, wobei zwischen drei verschiedenen Arten unterschieden wird:

  Content Cache Rule
   Eine Regel für Artikeltypen.
  PolicyHTTPCacheManager Cache Rule
   Regel für Objekte, die mit einem PolicyHTTPCachingManager assoziiert sind.
  Template Cache Rule
   Regel für Page Templates.

  Dabei wird immer die erste passende Regel verwendet.

- Im *Headers*-Reiter können HTTP-Header-Angaben für eine spezifische Policy angegeben werden.

  - Mit  ``max_age`` wird der *Expires Header* gesetzt, der dem Browser mitteilt, ob die Seite ohne Revalidierung erneut geladen werden darf. Wenn ``max_age`` in einem der Header Sets von CacheSetup auf ``0`` gesetzt wird, werden in der Ausgabe der Response Headers 10 Jahre abgezogen, um nicht-synchronisierte Clients abzufangen.
  - ``s-maxage`` gibt die Zeit an, die eine Seite im Proxy-Cache gehalten werden darf.

CacheFu für ``vs.registration``-Artikeltypen
============================================

Um die beiden in ``vs.registration`` definierten Artikeltypen für CacheFu zu konfigurieren, gehen Sie im *Rules*-Reiter zunächst zur *Content*-Cache-Regel und fügen dort *Registrant* zu den *Content Types* hinzu. Damit werden die Inhalte für nicht-angemeldete Nutzer bis zu einer Stunde im Proxy gespeichert.

Für angemeldete Nutzer werden die Inhalte mit einem *ETag* versehen, das verschiedenen Angaben wie Member ID und Modifikationsdatum enthält. *ETags* werden an den Browser gesendet, damit dieser entscheiden kann, ob eine Seite aus dem Cache geladen werden darf oder vom Server neu angefordert wird. Dabei nutzen verschiedene Nutzer jedoch nicht denselben Cache, damit auch das Caching personalisierter Seiten möglich ist. Der *ETag* hat normalerweise eine Laufzeit von einer Stunde (3600 Sekunden), danach wird das Objekt erneut abgerufen.

Schließlich ist noch *Registration* in die *Container*-Cache-Regel einzutragen.

Übernahme der Cache-Settings in unser Policy-Produkt
====================================================

Die Cache-Settings lassen sich exportieren und in andere Plone-Sites importieren indem im *Import*-Reiter des *Generic Setup Tool* das *CacheSetup*-Profil ausgewählt wird und anschließend im *Export*-Reiter die Einstellungen des *CacheFu Settings Tool* exportiert werden. Die ``cachesettings.xml``-Datei kann dann in das Standardprofil von ``vs.policy`` übernommen werden.

.. seealso::

    * `Initial setup and background`_
    * `Cachefu strategy`_
    * `Debugging cache settings`_

.. _`Initial setup and background`: http://guidelines.zestsoftware.nl/caching/caching1_background.html
.. _`Cachefu strategy`: http://guidelines.zestsoftware.nl/caching/caching2_cachefu.html
.. _`Debugging cache settings`: http://guidelines.zestsoftware.nl/caching/caching3_debugging.html

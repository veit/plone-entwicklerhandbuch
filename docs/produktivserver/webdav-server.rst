=============
WebDAV-Server
=============

Um einen WebDAV-Server zu konfigurieren kann z.B. im ``instance``-Abschnitt folgendes angegeben werden::

 webdav-address = 8091
 webdav-force-connection-close = off

.. Falls der Port des WebDAV-Servers auf denselben Port gelegt wird wie der Web-Server, kann Zope die meisten WebDAV-Clients erkennen und liefert dann nicht die komplette HTML-Seite sondern nur den Quelltext aus. Falls Zope den WebDAV-Client nicht kennen sollte, kann dieser auch explizit angegeben werden::

  zope-conf-additional =
      <http-server>
          webdav-source-clients WebDAVFS
      </http-server>

``enable-ms-author-via``
 Wird der Wert auf ``true`` gesetzt, können auch ältere Microsoft Web Folders- und Microsoft Office-Versionen sich mit dem Zope-Server verbinden. Der Standardwert ist ``off``, da hierdurch einige standardkonforme Anfragen schwierig werden. Weitere Informationen erhalten Sie unter http://www.zope.org/Collectors/Zope/1441

``enable-ms-public-header``
 Wird der Wert auf ``true`` gesetzt, wird ein ``Public``-Header als Antwort auf eine WebDAV-OPTIONS-Anfrage gesendet::

  zope-conf-additional =
      ...
      enable-ms-public-header on

 Versionen von Microsofts Web Folders ab Januar 2005 benötigen diese Header-Angabe (s.a.: http://www.redmountainsw.com/wordpress/archives/webfolders-zope).

Apache für WebDAV konfigurieren
===============================

Mit dem Webserver Apache 2 lässt sich der Zugriff auf WebDAV-Ressourcen komfortabel einrichten. Benötigt werden die Module ``dav`` und ``dav_fs``, die im Lieferumfang enthalten sind.

Die Standardkonfiguration umfasst neben der Anweisung zum Laden der Module lediglich eine Zeile zum Pfad der Datenbank für ``DAVLockDB``.

Nach dem Neustart des Webservers ist die Plonesite unter der browser-üblichen Adresse mit ``http://`` zu erreichen. Die Angabe eines zusätzlichen Ports in der Form ``http://www.veit-schiele.de:8091/`` entfällt. Die Konfiguration von Clients ist im `Plone-Nutzerhandbuch`_ näher beschrieben.

Für Clients, die mit fehlenden ´´/´´ am Ende nicht korrekt umgehen, kann der Apache wie folgt konfiguriert werden::

 <IfModule mod_setenvif.c>
  BrowserMatch "Microsoft Data Access Internet Publishing Provider" redirect-carefully
 </IfModule>

Zu den Details der möglichen Konfiguration mit ``mod_setenvif`` siehe auch `Apache-Umgebungsvariablen`_ in der offiziellen Apache-Dokumentation.

.. _`Plone-Nutzerhandbuch`: http://www.plone-nutzerhandbuch.de/plone-benutzerhandbuch/webdav

.. _`Apache-Umgebungsvariablen`: http://httpd.apache.org/docs/2.0/env.html.

======
Apache
======

Module
======

Damit der Apache-Webserver Anfragen an Zope weiterleiten kann, muss das ``mod_rewrite`` Modul mit seinen Abhängigkeiten in Apache’s ``httpd.conf`` angegeben werden::

 LoadModule alias_module    /usr/lib/apache2/modules/mod_alias.so
 LoadModule proxy_module    /usr/lib/apache2/modules/mod_proxy.so
 LoadModule proxy_http      /usr/lib/apache2/modules/mod_proxy_http.so
 LoadModule rewrite_module  /usr/lib/apache2/modules/mod_rewrite.so

Bei Debian- und Ubuntu-Distributionen kann die Konfiguration der Module vereinfacht werden mit ``a2enmod``. Die oben angegebenen Module lassen sich dann einfach aktivieren mit::

 $ a2enmod alias proxy proxy_http rewrite

In anderen Distributionen werden die Module meist schon verwendet oder die einzelnen Zeilen müssen nur noch auskommentiert werden.

Virtual Hosts
=============

Anschließend können Sie in ``httpd.conf`` oder einer eingebundenen Datei einen Virtual Host für die Domain ``www.veit-schiele.de`` angeben::

 NameVirtualHost 83.223.91.163:80
 <VirtualHost 83.223.91.163:80>
     ServerName    www.veit-schiele.de
     RewriteEngine on
     RewriteRule   ^/(.*) http://83.223.91.163:8082/VirtualHostBase/http/%{SERVER_NAME}:80/vs/VirtualHostRoot/$1 [P]
 </VirtualHost>

Dies definiert den *Virtual Host* für die Domain ``www.veit-schiele.de`` wenn Anfragen am Port ``80`` hereinkommen. Die IP-Adresse ``83.223.91.163`` sollte derjenigen in der ``Listen``-Anweisung entsprechen::

 Listen 83.223.91.163:80

Bei Debian- und Ubuntu-Distributionen kann die Erstellung von Virtual Hosts vereinfacht werden mit ``a2ensite``. Der oben angegebene Virtual Host lässt  sich dann einfach aktivieren mit::

 # a2ensite www.veit-schiele.de
 Site www.veit-schiele.de installed; run /etc/init.d/apache2 reload to enable.

Schließlich wird unter Verwendung der RewriteEngine eine RewriteRule definiert, die für alle dem regulären Ausdruck ``^(.*)``  entsprechenden URLs weiterleitet:

#. ``http://83.223.91.163:8082`` verweist auf den Zope-Server, auf den weitergeleitet wird;
#. ``VirtualHostBase`` informiert das VirtualHostMonster über Protokoll und Host auf den umgeschrieben werden soll. In diesem Fall auf ``http`` und ``veit-schiele.de:80``.
#. Als nächstes wird der Pfad auf das Objekt angegeben, das die *Site Root* sein soll, also unsere Plone-Site. ``VirtualHostRoot`` beendet die Pfadangabe
#. Mit ``$1`` wird Apache nun mitgeteilt, dass alle, dem regulären Ausdruck entsprechenden Teile der URL hier angehängt werden sollen.
#. ``L`` weist Apache an, wenn diese Regel zutreffend war, nicht nach weiteren Regeln zu suchen und ``P`` aktiviert das ``mod_proxy``-Modul, das das URL-Mapping übernimmt.

Anschließend kann Apache mit ``apachectl graceful`` neu gestartet werden und die Plone-Site sollte dann unter ``http://www.veit-schiele.de`` erreichbar sein.

**Anmerkung:** Das root-Verzeichnis des ZMI ist nicht über den virtuellen Host erreichbar. hierzu muss weiterhin ``83.223.91.163:8082`` aufgerufen werden.

Verschlüsselte Verbindungen
===========================

Üblicherweise liefern wir die gesamte Site ``https``-verschlüsselt aus. Dabei
wird beim Zugriff auf ``http://www.veit-schiele.de`` weitergeleitet mit::

 Redirect permanent / https://www.veit-schiele.de/

Für ``https://www.veit-schiele.de`` benötigt der Apache dann das SSL-Modul::

 LoadModule ssl_module      /usr/lib/apache2/modules/mod_ssl.so

Anschließend können Sie einen weiteren Virtual Host für die Domain ``www.veit-schiele.de`` am SSL-Port ``443`` angeben::

 NameVirtualHost 83.223.91.163:443
 <VirtualHost 83.223.91.163:443>
     ServerName            www.veit-schiele.de
     SSLEngine             on
     SSLCertificateFile    /etc/apache2/ssl.crt/server.crt
     SSLCertificateKeyFile /etc/apache2/ssl.key/server.key
 </VirtualHost>

Schließlich muss noch die ``Listen``-Anweisung für Anfragen am SSL-Port ``443`` eingetragen werden.

Login via SSL
-------------

Falls z.B. aus Performance-Gründen die Kommunikation der anonymen Nutzer nicht verschlüsselt werden soll, kann bei der Anmeldung auf einen anderen
``VirtualHost`` mit SSL-Verschlüsselung weitergeleitet werden. Umgekehrt sollen
die Nutzer bei der Abmeldung wieder unverschlüsselt auf die Site zugreifen
können. Entsprechend kommt für den VirtualHost an Port ``80`` folgende Rewrite-Regel hinzu::

  # Rewrites the came_from in the URL for https
  RewriteCond %{QUERY_STRING} came_from=http(.*)
  RewriteRule ^/(.*)login_form$ https://edit.veit-schiele.de/$1login_form?came_from=https%1 [NE,L]

Beachten Sie, dass ``?came_from=`` nicht direkt in einer ``RewriteRule`` angegeben werden kann und daher der ``QUERY_STRING`` zunächst in der ``RewriteCond`` ausgelesen wird.

Wird ``login_form`` direkt oder auf einem ungültigen Template (z.B. ``logged_out``) aufgerufen, wird folgende zusätzliche Regel benötigt::

  # Switches to https when hit login_form or login_success
  RewriteRule ^/login_(.*) https://edit.veit-schiele.de/login_$1 [NE,L]

Schließlich können in der Konfigurationsdatei des VirtualHost an Port ``443`` noch folgende RewriteRules angegeben werden::

  # Switches to http upon logout
  RewriteRule ^/(.*)logged_out http://www.veit-schiele.de/$1logged_out [L,P]

  # Keeps on https until log out
  RewriteRule ^/(.*) http://83.223.91.163:8080/VirtualHostBase/https/%edit.veit-schiele.de:443/vs/VirtualHostRoot/$1 [L,P]

**Amerkung 1:** Die Anleitung verweist bewusst auf einen anderen ``ServerName``,
da die Browser in ihrer Cookie-Verwaltung nicht zwischen ``http`` und ``https``
unterscheiden und daher versehentlich doch die Zugangsdaten unverschlüsselt
übertragen werden könnten.

**Amerkung 2:** Die Anleitung zur Anmeldung via SSL funktioniert nicht für das Login-Portlet.

.. `Setting up Plone behind Apache with SSL`_
.. `Zope behind an Apache 2 webserver`_
.. _`Setting up Plone behind Apache with SSL`: http://plone.org/documentation/how-to/apache-ssl
.. _`Zope behind an Apache 2 webserver`: http://cheimes.de/opensource/docs/zope-apache2

Management-Ansicht im öffentlichen Netz verbieten
=================================================

Hierzu wird die Konfiguration des VirtualHost folgendermaßen erweitert::

 # Forbidden HTTP status for all path components beginning with manage
 RedirectMatch 403 /manage

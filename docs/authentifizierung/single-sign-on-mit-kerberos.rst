Single Sign On mit Kerberos
===========================

Um eine lauffähige Kerberos-Umgebung sowie eine Plone bzw. Zope-Website mit
Single Sign On zu erhalten, sind Anpassungen auf mehreren Ebenen notwendig:

#. Einrichtung eines zentralen Kerberos-Servers (KDC, Key Distribution Center)
#. Einrichtung des Betriebssystems des vorgelagerten Webservers, sodass
   Kerberos-Tickets vom KDC bezogen werden können
#. Einrichtung des Betriebssystems des Website-Benutzers, sodass es beim
   Maschinen-Login Kerberos-Tickets vom KDC bezieht
#. Einrichtung des vorgelagerten Webservers, in diesem Falle Apache
#. Installation eines Zope-Zusatzproduktes, damit der User Folder die vom
   Webserver zusätzlich zur Verfügung gestellten Authentifizierungsdaten
   auswertet

Dieses Dokument befasst sich lediglich mit der serverseitigen Einrichtung. Das
Betriebssystem des Benutzers der Website muss also bereits so konfiguriert sein,
dass der Logon für den Benutzer bereits über Kerberos abgewickelt wird.

Unser Beispielsystem setzt auf einem Linux-Server auf, der als Kerberos-Server
konfiguriert wird. Der Apache-Server läuft ebenfalls unter Linux und agiert als
Kerberos-Client. Beim Anmeldevorgang wird automatisch ein Kerberos-Ticket
bezogen, welches die spätere Abwicklung der Kerberos-Authentifizierung zur
Website ermöglicht. Das Einrichten einer solchen Konstellation ist auf dem
Internet vielfach beschrieben, siehe auch die Weiterführenden Links am Ende des
Dokumentes.

Installation des ``mod_auth_kerb``-Authentication-Modul
=======================================================

Für Apache wird das Zusatzmodul ``mod_auth_kerb`` benötigt, welches unter Linux
mit den Bordmitteln des Betriebssystems installiert werden kann, wie z.B.
``apt-get`` unter Debian und Ubuntu oder ``yum`` unter RedHat-Systemen::

    # apt-get install libapache2-mod-auth-kerb

oder::

    # yum install mod_auth_kerb

Falls das Modul anschließend nicht automatisch geladen wird, kann dies manuelle
geschehen mit::

    # LoadModule auth_kerb_module /usr/lib/apache2/modules/mod_auth_kerb.so

Je nach OS muss der Pfadname des Moduls noch angepasst werden.

Da die Header der HTTP-Anfrage von Apache modifiziert werden, muss auch
``mod_headers`` installiert sein. In unserer Beispielkonfiguration wird Apache
als Proxy für Plone verwendet, womit auch ``mod_rewrite`` und ``mod_proxy`` aktiv sein müssen.

Erstellen eines *Service Principal*
===================================

Der *Service Principal* kann erstellt werden mit folgendem kadmin-Befehl::

    # kadmin -p bofh/admin -q "addprinc -randkey HTTP/www.example.com"

Erstellen einer Schlüsseltabelle (``keytab``)
=============================================

Ein keytab ist eine Datei zum Speichern der Schlüssel für einen oder mehrere
Kerberos-Prinzipals. ``mod_auth_kerb`` benötigt diese Tabelle um den oben
erstellten Service Principal nutzen zu können.

#. Die Schlüsseltabelle kann mit ``kadmin`` erstellt werden::

        # kadmin -p bofh / admin -q "ktadd -k /etc/apache2/http.keytab HTTP / www.example.com"

   oder auf RedHat-basierten Systemen im Pfad ``/etc/httpd/http.keytab``.

   Die ``-k``-Option spezifiziert den Pfadnamen der ``keytab``-Datei, die
   erstellt wird sofern sie noch nicht existiert.

   Anschließend muss der Eigentümer so geändert werden, dass der Apache-Prozess
   darauf zugreifen kann::

    # chown www-data /etc/apache2/http.keytab

   oder auf RedHat-basierten Systemen::

    # chown apache /etc/httpd/http.keytab

   Um zu überprüfen, ob der Schlüssel korrekt in die ``keytab`` eingetragen
   wurde, sollten wir uns als *Service Principal* authentifizieren und uns
   anschließend das resultierende Granting-Ticket mit ``klist`` anzeigen lassen::

    # kinit -k -t /etc/apache2/http.keytab HTTP/www.example.com
    # klist

Konfigurieren des Apache-Webservers
===================================

In der unten gezeigten Apache-Konfiguration lauscht die Zope-Instanz auf IP
``10.0.0.2`` am Port ``8080``, und Apache auf ``10.0.0.1`` am Port ``80``. Das
Plone-Portal befindet sich in der Zope-Instanz unter dem Pfad ``/portal``. In
Kerberos wird der Realm-Wert ``MYDOMAIN`` verwendet::

    <VirtualHost 10.0.0.1:80>
        ServerAdmin webmaster@mydomain.com
        ServerName intranet.mydomain.com

        <Location />
            AuthName "Intranet"
            AuthType  Kerberos
            KrbAuthoritative on
            KrbAuthRealms  MYDOMAIN
            KrbServiceName HTTP
            Krb5Keytab /etc/krb5.keytab
            KrbMethodNegotiate on
            KrbMethodK5Passwd off
            KrbSaveCredentials on
            require valid-user
            RequestHeader set X_REMOTE_USER %{remoteUser}e
        </Location>

        RewriteEngine On
        RewriteRule ^/(.*) http://10.0.0.2:8080/VirtualHostBase/http/intranet.mydomain.com:80/portal/VirtualHostRoot/$1 [L,P,E=remoteUser:%{LA-U:REMOTE_USER}]
    </VirtualHost>

Um diese Konfiguration nun verwenden zu können, muss der Apache-Webserver neu
gestartet werden mit::

    # service apache2 force-reload

Wie man erkennen kann, reicht das Einfügen der ``mod_auth_kerb``-Direktiven in
eine ``Location``-Direktive. Kerberos wird als Authentifizierungsmechanismus
festgelegt, und es wird eine positive Identifikation des Benutzers zum Zugriff
erfordert (require valid-user). Wichtig hierbei ist das Abschalten von
``KrbMethodK5Passwd``, um eine Abfrage und Übertragung des Kerberos-Logins
zwischen Browser und Apache zu verhindern. Es wird ausschliesslich die
Negotiate-Methode zugelassen (``KrbMethodNegotiate``), bei der keine Logins über
das Netz geschickt werden, sondern nur Kerberos-Ticket-Informationen.

Die Plone-Instanz selber muss kein Kerberos verstehen. Wie man in der
Apache-Konfiguration ersehen kann, wird der ermittelte Benutzername in einen
zusätzlichen HTTP-Header ``X_REMOTE_USER`` geschrieben und so weitergeleitet.

Beim Einsatz von ``mod_auth_kerb`` in Apache muss man beachten, dass man
Kerberos-Authentifizierung nicht mit anderen Authentifizierungen kombinieren
kann. Es ist nicht möglich, bei erfolgloser Kerberos-Authentifizierung auf z.B.
normale Basic Auth zurückzufallen. Ferner ist es nicht möglich, diese
Authentifizierung optional zu gestalten, sodass auch bei erfolglosem Kerberos-
Versuch der Besuch der Website gestattet wird. Das heisst, man kann auf einem
für Kerberos-Authentifizierung eingerichteten Hostnamen keine Besucher bedienen,
die anonym durchgelassen werden sollen oder die auf andere Weise authentifiziert
werden können.

Plone-Konfiguration
===================

#. Auf der Plone-Seite reicht die Installation und Konfiguration eines
   Zusatzproduktes, welches den von Apache gesetzten zusätzlichen HTTP-Header
   versteht und auswertet. Für unser Beispiel benutzen wir
   `Products.WebserverAuth
   <http://pypi.python.org/pypi/Products.WebServerAuth>`_
   (siehe auch Weiterführende Links unten). Das Produkt kann als Python Egg
   einfach in einen bestehenden Plone-Buildout eingebunden werden::

    [instance]
    …
    eggs =
        …
        Products.WebServerAuth

#. Nachdem das Buildout-Skript durchlaufen und die Instanz neu gestartet wurde,
   sollte in portal-url → site setup → Add-on Products *WebServerAuth* aktiviert
   werden können.

#. Damit wird im ``PluggableAuthService`` des Portals das
   ``WebServerAuth``-Plugin  zur Verfügung gestellt.

   Von der Standardkonfiguration auf dem Reiter *Options* wurde nur in einem
   Punkt abgewichen: Wir haben die Option ``"Only users with a pre-existing
   Plone account"`` gewählt, um nur solche Kerberos-Benutzer durchzulassen, die
   auch in der Plone-Instanz bekannt sind.

   Zudem muss das neue Plugin in unserer Beispielkonfiguration nur für zwei
   Dienste aktiviert werden, nämlich für ``Authentication`` und ``Extraction``.

   ``Extraction``
    ist für das Ermitteln von Login-Daten aus der hereinkommenden HTTP-Anfrage
    zuständig. Da jeder Zugriff über Apache automatisch den vom neuen Plugin
    ausgewerteten HTTP-Header enthält und die Verarbeitung dieses Headers
    schnell und einfach ist, setzen wir das neue Plugin als erstes aktives
    Extraction-Plugin ein.
   ``Authentication``
    nimmt die im ersten Schritt ermittelten Login-Daten und prüft, ob ein
    Benutzer mit diesen Login-Daten bekannt ist und angemeldet werden kann. Da
    in unserem Beispielszenario die Benutzer in ActiveDirectory vorgehalten
    werden und auch Plone dort die Benutzerdaten sucht, ist das neue Plugin als
    letztes aktives Authentication-Plugin geführt. Somit wird am bisherigen
    Verfahren vor dem Einsatz von Kerberos am wenigsten geändert.

#. Der Abmelden-Link des Plone-Portal (ZMI → Plone-Portal → portal_actions →
   Benutzer → Logout) sollte auf eine spezielle Logout-Seite umleiten, die z.B.
   den folgenden Inhalt trägt:

   *»Sorry, Sie müssen Ihren Web-Browser schließen um sich von diesem Portal
   abzumelden.«*

   Hierzu können Sie auch das ``logged_out``-Template entsprechend anpassen.

#. Das Login-Portlet sollte nicht angezeigt werden.
#. Der *Password ändern*-Link (z.B. in ZMI → Plone-Portal → portal_controlpanel)
   sollte ebenfalls nicht mehr angezeigt werden.

Zusammenfassung
===============

Nach den oben genannten Konfigurationsschritten sollte ein korrekt auf Windows
angemeldeter und in Plone bekannter Benutzer bei Besuch der Plone-Instanz sofort
und ohne Umweg über die Login-Maske angemeldet sein. Das ist schnell erkennbar
daran, dass z.B. kein Login-Link mehr angeboten wird, wohl aber eines auf die
eigenen Inhalte und Präferenzen.

Bei Problemen ist besonders das Dokument `Using mod_auth_kern and Windows
2000/2003 as KDC <http://www.grolmsnet.de/kerbtut/>`_ hilfreich. Es erklärt in
kleinen Schritten, wie die Konfiguration geprüft und Fehler ausgemerzt werden können.

Auf der Plone-Seite kann man die korrekte Weitergabe der Login-Informationen
sehr einfach mit einer simplen DTML-Methode testen, die die Werte des
``REQUEST`` ausgibt::

    <dtml-var REQUEST>

Dort muss im Bereich environ ein Header namens ``HTTP_X_REMOTE_USER`` sichtbar
sein, der den vollen Kerberos-Login-Namen des Benutzers enthält. Ist er es
nicht, wurde der Login nicht korrekt von Apache weitergegeben.

.. seealso::

    - `Single Sign On with Active Directory
      <http://plone.org/documentation/how-to/single-sign-on-with-active-directory>`_
    - `How to set up a Kerberos Server under Linux
      <http://beginlinux.com/blog/2010/02/kerberos-server-set-up/>`_
    - `Step by step guide to Kerberos 5 interoperability
      <http://technet.microsoft.com/en-us/library/bb742433.aspx>`_
    - `mod_auth_kerb Dokumentation
      <http://modauthkerb.sourceforge.net/configure.html>`_

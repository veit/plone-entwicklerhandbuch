===================
Verzeichnisstruktur
===================

``bin/``
 Verzeichnis, das alle Skripte dieses Projekts enthält, einschließlich der Skripte von Paste, Repoze, Zope, ZODB und ZEO.

 Die Repoze-Skripte sind:

 ``addzope2user``
  fügt einen Nutzer mit *Manage*-Rechten in Zopes ``acl_users``-Ordner hinzu; äquivalent zu ``zopectl adduser``.
 ``debugzope2``
  startet einen Python-Interpreter wobei das Zope-Objekt an ``app`` gebunden wird.
 ``runzope2script``
  startet ein Python-Skript wobei das Zope-Objekt an ``app`` gebunden wird; äquivalent zu ``zopectl run``.

``etc/``
 Verzeichnis, das die Konfigurationsdateien enthält, z.B.

 ``zope2.ini``
  Paste-Konfigurationsdatei,
 ``zope.conf`` und ``site.zcml``
  Zope-Konfigurationsdatei
 ``apache2.conf``
  mod_wsgi-Konfiguration für den Apache-Webserver.

``import/``
 Verzeichnis, um die ``.zexp``-Dateien importieren zu können.
``Products/``
 Verzeichnis, das klassische Zope2-Produkte enthalten kann.
``var/``
 Verzeichnis mit den Daten der Zope-Instanz.

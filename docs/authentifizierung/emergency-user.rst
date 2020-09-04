==============
Emergency user
==============

Sollten bei einer bereits existierenden Zope-Datenbank die Zugangsdaten verlorengegangen oder die Sicherheitseinstellungen so verändert haben, dass Sie selbst nicht mehr die notwendigen Änderungen vornehmen können, so gibt es ein Skript für die Zope-Instanz, mit dem Sie erneut Zugang zum ZMI erhalten können. Dieses Skript kann im Buildout-Verzeichnis folgendermaßen aufgerufen werden::

 $ cd parts/instance/
 $  python ../../parts/zope2/utilities/zpasswd.py access
 Username: veit
 Password:
 Verify password:
 Please choose a format from:

 SHA - SHA-1 hashed password (default)
 CRYPT - UNIX-style crypt password
 CLEARTEXT - no protection

 Encoding: SHA
 Domain restrictions:

``encoding``
 gibt die Art der Verschlüsselung an.
``domains``
 Domainnamen, von denen aus dieser Nutzer sich anmelden kann.

Anschließend sollte sich die Instanz starten lassen und der soeben erzeugte Nutzer sollte sich nun im ZMI anmelden können. Innerhalb des ZMI hat dieser sog. *emergency user* dann allerdings nicht die vollen Administrationsrechte sondern nur diejenigen zum Anlegen neuer Nutzer und Ändern der Sicherheitseinstellungen. Sie können also nun z.B. einen neuen Nutzer mit Management-Rechten anlegen, anschließend die Instanz stoppen. Nach dem erneuten Starten der Instanz sollten Sie als der im ZMI angelegt Nutzer wieder anmelden können. Vergessen Sie bitte nicht, die  ``access``-Datei wieder zu löschen.

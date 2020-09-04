Installieren und Konfigurieren des LDAP-Servers
===============================================

Die LDAP-Verbindung wird anhand eines OpenLDAP-Servers demonstriert.

Installation
------------

OpenLDAP kann heruntergeladen werden von http://www.openldap.org/. Es ist jedoch auch in vorkonfigurierten Pakete für viele Betriebssysteme verfügbar. Für Debian und Ubuntu können Sie diese installieren mit::

 # apt-get install slapd ldapscripts

.. Alternativ kann OpenLDAP auch mit Buildout installiert werden. Sehen Sie hierzu `LDAP, Certificates and Buildout, oh my! Bringing LDAP and SSL/SASL/TLS certificates into the buildout fold`_

Konfiguration
-------------

Falls der LDAP-Server noch nicht gestartet wurde, kann dies mit folgender Angabe erfolgen::

 # /etc/init.d/slapd restart

Anschließend lassen sich einige der von Ubuntu im ``LDIF``-Format mitgelieferten Schemata hinzufügen::

 # ldapadd -Y EXTERNAL -H ldapi:/// -f /etc/ldap/schema/cosine.ldif
 # ldapadd -Y EXTERNAL -H ldapi:/// -f /etc/ldap/schema/inetorgperson.ldif
 # ldapadd -Y EXTERNAL -H ldapi:/// -f /etc/ldap/schema/nis.ldif

Nachdem diese allgemeinen Schemata hinzugefügt worden sind, wird nun noch eine initiale ``cn=config``-Datenbank aufgesetzt, die die gesamte Konfiguration des OpenLDAP-Servers enthält. Hierzu erstellen wir zunächst die Datei ``db.ldif`` mit folgendem Inhalt::

 ###########################################################
 # DATABASE SETUP
 ###########################################################

 # Load modules for database type
 dn: cn=module{0},cn=config
 objectClass: olcModuleList
 cn: module{0}
 olcModulePath: /usr/lib/ldap
 olcModuleLoad: {0}back_hdb

 # Create directory database
 dn: olcDatabase={1}hdb,cn=config
 objectClass: olcDatabaseConfig
 objectClass: olcHdbConfig
 olcDatabase: {1}hdb
 olcDbDirectory: /var/lib/ldap
 olcSuffix: dc=veit-schiele,dc=de
 olcRootDN: cn=admin,dc=veit-schiele,dc=de
 olcRootPW: 1234
 olcAccess: {0}to attrs=userPassword,shadowLastChange by dn="cn=admin,dc=veit-schiele,dc=de" write by anonymous auth by self write by * none
 olcAccess: {1}to dn.base="" by * read
 olcAccess: {2}to * by dn="cn=admin,dc=veit-schiele,dc=de" write by * read
 olcLastMod: TRUE
 olcDbCheckpoint: 512 30
 olcDbConfig: {0}set_cachesize 0 2097152 0
 olcDbConfig: {1}set_lk_max_objects 1500
 olcDbConfig: {2}set_lk_max_locks 1500
 olcDbConfig: {3}set_lk_max_lockers 1500
 olcDbIndex: uid pres,eq
 olcDbIndex: cn,sn,mail pres,eq,approx,sub
 olcDbIndex: objectClass eq


 ###########################################################
 # DEFAULTS MODIFICATION
 ###########################################################
 # Some of the defaults need to be modified in order to allow
 # remote access to the LDAP config. Otherwise only root
 # will have administrative access.

 dn: cn=config
 changetype: modify
 delete: olcAuthzRegexp

 dn: olcDatabase={-1}frontend,cn=config
 changetype: modify
 delete: olcAccess

 dn: olcDatabase={0}config,cn=config
 changetype: modify
 add: olcRootPW
 olcRootPW: {CRYPT}7hzU8RaZxaGi2

 dn: olcDatabase={0}config,cn=config
 changetype: modify
 delete: olcAccess

Diese Konfiguration wird nun mit folgendem Befehl eingelesen::

 # ldapadd -Y EXTERNAL -H ldapi:/// -f db.ldif

Nun sollten noch minimale Einträge für den *LDAP DIT* (Directory Information Tree) angelegt werden. Hierzu erstellen wir eine weitere Datei ``base.ldif`` mit folgendem Inhalt::

 # Top level - the organization
 dn: dc=veit-schiele,dc=de
 objectClass: dcObject
 objectclass: organization
 o: veit-schiele.de
 dc: veit-schiele
 description: Top level

 # LDAP admin
 dn: cn=admin,dc=veit-schiele,dc=de
 objectClass: simpleSecurityObject
 objectClass: organizationalRole
 cn: admin
 userPassword: 1234
 description: LDAP admin

Dadurch wird der Benutzer ``"cn=admin,dc=veit-schiele,dc=de"`` mit dem Passwort ``1234`` erstellt, der anschließend alle Rechte am LDAP-Server hat. Das Passwort sollte natürlich angepasst werden.

Diese Datei wird eingelesen mit::

 # ldapadd -x -D cn=admin,dc=veit-schiele,dc=de -W -f base.ldif

Zum Testen kann nun der Directory Information Tree ausgelesen werden mit::

 ldapsearch -xLLL -b dc=veit-schiele,dc=de

Nun sollten wir noch einige Einträge in das LDAP-Repository erstellen. Hierzu erzeugen wir die Datei ``veit-schiele.ldif``::

 # Second level - organizational units
 dn: ou=people, dc=veit-schiele,dc=de
 ou: people
 description: All people in organisation
 objectclass: organizationalunit

 dn: ou=groups, dc=veit-schiele,dc=de
 ou: groups
 description: All groups in the organization
 objectclass: organizationalunit

 # Third level - people
 dn: uid=vschiele,ou=people,dc=veit-schiele,dc=de
 objectClass: pilotPerson
 objectClass: uidObject
 uid: vschiele
 cn: Veit Schiele
 sn: Schiele
 userPassword:: e1NIQX01ZW42RzZNZXpScm9UM1hLcWtkUE9tWS9CZlE9
 mail: kontakt@veit-schiele.de

 # Third level - groups
 dn: cn=Staff,ou=groups,dc=veit-schiele,dc=de
 objectClass: top
 objectClass: groupOfUniqueNames
 cn: Staff
 uniqueMember: uid=vschiele,ou=people,dc=veit-schiele,dc=de

- Die Organisation ``dc=veit-schiele,dc=de`` erhält zunächst zwei Organisationseinheiten (*organizational units*): *people* und *groups*.
- Nun wird ein Nutzer ``vschiele`` der Organisationseinheit *people* und eine Gruppe ``staff`` der Organisationseinheit *groups* hinzugefügt.
- Die Eigenschaft ``userPassword`` ist durch die beiden Doppelpunkte als SHA1 Hash-Wert gekennzeichnet.

- Schließlich kann die LDIF-Datei importiert werden mit::

   # ldapadd -xWD 'cn=admin, dc=veit-schiele,dc=de' -f veit-schiele.ldif

.. _`LDAP, Certificates and Buildout, oh my! Bringing LDAP and SSL/SASL/TLS certificates into the buildout fold`: http://rpatterson.net/blog/ldap-certificates-and-buildout-oh-my

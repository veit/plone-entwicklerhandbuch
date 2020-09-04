============================================
Reproduzierbare LDAP- und AD-Konfigurationen
============================================

Mit vs.genericsetup.ldap haben wir ein Produkt entwickelt, das den Im- und Export der LDAP- oder AD-Konfiguration von Plone-Sites erlaubt.

``vs.genericsetup.ldap`` nutzt das *Generic Setup Tool*, um die Konfiguration einer LDAP- oder Active Directory-Anbindung aus einer Plone-Site exportieren und in einer anderen Plone-Site wieder importieren zu können. Damit werden reproduzierbare und programmatische LDAP- und AD-Anbindungen möglich.

Installation
============

Um ``vs.genericsetup.ldap`` zu installieren, wird in der ``buildout.cfg-Datei`` folgendes eingetragen::

 [buildout]
 eggs =
     ...
     vs.genericsetup.ldap

 [instance]
 ...
 zcml =
     ...
     collective.genericsetup.ldap

Anwendung
=========

Nach der Installation von ``vs.genericsetup.ldap`` können Sie in das Generic Setup Tool Ihrer Plone-Site gehen und die Konfiguration Ihrer LDAP- oder AD-Anbindung exportieren, indem Sie im *Export*-Reiter *LDAP Settings Export* auswählen und anschließend auf *Export selected steps* klicken. Anschließend können Sie die ``ldap_plugin.xml``-Datei in ``src/vs.policy/vs/policy/profile/default/`` kopieren. Beim Installieren des ``vs.policy``-Produkts wird das *Plone LDAP plugin* oder *ActiveDirectory Multi Plugin* automatisch im *Pluggable Auth Service* erstellt. Ist ``vs.policy`` bereits für Ihre Website installiert, können Sie eines der beiden Plugins auch nachträglich hinzufügen, indem Sie im *Import*-Reiter des *Generic Setup Tool* den *LDAP Settings Import* auswählen und anschließend auf *Import selected steps* klicken.

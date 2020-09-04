================
Plone einrichten
================

#. Überprüfen Sie, ob ``ejabberd``, ``nginx`` und der ZEO-Cluster gestartet
   sind.
#. Erstellen Sie eine neue Plone-Site mit `collective.xmpp.chat <https://github.com/collective/collective.xmpp.chat>`_.
#. Gehen Sie zu den Konfigurationseinträgen unter ``http://localhost:8082/Plone/portal_registry`` und editieren die ``collective.xmpp.*``-Einträge.
#. Starten Sie anschließend die Instanz neu.
#. Melden Sie sich als Administrator an der Site an.
#. Erstellen Sie die gewünschten Nutzer.
#. Erstellen Sie die benötigten PubSub-Knoten durch Aufrufen des
   ``@@setup-xmpp``-View in Ihrer Plone-Site.

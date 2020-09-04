==========
Strophe.js
==========

`Strophe.js <http://strophe.im/strophejs/>`_ ist eine Javascript-Bibliothek die bidirektionales Streaming über HTTP-Verbindungen (BOSH) erlaubt.

Stanza Handlers
===============

::

 function chatMessageReceived {
     alert(Reviewved a message stanza);
     return true;
 }
 connection.addHandler(chatMessageReceived, null, 'message', 'chat');

Stanzas erstellen
=================

::

 var message = $msg({
             to: "someone@jabber.plone.org",
             type: "chat"
         }).c("body").t("Welcome to the plone chat");

ergibt z.B. folgende Stanza::

 <message to="someone@jabber.plone.org"
          type="chat">
     <body>Welcome to the plone chat</body>
 </message>

Plugins
=======

Hier nur einige der wesentlichen Plugins:

`muc <http://xmpp.org/protocols/muc/>`_
 Multi User Chat
`roster <http://xmpp.org/protocols/jabber_iq_roster/>`_
 Roster Management
`Pubsub <http://xmpp.org/protocols/pubsub/>`_
 Publish-Subscribe protocol

.. seealso::

    - `XEP-0124: Bidirectional-streams Over Synchronous HTTP (BOSH) <http://xmpp.org/extensions/xep-0124.html>`_
    - `XEP-0206: XMPP Over BOSH <http://xmpp.org/extensions/xep-0206.html>`_

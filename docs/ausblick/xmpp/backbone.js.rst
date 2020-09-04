===========
Backbone.js
===========

`Backbone.js <http://backbonejs.org/>`_ erlaubt strukturiertes Javascript mit

- Models
- Collections
- Views

Models
======

Erstellen eines Model
---------------------

::

 ChatBox = Backbone.Modeol.extend({
     initialize: function () {
         this.set ({
             'jid' : Strophe.getNodeFromJid(this.get('jid')),
             'box_id' : this.get('id'),
             'fullname' : this.get('fullname'),
         });
     }
 });

Instantiieren eines Model
-------------------------

::

 var box = new ChatBox({'id': hex_sha1(jid), 'jid': jid, 'fullname': name});

Views
=====

Die offensichtlichsten Views für ``collective.xmpp.chat`` sind definiert in `collective.xmpp.chat.browser.javascripts.converse.js <https://github.com/collective/collective.xmpp.chat/blob/master/src/collective/xmpp/chat/browser/javascripts/converse.js>`_:

- ``ControlBoxView``
- ``ChatRoomView``
- ``ChatBoxView``

Erstellen eines eigenen Views
-----------------------------

::

 ChatBoxView = Backbone.View.extend({
     tagName: 'div',
     className: 'chatbox',
     events: {'keypress textareea.chat-textarea': keyPressed'};
     template: _.template(
         '<div class="chat-title"> {{fullname}} </div>' +
         '<div class="chat-content"></div>' +
         '<form class="sendXMPPMessage" method="post">' +
             '<textarea type="text" class="chat-area" />' +
         '</form>'),
     render: function() {
         $(this.el).html(this.template(this.model.toJSON()));
             return this;
     },
     keyPressed: function (ev) {
         ...
     }
 });

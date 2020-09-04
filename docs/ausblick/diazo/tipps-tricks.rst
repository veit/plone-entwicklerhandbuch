==============
Tipps & Tricks
==============

Pop-ups
=======

Damit die Pop-ups für Kontakt- und Login-Formulare etc. funktionieren, sollte im Template ein ``div``-Tag mit der ID ``content`` vorhanden sein. Dies ist notwendig da ``popupforms.js`` ansonsten eine Fehlermeldung ausgibt::

 var common_content_filter = '#content>*:not(div.configlet),dl.portalMessage.error,dl.portalMessage.info';

===========
jarn.jsi18n
===========

`jarn.jsi18n <http://pypi.python.org/pypi/jarn.jsi18n/0.2>`_ bietet eine i18n-Infrastruktur für Javascripts in Plone.

Im Einzelnen bietet es

- das einfache Laden von ``gettext``-Katalogen aus
  Plone
- Message Factories, die denen in Python sehr
  ähnlich sind
- die Verweundung von *local storage* moderner Browser um das wiederholte Laden der *Message Cataologs* zu vermeiden.

Installation und Aktivierung
============================

Ihr Paket sollte abhängen von ``jarn.jsi18n``. Hierzu wird in der ``setup.py``-Datei unter ``install_requires`` folgendes eingetragen::

       install_requires=[
           'setuptools',
           'jarn.jsi18n'
       ],

Für die Aktivierung auf der Plone-Site wird es noch in die  ``profiles/default/metadata.xml`` eingetragen::

 <?xml version="1.0"?>
 <metadata>
   ...
   <dependencies>
     ...
     <dependency>profile-jarn.jsi18n:default</dependency>
   </dependencies>
 </metadata>

``MessageFactory``
==================

Zum Instanziieren und Verwenden Um einer ``MessageFactory`` muss der ``ì18n``-Katalog geladen werden. Dies kann z.B. so geschehen::

 $(document).ready(function () {
     jarn.i18n.loadCatalog('plone', 'de');
     _ = jarn.i18n.MessageFactory('plone')
 });

Der zweite Parameter in ``loadCatalog`` spezifiziert
die Sprache. Diese Angabe ist optional wenn das ``lang``-Attribut im HTML-Tag verwendet wird.

Übersetzungen
=============

Nachdem wir nun eine *Message Factory* haben, können wir auch Zeichenketten übersetzen::

 > _('contribute');
 hinzufügen

oder mit Keyword-Parametern::

 > _('Groups are: ${names}', {names: 'staff'})
 "Gruppen sind: Mitarbeiter"

Ggf. können auch mehrere Kataloge oder mehrere Sprachen für denselben Katalog geladen und instanziiert werden, z.B.::

 > jarn.i18n.loadCatalog('plone', 'en');
 > _en = jarn.i18n.MessageFactory('plone', 'en');
 > _en('Contributor');
 "Contributor"

Caching
=======

Sofern der Browser *local storage* unterstützt, werden die Kataloge lokal gespeichert. Somit lässt sich
vermeiden, dass nicht jedesmal ein Ajax-Request
ausgelöst wird um den Katalog erneut zu laden. Der
gespeicherte Katalog ist üblicherweise für 24 Stunden
gültig. Die Lebensdauer kann ggf. geändert werden mit
``jarn.i18n.setTTL(86400000)`` wobei der Wert in Millesekunden angegeben wird.

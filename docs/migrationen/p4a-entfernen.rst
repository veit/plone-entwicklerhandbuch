p4a entfernen
=============

.. note::

   Mit :doc:`wildcard.fixpersistentutilities` steht nun ein Modul zur Verfügung,
   mit dem sich Local Utilities, Subscribers, Adapters und Portal Tools auf der
   Web-Oberfläche entfernen lassen.

Ist in einer Instanz jemals ein Plone 4 Artists (p4a)-Produkt installiert
worden, lässt sich deren Utilities und Interfaces nicht mehr einfach entfernen.

Wir haben nun ein Skript entwickelt, mit dem sich diese Utilities und Interfaces
löschen lassen: `fixinterfaces.py <fixinterfaces.py>`_.

Dieses Skript sollte im Wurzelverzeichnis des Buildout-Projekts abgelegt werden.
Anschließend kann die Instanz im Debug-Modus gestartet werden::

 $ ./bin/instance debug

Sofern unsere Site nun die ID ``mysite`` hat, werden die Utilities und
Interfaces gelöscht.

Falls die Site eine andere ID enthält, lasst sich das Skript einfach ändern.
Auch für andere Zusatzprodukte kann das Skript leicht modifiziert werden.

==========
Einführung
==========

Das Plone-Entwicklerhandbuch möchte anhand eines konkreten Projekts aufzeigen,
wie Plone den eigenen Bedürfnissen angepasst werden kann. Gleichzeitig kommt
dabei die Überzeugung des Autors von agiler Software-Entwicklung, vor allem
testgetriebener Entwicklung, zum Ausdruck.

`Plone`_ ermöglicht die schnelle Erstellung von funktionsreichen und
performanten Websites, da es bereits mächtige Werkzeuge zur Verwaltung von
Rechten und Inhalten bereitstellt. So ist es einfach, öffentliche Websites,
Intra- und Extranets sowie branchenspezifische Web-Anwendungen schnell und
zuverlässig zu erstellen.

Dabei wird Plone von einer großen internationalen Community getragen. Zudem hält
die `Plone-Foundation`_ als eine nonprofit-Organisation die geistigen
Eigentums- und Markenrechte, sodass der weitere Entwicklungsprozess von Plone
stabil und kontrolliert möglich ist.

Plone basiert auf dem objektorientierten Web-Application-Framework `Zope`_ und
steht für viele Betriebssysteme wie Windows, Mac OS X und Linux/Unix zur
Verfügung.

Plone ist in `Python`_ geschrieben, einer mächtigen und dennoch einfach zu
nutzenden Programmiersprache.

Dieses Plone-Entwicklerhandbuch wird anhand einer Fallstudie aufzeigen, wie ein
prototypischer Verlauf eines Software-Entwicklungsprozesses mit Plone aussehen
kann.

Zielgruppe
==========

Das Buch richtet sich in erster Linie an Entwickler, die ihr webbasiertes
Content Management System mit Plone realisieren möchten. Zumindest einige
Kenntnis von Python, HTML und CSS werden erwartet, auch eigene frühere
Erfahrungen mit Zope und Plone können hilfreich sein.

Konventionen
============

In diesem Buch werden unterschiedliche Schriftstile zur Differenzierung der
Inhalte verwendet. So sieht die Darstellung von Codeabschnitten  so aus::

 [buildout]
 parts =
     zope2
     productdistros
     instance
     zopepy

während Angaben im Terminal so dargestellt werden::

 $ paster create -t plone3_buildout

bzw als root::

 # curl -O http://peak.telecommunity.com/dist/ez_setup.py

.. - `Plone 3. Eine Entscheidungshilfe`_
.. - `Paul Everitt: Plone-the-product vs. Plone-the-platform`_

.. _`Plone`: http://plone.org/
.. _`Plone-Foundation`: http://plone.org/foundation
.. _`Zope`: http://www.zope.org/
.. _`Python`: http://www.python.org/
.. _`Fallstudie`: fallstudie
.. _`Entwicklungsumgebung`: entwicklungsumgebung
.. _`Konfiguration`: erstellen-eines-site-policy-produkts
.. _`Zusatzprodukten`: zusatzprodukte
.. _`Erscheinungsbild`: erscheinungsbild
.. _`Artikeltypen`: artikeltypen
.. _`Berechtigungen und Arbeitsabläufe`: sicherheit-und-arbeitsablaufe
.. _`Formularen`: formulare
.. _`Internationalisierung und Lokalisierung`: http://www.veit-schiele.de/dienstleistungen/technische-dokumentation/plone-entwicklerhandbuch/internationalisierung
.. _`Anbindung relationaler Datenbanken`: relationale-datenbanken
.. _`Produktivumgebung`: produktivserver
.. _`LDAP-Server`: authentifizierung/ldap/
.. _`Upgrades und Migrationen`: migrationen

.. _`Plone 3. Eine Entscheidungshilfe`: http://www.zope.de/redaktion/dzug/anwendungen/plone3.pdf
.. _`Paul Everitt: Plone-the-product vs. Plone-the-platform`: http://radio.weblogs.com/0116506/2008/02/05.html#a450

Inhalt
======

.. toctree::
   :maxdepth: 1
   :titlesonly:

   entwicklungsumgebung/index
   erstellen-eines-site-policy-produkts/index
   zusatzprodukte/index
   erscheinungsbild/index
   archetypes-artikeltypen/index
   dexterity-artikeltypen/index
   sicherheit-und-arbeitsablaeufe/index
   formulare/index
   internationalisierung/index
   relationale-datenbanken/index
   produktivserver/index
   authentifizierung/index
   migrationen/index
   ausblick/index
   anhang/index

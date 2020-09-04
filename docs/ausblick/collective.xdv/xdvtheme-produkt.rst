================
xdvtheme-Produkt
================

Häufig sollen die Resourcen in einem Python-Paket verwaltet werden.

Erstellen und Registrieren des Python-Pakets
============================================

Ein solches Python-Paket lässt sich einfach erstellen mit::

 $ cd src/
 $ paster create -t plone vs.xdvtheme
  ...
 Register Profile (Should this package register a GS Profile) [False]: True
 ...

Hiermit erstellen wir das Python Egg ``vs.xdvtheme`` aus dem Template ``plone`` mit einem Profil für das *Generic Setup Tool*.

Damit dieses Egg auch der Instanz zur Verfügung steht, ändern Sie Ihre ``buildout.cfg``-Datei folgendermaßen ab::

 [buildout]
 ...
 eggs =
     ...
     vs.xdvtheme

 develop =
     ...
     src/vs.xdvtheme
 ...
 [instance]
 ...
 zcml =
 vs.xdvtheme

Rufen Sie anschließend Ihr ``./bin/buildout``-Skript erneut auf.

Erstellen Ihres xdv-Theme
=========================

Zunächst wird hierzu in ``vs.xdvtheme/vs/xdvtheme/configure.zcml`` das Verzeichnis ``Invention`` als Ressource registriert::

 <browser:resourceDirectory
     name="vs.xdvtheme" directory="Invention"  />

Erstellen Sie hierin ein eigenes Theme oder laden eins von `Open Source Web Design`_ herunter, z.B. `Invention`_::

 $ cd vs.xdvtheme/vs/xdvtheme/
 $ curl -O http://www.oswd.org/files/designs/3293/Invention.zip
 $ unzip -v Invention.zip

Für die XSLT-Transformationsregeln erstellen Sie anschließend in ``Invention`` die `rules.xml`_-Datei.

XDV-Konfiguration
=================

Damit Plone die Regeldatei mit den XSLT-Transformationen auch liest, wird ein Profil ``profiles/default/registry.xml`` erstellt, das die Werte im Formular *XDV theme settings* festlegt::

 <registry>

     <!-- collective.xdv settings -->
     <record field="enabled" interface="collective.xdv.interfaces.ITransformSettings">
         <field type="plone.registry.field.Bool">
             <title>Enabled</title>
         </field>
         <value>True</value>
     </record>
     <record interface="collective.xdv.interfaces.ITransformSettings" field="domains">
         <value>
             <element>localhost:8080</element>
         </value>
     </record>
     <record interface="collective.xdv.interfaces.ITransformSettings" field="rules">
         <value>python://vs.xdvtheme/Invention/rules.xml</value>
     </record>
     <record interface="collective.xdv.interfaces.ITransformSettings" field="theme">
         <value>python://vs.xdvtheme/Invention/index.html</value>
     </record>
     <record interface="collective.xdv.interfaces.ITransformSettings" field="absolute_prefix">
         <value>/++resource++vs.xdvtheme</value>
     </record>
 </registry>

``python://vs.xdvtheme/Invention/rules.xml``
 Die Ressourcen können nicht nur als Dateipfad angegeben werden sondern auch durch einen Python-Aufruf
``/++resource++vs.xdvtheme``
 Die Angabe im Feld ``absolute_prefix`` konvertiert relative URLs zu absoluten unter Verwendung dieses Präfixes.

CSS-Dateien registrieren
========================

Hierzu erstellen wir die Datei ``profiles/default/cssregistry.xml`` mit folgendem Inhalt::

 <?xml version="1.0"?>
 <object name="portal_css">

  <!-- Set conditions on stylesheets we don't want to pull in -->
  <stylesheet
      expression="not:request/HTTP_X_XDV | nothing"
      id="public.css"
      />

  <!-- Add new stylesheets -->

  <stylesheet title="" authenticated="False" cacheable="True"
     compression="safe" conditionalcomment="" cookable="True" enabled="on"
     expression="request/HTTP_X_XDV | nothing"
     id="++resource++vs.xdvtheme/css/style.css" media="" rel="stylesheet"
     rendering="link"
     applyPrefix="True"
     />

 </object>

``not:request/HTTP_X_XDV | nothing``
 sorgt dafür, dass die ``public.css``-Datei nicht ausgeliefert wird wenn in der HTML-Anfrage ``HTTP_X_XDV`` enthalten ist, also die Plone-Site über xdv ausgeliefert wird.

 ``request/HTTP_X_XDV | nothing`` würde umgekehrt eine Datei nur ausliefern, wenn die Anfrage durch xdv gestellt wird.

``++resource++vs.xdvtheme/styles.css``
 registriert unsere ``styles.css``-Datei an Plones *Stylesheets Registry*.
``applyPrefix``
 In Plone 4 kann eine Stylesheetdatei auch mit relativen URLs geparst werden.

Schließlich erstellen wir noch die Datei ``profiles/default/metadata.xml`` um mit unserem ``vs.xdvtheme``-Produkt auch gleichzeitig das benötigte ``collective.xdv`` mitzuinstallieren::

 <metadata>
     <version>1</version>
     <dependencies>
         <dependency>profile-collective.xdv:default</dependency>
     </dependencies>
 </metadata>

Wenn Sie nun das Buildout-Skript erneut aufrufen, anschließend die Instanz starten und eine neue Plone-Site mit dem Profil ``vs.xdvtheme`` erstellen, sollte die Plone-Site mit dem neuen Theme erscheinen.

Tipps & Tricks
==============

Zum Entwickeln Ihres Themes Sollen Sie die Zope-Instanz im ``debug``-Modus starten, da Änderungen am Template oder den XSLT-Regeln dann sofort sichtbar werden. Und wenn die *Stylesheets Registry* die css-Dateien ebenfalls im *Debug-Modus* ausliefert, werden auch die Änderungen in diesen Dateien sofort sichtbar.

.. _`Open Source Web Design`: http://www.oswd.org/
.. _`Invention`: http://www.oswd.org/design/information/id/3293
.. _`rules.xml`: rules.xml/view

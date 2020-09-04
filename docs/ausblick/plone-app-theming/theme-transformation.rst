====================
Theme-Transformation
====================

Erstellen eines Themes
======================

Wir können nun unser neues *Theme* erstellen indem wir in unserem Buildout-Projekt einen Ordner ``static`` erstellen und in diesem das `Invention`_-Theme von Open Source Web Design bereitstellen::

 $ cd plone.app.theming_buildout
 $ curl -O http://www.oswd.org/files/designs/3293/Invention.zip
 $ unzip Invention.zip

Nun erstellen wir in unserem ``Invention``-Ordner noch die `rules.xml`_-Datei mit den Angaben für die XSLT-Transformationen.

Aktivieren und Konfigurieren von ``plone.app.theming``
======================================================

Setzen Sie nun eine neue Plone-Site mit dem *Extension*-Profile ``Diazo theme support`` auf und wählen anschließend in deren *Plone Control Panel* die Konfiguration für das *Diazo theme*-Zusatzprodukt aus:

Basic settings
--------------

Enabled
 ändert die plone.app.theming-Transformation.

 Aktivieren Sie diese Option.

Select a theme
 Wählen Sie ein Theme aus

Advanced settings
-----------------

Hier können Sie eine eigene Regeldatei für Diazo, den Pfad zu den statischen Dateien oder die URL zu einem entfernten Server angeben. den angeben.

Rules file
 Der Pfad zu einer XML-Datei, die die Regeln für die Transformation enthält, also z.B.::

  Invention/rules.xml

 Es lassen sich auch Python-Pfade angeben, z.B.::

  python://vs.theme/static/rules.xml

Absolute path prefix
 Verwendet Ihr Theme relative Pfade zu Bildern, CSS-Dateien oder anderen Ressourcen, kann hier ein Präfix eingegeben werden, der gewährleistet, dass diese Ressourcen an jeder Stelle der Plone-Site verfügbar sind.

Read network
 erlaubt die Verwendung von Regeln und Themes von entfernten Servern.

Unthemed host names
 Sofern es Namen von Hosts gibt, die nicht gestaltet werden sollen, können diese hier zeilenweise aufgelistet werden. Dies ist zumindest während der Entwicklung des Themes sinnvoll um die Ausgaben der ungestaltetem Website mit der gestalteten zu vergleichen.

 Der Standardwert ist ``127.0.0.1``

Parameter expressions
 Hier können Parameter definiert werden, die in den Regeln des Themes verwendet werden können, z.B. mit ``$name``. Diese Parameter werden mittels TALES-Ausdrücken definiert, die entweder ``string``, ``number``, ``boolean`` oder ``None`` ausgeben sollten. Verfügbare Variablen sind:

 - ``context``
 - ``request``
 - ``portal``
 - ``portal_state``
 - ``context_state``

 Je Zeile kann eine Variable definiert werden im Format ``name = expression``.

.. _`Invention`: http://www.oswd.org/design/information/id/3293
.. _`rules.xml`: rules.xml/view

============================
Migration von collective.xdv
============================

`plone.app.theming`_ ist eine Weiterentwicklung von `collective.xdv`_ so wie `Diazo`_ eine Weiterentwicklung von `XDV`_ ist.

.. _`plone.app.theming`: http://pypi.python.org/pypi/plone.app.theming
.. _`collective.xdv`: http://pypi.python.org/pypi/collective.xdv
.. _`Diazo`: http://pypi.python.org/pypi/Diazo
.. _`XDV`: http://pypi.python.org/pypi/XDV


Migrating der XDV-Regeln zu Diazo-Regeln
=========================================

Die Syntax der Diazo-Regeln ist denen von XDV sehr ähnlich. Zunächst einmal haben sich die Namespaces geändert. Während diese in XDV noch angegeben wurden mit::

 <rules
     xmlns="http://namespaces.plone.org/xdv"
     xmlns:css="http://namespaces.plone.org/xdv+css"
     xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
     ...
 </rules>

lauten diese für Diazo nun::

 <rules
     xmlns="http://namespaces.plone.org/diazo"
     xmlns:css="http://namespaces.plone.org/diazo/css"
     xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
     ...
 </rules>

Zusätzlich haben sich einige Regeln vereinfacht, z.B.:

- ``<copy />`` sollte nur zum Kopieren von Attributen verwendet werden, zum Ersetzen bestehender Attribute sollte ``<replace />`` mit ``theme-children`` verwendet werden
- ``<prepend />`` wurde ersetzt durch ``<before />``mit ``theme-children``.
- ``<append />`` wurde ersetzt durch ``<after />`` mit ``theme-children``.

In der `Diazo-Dokumentation`_ finden Sie weitere Hinweise über verfügbare Rwgeln.

.. _`Diazo-Dokumentation`: http://diazo.org/

Änderungen in der Plone-Integration
===================================

Zum Aktualisieren einer Website, die mit collective.xdv gestaltet wurde, sind die folgenden Schritte nötig:

#. Deinstallieren Sie das XDV-Theme-Paket im *Quickinstaller Tool*.
#. Stoppen Sie die Instanz und entfernen collective.xdv aus Ihrem Buildout (entweder in ``buildout.cfg``, einer ähnlichen Konfigurationsdatei oder in der ``setup.py``-Datei unter ``install_requires``).
#. Installieren Sie ``plone.app.theming`` und ändern Ihre Regeln wie oben beschrieben.

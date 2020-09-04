==========================
Protected und Trusted Code
==========================

Sicherheitsannahmen werden an den folgenden Stellen getroffen:

- ``browser``-Komponenten wie ``views`` und ``resource``, die in ZCML deklariert und mit einer Berechtigung versehen werden.
- *Page Templates* und andere Ressourcen, die durch das *Skins*-Tool verwaltet werden, werden explizit bestimmten Rollen zugewiesen. So wird z.B. ``prefs_install_products_form.pt`` in der assoziierten Datei ``prefs_install_products_form.pt.metadata`` explizit auf die ``Manager``-Rolle eingeschränkt::

   [security]
   View = 0:Manager

- Attribute und Methoden von persistenten Objekten wie Artikeltypen und Tools können auf zweierlei Art geschützt werden:

  - durch ZCML-Berechtigungen mit ``class``- oder ``require``-Anweisungen
  - durch Python-Code, der ein ``AccessControl.ClassSecurityInfo``--Objekt verwendet.

Zusätzlich kann die Variable ``__allow_access_to_unprotected_subjects__`` einer Klasse hinzugefügt werden um zu bestimmen, wie sich Attribute, die ihrerseits nicht durch Security-Annahmen geschützt sind, verhalten sollen.

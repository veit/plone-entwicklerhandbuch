=========
Chameleon
=========

Chameleon ist eine Reimplementierung der ZopePageTemplates, die durch Precompiling eine deutliche Performance-Optimierng erlaubt. Durchschnittlich dürfte isch so eine Performance-Steigerung für ungecachte Inhalte um ca. 20% ergeben.

`Chameleon <http://www.pagetemplates.org/>`_ kann einfach für Plone 4 installiert
werden indem als einzige Abhängigkeit `five.pt
<http://pypi.python.org/pypi/five.pt>`_ in einer Version ≥2.1 installiert wird::

    [instance]
    ...
    eggs =
        ...
        five.pt

Die automatische Paketkonfiguration von Plone installiert dann automatisch
Chameleon nach.

Eine ausführliche Dokumentation zu Chameleon erhalten Sie in `Chameleon
documentation <http://chameleon.readthedocs.org/>`_.

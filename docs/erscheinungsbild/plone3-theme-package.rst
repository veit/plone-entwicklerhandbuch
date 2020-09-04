Plone3-Theme-Package
====================

Erstellen des Eggs
------------------

::

    $ cd src
    $ paster create -t plone3_theme

    Enter namespace_package (Namespace package (like plonetheme)) ['plonetheme']: vs
    Enter package (The package contained namespace package (like example)) ['example']: theme
    Enter skinname (The skin selection to be added to 'portal_skins' (like 'My Theme')) ['']: vs.theme
    Enter skinbase (Name of the skin selection from which the new one will be copied) ['Plone Default']:
    Enter empty_styles (Override default public stylesheets with empty ones?) [True]: False
    Enter include_doc (Include in-line documentation in generated code?) [False]:
    Enter zope2product (Are you creating a Zope 2 Product?) [True]:
    …
    Enter zip_safe (True/False: if the package can be distributed as a .zip file) [False]:

``Enter empty_styles``
    Wenn die Skin-Anpassungen sehr umfangreich sind oder es sich um eine
    performance-kritische Anwendung handelt empfehle ich, den Skin vollständig
    neu aufzusetzen und Enter ``empty_styles`` mit ``True`` anzugeben.
``Enter skinbase``
    In Plone 4 kann hier zwischen folgenden beiden Skins gewählt werden:

    Sunburst Theme
        Ein neuer Skin aus dem plonetheme.sunburst-Egg.

        Sunburst ist der Standard-Skin für neu erstellte Plone-4-Sites.

    Plone Classic Theme
        Der aus Plone 3 bekannte Plone Default-Skin. Er ist nun im
        ``plonetheme.classic``-Egg zu finden.
    Plone Default
        Der Plone Default-Skin ist in Plone 4 nur noch ein minimalistischer
        Skin, der ideal geeignet ist für die nachgelagerte Gestaltung einer
        Plone-Site mit XDV oder Deliverance.

    In Plone 3 besteht üblicherweise die Wahl zwischen zwei Skins:

    Plone Default
        Der Standard-Skin.
    NuPlone
        Ein modernerer Skin für Plone 3.

Verzeichnisübersicht des ``vs.theme``-Produkts

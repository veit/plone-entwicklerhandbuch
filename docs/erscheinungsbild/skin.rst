====
Skin
====

Eigenen Skin erstellen
======================

Um nun das Plone Skin Tools für unsere Bedürfnisse anzupassen, wurde die Datei ``src/vs.theme/vs/theme/profiles/default/skins.xml`` folgendermaßen erstellt::

 <?xml version="1.0"?>
 <object name="portal_skins" allow_any="False" cookie_persistence="False"
         default_skin="vs.theme">

     <object name="vs_theme_custom_images"
             meta_type="Filesystem Directory View"
             directory="vs.theme:skins/vs_theme_custom_images"/>
     <object name="vs_theme_custom_templates"
             meta_type="Filesystem Directory View"
             directory="vs.theme:skins/vs_theme_custom_templates"/>
     <object name="vs_theme_styles"
             meta_type="Filesystem Directory View"
             directory="vs.theme:skins/vs_theme_styles"/>

     <skin-path name="vs.theme" based-on="Plone Default">
         <layer name="vs_theme_custom_images"
                insert-after="custom"/>
         <layer name="vs_theme_custom_templates"
                insert-after="vs_theme_custom_images"/>
         <layer name="vs_theme_styles"
                insert-after="vs_theme_custom_templates"/>
     </skin-path>

 </object>

Damit werden die drei Verzeichnisse ``vs_theme_custom_images``, ``vs_theme_custom_templates`` und ``vs_theme_styles`` registriert und ein neuer Skin *vstheme*, der auf *Plone Default* basiert und zudem die drei oben genannten Layer enthält, als Standard-Skin angegeben.

.. note::
    Sollen die Layer allen Skins zugewiesen werden, kann dies einfach so angegeben werden::

        <skin-path name="*">
            ...
        </skin-path>

Entfernen von Layern
--------------------

Layer können auch einfach wieder entfernt werden mit::

  <object name="vs_theme_custom_templates" remove="True "/>

Dies kann z.B. für ein ``uninstall``-Profil verwendet werden.

Elemente in einem Skin-Layer überschreiben
==========================================

Wollen Sie z.B. das Logo durch ein eigenes im gif-Format ersetzen, sollten Sie zunächst in der Datei ``src/vs.theme/vs/theme/skins/vs_theme_styles/base_properties.props`` die Angabe für ``logoName`` ändern::

 logoName:string=logo.gif

Anschließend können Sie Ihr Logo in ``src/vs.theme/vs/theme/skins/vs_theme_custom_images/`` einfügen.

.. note::
    Um die DTML-Variable ``fontFamily`` in einer CSS-Datei verwenden zu können, darf sie nicht mit ``&dtml-fontFamily;`` eingebunden werden sondern mit ``<dtml-var fontFamily>;``, da ansonsten das Zeichen ``"`` als ``&quot;`` interpretiert würde.

.. note::
    Sollen PageTemplates überschrieben werden, die auch Meta-Angaben in einer ``.metadata``-Datei enthalten, dann sollte auch diese Datei mitkopiert werden.

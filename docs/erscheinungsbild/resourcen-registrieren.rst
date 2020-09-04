======================
Resourcen registrieren
======================

Um die CSS-Datei ``src/vs.theme/vs/theme/browser/stylesheets/main.css`` am *CSS Registry Tool* zu registrieren, wird die Datei ``src/vs.theme/vs/theme/profiles/default/cssregistry.xml`` folgendermaßen geändert::

 <?xml version="1.0"?>
 <object name="portal_css">

  <stylesheet title=""
     id="++resource++vs.theme.stylesheets/main.css"
     media="screen"
     rel="stylesheet"
     rendering="import"
     cacheable="True"
     compression="safe"
     cookable="True"
     enabled="1"
     expression=""/>

 </object>

``id``
 ergibt sich daraus, dass das Verzeichnis ``src/vs.theme/vs/theme/browser/stylesheets``, das die ``main.css``-Datei enthält, als ``resourceDirectory`` in ``src/vs.theme/vs/theme/browser/configure.zcml`` registriert ist.
``Title``
 Durch die Angabe eines Titels zusammen mit ``rel=stylesheet`` wird ein Stylesheet-Dokument vor anderen bevorzugt.
``expression``
 Die Bedingung, unter der das Stylesheet ausgeführt werden soll, als TALES-Ausdruck.

 Im Folgenden einige der häufigsten Bedingungen:

 - nach Artikeltyp::

    expression = "python:object.meta_type == 'ATFolder'"

 - nach View::

    expression="object/@@registration_view/enabled | nothing"

   - nach globalen Views::

      expression="python:portal.restrictedTraverse ('@@plone_portal_state').is_rtl()"

 - nach Rollen::

    expression="not: portal/portal_membership/isAnonymousUser"

   oder::

    expression="python: not here.restrictedTraverse
                            ('@@plone_portal_state').anonymous()"

``media``
 Das Medium, für das das Stylesheet gilt:

 ``all``, ``aural``, ``braille``, ``embossed``, ``handheld``, ``print``, ``projection``, ``screen``, ``tty`` und ``tv``.

``rel``
 mögliche Werte sind ``stylesheet`` und ``alternate stylesheet``. Der Standardwert ist ``stylesheet``.
``rendering``
  Angabe, wie das Stylesheet in die HTML-Seiten eingebunden werden soll. Mögliche Werte sind ``import``, ``link`` und ``inline``.
``compression``
 Angabe, ob und wie das Stylesheet komprimiert werden darf. Mögliche Werte sind ``none``, ``safe`` oder ``full``.
``enabled``
 Angabe, ob das Stylesheet aktiv ist.
``cookable``
 Angabe, ob das Zusammenfügen mit anderen Stylesheets erlaubt wird.
``cacheable``
 Angabe, ob das Caching des Stylesheets erlaubt wird.
``conditionalcomment``
 Ab der Plone-Version 3.3 kann mit der *CSS-Registry* das Einbinden der CSS-Datei auch in sog. *Conditional Comments* erfolgen, also z.B.::

  <!--[if IE]>
  <style type="text/css" media="all">@import url(http://localhost:8080/mysite/portal_css/vs.theme/iefixes-cachekey7904.css);</style>
  <![endif]-->

 Hierzu wird in der ``cssregistry.xml``-Datei folgendes angegeben::

  <stylesheet title=""
              …
              conditionalcomment="IE"
              id="iefixes.css"/>

 Weitere Hinweise zu *Conditional Comments* erhalten Sie in `About Conditional Comments`_.

.. note::
    Zum Entwickeln von Stylesheets empfiehlt sich, entweder die Instanz im Debug-Modus zu starten oder im ZMI der CSS Registry *Debug/development mode* zu aktivieren und damit das Caching von CSS-Dateien im Browser zu verhindern.

Entfernen von css-Dateien
-------------------------

CSS-Dateien können entfernt werden mit::

 <stylesheet id="++resource++vs.theme.stylesheets/main.css" remove="True"/>

Dies kann z.B. für ein ``uninstall``-Profil verwendet werden.

.. `Have your views rendered with DTML`_
.. _`Have your views rendered with DTML`: http://glenfant.wordpress.com/2008/08/16/have-your-views-rendered-with-dtml/
.. _`About Conditional Comments`: http://msdn.microsoft.com/en-us/library/ms537512.aspx

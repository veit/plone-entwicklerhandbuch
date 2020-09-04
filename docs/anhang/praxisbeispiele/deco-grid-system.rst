================
Deco Grid System
================

Spaltenbreite
=============

Die Breite der Klassen lässt sich dann einfach berechnen mit6.25*n - 2.25)%.
Dies führt dann z.B. zu folgenden Klassen:

``width-full``
 Die volle Breite beträgt 97.75%, da links und rechts jeweils eine Margin von
 1,125% erhalten bleiben.
``width-1:2``
 Die Breite beträgt 47.75%.
``width-3:4``
 Die Breite beträgt 72.75%.

Positionierung
==============

Die Positionierung der Klassen wird vom rechten Rand aus vorgenommen mit
``margin-left: -100 + (6.25*n) + 1.125``. Dies führt z.B. zu folgenden Klassen:

``position-0``
 ``{margin-left: -73.875%;}``
``position-1:4``
 ``{margin-left: -73.875%;}``
``position-1:2``
 ``{margin-left: -48.875%;}``
``position-3:4``
 ``{margin-left: -23.875%;}``

Verschieben von Spalten
=======================

Sollen nun beispielsweise die beiden Portlet-Spalten links vom Inhalt
positioniert werden, so sind hierfür nur geringe Änderungen notwendig:

Zunächst wird der bestehende sunburstview überschrieben in
``vs.theme/vs/theme/browser/configure.zcml``::

 <browser:page
     for="*"
     name="sunburstview"
     class=".sunburstview.SunburstView"
     layer=".interfaces.IThemeSpecific"
     permission="zope.Public"
     allowed_interface="plonetheme.sunburst.browser.interfaces.ISunburstView"
     />

Anschließend kopieren wir sunburstview.py in unser browser-Package und ändern
darin die Berechnung der css-Klasse für denjenigen div-Tag, der den
Inhaltsbereich enthält:

Sofern beide Portlet-Spalten angezeigt werden, soll der Inhaltsbereich 2 von
4 Spalten breit sein und ab der Hälfte der Seite beginnen, also::

 elif sl and sr:
     return "cell width-1:2 position-1:2"

Sofern nur die rechte Portlet-Spalte, nicht jedoch die linke angezeigt werden
soll, bleibt die rechte Spalte an ihrer Position stehen und auch in diesem Fall
wird der Inhalt 2 Spalten breit sein und ab der Hälfte der Seite beginnen::

 elif (sr and not sl) and (not portal_state.is_rtl()):
     return "cell width-1:2 position-1:2"

Schließlich müssen wir noch die main_template.pt-Datei anpassen um die rechte
Portlet-Spalte immer an zweiter Stelle im Raster-layout anzuzeigen. Hierfür wird
für den div-Tag mit der ID portal-column-two die position-Klasse geändert in::

 <div id="portal-column-two"
     class="cell width-1:4 position-1:4"
     ...
     tal:attributes="class python:isRTL and 'cell width-1:4 position-0' or 'cell width-1:4 position-1:4'">

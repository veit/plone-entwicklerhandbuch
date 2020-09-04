======================
Skalierung von Bildern
======================

Dieie Angabe der Bildgröße erfolgt hierbei nicht in der Schemadefinition sondern im Page Template::

    <img tal:define="scale context/@@images"
     tal:replace="structure python: scale.scale('image',
                  width=260, height=160, direction='down').tag()" />

Die Berechnung der Bildgröße erfolgt dann beim Aufrufen der Seite.

Folgende Parameter sind verfügbar:

``up``
    skaliert die kürzere Seite auf die gewünschte Größe und beschneidet die andere Seite falls nötig.

``down``
    skaliert die längere Seite auf die gewünschte Größe und beschneidet die andere Seite falls nötig.

``thumbnail``
    skaliert das Bild auf die gewünschte Größe ohne es zu beschneiden.

    Die Proportionen des Bildes können sich hierdurch verändern.

    Diese Option erfordert die Angabe sowohl der Höhe als auch der Breite.

``quality``
    Qualität des resultierenden Bildes.

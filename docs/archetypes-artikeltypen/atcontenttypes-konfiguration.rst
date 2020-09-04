============================
ATContenttypes-Konfiguration
============================

Die ATContenttypes liefern in ``Products/ATContentTypes/etc/atcontenttypes.conf.in`` die Vorlage für eine Konfigurationsdatei. Um diese nun anpassen zu können, kann die Buildout-Konfiguration folgendermaßen geändert werden::

 [buildout]
 ...
 parts =
     ...
     atct_conf
 ...
 [atct_conf]
 recipe = plone.recipe.command
 target = ${instance:location}/etc/atcontenttypes.conf
 command = ln -s ${buildout:directory}/etc/atcontenttypes.conf ${:target}

Schauen wir uns nun ``etc/atcontenttypes.conf`` genauer an.

``mxtidy``
 HTML-Filter-Optionen:

 ``drop_font_tags``
  Sofern auf ``yes`` gesetzt, verwirft Tidy alle ``font``- und ``center``-Tags.
 ``drop_empty_paras``
  Sofern auf ``yes`` gesetzt, werden leere Paragraphen verworfen. Bei ``no`` werden leere Absätze durch zwei ``br``-Elemente ersetzt.
 ``input_xml``
  Sofern auf ``yes`` gesetzt, verwendet Tidy den XML-Parser und nicht den HTML-Parser.
 ``output_xhtml``
  Sofern auf ``yes`` gesetzt, generiert Tidy wohlgeformtes HTMLund der Doctpe wird in XHTML geändert.
 ``quiet``
  Sofern auf ``yes`` gesetzt, gibt Tidy nicht die Anzahl der Fehler und Warnungen aus.
 ``show_warnings``
  Sofern auf ``no``gesetzt, werden Warnungen unterdrückt.
 ``indent_spaces``
  Setzt die Anzahl der Leerzeichen zum Einrücken der Inhalte.
 ``word_2000``
  Sofern auf ``yes`` gesetzt, filtert Tidy zusätzliche Anweisungen aus, die Microsoft Word 2000 beim Speichern als *Web pages* einfügt.
 ``wrap``
  Setzt die Anzahl der Zeichen, nach denen spätestens umbrochen wird.

  Falls kein automatischer Zeilenumbruch gewünscht ist, kann hier einfach ``0`` angegeben werden.
 ``tab_size``
  Setzt die Anzahl der Leerzeichen bei der Eingabe eines Tabulators.
 ``char_encoding``
  Bestimmt die Interpretation von Zeichen.

  Bei ``ascii`` akzeptiert Tidy *Latin-1*-Zeichen und Entitäten für alle Zeichen ``> 127``.

 Eine vollständige Liste der Optionen finden Sie in `HTML Tidy Options <http://www.egenix.com/products/python/mxExperimental/mxTidy/doc/#_Toc233711195>`_.

``feature swallowImageResizeException``
 Sofern ``enable yes`` gesetzt ist, werden Fehlermeldungen beim Ändern der Bildgröße nicht ausgegeben.
``pil_config``
 Konfiguration der Python Imaging Library (PIL).

 ``quality``
  Qualität, mit der die Bilder berechnet werden. Die Skala reicht von ``1`` bis ``100``. Bei ``100`` wird jedoch keine `JPEG Quantisierung <http://de.wikipedia.org/wiki/JPEG#Quantisierung>`_ mehr verwendet.
 ``resize_algo``
  Algorithmus, mit dem die Größenänderungen von Bildern berechnet werden.

  Mögliche Angaben sind:

  - ``nearest``
  - ``bilinear``
  - ``bicubic``
  - ``antialias``

``archetype``
 Konfiguration der Archetypes-Artikeltypen

 ``contenttypes``
  MIME-Type des ATContenttype.

  ``default``
   Standardwert des MIME-Type
  ``allowed``
   Zulässige MIME-Types

 ``max_file_size``
  Maximale Dateigröße in ``byte``, ``kb`` oder ``mb``.

  ``0`` begrenzt die Dateigröße nicht.

 ``max_image_dimension``
  Maximale Breite und Höhe von Bildern.

   ``0,0`` begrenzt weder die Breite noch die Höhe der Originalbilder.

 ``allow_document_upload``
  ``yes`` erlaubt das Hochladen von Artikeln.


``metadate``
 Ein einzelnes Metadata-Element.

 Folgende Attribute sind möglich:

 - ``name``
 - ``friendlyName``
 - ``description``
 - ``enabled``

``index``
 Ein einzelnes Metadata-Element.

 Folgende Attribute sind möglich:

 - ``name``
 - ``friendlyName``
 - ``description``
 - ``enabled``
 - ``criterion``

``topic_tool``
 Standardkonfiguration des Topic-Tools.
``atct_tool``
 Standardkonfiguration des ATCT-Tools.

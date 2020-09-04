==============
Zope-Neustarts
==============

Früher wurden Änderungen in Templates oder Python-Skripten im Debug-Modus oder
mit refresh.txt einfach übernommen, und ein Neustart von Zope war nur selten
nötig.

Heute mag es häufig so erscheinen, als ob Zope bei jeder kleinen Änderung neu gestartet werden muss, damit die Änderungen auch übernommen werden. Ich gebe hier nun mal einen Überblick, welche Änderungen wie übernommen werden:

- Wird die Instanz im Debug-Modus gestartet, werden für Änderungen an Page-Templates und Zope-3-Browser-Ressourcen keine Neustarts benötigt.
- Die Generic-Setup-XML-Dateien werden bei jedem Import durch das Generic-Setup-Tool ausgelesen.
- Auch die ``Install.py``-Dateien in einem ``Extensions``-Verzeichnis, die vom Portal-Quickinstaller verwendet werden, können ohne Neustart verändert werden.
- Und auch alle Dateien im ``skins``-Ordner, einschließlich der Python-Skripte, werden ohne Neustart aktualisiert.
- Andere Python-Skripte, also z.B. ``setuphandlers.py``, werden jedoch nur bei einem Neustart aktualisiert. Hier schafft `sauna.reload <http://pypi.python.org/pypi/sauna.reload>`_ Abhilfe, indem es Code und ZCML-Dateien nachlädt. Um ``sauna.reload`` zu installieren, geben Sie folgendes in der ``buildout.cfg``-Datei an::

   [buildout]
   …
   eggs =
       …
       sauna.reload

   [instance]
   …
   zope-conf-additional =
       %import sauna.reload

  Nach dem Aufruf des buildout-Skripts sollte die Instanz gestartet werden mit::

   $ RELOAD_PATH=src/ ./bin/instance fg

  Anschließend können Sie sich im ZMI anmelden und folgende URL aufrufen::

   http://localhost:8080/@@saunareload

- Darüberhinaus helfen `pyflakes <http://pypi.python.org/pypi/pyflakes>`_ und `PDBDebugMode <http://plone.org/products/pdbdebugmode>`_  schon vor einem Neustart die Fehler zu finden.
- Und schließlich wird bei Test Driven Development nicht der Zope-Server selbst sondern nur der Testrunner aufgerufen  ;-)

.. note::
    Achten Sie auch darauf, dass die Resource Registries CSS-, JavaScripts- und KSS-Registry im Debug/development-Modus betrieben werden, damit die zugehörigen Dateien nicht gecachet und entsprechende HTTP-Header ausgeliefert werden.

.. note::
    Unter Windows muss `PyYAML <http://www.pyyaml.org/>`_ unter Verwendung der
    Binärdateien installiert werden.

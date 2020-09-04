=====================================
Zusätzliche Informationen für Windows
=====================================

Installation und Konfiguration von Python 2.6.6 und 2.4.4, MinGW, Libxml- und
Libxslt-Python-Bindings.

Python 2.6.6
============

#. Herunterladen und Installieren von Python 2.6.6 mit `python-2.6.6.msi`_.

   Wählen Sie *Install for all users*.

   Der Standard-Installationsort ist ``C:\Python26``.

.. _`python-2.6.6.msi`: http://www.python.org/ftp/python/2.6.6/python-2.6.6.msi

#. Herunterladen und Installieren der pywin32-Extension von http://sourceforge.net/projects/pywin32/files/pywin32/Build%20214/pywin32-214.win32-py2.6.exe/download.

.. #. Herunterladen und Installieren der Python imaging library (PIL) von http://effbot.org/media/downloads/PIL-1.1.6.win32-py2.6.exe

#. Eintragen von Python in die Systemvariable ``PATH``, sodass nicht jedesmal der gesamte Pfad angegeben werden muss.

   #. Öffnen Sie die *Systemeigenschaften* und klicken anschließend zunächst auf den *Erweitert*-Reiter, dann auf *Umgebungsvariablen*.
   #. Fügen Sie anschließend die Pfade zu Ihrer Python-Installation ein, z.B.::

       C:\Python26;C:\Python26\Scripts;

      Beachten Sie bitte, dass die verschiedenen Pfade durch Semikolon voneinander getrennt sind:

      .. figure:: windows-umgebungsvariablen.png
        :alt: Windows-Umgebungsvariablen

   #. Öffnen Sie nun eine neue Shell mit ``Windows``-``r`` und geben ``cmd`` in das Popup-Fenster ein.

   #. Mit ``python -V`` wird Ihnen die Versionsnummer des verwendeten Python ausgegeben – dies sollte ``Python 2.6.6`` sein.

Python 2.4.4
============

#. Herunterladen und Installieren von Python 2.4.4 mit `python-2.4.4.msi`_;

   Wählen Sie *Install for all users*.

   Der Standard-Installationsort ist ``C:\Python24``.

#. Herunterladen und Installieren der pywin32-Extension von http://downloads.sourceforge.net/pywin32/pywin32-210.win32-py2.4.exe.

.. #. Herunterladen und Installieren der Python imaging library (PIL) von http://effbot.org/downloads/PIL-1.1.6.win32-py2.4.exe

#. Eintragen von Python in die Systemvariable ``PATH``, sodass nicht jedesmal der gesamte Pfad angegeben werden muss.

   #. Öffnen Sie die *Systemeigenschaften* und klicken anschließend zunächst auf den *Erweitert*-Reiter, dann auf *Umgebungsvariablen*.
   #. Fügen Sie anschließend den Pfad zu Ihrer Python-Installation ein, z.B.::

       C:\Python24;C:\Python24\Scripts;

      .. figure:: windows-umgebungsvariablen.png
        :alt: Windows-Umgebungsvariablen

      Beachten Sie bitte, dass die verschiedenen Pfade durch Semikolon voneinander getrennt sind.

   #. Öffnen Sie nun eine neue Shell mit ``Windows``-``r`` und geben ``cmd`` in das Popup-Fenster ein.

   #. Mit ``python -V`` wird Ihnen die Versionsnummer des verwendeten Python ausgegeben – dies sollte ``Python 2.4.4`` sein.

MinGW
=====

Dies ist ein gcc-Compiler für Windows, womit C-Komponenten von Zope auf Windows kompiliert werden können.

#. Herunterladen des MinGW-Installationsprogramms von http://downloads.sourceforge.net/mingw/MinGW-5.1.4.exe.
#. Geben Sie beim Ausführen des Installationsprogramms als Optionen *MinGW base tools* und *MinGW Make* an.

   Das Programm wird üblicherweise nach ``C:\MinGW`` installiert.

   Das Installationsprogramm holt sich die benötigten Dateien von sourceforge.net, wobei es gegebenenfalls mehrfach aufgerufen werden muss bis alle Dateien heruntergeladen wurden.
#. Tragen Sie nun ``C:\MinGW\bin`` in ``PATH`` ein.
#. Testen Sie die Installation in einer Shell mit::

    gcc --version

   Die Ausgabe sollte ``gcc (GCC) 3.4.5`` oder neuer sein.

#. Anschließend wird Distutils für MinGW konfiguriert. Hierzu erstellen Sie die Datei ``distutils.cfg`` in ``C:\Python24\Lib\distutils`` mit folgendem Inhalt::

       [build]
       compiler=mingw32

Libxml- und Libxslt-Python-Bindings
===================================

#. Die Bindings können heruntergeladen werden von http://users.skynet.be/sbi/libxml-python/binaries/libxml2-python-2.7.7.win32-py2.6.exe.

Python Imaging Library (PIL)
============================

Tragen Sie in der Buildout-Konfigurationsdatei statt ``PIL`` bitte `Pillow`_ ein, also::

 [instance]
 …
 eggs =
     Pillow
     Plone
     …

.. _`Pillow`: http://pypi.python.org/pypi/Pillow

Windows-Service
===============

Nun können Sie ein Buildout-Projekt erstellen, wobei jedoch im Pfad keine Leer- oder Sonderzeichen enthalten sein dürfen.

Anschließend können Sie die Zope-Instanz als Windows-Service installieren, indem Sie in der Shell folgendes angeben::

 > bin\instance.exe install

Anschließend lässt sich die Instanz starten mit::

 > bin\instance.exe start

Soll der Service wieder entfernt werden, geben Sie einfach folgendes an::

 > bin\instance.exe remove

.. _`python-2.4.4.msi`: http://www.python.org/ftp/python/2.4.4/python-2.4.4.msi

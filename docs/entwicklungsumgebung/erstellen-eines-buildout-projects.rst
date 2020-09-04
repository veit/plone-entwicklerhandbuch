Erstellen eines Buildout-Projekts
=================================

#. Ein Buildout-Projekt für Plone lässt sich am einfachsten aus meiner
   `vs_buildout <https://github.com/veit/vs_buildout>`_-Vorlage bei github
   erstellen::

    $ curl -o master.zip  https://codeload.github.com/veit/vs_buildout/zip/master
    $ unzip master.zip
    $ cd vs_buildout-master
    $ python bootstrap.py -c devel.cfg
    …
    Got distribute 0.6.28.
    Generated script '/Users/plone/vs_buildout-master/bin/buildout'.

   ``-d``
    verwendet `Distribute <http://packages.python.org/distribute/>`_
    anstatt der `Setuptools <http://pypi.python.org/pypi/setuptools>`_.
   ``-c``
    erlaubt die Angabe eines Pfades zu einer Buildout-Konfigurationsdatei,
    in unserem Fall ``devel.cfg``.

   .. note:: Falls das ``buildout``-Skript für den Nutzer, z.B. ``plone``,
      noch nicht in ``PATH`` eingetragen wurde, ändern wir die ``~/.bashrc``
      (oder auf dem Mac in ``~/.bash_profile``) folgendermaßen::

       export PATH=/opt/python/Python-2.7.5/bin/:$PATH

      Danach kann die Konfiguration neu eingelesen werden mit::

       $ source ~/.bashrc

#. Bevor nun Plone mit Buildout installiert werden kann, sollten die für die
   `Python Imaging Library (PIL) <http://www.pythonware.com/products/pil>`_
   benötigten Bibliotheken installiert werden.

   Anforderungen:

   - Für JPEG-Unterstützung benötigen Sie die *IJG JPEG library,* Version 6a
     oder 6b:

     http://www.ijg.org

   - Für PNG- und ZIP-Unterstützung benötigen Sie die *ZLIB library.*

     http://www.info-zip.org/pub/infozip/zlib/

   - Für TrueType/OpenType-Unterstützung benötigen Sie die *FreeType 2.0
     library:*

     http://www.freetype.org

   Unter Debian und Ubuntu können Sie die Pakete installieren mit::

    $ sudo apt-get install libjpeg62-dev libfreetype6

   Unter Fedora und CentOS können Sie die Pakete installieren mit::

    $ sudo yum install libjpeg-turbo-devel freetype-devel

   Unter Mac OS X können Sie die Pakete z.B. mit `Homebrew
   <http://mxcl.github.com/homebrew/>`_ installieren::

    $ brew install freetype jpeg libtiff

   Sofern diese Anforderungen erfüllt sind, wird die PIL mit folgendem Eintrag
   in der ``base.cfg``-Datei installiert::

    [buildout]
    …
    versions = versions
    …
    eggs =
        Pillow

    [versions]
    …
    Pillow = 1.7.8

#. Schließlich wird ab Plone 4.2 auch `lxml <http://lxml.de/>`_ benötigt.

   Unter Debian und Ubuntu können Sie die Pakete installieren mit::

    $ sudo apt-get install libxml2-dev libxslt1-dev

   Unter Fedora und CentOS können Sie die Pakete installieren mit::

    $ sudo yum install libxml2-devel libxslt-devel

#. Nun kann Buildout aufgerufen werden::

       $ ../venv/bin/buildout -c devel.cfg
       …
       --------------------------------------------------------------------
       SETUP SUMMARY (Pillow 1.7.8 / PIL 1.1.7)
       --------------------------------------------------------------------
       version      1.7.8
       platform     darwin 2.7.3 (default, Feb  8 2013, 10:02:27)
                    [GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2336.11.00)]
       --------------------------------------------------------------------
       --- TKINTER support available
       --- JPEG support available
       --- ZLIB (PNG/ZIP) support available
       --- FREETYPE2 support available
       *** LITTLECMS support not available

       --------------------------------------------------------------------

   Dieser Prozess kann längere Zeit dauern, da Zope, Plone und alle
   Zusatzprodukte heruntergeladen und installiert werden.

#. Ist der Prozess abgeschlossen, kann der Zope-Server gestartet werden mit::

    § ./bin/instance start

   Und das Stoppen des Zope-Servers geht mit::

    § ./bin/instance stop

   Schlägt das Starten des Zope-Servers fehl, können Sie den Zope-Server im
   Vordergrund starten und bekommen dann auf der Konsole ausgegeben, an welcher
   Stelle Zope den Startvorgang abbricht::

    $ ./bin/instance fg

   Mit ``STRG-c`` kann dieser Prozess wieder beendet werden.

   .. _`Python Imaging Library (PIL)`: http://www.pythonware.com/products/pil

#. Schließlich sollten Sie noch den ``admin``-Zugang ersetzen. Hierzu starten
   Sie zunächst die Instanz und gehen dann in den *User Folder* des Zope
   Management Interface (ZMI): ``http://localhost:8080/acl_users/manage``.

   Hier können Sie unter ``http://localhost:8080/acl_users/manage_users`` einen
   neuen Nutzer anlegen und diesem die Rolle *Manager* zuweisen.

   Anschließend können im ZMI ``Logout`` auswählen und sich gleich anschließend
   wieder mit den neuen Zugangsdaten anmelden.

   Nun sollten Sie noch den ``admin``-Nutzer löschen.

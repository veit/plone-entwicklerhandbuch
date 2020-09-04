Konzepte
========

`Buildout <http://pypi.python.org/pypi/zc.buildout/>`_
    erlaubt, identische Entwicklungsumgebungen einfach aufzusetzen. Hierzu nutzt
    ``buildout`` die Fähigkeit der `setuptools
    <http://peak.telecommunity.com/DevCenter/setuptools>`_, automatisch
    Abhängigkeiten aufzulösen und Aktualisierungen durchzuführen (s.a.: `Jim
    Fulton: Buildout Tutorial <http://buildout.zope.org/docs/tutorial.html>`_).
`Python Eggs <http://peak.telecommunity.com/DevCenter/PythonEggs>`_
    sind ein Deploymentformat für Python-Packages. Sie enthalten ein
    ``setup.py``-Skript mit Metainformationen (Lizenz, Abhängigkeiten, etc.) Mit
    der Python-Bibliothek *Setuptools* können solche Abhängigkeiten automatisch
    nachgeladen werden, wobei in Eggs spezifische Versionen angegeben werden
    können.
`Python Package Index PyPI <http://pypi.python.org/pypi/>`_ (aka Cheese Shop)
    Index mit tausenden von Python-Paketen. Setuptools, ``easy_install`` und
    Buildout nutzen diesen Index, um Eggs automatisch zu installieren.
`EasyInstall <http://peak.telecommunity.com/DevCenter/EasyInstall>`_
    Python-Modul mit dem der *Python Package Index* durchsucht werden kann und
    das die Pakete in die globale Python-Umgebung installiert. Wir werden nur
    Buildout mit EasyInstall installieren, alle weiteren Eggs werden von
    Buildout in das lokale Buildout-Projekt heruntergeladen, unter anderem um
    Versionskonflikte zu vermeiden.

Installation
============

Bevor ``zc.buildout`` installiert werden kann, sind folgende Schritte
erforderlich:

#. Installation von `Python <http://www.python.org/download/releases/>`_.

   #. Anforderungen

      - bash oder eine andere Shell
      - ein C- und C++-Compiler
      - GNU make
      - Zope setzt das Python-zlib-Modul voraus, das
        Python beim Kompilieren erstellt sofern zlib.h
        in ``/usr/include`` installiert ist.

      Für diese Anforderungen müssten auf Debian- und
      Ubuntu-Systemen folgende Pakete installiert
      werden::

       $ sudo apt-get install build-essential zlib1g-dev

      oder::

       $ sudo yum install make gcc-c++ zlib-devel

      Falls Sie die SSL-Bibliotheken benötigen, z.B.
      zum Verschicken von Mails mit TLS, sollten Sie
      auf Debian- und Ubuntu-Systemen das OpenSSL-
      Paket installieren::

       $ sudo apt-get install libssl-dev

      oder::

       $ sudo yum install openssl-devel

      Mir der GNU Readline-Bibliothek können Sie im
      Python-Prompt die zuletzt eingegebenen Befehle
      erneut aufrufen::

       $ sudo apt-get install libreadline6-dev

      Für die Indizierung von Word- und PDF-Dokumenten
      werden darüberhinaus noch die folgenden Pakete
      benötigt::

       $ sudo apt-get install wv poppler-utils

      oder::

       $ sudo yum install wv poppler-utils

   #. Erstellen und Installieren

      .. note::
        Im Folgenden wird Python 2.7 für Plone 4.3 installiert. Für Plone 4.1
        und 4.0 benötigen Sie jedoch Python 2.6 und für Plone 3 Python 2.4. Die
        Installationsschritte für moderne Linux-Installationen unterscheiden
        sich jedoch, sodass sie besonders behandelt werden.

      ::

          $ sudo apt-get install python-dev python-libxml2 python-libxslt1 python-virtualenv

      oder::

          $ sudo yum install python27-devel python-lxml python-virtualenv

      Anschließend können Sie ein Virtual Environment erstellen und darin
      ``zc.buildout`` installieren::

          $ virtualenv --system-site-packages venv
          $ cd venv
          $ ./bin/pip install zc.buildout

      Alternativ können Sie selbst Python aus den Sourcen kompilieren.
      Gehen Sie hierzu in das Verzeichnis, in dem Sie die aktuelle Python-
      Version installieren möchten, z.B. in ``/opt/``. Anschließend
      laden Sie das Python-Paket herunter und entpacken es::

       # curl -O http://www.python.org/ftp/python/2.7.9/Python-2.7.9.tgz
       # tar -xvzf Python-2.7.9.tgz

      Installieren Sie das Python-2.7.9-Paket::

       # cd Python-2.7.9
       # ./configure --prefix=/opt/python/2.7.9

      ``--prefix``
       Python-Installationspfad. Ohne Angabe wird
       Python in ``/usr/local`` erstellt.

      Anschließend fahren Sie mit der Installation fort::

       # make
       # make install

#. Der Python-Interpreter kann nun in ``PATH`` eingetragen werden. Hierzu wird folgendes in die ``~/.bashrc`` (oder auf dem Mac in ``~/.bash_profile``) eingetragen::

    export PATH=/opt/python/2.7.9/bin:$PATH

   Danach kann die Konfiguration neu eingelesen werden mit::

    $ source ~/.bashrc

#. Buildout benötigt zusätzlich auch noch ``easy_install``::

    # mkdir /opt/python/2.7.9/Extensions
    # cd $_
    # curl -O http://peak.telecommunity.com/dist/ez_setup.py
    # python ez_setup.py

   Welche Versionen dieser Python-Pakete mit ``easy_install`` installiert wurde,
   erfahren Sie indem Sie das jeweilige Skript aufrufen mit der Option
   ``--version``.

   Wollen Sie zu einem späteren Zeitpunkt eines dieser Python-Pakete
   aktualisieren, so können Sie dies mit der Option ``-U``, also z.B.::

    # easy_install -U setuptools

   Sie können auch spezifische Versionen angeben, z.B.::

    # easy_install setuptools==0.9.8

   .. note::
    Verwenden Sie z.B. Subversion 1.5 zusammen mit Buildout und erhalten folgende Fehlermeldung::

        NameError: global name 'log' is not defined

    dann benötigen Sie mindestens die ``dev06``-Version der setuptools. Dies erhalten Sie mit::

        # easy_install setuptools>=dev06

Mac OS X
--------

#. Installieren der `OSX development tools (XCode) <http://developer.apple.com/>`_.
#. Installieren von `Macports <http://www.macports.org/>`_.
#. Um ``bootstrap.py`` aufzurufen, sollte folgender Befehl verwendet werden um zu
   gewährleisten, dass der Python-Interpreter von Macports verwendet wird::

    $ python2.7 bootstrap.py

Weitere Informationen
---------------------

Buildout hinter einem Proxy
 Häufig kann Buildout nicht direkt auf die Quellen zugreifen um Python Eggs o.ä.herunterzuladen. In diesem Fall sollte der Proxy zunächst als Environment-Variable z.B. in der ``~/.bashrc``-Datei angegeben werden::

  export http_proxy = http://localhost:8123/
  export https_proxy = http://localhost:8123/

 Alternativ kann auch über einen ssh-Tunnel auf den entfernten Server zugegriffen werden::

  $ ssh -L 8123:localhost:8123 yourserver.com

Setzen des ``LD_LIBRARY_PATH``
 ``LD_LIBRARY_PATH`` ist eine Unix-Environment-Variable, die angibt, aus welchem Verzeichnis dynamisch verlinkte Bibliotheken (``*.so``-Dateien) geladen werden sollen. Falls die systemweit verfügbaren Bibliotheken überschrieben werden sollen, kann dies mit ``environment-vars`` aus dem ``zope2instance``-Rezept geschehen::

  [instance]
  …
  # Use statically compiled libxml2
  environment-vars =
      LD_LIBRARY_PATH ${buildout:directory}/parts/lxml/libxml2/lib:${buildout:directory}/parts/lxml/libxslt/lib

 s.a. `Issue 11715: Building Python on multiarch Debian and Ubuntu - Python tracker
 <http://bugs.python.org/issue11715l>`_.

Python 2.6
----------

Für Python 2.6 müssen zunächst einige Dateien geändert werden bevor sie auf
moderneren Linux-Distributionen mit ``multiarch``-Features, die manche
Bibliotheken in architekturspezifischen Verzeichnissen speichern, so z.B. in
``/usr/lib/x86_64-linux-gnu/libz.so``.

#. Zunächst wird die Python-Distribution heruntergeladen und entpackt::

    # wget https://www.python.org/ftp/python/2.6.9/Python-2.6.9.tar.xz
    # tar xvzf Python-2.6.9.tgz

#. Anschließend wechseln wir in dieses Verzeichnis und ergänzen in der Datei
   ``setup.py`` die ``lib_dirs`` um ``/usr/lib/x86_64-linux-gnu``, sodass der
   Abschnitt anschließend folgendermaßen aussieht::

    lib_dirs = self.compiler.library_dirs + [
        '/lib64', '/usr/lib64',
        '/lib', '/usr/lib',
        '/usr/lib/x86_64-linux-gnu'
        ]

#. Anschließend ändern wir in der Datei ``Modules/_ssl.c`` den Abschnitt mit ``PySSL_BEGIN_ALLOW_THREADS``::

    PySSL_BEGIN_ALLOW_THREADS
    if (proto_version == PY_SSL_VERSION_TLS1)
        self->ctx = SSL_CTX_new(TLSv1_method()); /* Set up context */
    else if (proto_version == PY_SSL_VERSION_SSL3)
        self->ctx = SSL_CTX_new(SSLv3_method()); /* Set up context */
    else if (proto_version == PY_SSL_VERSION_SSL23)
        self->ctx = SSL_CTX_new(SSLv23_method()); /* Set up context */
    PySSL_END_ALLOW_THREADS

#. In derselben Datei sind auch noch die Protokoll-Versionen anzupassen::

    /* protocol versions */
    PyModule_AddIntConstant(m, "PROTOCOL_SSLv3",
                            PY_SSL_VERSION_SSL3);
    PyModule_AddIntConstant(m, "PROTOCOL_SSLv23",
                            PY_SSL_VERSION_SSL23);
    PyModule_AddIntConstant(m, "PROTOCOL_TLSv1",
                            PY_SSL_VERSION_TLS1);

#. Auch in ``Lib/ssl.py`` sind die Protokoll-Versionen noch anzupassen:

   Die Zeile

   ::

    from _ssl import PROTOCOL_SSLv2, PROTOCOL_SSLv3, PROTOCOL_SSLv23, PROTOCOL_TLSv1

   sollte ersetzt werden durch

   ::

    from _ssl import PROTOCOL_SSLv3, PROTOCOL_SSLv23, PROTOCOL_TLSv1

#. Nun kann Python 2.6 konfiguriert und erstellt werden mit

   ::

    # env CPPFLAGS="-I/usr/lib/x86_64-linux-gnu" LDFLAGS="-L/usr/include/x86_64-linux-gnu"  ./configure --prefix=/opt/python/2.6.9
    # make
    # make install

#. Schließlich kann noch EasyInstall installiert werden mit::

    # cd /opt/python/2.4.6/
    # mkdir Extensions
    # cd $_
    # wget https://pypi.python.org/packages/2.4/s/setuptools/setuptools-0.6c11-py2.4.egg#md5=bd639f9b0eac4c42497034dec2ec0c2b
    # export PATH=/opt/python/2.4.6/bin:$PATH
    # sh setuptools-0.6c11-py2.4.egg

.. Weitere Infos unter http://ubuntuforums.org/showthread.php?t=1976837

Python 2.4
----------

Auch für Python 2.4 müssen zunächst einige Änderungen vorgenommen werden bevor
es auf moderneren Linux- oder Debian-Distributionen mit sog. ``multiarch``-
Architektur lauffühig ist.

#. Zunächst wird die Python-Distribution heruntergeladen und entpackt::

    # wget https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz
    # tar xvzf Python-2.4.6.tgz

#. Anschließend wechseln wir in dieses Verzeichnis und ergänzen in der Datei
   ``setup.py`` die ``lib_dirs`` um ``'/usr/lib/x86_64-linux-gnu'``, sodass der
   Abschnitt anschließend folgendermaßen aussieht::

    lib_dirs = self.compiler.library_dirs + [
        '/lib64', '/usr/lib64',
        '/lib', '/usr/lib',
        '/usr/lib/x86_64-linux-gnu'
        ]

#. Weiter unten in derselben Datei sind die Pfade nochmals anzupassen in
   ``ssl_libs``::

    ssl_libs = find_library_file(self.compiler, 'ssl',lib_dirs,
                                 ['/usr/local/ssl/lib',
                                  '/usr/contrib/ssl/lib/',
                                  'x86_64-linux-gnu'
                                 ] )

#. Nun wird Python 2.4 konfiguriert und erstellt mit::

    # env CPPFLAGS="-I/usr/lib/x86_64-linux-gnu" LDFLAGS="-L/usr/include/x86_64-linux-gnu"  ./configure --prefix=/opt/python/2.4.6
    # make
    # make install

#. Schließlich kann noch EasyInstall installiert werden mit::

    # cd /opt/python/2.4.6/
    # mkdir Extensions
    # cd $_
    # wget https://pypi.python.org/packages/2.4/s/setuptools/setuptools-0.6c11-py2.4.egg#md5=bd639f9b0eac4c42497034dec2ec0c2b
    # export PATH=/opt/python/2.4.6/bin:$PATH
    # sh setuptools-0.6c11-py2.4.egg

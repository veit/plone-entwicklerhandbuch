====================
Jenkins-Installation
====================

.. note:: Eine Anleitung zum Installieren von Jenkins finden Sie in `Installing
          Jenkins <https://wiki.jenkins-ci.org/display/JENKINS/Installing+Jenkins>`_.
          Falls jedoch keine dieser Möglichkeiten zutreffend sein sollte, können
          Sie den Jenkins Continous Integration Server auch einfach mit Buildout
          und dem Rezept `jarn.jenkins`_ installieren.

::

 [buildout]

    [buildout]

    parts =
       jetty-download
       jenkins-download
       jenkins

    [jetty-download]
    recipe = hexagonit.recipe.download
    url =  http://ftp.halifax.rwth-aachen.de/eclipse//jetty/stable-9/dist/jetty-distribution-9.2.2.v20140723.tar.gz
    strip-top-level-dir = true

    [jenkins-download]
    recipe = hexagonit.recipe.download
    url = http://mirrors.jenkins-ci.org/war/latest/jenkins.war
    download-only = true

    [jenkins]
    recipe = jarn.jenkins
    jetty-location = ${jetty-download:location}
    jenkins-location = ${jenkins-download:location}
    host = localhost
    port = 8070

.. _`jarn.jenkins`: http://pypi.python.org/pypi/jarn.jenkins/

Hiermit wird sowohl jetty als auch Jenkins heruntergeladen und ein ausführbare Jetty-Umgebung in ``parts/jenkins`` erstellt. Außerdem wird mit ``bin/jenkins`` ein Skript erstellt, mit dem sich der Jenkins-Server starten und Stoppen lässt.

Um die Installation zu testen können Sie einfach folgendes angeben::

 $ ./bin/jenkins fg

Damit wird der Jetty-Server am Port ``8070`` gestartet. Die Jenkins-Instanz ist dann erreichbar unter ``http://127.0.0.1:8070/jenkins/``.

Log-Datei
 Diese wird von Jenkins schreibt nach ``var/jenkins/log`` geschrieben.
Konfiguration
 Die Konfiguration einschließlich der auszuführenden Jobs wird von Jenkins nach ``var/jenkins/data`` geschrieben. Dabei entspricht der Verzeichnisname in ``var/`` dem Namen des Abschnitts, das das Rezept ``jarn.jenkins`` verwendet.

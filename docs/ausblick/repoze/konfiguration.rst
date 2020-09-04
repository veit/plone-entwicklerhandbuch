=============
Konfiguration
=============

Die Konfigurationsdatei des Repoze-Projekts ``etc/zope2.ini`` gliedert sich in folgende Abschnitte:

``[Default]``
 Dieser Abschnitt enthält globale Angaben. Zunächst ist nur folgendes angegeben::

  debug = True

 Hiermit wird das Repoze-Projekt üblicherweise im Debug-Modus gestartet, wobei hiervon nicht nur der Zope-Server, sondern auch weitere Paste-Middleware beeinflusst werden kann.

``[app:zope2]``
 In diesem Abschnitt wird die ``zope2``-WSGI-Anwendung definiert.

 ``paste.app_factory``
  Paste-spezifische Angabe für den Aufruf einer WSGI-Anwendung.

 Die weiteren Angaben dieses Abschnitt sind Konfigurationen von ``obob``, einem Object Publishing Framework für Repoze.

 ``zope.conf``
  gibt den Ort der Zope-Konfigurationsdatei an, wobei ``%(here)s`` eine Paste-Konvention für das Verzeichnis ist, in der die Paste-Konfigurationsdateien liegen.

``[pipeline]``
 Abschnitt, der jeweils eine WSGI-Pipeline definiert. Eine Pipeline kann aus keiner oder mehr Middleware und einer Anwendung bestehen::

  [pipeline:main]
  pipeline = egg:Paste#cgitb
             egg:Paste#httpexceptions
  #           egg:Paste#translogger
             egg:repoze.retry#retry
             egg:repoze.tm#tm
             egg:repoze.vhm#vhm_xheaders
             errorlog
             zope2

 In dieser Konfiguration steht ``zope2`` am Ende und verweist auf die im Abschnitt ``[app:zope2]`` definierte Zope-WSGI-Anwendung.

 ``egg:Paste#cgitb``
  Exception handler, der die Ausgabe des tracebacks coloriert. Es können auch andere exception handler, wie z.B. `evalerror`_, verwendet werden::

   egg:Paste#evalerror

 ``egg:Paste#httpexceptions``
  gibt für bestimmte Python-Exceptions entsprechende HTTP-Exceptions aus, z.B. ``404 Not Found``, ``302 Redirect``, ``401 Unauthorized``.
 ``egg:Paste#translogger``
  Wird der ``translogger`` eingeschaltet, wird das Access-Log in der Konsole ausgegeben.
 ``egg:repoze.retry#retry``
  Implementierung einer *retry policy*, wobei konfiguriert werden kann, bei welchen Fehler eine erneute Anfrage erfolgt und wie oft eine solche Anfrage wiederholt wird.
 ``egg:repoze.tm#tm``
  Implementierung der *ZODB transaction management policy*. ``repoze.tm`` kann auch verwendet werden um Transaktionen z.B. von relationalen Datenbanken oder von Dateisystem-Operationen zu steuern.
 ``egg:repoze.vhm#vhm_xheaders``
  Zope’s Virtual Host Monster entsprechende WSGI-Middleware. Die Schreibweise unterscheidet sich zwar, die Wirkung ist jedoch dieselbe (s.a. `README.txt`_).
 ``errorlog``
  Ersatz für Zope2’s ``error_log``.

``[server:main]``
 Dieser Abschnitt definiert, welcher HTTP-Server in welcher Konfiguration verwendet wird. Statt des ZServers könnte hier auch Paste, WSGIUtils oder cherrypy angegeben werden. Einen Überblick über verschiedene Server-Konfigurationen finden Sie hier: `In the Fitting Room: Trying on WSGI Servers`_.

.. _`README.txt`: http://svn.repoze.org/repoze.vhm/trunk/README.txt
.. _`evalerror`: http://pythonpaste.org/screencasts/evalerror-screencast.html
.. _`In the Fitting Room: Trying on WSGI Servers`: http://blog.repoze.org/fitting_room-20071029.html

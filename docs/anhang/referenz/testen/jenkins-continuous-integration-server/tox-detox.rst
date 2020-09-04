=========
tox/detox
=========

Auf virtualenv basierende Automatisierung von Tests.

`tox <https://pypi.python.org/pypi/tox/1.4.3>`_ kann verwendet werden

- zur Überprüfung, ob Ihr Paket mit verschiedenen Python-Versionen und
  Interpretern installiert werden kann
- zum Ausführen der Tests in verschiedenen Environments und mit verschiedenen
  Testwerkzeugen
- als Frontend für Continous Integration Server, das unnötige Wiederholungen
  vermeidet sowie CI- und Shell-basierte Tests verbindet.

`detox <https://pypi.python.org/pypi/detox>`_ erlaubt das verteilte Aufrufen von
``tox``, sodass Tests parallel ausgeführt werden können. Die Optionen und die
Konfigurationsmöglichkeiten entsprechen denen von ``tox``.

Weitere Informationen erhalten Sie in der Dokumentation zum `tox automation
project <http://testrun.org/tox/latest//>`_. Dort ist auch die Verwendung
zusammen mit dem Jenkins Integration Server beschrieben: `Using Tox with the
Jenkins Integration Server
<http://tox.readthedocs.org/en/latest/example/jenkins.html>`_.

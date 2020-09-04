=====================================
Jenkins Continuous Integration Server
=====================================

Mit einem Continuous Integration Server können periodisch Unit- und Integrationstests durchlaufen werden.

Der `Jenkins Continuous Integration Server`_ kann Sie zudem sofort informieren, wenn ein Test fehlschlägt. Dies wird vor allem dann bedeutsam, wenn Sie mit anderen an derselben Code-Basis arbeiten. Dabei informiert Sie Jenkins, welches Checkin fehlschlug mit Revisionsnummer, Cheickin-Nachricht und Autor.

Mit `collective.xmltestreport`_ kommt ein Test-Runner, dessen XML-Ausgabe von Jenkins zur Erstellung von Grafiken und Trends verwendet werden kann.

.. _`Jenkins Continuous Integration Server`: http://jenkins-ci.org/
.. _`collective.xmltestreport`: http://pypi.python.org/pypi/collective.xmltestreport

.. toctree::
    :titlesonly:
    :maxdepth: 1

    jenkins-installation
    erstellen-eines-jobs
    tox-detox

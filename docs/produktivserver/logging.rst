=======
Logging
=======

Zope erstellt drei verschiedene Arten von Log-Dateien:

``eventlog``
    Ereignisse, die Debug-Informationen über in der Zope-Instanz verwendete Produkte enthalten.
``logger access``
    Zugriffe, mit denen sich Site-Statistiken produzieren lassen.
``logger trace``
    Detaillierte Informationen über Server-Anfragen (requests).

Die Standardkonfiguration für eine Log-Datei sieht so aus::

    <eventlog>
        level info
        <logfile>
            path  /home/veit/myproject/var/log/instance.log
            level info
        </logfile>
    </eventlog>

Mögliche Angaben für ``level`` sind ``critical``, ``error``, ``warn``, ``info``,
``debug`` und ``all``.

Handler
=======

Jeder der drei ``logger``-Abschnitte der ``zope.conf`` kann mehrere ``handler``-
Abschnitte enthalten.

Fünf verschiedene Handler lassen sich angeben:

- ``logfile``
- ``syslog``
- ``win32-eventlog``
- ``http-handler``
- ``email-notifier``

Um z.B. eine E-Mail-Benachrichtigung bei Fehlern zu erhalten kann der Eintrag folgendermaßen geändert werden::

    <eventlog>
        level info
        <logfile>
            path ${buildout:directory}/var/log/instance.log
            level info
        </logfile>
        <email-notifier>
            from zope@veit-schiele.de
            to admin@veit-schiele.de
            subject "Zope Error"
            level error
        </email-notifier>
    </eventlog>

Mögliche Angaben für jeden Handler sind in
``parts/zope2/lib/python/ZConfig/components/logger/handlers.xml`` beschrieben.

Packen und Rotieren der Log-Dateien
===================================

Plone ≥ 4.2.2
-------------

Ab Plone 4.2.2 wird Plone mit einer Version von ``plone.recipe.zope2instance``
ausgeliefert, die die Konfiguration der Log-Rotation in der ``deploy.cfg``-Datei
angegeben werden, z.B.::

    [instance-base]
    ...
    event-log-max-size = 5 MB
    event-log-old-files = 7
    access-log-max-size = 20 MB
    access-log-old-files = 7

Hiermit werden 7 Generationen der Log-Dateien mit maximal 5 MB für Event-Logs und 10 MB für Access-Logs aufbewahrt.

Plone ≥ 4.0
-----------

Ab Zope 2.11 kann die Rotation der Zope-Log-Dateien von Zope selbst vorgenommen
werden. Hierzu kann in der ``deploy.cfg``-Datei z.B. Folgendes angegeben werden::

    [instance]
    recipe = plone.recipe.zope2instance
    ...
    event-log-custom =
        <logfile>
            path ${buildout:directory}/var/log/${:_buildout_section_name_}.log
            when D
            old-files 7
        </logfile>
    access-log-custom =
        <logfile>
            path ${buildout:directory}/var/log/${:_buildout_section_name_}-Z2.log
            when D
            old-files 7
        </logfile>

Folgende Angaben sind zum Rotieren der Log-Dateien möglich:

``path``
    Erforderliche Pfadangabe, z.B. ``${buildout:directory}/var/log/instance.log``
``old-files``
    Wieviele alte Log-Dateien sollen aufbewahrt werden?

    Der Standardwert ist ``0``.
``max-size``
    Maximale Größe der Log-Datei
``when``
    Wann sollen die Log-Dateien rotiert werden, z.B. ``D`` für täglich
``interval``
    Intervall zwischen den zu rotierenden Log-Dateien
``format``
    Format der Log-Dateien.

    Der Standardwert ist ``%(name)s %(message)s`` und der Suffix ``.log_format``.

Alternativ können auf \*ix-Betriebssystemen die Log-Dateien auch mit
``logrotate`` rotiert werden:

- Ändern Sie die ``deploy.cfg`` folgendermaßen::

    [buildout]
    parts =
        ...
        logrotate
        ...
    [logrotate]
        recipe = collective.recipe.template
        input = templates/logrotate.conf.in
        output = ${buildout:directory}/etc/logrotate.conf

  Mit `collective.recipe.template
  <http://pypi.python.org/pypi/collective.recipe.template>`_ lassen sich
  Textdateien aus einer Vorlage generieren, wobei die ``buildout``-Variablen
  verwendet werden können.

- Dabei können Sie ein Verzeichnis ``templates`` und darin eine
  ``logrotate.conf``-Datei erstellen, z.B. mit folgendem Inhalt::

    daily
    missingok
    rotate 14
    mail zope-logs@veit-schiele.de
    compress
    delaycompress
    notifempty
    size 1k

    ${buildout:directory}/var/log/zeoserver.log {
        postrotate
            ${buildout:bin-directory}/zeoserver logreopen
        endscript
    }

    ${buildout:directory}/var/log/instance.log ${buildout:directory}/var/log/instance-Z2.log {
        sharedscripts
        postrotate
            ${buildout:bin-directory}/instance logreopen
        endscript
    }

    ${buildout:directory}/var/log/instance2.log ${buildout:directory}/var/log/instance2-Z2.log {
        sharedscripts
        postrotate
            ${buildout:bin-directory}/instance2 logreopen
        endscript
    }

  - Damit werden alle Log-Dateien in ``/home/veit/myproject/var/log/`` täglich
    rotiert;
  - Log-Dateien älter als 14 Tage werden gelöscht.
  - Die Log-Dateien werden an die E-Mail-Adresse ``zope-logs@veit-schiele.de``
    gesendet.
  - Weitere Informationen zu ``logrotate`` erhalten Sie mit ``man logrotate``.

Cron
====

Ein Eintrag in die crontab mit ``crontab -e`` könnte z.B. so aussehen::

    7 0 * * * /usr/sbin/logrotate -s  /home/veit/myproject/var/log/logrotate-status /home/veit/myproject/etc/logrotate.conf

Damit wird täglich um 0:07 Uhr logrotate mit den Einstellungen von ``/home/veit/myproject/etc/logrotate-zope`` aufgerufen und ein Statusbericht in ``/home/veit/myproject/var/log/logrotate-status`` geschrieben.

Dieser Eintrag kann auch automatisiert mit dem Rezept ``z3c.recipe.usercrontab`` erstellt werden. Hierzu wird in der ``deploy.cfg`` folgendes eingetragen::

    [buildout]
    parts =
        ...
        logrotate-crontab
    ...
    [logrotate-crontab]
    recipe = z3c.recipe.usercrontab
    times = 7 0 * * *
    command = /usr/sbin/logrotate -s ${buildout:directory}/var/log/logrotate-status ${buildout:directory}/etc/logrotate.conf

**Anmerkung:** Falls Sie unter Windows eine Version von Zope verwenden, die kleiner als Zope 2.11 ist, können Sie sich ein eigenes Batch-Skript schreiben, das Ihnen die Log-Dateien rotiert. Als Vorbild kann z.B. folgendes Skript genommen werden: `Apache for Win32 Log file Rotation <http://www.sprint.net.au/~terbut/usefulbox/apachelogrot.htm>`_.

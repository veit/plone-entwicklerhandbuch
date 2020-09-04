===============================
ZEO-Cluster automatisch starten
===============================

Damit der ZEO-Cluster beim Starten des Hosts automatisch mitgestartet wird, legen wir ein Shell-Skript an, das anschließend in das /etc/init.d-Verzeichnis eingebunden wird.

Das Skript ``/srv/myproject/zeo`` kann z.B. so aussehen::

 #!/bin/sh
 # /etc/rc.d/init.d/zeo
 # Startup script for a ZEOCluster
 #
 # chkconfig: 345 80 20
 # description: Zope, a scalable web application server
 #
 # config: /srv/myproject/deploy.cfg
 #
 # LSB Source function library
 . /lib/lsb/init-functions

 RETVAL=0
 # list zeo clients in the list below
 zeoclients="instance instance2"
 # this is for the default install path
 clusterpath="/srv/myproject"
 prog="ZEOCluster"

 start() {
     echo -n $"Starting $prog: "
     output=`${clusterpath}/bin/zeoserver start`
     # the return status of the zeoserver is not reliable, we need to parse
     # its output via substring match
     if echo $output | grep -q "start"; then
             # success
             touch /var/lock/zope/$prog
             log_success_msg "zeoserver started successfully"
             echo
             RETVAL=0
     else
             # failed
             log_failure_msg "zeo failed to start or was already started"
             echo
             RETVAL=1
     fi
     for client in $zeoclients
         do
             echo -n $"Starting $client: "
             output=`${clusterpath}/bin/${client} start`
             # the return status of the instance is not reliable, we need to parse
             # its output via substring match
             if echo $output | grep -q "start"; then
                 # success
                 touch /var/lock/zope/${client}
                 log_success_msg "$client started successfully"
                 echo
                 RETVAL=0
             else
                 # failed
                 log_failure_msg "$client failed to start or was already started"
                 echo
                 RETVAL=1
             fi
         done
         return $RETVAL
 }

 stop() {

 for client in $zeoclients
     do
        echo -n $"Stopping $client: "
        output=`${clusterpath}/bin/${client} stop`
        # the return status of the instance is not reliable, we need to parse
         # its output via substring match
         if echo $output | grep -q "stop"; then
             # success
             rm /var/lock/zope/${client}
             log_success_msg "$client stopped successfully"
             echo
             RETVAL=0
         else
             # failed
             log_failure_msg "$client failed to stop or was already stopped"
             echo
             RETVAL=1
         fi
     done
     echo -n $"Stopping $prog: "
     output=`${clusterpath}/bin/zeoserver stop`
     # the return status of the instance is not reliable, we need to parse
     # its output via substring match
     if echo $output | grep -q "stop"; then
             # success
             rm /var/lock/zope/$prog
             log_success_msg "zeoserver stopped successfully"
             echo
             RETVAL=0
     else
             # failed
             log_failure_msg "zeoserver failed to stop or was already stopped"
             echo
             RETVAL=1
     fi
         return $RETVAL
 }

 restart() {
    stop
    start
 }

 case "$1" in
   start)
     start
     ;;
   stop)
     stop
     ;;
   status)
         echo "ZEO Server:"
         output=`${clusterpath}/bin/zeoserver status`
         echo $output
         for client in $zeoclients
         do
                 echo "Zope Client" $client
                 output=`${clusterpath}/bin/${client} status`
                 echo $output
         done
         ;;
   restart)
     restart
     ;;
   condrestart)
     [ -e /var/lock/zope/$prog ] && restart
     ;;
   *)
     echo $"Usage: $0 {start|stop|status|restart|condrestart}"
     RETVAL=2
 esac

 exit $RETVAL

Dabei enthält das Skript folgende Optionen:

- ``start``
- ``stop``
- ``status``
- ``restart``
- ``condrestart``

**Anmerkung 1:** Da der ``effective-user`` auf ``zope`` gesetzt wurde (s.a. `Buildout für Produktivserver`_) sollte der Nutzer ``zope`` nun selbstverständlich in ``/var/lock/zope/`` schreiben dürfen.

**Anmerkung 2:** Gegebenenfalls sollte auch die Environment-Variable für den ``PYTHON_EGG_CACHE`` in der ``deploy.cfg``-Datei festgelegt werden::

 [instance]
 ...
 environment-vars =
     PYTHON_EGG_CACHE = /home/zope/.python-eggs

init-Prozess
============

Sofern symbolische Links in ``/etc/rc?.d`` angelegt sind, wird beim Neustart des Hosts der ZEO-Cluster ebenfalls gestartet werden. Dabei ist ``?`` eine Zahl zwischen ``0`` und ``6``, die für die unterschiedlichen Runlevel des Systems stehen. Üblicherweise wird Zope in den Runlevel ``3``, ``4`` und ``5`` gestartet. Hierfür wird nun zunächst in ``/etc/init.d`` ein symbolischer Link auf unser Skript erzeugt und dann beim Starten dieses Skripts die weiteren symbolischen Links für die genannten Runlevel erzeugt::

 $ cd /etc/init.d
 $ sudo ln -s /srv/myproject/zeo .
 $ sudo /etc/init.d/zeo start

Und falls die symbolischen Links für die Runlevel wieder entfernt werden sollen, kann dies durch folgenden Aufruf geschehen::

 $ sudo chkconfig --level 345 zeo off

User-crontab
============

Falls sie nicht die notwendigen Rechte besitzen sollten, um die entsprechenden ``init``-Skripte zu schreiben zu können, kann der Cluster beim Neustart auch über einen Eintrag in der User-crontab gestartet werden. Der Eintrag hierfür kann in der ``deploy.cfg`` angegeben werden::

 [buildout]
 ...
 parts =
     ...
     reboot

 [reboot]
 recipe = z3c.recipe.usercrontab
 times = @reboot
 command = ${buildout:directory}/zeo start

Subversion
==========

Soll das ``zeo``-Skript unter Versionsverwaltung von Subversion gestellt werden, muss Subversion noch mitgeteilt werden, dass es sich um eine ausführbare Datei handeln soll::

 $ svn propset svn:executable ON zeo

.. `Buildout für Produktivserver`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/produktivserver

.. _`Buildout für Produktivserver`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/produktivserver

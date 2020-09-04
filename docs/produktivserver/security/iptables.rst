========
iptables
========

iptables-Konfiguration
----------------------

Auf der virtuellen Maschine mit dem ZEO-Server ist der Port 9000 zu öffnen::

 # system-config-firewall-tui

 Firewall-Konfiguration: Anpassen
 Trusted Dienste: WWW (HTTP)
 Andere Ports: Hinzufügen
 Port/Port-Bereich: 9000
 Protokoll: tcp

Dies generiert die Datei ``/etc/sysconfig/iptables``::

 # Firewall configuration written by system-config-firewall
 # Manual customization of this file is not recommended.
 *filter
 :INPUT ACCEPT [0:0]
 :FORWARD ACCEPT [0:0]
 :OUTPUT ACCEPT [0:0]
 -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
 -A INPUT -p icmp -j ACCEPT
 -A INPUT -i lo -j ACCEPT
 -A INPUT -m state --state NEW -m tcp -p tcp --dport 22 -j ACCEPT
 -A INPUT -m state --state NEW -m tcp -p tcp --dport 9000 -j ACCEPT
 -A INPUT -j REJECT --reject-with icmp-host-prohibited
 -A FORWARD -j REJECT --reject-with icmp-host-prohibited
 COMMIT

Eingehende Anfragen lassen sich überprüfen mit::

 # watch iptables --list -v
 Every 2,0s: iptables --list -v                                                                  Wed Mar 20 18:30:34 2013

 Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
  pkts bytes target     prot opt in     out     source               destination
  1476  202K ACCEPT     all  --  any    any     anywhere             anywhere            state RELATED,ESTABLISHED
     0     0 ACCEPT     icmp --  any    any     anywhere             anywhere
     1    60 ACCEPT     all  --  lo     any     anywhere             anywhere
     1    60 ACCEPT     tcp  --  any    any     anywhere             anywhere            state NEW tcp dpt:ssh
     0     0 ACCEPT     tcp  --  any    any     anywhere             anywhere            state NEW tcp dpt:nfs
     6   360 ACCEPT     tcp  --  any    any     anywhere             anywhere            state NEW tcp dpt:cslistener
    18   576 REJECT     all  --  any    any     anywhere             anywhere            reject-with icmp-host-prohibited

 Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
  pkts bytes target     prot opt in     out     source               destination
     0     0 REJECT     all  --  any    any     anywhere             anywhere            reject-with icmp-host-prohibited

 Chain OUTPUT (policy ACCEPT 1405 packets, 117K bytes)
  pkts bytes target     prot opt in     out     source               destination

Nun können wir uns die aktiven Internetverbindungen anschauen mit::

 # netstat -tulpen
 Aktive Internetverbindungen (Nur Server)
 Proto Recv-Q Send-Q Local Address               Foreign Address             State       Benutzer   Inode      PID/Program name
 ...
 ...        0      0 0.0.0.0:9000                0.0.0.0:*                   LISTEN      502        1302676    23572/python
 ...

Analog sollten nun auch ``iptables`` für die Instanzen konfiguriert werden.

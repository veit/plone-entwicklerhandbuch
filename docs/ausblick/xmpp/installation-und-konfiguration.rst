==============================
Installation und Konfiguration
==============================

ejabberd
========

`ejabberd <http://www.ejabberd.im/>`_ ist ein XMPP-Applikationsserver, der vorwiegend in `Erlang <http://www.erlang.org/>`_ geschrieben ist.

Voraussetzungen
---------------

ejabberd setzt neben GNU Make und GCC mindestens auch `Expat <http://www.libexpat.org/>`_ und `Erlang <http://www.erlang.org/>`_ voraus::

 # apt-get install libexpat1-dev erlang

Installation
------------

Dies erfolgt im Buildout-Abschnitt ``[ejabberd]``::

 [ejabberd]
 recipe = rod.recipe.ejabberd
 erlang-path = /usr/bin
 url = http://www.process-one.net/downloads/ejabberd/2.1.8/ejabberd-2.1.8.tar.gz

Konfiguration
-------------

Auch die Konfiguration erfolgt mit Buildout::

 [ejabberd.cfg]
 recipe = collective.recipe.template
 input = templates/ejabberd.cfg.in
 output = ${buildout:directory}/etc/ejabberd.cfg
 xmppdomain = localhost
 pubsub_max_items_node = 1000
 admin_userid = admin
 collaboration_allowed_subnet = 0,0,0,0
 collaboration_port = 5347
 component_password = secret

Das Template finden Sie hier: `templates/ejabberd.cfg.in <ejabberd.cfg.in/view>`_.

nginx
=====

`nginx <http://wiki.nginx.org/>`_

Voraussetzungen
---------------

Die ``pcre``-Bibliothek wird benötigt für reguläre Ausdrücke in der ``location``-Direktive und für das ``ngx_http_rewrite_module``::

 # apt-get install pcre-devel

Installation
------------

Herunterladen und Installation erfolgen mit Buildout::

 [nginx]
 recipe = zc.recipe.cmmi
 url = http://nginx.org/download/nginx-1.0.8.tar.gz
 md5sum = 1049e5fc6e80339f6ba8668fadfb75f9

Konfiguration
-------------

Die Konfiguration erfolgt ebenfalls in Buildout::

 [nginx-conf]
 recipe = gocept.nginx
 configuration =
   worker_processes 1;
   daemon off;
   events {
     worker_connections 1024;
   }
   http {
     proxy_read_timeout 400;
     server {
         listen       8080;
         server_name  localhost;

         location ~ ^/http-bind {
             proxy_pass http://localhost:5280;
         }

         location / {
            proxy_pass http://localhost:8081/VirtualHostBase/http/localhost:8080/Plone/VirtualHostRoot/;
        }

    }
  }

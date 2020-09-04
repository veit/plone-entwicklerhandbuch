==========
Deployment
==========

Für das Deployment wird ein Proxy-Web-Server benötigt, der die XSL-Transformationen ausführen kann.

Nginx
=====

Um das Diazo-Theme über Nginx auszuliefern, muss Nginx Moment in einer speziellen Version des `html-xslt <http://code.google.com/p/html-xslt/>`_-Projekts kompiliert werden. Hierzu geben Sie folgendes an::

 $ ./configure --with-http_xslt_module

Falls libxml2 und libxslt nicht an den erwarteten Stellen installiert wurden, müssen mit ``--with-libxml2=<path>`` und ``--with-libxslt=<path>`` die passenden Pfade angegeben werden.

Anschließend wird die Site entpsrechend konfiguriert::

 location / {
     xslt_stylesheet /etc/nginx/theme.xsl
         path='$uri'
         ;
     xslt_html_parser on;
     xslt_types text/html;
     rewrite ^(.*)$ /VirtualHostBase/http/localhost/Plone/VirtualHostRoot$1 break;
     proxy_pass http://127.0.0.1:8080;
     proxy_set_header Host $host;
     proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
     proxy_set_header X-Diazo "true";
     proxy_set_header Accept-Encoding "";
 }

Varnish
=======

Um Edge Side Includes (ESI) in Varnish zu ermöglichen, fügen wir in der Varnish-Konfigurationsdatei folgendes hinzu::

 sub vcl_fetch {
     if (obj.http.Content-Type ~ "text/html") {
         esi;
     }
 }

Apache
======

Apache erfordert ``mod_transform`` mit *html parsing*-Unterstützung. Dann kann die Konfiguration folgendermaßen aussehen::

 NameVirtualHost *
 LoadModule transform_module /usr/lib/apache2/modules/mod_transform.so
 <VirtualHost *>

     FilterDeclare THEME
     FilterProvider THEME XSLT resp=Content-Type $text/html

     TransformOptions +ApacheFS +HTML +HideParseErrors
     TransformSet /theme.xsl
     TransformCache /theme.xsl /etc/apache2/theme.xsl

     <LocationMatch "/">
         FilterChain THEME
     </LocationMatch>

 </VirtualHost>

.. note::
    Apache ist zum aktuellen Zeitpunkt leider nicht in der Lage, Error-Responses durch die WSGI-Pipeline zu schleusen. Daher lassen sich mit Apache zum aktuellen Zeitpunkt z.B. nicht *404 Not Found*-Seiten gestalten.

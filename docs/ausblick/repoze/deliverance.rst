===========
Deliverance
===========

Deliverance erlaubt Gestaltungen auf Inhalte nach bestimmten Regeln anzuwenden.

#. `Deliverance`_ kann einfach in einem Repoze-Projekt installiert werden mit::

    $ sudo easy_install Deliverance

#. Anschließend wird in ``etc/zope2.ini`` im Abschnitt ``pipeline:main`` deliverance hinzugefügt::

    [pipeline:main]
    pipeline = egg:Paste#cgitb
               egg:Paste#httpexceptions
    #           egg:Paste#translogger
               egg:repoze.retry#retry
               egg:repoze.tm#tm
               egg:repoze.vhm#vhm_xheaders
               errorlog
               deliverance
               zope2

#. Dann wird ein neuer Abschnitt eingefügt::

    [filter:deliverance]
    paste.filter_app_factory = deliverance.wsgimiddleware:make_filter
    theme_uri = http://www.veit-schiele.de/frontpage
    rule_uri = file:///%(here)s/rules.xml

#. Schließlich wird die Datei ``etc/rules.xml`` mit folgendem Inhalt erstellt::

    <?xml version="1.0" encoding="UTF-8"?>
    <rules xmlns:xi="http://www.w3.org/2001/XInclude" xmlns="http://www.plone.org/deliverance">
      <prepend theme="//head" content="//head/link" nocontent="ignore" />
      <prepend theme="//head" content="//head/style" nocontent="ignore" />
      <append theme="//head" content="//head/script" nocontent="ignore" />
      <append theme="//head" content="//head/meta" nocontent="ignore" />
      <append-or-replace theme="//head"
                         content="//head/title"
                         nocontent="ignore" />
      <replace theme="//body//div[@id='content']"
               content="//body//div[@id='content']"
               nocontents="ignore" />
    </rules>

#. Nach dem Neustart der Zope-Instanz mit::

    $ ./bin/paster serve etc/zope2.ini

   sollte die Plone-Site nun das Motiv meiner Website übernommen haben:

   .. figure:: deliverance-theme.png
        :alt: Deliverance-Motiv

.. _`Deliverance`: http://www.openplans.org/projects/deliverance

.. - `plone.recipe.deliverance`_
.. - `Install Plone 3 behind Apache and mod_wsgi using Repoze`_
.. - `Repoze under mod_wsgi is not slow`_
.. - `Promote Deliverance as the branding/corporate ID mechanism`_
.. - `Plone Sitetheming Part 1: Why Not`_
.. - `Plone Sitetheming Part 2: Why and What`_
.. - `Kupu and deliverance`_
.. - `XDV-Server`_
.. - `Products.PloneOrg`_
.. - `Theming with collective.xdv`_

.. _`plone.recipe.deliverance`: http://pypi.python.org/pypi/plone.recipe.deliverance
.. _`Install Plone 3 behind Apache and mod_wsgi using Repoze`: http://plone.org/documentation/tutorial/install-plone-3-behind-apache-and-mod_wsgi-using-repoze
.. _`Repoze under mod_wsgi is not slow`: http://martinaspeli.net/articles/update-repoze-under-mod-wsgi-is-not-slow
.. _`Promote Deliverance as the branding/corporate ID mechanism`: http://dev.plone.org/plone/ticket/7852
.. _`Plone Sitetheming Part 1: Why Not`: http://blog.repoze.org/why-sitetheming-1-20080214.html
.. _`Plone Sitetheming Part 2: Why and What`: http://blog.repoze.org/what-sitetheming-2-20080218.html
.. _`Kupu and deliverance`: http://vanrees.org/weblog/archive/2008/03/29/kupu-and-deliverance
.. _`XDV-Server`: http://codespeak.net/svn/z3/deliverance/sandboxes/optilude/dv.xdvserver/trunk/
.. _`Products.PloneOrg`: http://svn.plone.org/svn/plone/Products.PloneOrg/trunk/
.. _`Theming with collective.xdv`: http://plone.org/products/collective.xdv/documentation/reference-manual/theming/referencemanual-all-pages

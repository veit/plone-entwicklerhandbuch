========
Security
========

Security Advisories
===================

`Plone Announce Mailinglist <http://lists.sourceforge.net/mailman/listinfo/plone-announce>`_-Mailingliste
    Eine Mailingliste mit extrem geringem Datenaufkommen, für neue Releases und
    Sicherheitshinweise. Die Liste ist moderiert und nur das Plone-Team kann auf
    dieser Liste veröffentlichen.
`RSS Feed of Plone Security Advisories <http://plone.org/products/plone/security/advisories/all-advisories/RSS>`_
    RSS 1.0-Feed

Das Abonnieren der Mailingliste oder des RSS-Feed wird unbedingt empfohlen.

Plone-Hotfixes
==============

Einen Überblick, welche Plone-Versionen welche Hotfixes benötigen, erhalten Sie
unter `Plone Hotfixes <http://jone.github.io/plone-hotfixes/>`_.

plone.protect
=============

`plone.protect <https://pypi.python.org/pypi/plone.protect>`_ bietet Methoden um
die Sicherheit von Web-Formularen in Plone zu erhöhen.

Einschränken der Requests auf HTTP-POST
---------------------------------------

::

    from plone.protect import PostOnly
    from plone.protect import protect

    @protect(PostOnly)
    def something(self, param, REQUEST=None):
        pass

Form authentication (CSRF)
--------------------------

Cross-Site-Request-Forgery
`CSRF <https://de.wikipedia.org/wiki/Cross-Site-Request-Forgery>`_ ist ein
Angriffsverfahren, bei dem ein ein HTTP-Formular an einen anderen Ort
übermittelt wird und anschließend die Parameter ausgewertet werden. *Form
authentication* soll verhindern, dass diese Parameter ausgewertet werden können
da zunächst die Authentizität überprüft wird.

Der erforderliche Token kann einfach generiert werden mit::

   <span tal:replace="structure context/@@authenticator/authenticator"/>

Zur Überprüfung des Tokens können verschiedene Methoden verwendet werden:

#. ZCA::

    authenticator=getMultiAdapter((context, request), name=u"authenticator")
    if not authenticator.verify():
        raise Unauthorized

#. mit einem Decorator::

    from plone.protect import CheckAuthenticator
    from plone.protect import protect

    @protect(CheckAuthenticator)
    def something(self, param, REQUEST=None):
        pass

#. Anfrage an einen Funktionsvalidator weiterreichen::

    from plone.protect import CheckAuthenticator
    ...
    CheckAuthenticator(self.context.REQUEST)
    ...

.. Headers

   Sie können auch einen Token übergeben, indem Sie den Header  ``X-CSRF-TOKEN``
   verwenden. Dies kann z.B. für AJAX-Requests sinnvoll sein.

Automatischer CSRF-und Clickjacking-Schutz
------------------------------------------

Seit Version 3 bietet ``plone.protect`` einen automatischen CSRF-Schutz indem  automatisch ein Auth-Token in allen internen Formularen verwendet wird, wenn der Benutzer angemeldet ist oder in die ZODB geschrieben werden soll.

Zum Schutz vor `Clickjacking <https://de.wikipedia.org/wiki/Clickjacking>`_
setzt Plone zudem den `X-Frame-Options
<https://developer.mozilla.org/en-US/docs/Web/HTTP/X-Frame-Options>`_-Header auf
``SAMEORIGIN``.

Um diesen Wert zu ändern gibt es drei Möglichkeiten:

#. In einem View überschreiben, z.B. mit::

    self.request.response.setHeader ('X-Frame-Options "," AllowAll'))

#. Im Proxy-Server überschreiben
#. Die Umgebungsvariable ``PLONE_X_FRAME_OPTIONS`` ändern

s.a. `Debugging CSRF Protection False Positives in Plone
<http://devblog.4teamwork.ch/blog/2015/10/12/debugging-csrf-protection-false-positives-in-plone/>`_

.. seealso::
    `Plone Developer Documentation: Security <http://developer.plone.org/security/index.html>`_
        Zope security facilities, Sandboxing and SELinux
    `PySprint: Sicherheit und Datenschutz bei Zope-Anwendungen <http://www.pysprints.de/sicherheit-und-datenschutz/index.html>`_
        Anhand des deutschen `Bundesdatenschutzgesetz
        <http://de.wikipedia.org/wiki/Bundesdatenschutzgesetz>`_ (BDSG) wird
        überprüft, wie Zope-Anwendungen diesen Anforderungen gerecht werden
        können.
    `WebLion: Secure Zope <https://weblion.psu.edu/trac/weblion/wiki/SecureZope>`_
        Declare IP-Addresses and :doc:`iptables` config
    `Steve McMahon, Eric Rose: Protecting Plone From The Big Bad Internet <http://www.slideshare.net/ErikRose/protecting-plone-from-the-big-bad-internet-presentation>`_
        Presentation from Plone Conference 2008 in Washington, D.C.
    `Security overview of Plone <http://plone.org/products/plone/security/overview>`_
        The ten most common security issues in web applications, and how Plone
        addresses them.
    `zopyx.plone.cassandra <http://pypi.python.org/pypi/zopyx.plone.cassandra>`_
        Show all assigned local roles within a subtree for any Plone 4 site.

.. toctree::
    :titlesonly:
    :maxdepth: 0
    :hidden:

    iptables

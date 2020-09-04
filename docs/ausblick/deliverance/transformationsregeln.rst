=====================
Transformationsregeln
=====================

Regeln
======

::

 <rule class="static" />
 <rule class="plone" suppress-standard="true">

``<rule>``
 definiert eine Reihe von Transformtionen.

 Es werden sowohl `page classes`_ als auch `request/response matching`_ unterstützt.

 .. _`page classes`: http://packages.python.org/Deliverance/configuration.html#page-classes

 .. _`request/response matching`: http://packages.python.org/Deliverance/configuration.html#request-response-matching

 Mit *page classes* lässt sich eine ``rule class`` einem bestimmten ``patch``, einer bestimmten ``domain`` oder einem bestimmten ``response-header`` zuweisen, z.B::

  <rule class="news-section">
      <theme href="/static/news.html" />

  <match path="regex:^/news" class="news-section" />

 Weitere Informationen hierzu erhalten Sie im Abschnitt `match and page classe`_.

.. _`match and page classe`: http://packages.python.org/Deliverance/configuration.html#match-and-page-classes

``suppress-standard="true"``
 Deliverance kommt üblicherweise mit einer Reihe von Aktionen, die das Kopieren des Titels oder eines Skripts erlauben. Diese sind::

  <rule>
      <replace content="children:/html/head/title"
               theme="children:/html/head/title" nocontent="ignore" />
      <append content="elements:/html/head/link"
              theme="children:/html/head" nocontent="ignore" />
      <append content="elements:/html/head/script"
              theme="children:/html/head" nocontent="ignore" />
      <append content="elements:/html/head/style"
              theme="children:/html/head" nocontent="ignore" />
  </rule>

Diese Regeln können unterbunden werden mit dem ``suppress-standard="true"``-Attribut.

Theme
=====

::

 <theme href="/static/index.html" />

``<theme>``
 definiert das Thema, das Sie verwenden in Form einer URL.

Aktionen
========

``<replace>``
 ersetzt ein Element aus ``theme`` durch ein Element aus ``content``.

 Die folgende Aktion ersetzt z.B. den Titel des *Themes* durch denjenigen aus Plone::

  <replace content='/html/head/title' theme='/html/head/title' />

``<append>``
 fügt ein Element aus ``content`` am Ende eines Elements aus ``theme`` ein.

 Die folgende Aktion hängt z.B. die ``base``-Url aus Plone an die ``head``-Angaben des *Theme*. Dies gewährleistet, dass die Links aus Plone weiterhin funktionieren::

  <append content='/html/head/base' theme='children:/html/head' />

``<prepend>``
 fügt ein Element aus ``content`` am Anfang eines Elements aus ``theme`` ein.

 Die folgende Aktion stellt  z.B. das Navigationsportlet aus Plone an den Anfang der rechten Spalte des Theme::

  <prepend content='dl.portletNavigationTree' theme='children:#rightbar' />

``<drop>``
 entfernt das Element aus dem ``content`` oder ``theme``.

 Die folgende Aktion entfernt z.B. das User-Icon von Plone::

  <drop content='#user-name img' />

Selektoren
==========

CSS3-Selektoren
 Jede Aktion beruht auf der Auswahl der Elemente des Theme und des Inhalts. Die einfachste Auswahl kann anhand von CSS-Selektoren erfolgen.
XPath
 Es können auch XPath-Angaben als Selektoren verwendet werden. Diese beginnen immer mit ``/``.

Diese beiden Selektoren verweisen immer auf Elemente. Um spezifischere Aktionen ausführen zu können, wurden daher noch die folgenden Selektoren eingeführt:

``elements``
 Der Standardselektor.
``children``
 erlaubt, Regeln auf Kindelemente der ausgewählten Elemente anzuwenden. Hiermit lassen sich auch Aktionen auf Textinhalte anwenden.
``attributes``
 Hiermit lassen sich Aktionen nur auf bestimmte Attribute der ausgewählten Elemente anwenden.
``tag``
 Dieser Selektor erlaubt, Aktionen nur auf einen Tag, nicht jedoch auf dessen Kindelemente anzuwenden.

``||``-Operator
===============

Der ``||``-Operator nimmt die Ergebnisse des ersten Selektors, sofern vorhanden. Andernfalls nimmt er die Ergebnisse des zweiten Selektrors. So verwendet z.B. die folgende Aktion alle Elemente der ID ``content``; sind in ``content`` jedoch keine Elemente vorhanden, werden die Kindelemente von ``<body>`` verwendet::

 content="#content || children:body"

``if-content``
==============

Alle Aktionen können das Attribut ``if-content`` erhalten womit die Aktion nur ausgeführt wird wenn die Bedingung erfüllt ist, z.B.::

 <replace if-content='body.section-news' content='children:dl.portletEvents dt.portletHeader a' theme='children:#rightbar h2' />

Dem zu überprüfenden Wert kann auch ``not:`` vorangestellt werden.

Externe Inhalte einbinden – Mashup
==================================

Deliverance erlaubt auch das Einbinden von externen Quellen. Hierzu wird das ``href``-Attribut für eine Aktion verwendet, z.B.::

 <append href="http://twitter.com/plone"
         content="#timeline"
         theme='#rightbar' />

Somit ist Deliverance nicht nur für das Theming beliebiger Webanwendungen geeignet, es kann auch das Mashup verschiedener Inhalte von Webanwendungen übernehmen.

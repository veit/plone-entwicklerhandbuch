=============================
Fortgeschrittene Diazo-Regeln
=============================

Bedingte Regeln
===============

… basierend auf Knoten im Inhalt
--------------------------------

``if-content`` oder ``css:if-content``
  spezifiziert ein Element im ``content``
``if-not-content`` oder ``css:if-not-content``
 kehrt die Bedingung für ein Element im ``content`` um, z.B.::

  <drop css:theme="#portlet-wrapper" css:if-not-content=".portlet"/>

``if-not-path``
  spezifiziert einen URL-Pfad, der mit dem aktuellen Request **nicht** erfüllt sein darf damit die Regel angewendet wird, z.B.::

   <drop css:theme="#news-box" if-not-path="/news"/>

… basierend auf Pfadangaben im Inhalt
-------------------------------------

``if-path`` oder ``css:if-path``
  spezifiziert einen Pfad in ``content``

  Soll der Pfad z.B. beginnen mit ``somewhere``, sieht die Regel folgendermaßen aus::

   <copy
       if-path="/somewhere"
       css:theme="#content"
       css:content="body > *"
       />

  Angabe eines exakter Pfad mit::

       if-path="/somewhere/"

  Angabe des Pfadende mit::

      if-path="somewhere/"

  Angabe eines Pfadbestandteils mit::

      if-path="somewhere"

``if-not-path`` oder ``css:if-not-path``
 kehrt die Bedingung für einen Pfad im ``content`` um

… basierend auf XPath-Ausrücken
-------------------------------

``if="$mode=''"``
  spezifiziert einen Knoten, der vorhanden sein muss, damit eine Regel oder
  ein Theme angewendet werden::

      <drop css:theme=".warning" if="$mode = 'anon-personalbar'" />

``if-not="$mode=''"``
  spezifiziert einen Knoten, der **nicht** vorhanden sein darf, damit eine
  Regel oder ein Theme ausgeführt werden

Gruppierung und Verschachtelung von Bedingungen
===============================================

Gruppierung von Bedingungen::

  <rules xmlns="http://namespaces.plone.org/diazo"
         xmlns:css="http://namespaces.plone.org/diazo/css"
         xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
      <rules css:if-content="#personal-bar">
          <after css:theme-children="#header-box" css:content="#user-prefs"/>
          <after css:theme-children="#header-box" css:content="#logout"/>
      </rules>
      …
  </rules>

Verschachtelung von Bedingungen::

 <rules if="condition1">
     <rules if="condition2">
         <copy if="condition3" css:theme="#a" css:content="#b"/>
     </rules>
 </rules>

entspricht::

 <copy if="(condition1) and (condition2) and (condition3)" css:theme="#a" css:content="#b"/>

Mehrere bedingte Themes
=======================

::

 <theme href="theme.html"/>
 <theme href="news.html" css:if-content="body.section-news"/>
 <theme href="members.html" css:if-content="body.section-members"/>

Ausgabe ändern
==============

Mit Inline-XSLT-Anweisungen lassen sich z.B. die Leerzeichen zwischen ELementen entfernen und automatische Einrückungen vornehmen::

 <xsl:strip-space elements="*" />
 <xsl:output indent="yes"/>

Inline XSLT-Anweisungen werden direkt innerhalb des ``<rules>``-Tag angegeben und ohne Bedingungen ausgeführt.

Ändern des Themes
=================

Inline-Markup
-------------

::

 <after theme-children="/html/head">
     <style type="text/css">
         /* From the rules */
         body > h1 { color: red; }
     </style>
 </after>

XSLT-Anweisungen
----------------

::

 <replace css:theme="#details">
     <dl id="details">
         <xsl:for-each css:select="table#details > tr">
             <dt><xsl:copy-of select="td[1]/text()"/></dt>
             <dd><xsl:copy-of select="td[2]/node()"/></dd>
         </xsl:for-each>
     </dl>
 </replace>

Ändern des Inhalts
==================

Inline-Markup
-------------

Mit ``<replace>`` lässt sich auch der Inhalt modifizieren, so kann z.B. das ``input``-Element mit der Klasse ``searchButton`` ersetzt werden durch ein ``button``-Element vom Typ ``submit``::

 <replace css:content="div#portal-searchbox input.searchButton">
     <button type="submit">
         <img src="images/search.png" alt="Search" />
     </button>
 </replace>

Entfernen leerer Tags
---------------------

Ein Absatz ohne Inhalte lässt sich z.B. so entfernen::

 <drop content="p[not(*) and (not(normalize-space()) or text() = '&#160;')]"/>

Einfügen eines Tags
-------------------

Tags lassen sich z.B. am Beginn oder Ende eines Inhaltsbereichs einfügen::

 <replace css:theme="#account a.dropdown-toggle"
          css:content="#portal-personaltools li#anon-personalbar a" />
 <before css:theme-children="#account a.dropdown-toggle"
         method="raw">
     <i class="icon-user"></i>
 </before>

Etwas aufwändiger wird es, wenn Tags innerhalb von Inhaltselementen eingefügt werden sollen::

 <replace css:content-children="#content" css:theme-children="#content"/>
 <before css:theme-children="#content">
     <div id="wrapper">
       <xsl:apply-templates css:select="#title" mode="raw"/>
       <xsl:apply-templates css:select="#description" mode="raw"/>
     </div>
 </before>
 <drop css:content="#title"/>
 <drop css:content="#description"/>

Attribute ändern
----------------

Auch die Attribute eines Tags lassen sich ändern. So kann z.B. eine css-
Klasse hinzugefügt werden mit::

 <xsl:template match="ul[@id='portal-globalnav']/li/@class[contains(., 'selected')]">
     <xsl:attribute name="class"><xsl:value-of select="." /> current-menu-item</xsl:attribute>
 </xsl:template>

Auch Bilder in ``content``  lassen sich hiermit in einer bestimmten Größe anzeigen mit::

 <replace css:theme="#content" css:content="#content" />
 <xsl:template match="img/@src[not(contains(., '@@'))]">
     <xsl:attribute name="src"><xsl:value-of select="." />/@@/images/image/thumb</xsl:attribute>
 </xsl:template>

Dies ändert z.B.::

 <img src="smiley.gif" class="myimage" />

in::

 <img src="smiley.gif/@@/images/image/thumb" class="myimage" />

Text einfügen
-------------

Mit ``xsl:copy`` lassen sich Texte im Inhalt ergänzen, z.B.::

 <replace css:theme="#content"
          css:content="#content" />
 <xsl:template match="h2/text()">
      <xsl:copy /> – Extra text
 </xsl:template>

Einbinden weiterer ``rules``-Dateien
====================================

Mit dem ``XInclude``-Protokoll lassen sich andere ``rules``-Dateien einschließen, z.B.::

 <rules
     …
     xmlns:xi="http://www.w3.org/2001/XInclude">
     <xi:include href="base.xml" />
 </rules>

Einbinden externer Inhalte
==========================

::

    <replace  css:theme-children="#navigation ul.dropdown-menu li a"
              css:content-children=".navTreeLevel2  > li > div"
              href="/sitemap" />

Um entfernte Inhalte einbinden zu können, muss Diazo folgendermaßen
konfiguriert werden::

    [filter:theme]
    use = egg:collective.diazo.readheaders
    #You can use any other Diazo middleware options here, too!
    read_network = True


XSLT-Anweisungen
----------------

Da der von Diazo verwendete libxml2-HTMLParser Namespace-Präfixe herauskürzt, kann z.B. der FaceBook Like-Button ``<fb:like></fb:like>`` nicht integriert werden mit ``//*[local-name()="like"]``. Stattdessen kann z.B. folgende XSL-Transformation verwendet werden::

 <xsl:template match="activity|add-profile-tab|bookmark|comments|friendpile|like|like-box|live-stream|login-button|pronoun|recommendations|serverFbml|profile-pic|user-status">
   <xsl:element name="fb:{local-name()}" xmlns:fb="http://www.facebook.com/2008/fbml">
     <xsl:apply-templates select="@*|node()"/>
   </xsl:element>
 </xsl:template>

Doctype
=======

Üblicherweise gibt Diazo den HTML-Seiten den Doctype ``XHTML 1.0 Transitional``. Um ``Strict`` anzugeben, sollte folgende XSLT angegeben werden::

 <xsl:output
     doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN"
     doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"/>

Es ist nicht möglich, den HTML5-Doctype mit XSLT zu setzen. Stattdessen sollte dann ``<!DOCTYPE html>`` gesetzt werden.

.. seealso::

    `Advanced usage <http://docs.diazo.org/en/latest/advanced.html>`_
        Englische Diazo-Dokumentation
    `diazo/lib/diazo/tests <https://github.com/plone/diazo/tree/master/lib/diazo/tests>`_
        Die Tests von Diazo enthalten viele gebräuchliche Regeln
    `Diazo Snippets Library <http://pigeonflight.github.io/lessArcane/>`_
        Snippets vor allem zur Nutzung von Bootstrap und Foundation

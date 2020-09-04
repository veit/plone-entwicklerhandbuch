Javascripts
===========

Plone bringt einige Javscripts mit, die sich einfach in Templates und Inhalten verwenden lassen.

``form_tabbing.js``
 Um Reiter in Formularen zu erhalten, erwartet dieses Skript folgendes Markup:

 ::

  <form class="enableFormTabbing">
      <fieldset id="fieldset-id1">
          <legend id="fieldsetlegend-id1">Tab one</legend>
      </fieldset>
      <fieldset id="fieldset-id2">
          <legend id="fieldsetlegend-id2">Tab two</legend>
      </fieldset>
  </form>

 Alternativ kann auch folgendes Markup verwendet werden:

 ::

  <dl class="enableFormTabbing">
      <dt id="fieldsetlegend-id1">tab one</dt>
      <dd id="fieldset-id1">content one</dd>
      <dt id="fieldsetlegend-id2">tab two</dt>
      <dd id="fieldset-id2">content two</dd>
  </dl>

``table_sorter.js``
 Um Tabellen zu sortieren kann dieses Javascript einfach in folgendem Markup verwendet werden:

 ::

  <table class="listing" id="my-table">
      <thead>
          <tr>
              <th>First Name</th>
              <th>Last name</th>
          </tr>
      </thead>
      <tbody>
          <tr>
              <td>
                  Veit
              </td>
              <td>
                  Schiele
              </td>
          </tr>
          <tr>
              <td>
                  Sönke
              </td>
              <td>
                  Löffler
              </td>
          </tr>
      </tbody>
  </table>

 - Beachten Sie bitte, dass das ``table_sorter.js``-Javascript normalerweise nur angemeldeten Nutzern zur Verfügung steht. Wollen Sie es auch anonymen Nutzern zur Verfügung stellen, sollte Ihr ``jsregistry.xml``-Profil so aussehen:

 ::

    <?xml version="1.0"?>
    <object name="portal_javascripts" meta_type="JavaScripts Registry">
    ...
    <javascript
        cacheable="True"
        compression="safe"
        cookable="True"
        enabled="True"
        expression=""
        id="table_sorter.js"
        inline="False"/>
    </object>

 - Das Skript erwartet die Klasse ``listing`` und eine eindeutige ID für die Tabelle sowie ``<th>``-Tags innerhalb von ``<thead>``-Tags.
 - Soll eine Tabelle der Klasse ``listing`` keine sortierbaren Spalten enthlaten, kann der Tabelle eine Klasse ``nosort`` hinzugefügt werden.
 - Soll nur eine Spalte innerhalb einer Tabelle nicht sortiert werden können, so kann dem entsprechenden ``<th>``-Tag die Klasse ``nosort`` zugewiesen werden.

``collapsiblesections.js``
 Dieses Javascript kannn bei folgendem Markup verwendet werden:

 ::

  <dl class="collapsible">
      <dt class="collapsibleHeader">
          Title
      </dt>
      <dd class="collapsibleContent">
          Content
      </dd>
  </dl>

 Sobald ``collapsible`` umgeschaltet wurde, erhalt das ``dl``-Tag eine zusätzliche Klasse, die zwischen ``collapsedBlockCollapsible`` und ``expandedBlockCollapsible`` hin- und herschaltet. Hierfür können Sie dann z.B. folgende CSS-Anweisungen angeben:

 ::

  .expandedBlockCollapsible .collapsibleContent {
      display: block;
  }

  .collapsedBlockCollapsible .collapsibleContent {
      display: none;
  }

 Wird die ``collapsedOnLoad``-Klasse dem ``dl``-Tag hinzugefügt, wird die Definitionsliste bereits beim Laden der Seite ausgeklappt.

 Wird die ``inline``-Klasse für das ``dl``-Tag angegeben, wird zwischen ``collapsedInlineCollapsible`` und ``expandedInlineCollapsible`` umgeschaltet anstatt zwischen ``collapsedBlockCollapsible`` und ``expandedBlockCollapsible``.

``jQuery``
 JavaScript-Bibliothek, die die Traversierung und das Event-Handling von HTML-Dokumenten vereinfacht. So lässt sich z.B. in einem Einzeiler angeben, dass alle PDFs in einem neuen Fenster geöffnet werden sollen:

 ::

  jQuery("#content a[ @href $= '.pdf']").attr('target', '_blank');

 Weitere Informationen zu jQuery erhalten Sie unter:

 - http://jquery.com/
 - http://docs.jquery.com

 Und mit `FireQuery`_ gibt es eine Firefox-Extension, die in Firebug integriert ist.

.. _`FireQuery`: http://firequery.binaryage.com/

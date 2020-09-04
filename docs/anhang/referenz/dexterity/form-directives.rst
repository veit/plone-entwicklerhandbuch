===============
Form-Directives
===============

Directives ermöglichen die Konfiguration der Formulare aus den Schemata.

Dexterity verwendet `plone.autoform`_ um die auf `z3c.form`_ basierenden Hinzufügen- und Bearbeiten-Formulare zu konfigurieren. Somit lassen sich Schema mit Anmerkungen versehen, die das Formular konfigurieren.

.. _`plone.autoform`: http://pypi.python.org/pypi/plone.autoform
.. _`z3c.form`: http://docs.zope.org/z3c.form

Diese Anmerkungen können einfach mit Direktiven aus `plone.directives.form`_ und `plone.directives.dexterity`_ einem mit ``plone.directives.form.Schema`` erstellten Schema hinzugefügt werden.

.. _`plone.directives.form`: http://pypi.python.org/pypi/plone.directives.form
.. _`plone.directives.dexterity`: http://pypi.python.org/pypi/plone.directives.dexterity

Ein einfaches Beispiel kann so aussehen::

 from zope import interface, schema
 from plone.directives import form
 …

 class IExcludeFromNavigation(form.Schema):
     """Interface to exclude items from navigation.
     """

     form.fieldset('settings', label=u"Settings",
                   fields=['exclude_from_nav'])

     exclude_from_nav = schema.Bool(
                 title=_(u'label_exclude_from_nav', default=u'Exclude from navigation'),
                 description=_(u'help_exclude_from_nav', default=u'If selected, this item will not appear in the navigation tree'),
                 default=False
                 )

     form.omitted('exclude_from_nav')

Form-Directives
---------------

Im folgenden eine Übersicht über alle Form-Directives
aus `plone.directives.form`_:

.. _`plone.directives.form`: http://pypi.python.org/pypi/plone.directives.form

+--------------------------------+----------------------------------------------------------------+
| Name                           | Beschreibung                                                   |
+================================+================================================================+
| ``widget``                     | Spezifiziert ein alternatives Widget für ein Feld.             |
|                                | Dabei wird der Feldname als Key und der Widget-Name als Value  |
|                                | angegeben. Das Widget kann entweder eine Instanz aus           |
|                                | z3c.form.widget sein oder ein Dotted Name eines Widgets.       |
+--------------------------------+----------------------------------------------------------------+
| ``omitted``                    | Spart ein oder mehrere Felder aus einem Formular aus.          |
|                                | Als Parameter kann eine Sequenz der Feldnamen angegeben werden.|
+--------------------------------+----------------------------------------------------------------+
| ``mode``                       | Folgende Modi sind möglich: ``input``, ``display``oder         |
|                                | ``hodden``. Dabei wird der Feldname als Key und der Modus als  |
|                                | Value angegeben.                                               |
+--------------------------------+----------------------------------------------------------------+
| ``order_before``               | Spezifiziert, dass das betreffende Feld vor einem anderen      |
|                                | gerendert werden soll. Ist das Feld in einem zusätzlichen      |
|                                | Schema definiert (z.B. in einem Behavior), ist der Name z.B.   |
|                                | ``ICategorization.language``.  Alternativ kann auch ``*``      |
|                                | verwendet werden um das Feld am Anfang des Formulars           |
|                                | anzuzeigen.                                                    |
+--------------------------------+----------------------------------------------------------------+
| ``order_after``                | Spezifiziert, dass das betreffende Feld nach einem anderen     |
|                                | gerendert werden soll. Ist das Feld in einem zusätzlichen      |
|                                | Schema definiert (z.B. in einem Behavior), ist der Name z.B.   |
|                                | ``ICategorization.language``.  Alternativ kann auch ``*``      |
|                                | verwendet werden um das Feld am Ende des Formulars             |
|                                | anzuzeigen.                                                    |
+--------------------------------+----------------------------------------------------------------+
| ``primary``                    | Markiert ein bestimmtes Feld als Primary Field in einem Schema.|
|                                | Dies wird beim Zugriff per WebDAV für das Marshalling des      |
|                                | Objekts verwendet.                                             |
+--------------------------------+----------------------------------------------------------------+
| ``fieldset``                   | Erstellt ein Fieldset, das in Plone als Reiter im Bearbeiten-  |
|                                | Formular angezeigt wird.                                       |
+--------------------------------+----------------------------------------------------------------+

Security-Directives
-------------------

Im folgenden die Security-Directives aus ``plone.directives.dexterity``:

+--------------------------------+----------------------------------------------------------------+
| Name                           | Beschreibung                                                   |
+================================+================================================================+
| ``read_permission``            | Setzt die Zope3-Permission, die zum Lesen des Feldwerts        |
|                                | erforderlich ist. Dabei wird der Feldname als Schlüssel und    |
|                                | die Berechtigung als Wert angegeben.                           |
+--------------------------------+----------------------------------------------------------------+
| ``write_permission``           | Setzt die Zope3-Permission, die zum Schreiben des Feldwerts    |
|                                | erforderlich ist. Dabei wird der Feldname als Schlüssel und    |
|                                | die Berechtigung als Wert angegeben.                           |
+--------------------------------+----------------------------------------------------------------+

=======
Widgets
=======

Falls die übliche Verwendung von Widgets nicht ausreicht, können auch spezifische Widgets verwendet werden, die eine größere Kontrolle über die Ausgabe erlauben.

Als Beispiel verwenden wir die ``View``-Klasse aus `Views`_, die wir jedoch diesmal von ``plone.directives.dexterity.DisplayForm`` ableiten::

 class View(dexterity.DisplayForm):
     grok.context(ISession)
     grok.require('zope2.View')

.. _`Views`: views

Hierdurch erhalten wir einige zusätzliche Eigenschaften, die wir in unserem Template verwenden können:

``view.w``
 ist ein Dictionary aller Display-Widgets.

 Als Schlüssel für diese Widgets wird der Feldname verwendet oder, sofern das Feld aus einem *Behavior* kommt, wird dem Feldnamen das Interface dieses *Behavior* vorangestellt

``view.widgets``
 enthalten eine Liste von Widgets in der Reihenfolge des Standard-Fieldset
``view.groups``
 enthält eine Liste von Fieldsets
``view.fieldsets``
 enthält ein Distionary, das Fieldset-Namen Fieldsets zuweist.

 Auf einen Fieldset (group) können alle dort verfügbaren Widgets aufgelistet werden.

In ``project_templates/view.pt`` kann dann z.B.::

 <div tal:content="structure context/details/output" />

ersetzt werden durch::

 <div tal:content="structure view/w/details/render" />

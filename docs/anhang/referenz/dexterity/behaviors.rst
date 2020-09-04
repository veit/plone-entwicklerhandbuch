=========
Behaviors
=========

Eine Liste der gebräuchlichsten Dexterity-Behaviors.

Dexterity kommt mit einer Reihe von Behaviors. Die folgende Tabelle liefert die Interfaces, die in den Factory Type Information (FTI) angegeben werden um die jeweiligen Behaviors zu verwenden.


+----------------------------------------------------------------+----------------------------------------------------------------+
| Interface                                                      | Beschreibung                                                   |
+================================================================+================================================================+
| ``plone.app.dexterity.behaviors.metadata.IBasic``              | Fügt die Standardfelder Titel und Beschreibung hinzu.          |
+----------------------------------------------------------------+----------------------------------------------------------------+
| ``plone.app.dexterity.behaviors.metadata.ICategorization``     | Fügt das Fieldset Kategorisierung mit dessen Feldern hinzu     |
+----------------------------------------------------------------+----------------------------------------------------------------+
| ``plone.app.dexterity.behaviors.metadata.IPublication``        | Fügt das Datum-Fieldset und dessen Felder hinzu.               |
+----------------------------------------------------------------+----------------------------------------------------------------+
| ``plone.app.dexterity.behaviors.metadata.IOwnership``          | Fügt das Urheber-Fieldset und dessen Felder hinzu.             |
+----------------------------------------------------------------+----------------------------------------------------------------+
| ``plone.app.dexterity.behaviors.metadata.IDublinCore``         | Fügt alle DublinCore-Felder der oben genannten Behaviors hinzu.|
+----------------------------------------------------------------+----------------------------------------------------------------+
| ``plone.app.content.interfacess.INameFromTitle``               | Berechnet den Namen aus dem Titel-Attribut.                    |
+----------------------------------------------------------------+----------------------------------------------------------------+
| ``plone.app.dexterity.behaviors.metadata.IRelatedItems``       | Fügt ein Related Items-Feld zum Kategorisierung-Fieldset hinzu.|
+----------------------------------------------------------------+----------------------------------------------------------------+

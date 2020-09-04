=============================================
Eigenschaften und Methoden der Inhaltsobjekte
=============================================

Alle Felder von Dexterity Inhaltstypen sind als Eigenschaft eines Objekts verfügbar.

Im folgenden eine Liste der gebräuchlichsten Eigenschaften und Methoden von Dexterity Artikeltypen:

+--------------------------------+--------------------------------+----------------------------------------------------------------+
| Eigenschaft/Methode            | Typ                            | Beschreibung                                                   |
+================================+================================+================================================================+
| ``__name__``                   | ``unicode``                    | Der Name (ID) des Objekts in seinem Container. Dies kann eine  |
|                                |                                | Unicode-Zeichenkette sein wobei aktuell Zope2 jedoch nur       |
|                                |                                | ASCII-Zeichen in URLs erlaubt.                                 |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``id``                         | ``str``                        | Der Name (ID) des Objekts in seinem Container. Dies ist das    |
|                                |                                | ASCII-ENcoding von ``__name__``.                               |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``getId()``                    | ``str``                        | Gibt den Wert der ID-Eigenschaft aus.                          |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``isPrincipaFolderish``        | ``bool/int``                   | ``True`` oder ``1`` wenn das Objekt ein Ordner ist, ``False``  |
|                                |                                | oder ``0`` wenn das Objekt kein Ordner ist.                    |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``portal_type``                | ``str``                        | Der Artikeltyp dieser Instanz.                                 |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``meta_type``                  | ``str``                        | Zope2-spezifische Art, eine Klasse zu beschreiben              |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``title_or_id()``              | ``str``                        | Gibt den Wert des Titels aus oder sofern dieser nicht gesetzt  |
|                                |                                | ist, die ID-Eigenschaft.                                       |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``absolute_url()``             | ``str``                        | Die vollständige URL des Inhaltsobjekts. Berücksichtigt        |
|                                |                                | Virtual Hosting und die aktuelle Domain.                       |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``getPhysicalPath()``          | ``tuple``                      | Eine Sequenz von Pfadelementen ab dem Wurzelverzeichnis der    |
|                                |                                | Anwendung. Die Angabe sollte nicht verwendet werden um         |
|                                |                                | relative URLs zu konstruieren, da Virtual Hosting nicht        |
|                                |                                | berücksichtigt wird.                                           |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``getIcon()``                  | ``str``                        | Gibt eine Zeichenkette zurück, die als ``src``-Attribut in     |
|                                |                                | einem ``<img />``-Tag verwendet werden kann.                   |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``title``                      | ``unicode/str``                | Titel-Eigenschaft des Objekts. Üblicherweise Teil des Schemas  |
|                                |                                | eines Objekts, das durch das `ÌBasic``-Behavior``              |
|                                |                                | bereitgestellt wird.                                           |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``Title()``                    | ``iunicode/str``               | DublinCore-Accessor für die Titel-Eigenschaft.                 |
|                                |                                | Es kann auch ``setTitle()``verwendet werden.                   |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``listCreators()``             | ``tuple``                      | Eine Liste von User-IDs, Der erste Ersteller ist üblicherweise |
|                                |                                | der Eigentümer des Objekts.                                    |
|                                |                                | Mit ``setCreators()`` kann die Liste verändert werden.         |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``Creator()``                  | ``str``                        | Der erste Ersteller, der aus der ``listCreators()``-Methode    |
|                                |                                | ausgegeben wird. Üblicherweise wird hier der Eigentümer des    |
|                                |                                | Objekts ausgegeben.                                            |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``Subject()``                  | ``tuple``                      | DublinCore-Accessor für Schlagwörter. Die Liste kann           |
|                                |                                | bearbeitet werden mit der ``setSubject()``-Methode.            |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``Description()``              | ``unicode/str``                | DublinCore-Accessor für die Beschreibung, die üblicherweise    |
|                                |                                | mit dem ``ÌBase``-Behavior mitkommt. Die Beschreibung kann     |
|                                |                                | geändert werden mit der ``setDescription()``-Methode.          |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``listContributors()``         | ``tuple``                      | DublinCore-Accessor für die Liste der an dem Objekt            |
|                                |                                | Beteiligten. Die Beschreibung kann  geändert werden mit der    |
|                                |                                | ``setContributors()``-Methode.                                 |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``Date()``                     | ``str``                        | DublinCore-Accessor für das Datum des Artikels im ISO-Format.  |
|                                |                                | Sofern vorhanden wird ``EffectiveDate`` verwendet,             |
|                                |                                | andernfalls ``ModificationDate``.                              |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``CreationDate()``             | ``str``                        | DublinCore-Accessor für das Erstellungsdatum des Artikels im   |
|                                |                                | ISO-Format.                                                    |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``EffectiveDate()``            | ``str``                        | DublinCore-Accessor für das Veröffentlichungsdatum des         |
|                                |                                | Artikels im ISO-Format. Das Veröffentlichungsdatum kann        |
|                                |                                | geändert werden mit der ``setEffectiveDate()``-Methode.        |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``ExpirationDate()``           | ``str``                        | DublinCore-Accessor für das Ablaufdatum des Artikels im        |
|                                |                                | ISO-Format. Das Ablaufdatum kann geändert werden mit der       |
|                                |                                | ``setExpirationDate()``-Methode.                               |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``ModificationDate()``         | ``str``                        | DublinCore-Accessor für das Änderungsdatumdes Artikels im    . |
|                                |                                | ISO-Format.                                                    |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``Language()``                 | ``str``                        | DublinCore-Accessor für die Sprache des Artikels. Diese kann   |
|                                |                                | geändert werden mit der ``setLanguage()``-Methode.             |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``Rights()``                   | ``str``                        | DublinCore-Accessor für die Copyright-Angabe. Diese kann       |
|                                |                                | geändert werden mit der ``setRights()``-Methode.               |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``created()``                  | ``DateTime``                   | Gibt die Zope2-DateTime-Angabe für das Erstellungsdatum zurück.|
|                                |                                | Falls diese nicht gesetzt ist, wird ``January 1st, 1970``      |
|                                |                                | ausgegeben.                                                    |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``modified()``                 | ``DateTime``                   | Gibt die Zope2-DateTime-Angabe für das Änderungsdatum zurück.  |
|                                |                                | Falls diese nicht gesetzt ist, wird ``January 1st, 1970``      |
|                                |                                | ausgegeben.                                                    |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``effective()``                | ``DateTime``                   | Gibt die Zope2-DateTime-Angabe für das Veröffentlichungsdatum  |
|                                |                                | zurück. Falls diese nicht gesetzt ist, wird ``January 1st,     |
|                                |                                | 1970`` ausgegeben.                                             |
+--------------------------------+--------------------------------+----------------------------------------------------------------+
| ``expires()``                  | ``DateTime``                   | Gibt die Zope2-DateTime-Angabe für das Ablaufdatum zurück.     |
|                                |                                | Falls diese nicht gesetzt ist, wird ``January 1st, 1970``      |
|                                |                                | ausgegeben.                                                    |
+--------------------------------+--------------------------------+----------------------------------------------------------------+

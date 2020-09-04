=============
Content rules
=============

Content rules lassen sich in neueren Plone-Versionen mit einem Generic Setup-Profil erstellen. Wie ein solches Profil aussehen kann, sehen Sie in der Datei :download:`contentrules.xml`.

In diesem Profil ist eine Regel definiert::

 <rule
     name="rule-1"
     title="Mail notification"
     description=""
     enabled="True"
     event="Products.CMFCore.interfaces.IActionSucceededEvent"
     stop-after="False">

``name``
 Name (ID) der Regel
``title``
 Titel der Regel
``description``
 Beschreibung der Regel
``enabled``
 Ist die Regel aktiv?
``event``
 Welches Ereignis löst die Regel aus.
``stop-after``
 Sollen weitere Regeln nach dieser Regel ausgeführt werden?

Anschließend folgen drei weitere Abschnitte:

#. Eine Liste von Bedingungen (``conditions``) für diese Regel
#. Eine Liste von Aktionen (``actions``) für diese Regel
#. Die Zuweisung von Regeln einem bestimmten Kontext

Bedingungen (``conditions``)
----------------------------

``plone.app.contentrules`` kommt mit den folgenden Bedingungen:

Artikeltyp (``plone.conditions.PortalType``)
 Mit dieser Bedingung legen Sie fest, dass eine Aktion nur bei bestimmten Artikeltypen ausgeführt wird.
Dateiendung (``plone.conditions.FileExtension``)
 Mit dieser Bedingung können Sie festlegen, dass eine Aktion nur bei bestimmten Dateiendungen ausgeführt wird.
Stadien (``plone.conditions.WorkflowState``)
 Mit dieser Bedingung legen Sie fest, dass eine Aktion nur bei Artikeln angewendet wird, die sich in einem bestimmten Status befinden.
Übergänge (``plone.conditions.WorkflowTransition``)
 Mit dieser Bedingung legen Sie fest, dass eine Aktion nur bei bestimmten Workflow-Übergängen (``transitions``) angewendet wird.
Gruppe (``plone.conditions.Group``)
 Mit dieser Bedingung legen Sie fest, dass eine Aktion nur ausgeführt wird, wenn der aktuelle Benutzer Mitglieder in einer bestimmten Gruppe ist.
Rolle (``plone.conditions.Role``)
 Mit dieser Bedingung legen Sie fest, dass eine Aktion nur ausgeführt wird, wenn der Benutzer eine bestimmte Rolle hat.

Aktionen (``actions``)
----------------------
Name des Protokolls (``plone.actions.Logger``)
 protokolliert ein bestimmtes Ereignis
Nachricht (``plone.actions.Notify``)
 gibt eine Nachricht im Browser des Nutzers aus.
Kopieren (``plone.actions.Copy``)
 kopiert den Artikel in einen bestimmten Ordner.
Verschieben (``plone.actions.Move``)
 verschiebt den Artikel in einen bestimmten Ordner.
Löschen (``plone.actions.Delete``)
 löscht den Artikel.
Statusänderung (``plone.actions.Workflow``)
 ändert den Status des Artikels.
Mail versenden (``plone.actions.Mail``)
 Versenden einer E-Mail unter Angabe von Betreff, Absender, Empfänger und Nachrichtentext.

 Dabei können Sie für diese Felder folgende Variablen verwenden:

 ``${absolute_url}``
  URL des Artikels
 ``${user_email}``
  E-Mail-Adresse des Nutzers
 ``${user_fullname}``
  Name des Nutzers
 ``${user_id}``
  Id des Nutzers
 ``${contributors}``
  Beteiligte
 ``${created}``
  Erstellungsdatum
 ``${creators}``
  Ersteller
 ``${description}``
  Beschreibung
 ``${effective}``
  Veröffentlichungsdatum
 ``${expires}``
  Ablaufdatum
 ``${format}``
  Format
 ``${identifier}``
  Identifier (URI)
 ``${keywords}``
  Betreff
 ``${language}``
  Sprache
 ``${modified}``
  Änderungsdatum
 ``${rights}``
  Veröffentlichungsrechte
 ``${subject}``
  Betreff
 ``${title}``
  Titel
 ``${type}``
  Artikeltyp
 ``${manager_emails}``
  E-Mails an Verwalter
 ``${member_emails}``
  E-Mail an Mitglieder
 ``${owner_emails}``
  E-Mail an Eigentümer
 ``${reviewer_emails}``
  E-Mail an Redakteure
 ``${change_authorid}``
  Geänderter Name des Autors
 ``${change_comment}``
  Kommentar
 ``${change_title}``
  Geänderter Titel
 ``${change_type}``
  Geänderter Artikeltyp
 ``${review_state}``
  Geänderter Status

Zuweisung (``assignment``)
--------------------------

::

 <assignment
     location="/news"
     name="rule-1"
     enabled="True"
     bubbles="False"
     insert-before="*"
 />

``location`` (erforderlich)
 Der Ort,an dem die Regel greifen soll. Üblicherweise sind dies in Plone Ordner, die mit dem ``IRuleAssignable``-Interface markiert werden.

 Hier wird eine Pfadangabe relativ zu *portal root* erwartet.

``name`` (erforderlich)
 Der Name der Regel, die zugewiesen werden soll.
``enabled`` (optional)
 Soll die Regel an dem angegebenen Ort aktiv sein?
``bubbles`` (optional)
 Soll die Regel auch in Unterordnern zugewiesen werden?

 Der Standardwert ist ``False`` wodurch die Regel nicht auf passende Events in Unterordnern angewendet wird.

``insert-before`` (optional)
 Dies kann verwendet werden um die Reihenfolge, in der die Zuweisungen für einen bestimmten Ort ausgeführt werden sollen, zu beeinflussen.

 Wird hier nichts angegeben, wird die Regel nach allen anderen Regeln an diesem Ort ausgeführt.

 ``*`` bewirkt, dass die Regel als erste ausgeführt wird.

.. seealso::

    - `Content rules`_
    - `Creating Content Rule Conditions and Actions`_
    - `Time based workflow transitions`_

.. _`Content rules`: http://plone.org/documentation/kb/content-rules
.. _`Creating Content Rule Conditions and Actions`: http://plone.org/documentation/kb/creating-content-rule-conditions-and-actions
.. _`Time based workflow transitions`: http://plone.org/documentation/kb/time-based-workflow-transitions

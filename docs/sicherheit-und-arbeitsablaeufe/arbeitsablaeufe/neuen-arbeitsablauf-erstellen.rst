=============================
Neuen Arbeitsablauf erstellen
=============================

Wir wollen nun für unsere beiden Artikeltypen spezifische Arbeitsabläufe erstellen. Hierzu fügen wir in ``src/vs.registration/vs/registration/profiles/default/`` die Datei ``workflows.xml`` mit folgendem Inhalt hinzu::

 <?xml version="1.0"?>
 <object name="portal_workflow"
         meta_type="Plone Workflow Tool">
     <object name="registrant_workflow" meta_type="Workflow"/>
     <object name="registration_workflow" meta_type="Workflow"/>
     <bindings>
         <type type_id="Registrant">
             <bound-workflow workflow_id="registrant_workflow"/>
         </type>
         <type type_id="Registration">
             <bound-workflow workflow_id="registration_workflow"/>
         </type>
     </bindings>
 </object>

Anschließend werden die verschiedenen Stadien und Übergänge der neuen Arbeitsabläufe definiert. Dazu werden die Ordner ``src/vs.registration/vs/registration/profiles/default/workflows/registrant_workflow/`` und ``src/vs.registration/vs/registration/profiles/default/workflows/registration_workflow/`` erstellt. Der Name der Ordner muss dabei exakt der in ``workflows.xml`` angegebenen ID entsprechen. In jedem dieser Ordner wird dann die Datei ``definition.xml`` angelegt. Für den Artikeltyp ``registrant`` sieht sie z.B. so aus::

 <?xml version="1.0"?>
 <dc-workflow workflow_id="registrant_workflow"
              title="registrant_workflow"
              state_variable="review_state"
              initial_state="unconfirmed">

Zunächst werden allgemeine Angaben zum Arbeitsablauf wie ID, Titel, Variablenname und initialer Status gemacht. Der Variablenname ``state_variable`` sollte dabei immer ``review_state`` sein.

Anschließend werden die Rechte (*Permissions*) angegeben, die durch den Arbeitsablauf geändert werden sollen::

     <permission>Delete objects</permission>
     <permission>Modify portal content</permission>
     <permission>View</permission>

Nun werden die verschiedenen Stadien definiert. Dabei wird für jedes Stadium in ``exit-transition`` angegeben, welche Übergänge möglich sind und eine Zuweisung der Rollen und Rechte vorgenommen::

     <state state_id="confirmed"
            title="Confirmed">
         <exit-transition transition_id="reject-open"/>
         <permission-map name="Delete objects"
                         acquired="False">
             <permission-role>Manager</permission-role>
         </permission-map>
         <permission-map name="Modify portal content"
                         acquired="False">
             <permission-role>Owner</permission-role>
             <permission-role>Manager</permission-role>
         </permission-map>
         <permission-map name="View"
                         acquired="False">
             <permission-role>Manager</permission-role>
         </permission-map>
     </state>
     ...

Den Übergängen werden ID, Titel und Auslöser (``trigger``) zugewiesen. ``trigger`` kann dabei die Werte ``USER`` oder ``AUTOMATIC`` annehmen. Der ``<action />``-Tag enthält den Namen, der in Plone’s *Status*-Menü angezeigt wird und die URL, auf die diese Aktion verlinkt. Üblicherweise wird hier das ``content_status_modify``-Skript verwendet. Schließlich wird der Übergang noch geschützt durch die Angabe im ``<guard />``-Tag::

     <transition transition_id="confirm"
                 title="Confirm"
                 new_state="confirmed"
                 trigger="USER"
                 before_script=""
                 after_script="">
         <action url="%(content_url)s/content_status_modify?workflow_action=confirm"
                 category="workflow">
             Confirm
         </action>
         <guard>
         </guard>
     </transition>
     ...
 </dc-workflow>

Der Arbeitsablauf kann mittels ``i18n:``-Attributen internationalisiert werden.
Dabei besteht prinzipiell Zugriff auf alle verwendeten Zeichenketten. Siehe auch
:doc:`../../internationalisierung/uberschreiben-von-plone-ubersetzungen`.

.. _`Changing workflow state – quickly – on CMF/Plone content`: http://glenfant.wordpress.com/2010/04/02/changing-workflow-state-quickly-on-cmfplone-content/

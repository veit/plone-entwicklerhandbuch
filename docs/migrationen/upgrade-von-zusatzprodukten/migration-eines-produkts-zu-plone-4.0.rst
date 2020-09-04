=====================================
Migration eines Produkts zu Plone 4.0
=====================================

Für die Migration von Plone3 auf Plone4 sollten die folgenden Änderungen beachtet werden.

Globale Definitionen
====================

Viele globale Definitionen aus ``global_defines.pt`` werden nicht mehr vollständig im ``main_template.pt`` eingebunden, da dies die Performance deutlich beeinträchtigt. Einige globale Variablen wie z.B. ``context``, ``view`` und ``template`` bleiben jedoch erhalten. Nicht erhalten geblieben sind jedoch die Definitionen aus der ``_initializeData``-Klasse im ``@@plone``-View von Plone3: `Products/CMFPlone/browser/ploneview.py`_

Es empfiehlt sich daher, alle Seiten Ihres Produkts sich in einer Plone4-Site anzuschauen und dann ggf. die globalen Definitionen selbst einzubinden, also z.B.::

 tal:attributes="action string:$here_url/${template/getId}"

ersetzen durch::

 tal:attributes="action string:${context/@@plone_context_state/object_url}/${template/getId}"

**Achtung:** Sie erhalten keine Fehlermeldung, wenn Sie globale Definitionen in der Überprüfung von ``exists`` verwenden z.B.::
 tal:condition="python:exists('portal/mystyle.css')"

Diese Bedingung führt zu keinem Fehler, sondern die Überprüfung schlägt auch fehl, wenn ``portal`` nicht definiert ist. Daher sollten Sie alle Templates nach ``exists`` durchsuchen und überprüfen, ob die verwendeten globalen Definitionen auch tatsächlich vorhanden sind.

Wegfall des *Action Icons Tool*
===============================

Produkte, die Icons für CMF-Aktionen am *Action Icons Tool* regsitrierten, sollten zukünftig die ``icon_expr``-Anweisung verwenden um Icons am 'Actions Tool* oder im *Control Panel Tool* zu registrieren. So wird beispielsweise in Plone4 das Icon für *Document* in ``Products/CMFPlone/profiles/default/types/Document.xml`` so angegeben::

 <property name="icon_expr">string:${portal_url}/document_icon.png</property>

.. _`Products/CMFPlone/browser/ploneview.py`: http://dev.plone.org/plone/browser/CMFPlone/branches/3.0/browser/ploneview.py#L77

Wegfall der Zope2-Interfaces
============================

Zope2 vor Version 2.12.0 unterstützte zwei verschiedene Arten von Interfaces, die Zope2- und die Zope3-Implementierung:

Zope2::

 from Interface import Interface
 class MyInterface(Interface):
     pass

 class MyClass(object):
     __implements__ = (MyInterface,)

Zope3::

 from zope.interface import Interface
 class MyInterface(Interface):
     pass

 class MyClass(object):
     implements(MyInterface)

In Zope2.12 werden Zope3-Interfaces unterstützt.

Bei einer Zope2-Implementierung von Intervace wird dann folgender Fehler ausgegeben::

 ImportError: No module named Interface

Imports
=======

Diverse *import*-Methoden sind verschoben worden. Früher bereits als *deprecated*  gekennzeichnete Methoden wurden entfernt.

Folgende Methoden wurden verschoben:

+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| alt                                                                                  | neu                                                                              |
+======================================================================================+==================================================================================+
| Products.​ATContentTypes.​content.​folder.​ATFolder                                  | plone.app.folder.folder.ATFolder                                                 |
+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Products.​ATContentTypes.​content.folder.​ATFolderSchema                             | plone.app.folder.folder.ATFolderSchema                                           |
+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Products.​CMFPlone.​browser.​navtree.​SitemapNavtreeStrategy.​icon                   | Products.​CMFPlone.​browser.​navtree.​SitemapNavtreeStrategy.​item_icon          |
+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Products.CMFPlone.browser.plone                                                      | Products.CMFPlone.browser.ploneview                                              |
+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Products.​CMFPlone.​browser.​ploneview.​cache_decorator                              | plone.memoize.instance.memoize                                                   |
+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Products.​CMFPlone.​browser.​ploneview.​IndexIterator                                | Products.CMFPlone.utils.IndexIterator                                            |
+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Products.​CMFPlone.​browser.​ploneview.​Plone.​isRightToLeft                         | @@plone_portal_state/is_rtl                                                      |
+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Products.​CMFPlone.​browser.​ploneview.​Plone.​keyFilteredActions                    | @@plone_context_state/keyed_actions                                              |
+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Products.CMFPlone.browser.portlets                                                   | plone.app.portlets.portlets                                                      |
+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Products.​CMFPlone.​interfaces.​OrderedContainer.​IOrderedContainer                  | OFS.interfaces.IOrderedContainer                                                 |
+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Products.CMFPlone.utils.BrowserView                                                  | Products.Five.BrowserView                                                        |
+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Products.CMFPlone.utils.getGlobalTranslationService                                  | Products.​PageTemplates.​GlobalTranslationService.​getGlobalTranslationService   |
+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Products.CMFPlone.utils.scale_image                                                  | Products.PlonePAS.utils.scale_image                                              |
+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Products.CMFPlone.utils.utranslate                                                   | zope.i18n.translate                                                              |
+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Products.​PageTemplates.​GlobalTranslationService.​getGlobalTranslationService       | zope.i18n                                                                        |
+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Products.CMFPlone.utils.ulocalized_time                                              | Products.CMFPlone.i18nl10n.ulocalized_time                                       |
+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| zope.app.cache.interfaces.ram.IRAMCache                                              | zope.ramcache.interfaces.ram.IRAMCache                                           |
+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Products.​ATReferenceBrowserWidget.​ATReferenceBrowserWidget.​ReferenceBrowserWidget | archetypes.​referencebrowserwidget.​ReferenceBrowserWidget                       |
+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+

Nicht mehr vorhandene Methoden
==============================

- ``Products.CMFPlone.CatalogTool.registerIndexableAttribute``

  Stattdessen sollte ``plone.indexer`` verwendet werden.

- ``Products.CMFPlone.PloneTool.setDefaultSkin``

- ``Products.CMFPlone.PloneTool.setCurrentSkin``

- ``Products.CMFPlone.PortalContent``

- *Favorite*-Artikeltyp

- ``use_folder_tabs`` aus den ``site_properties``

- ``keyed_actions``

  Sollte durch die ``actions``-Methode aus ``@@plone_context_state`` ersetzt werden, die nun als einzigen Parameter eine *action category* benötigt.

Validatoren
===========

Auch Validatoren benötigen nun Zope3-Interfaces da ansonsten beim Starten der Instanz folgender Fehler ausgegeben wird::

 Products.validation.exceptions.FalseValidatorError:
 <vs.registration.validators.ProjectIdValidator instance at 0xa92082c>

Die Zeile::

 __implements__= (IValidator,)

sollte ersetzt werden durch::

 from zope.interface import implements
 ...
 try:
    # Plone 4 and higher
     import plone.app.upgrade
     USE_BBB_VALIDATORS = False
 except ImportError:
     # BBB Plone 3
     USE_BBB_VALIDATORS = True
 ...
 if USE_BBB_VALIDATORS:
     __implements__ = (ivalidator,)
 else:
    implements(IValidator)

Aufruf der ``translate``-Methode
================================

Folgende Module stehen nicht mehr zur Verfügung::

 Products.CMFPlone.utils.utranslate
 Products.PageTemplates.GlobalTranslationService.getGlobalTranslationService

Stattdessen sollte ``zope.i18n.translate`` verwendet werden.

Und mit ``zope.i18n.translate`` ändert sich dann auch der Aufruf gegenüber ``utranslate``:

- ``msgid`` ist nun das erste und nicht mehr erst das zweite Argument dieses Aufrufs.
- ``domain`` ist nun optional.

*Add view* für Artikeltypen
===========================

In Plone 4 kann jeder Artikeltyp im Portal Types Tool eine zusätzliche Eigenschaft für die Ansicht beim Hinzufügen haben. Diese Eigenschaft wird als ``TALES``-Ausdruck für eine URL angegeben werden. Ein Link mit dieser URL wird Nutzern dann im *Hinzufügen*-Menü von Plone angezeigt.

Diese Eigenschaft hat den Titel *Add view URL (expression)* und die interne ID ``add_view_expr``

This property has the title Add view URL (expression) and the internal id ``add_view_expr``.

Auf diese Weise lässt sich z.B. für ein selbst-entwickeltes Hinzufügen-Formular folgender Ausdruck angeben::

 string:${folder_url}/@@add-my-content

Beachten Sie hierbei, dass der View für den ``folder``-Artikeltyp registriert wird und nicht für den zu erstellenden Artikeltyp.

``send`` statt ``secureSend``
=============================

Mit der ``send``-Methode ändern sich auch weitere Angaben:

Message Type
------------

Nun wird der vollständige MIME type als ``msg_type`` angegeben und nicht mehr nur der subtype-Parameter, also z.B.::

 msg_type='text/plain'

statt::

 subtype='plain'

Eigene Headers-Angaben
----------------------

Um eigene Headers-Angaben für eine Nachricht anzugeben, kann z.B. folgendes angegeben werden::

 from email import message_from_string
 from email.Header import Header
 my_message = message_from_string(message_body.encode('utf-8'))
 my_message.set_charset('utf-8')
 my_message['CC']= Header('someone@example.com')
 my_message['BCC']= Header('secret@example.com')
 my_message['X-Custom'] = Header(u'Some Custom Parameter', 'utf-8')
 mailhost.send(my_message, mto, mfrom, subject)

Geänderte Syntax des Portlets-Profil
====================================

In Plone 3 wird ein Portlet an einen bestimmten Portlet-Manager gebunden mit der Anweisung::

 for="plone.app.portlets.interfaces.IColumn"

In Plone 4 erfolgt dies nun mit::

 <for interface="plone.app.portlets.interfaces.IColumn" />

Somit lassen sich auch mehrere Werte im ``for``-Feld angeben::

 <for interface="plone.app.portlets.interfaces.IColumn" />
 <for interface="plone.app.portlets.interfaces.IDashboard" />

Zum Weiterlesen
===============

- `Upgrading Plone 3.x to 4.0`_
- `Migrating a Product to Plone 4.0`_
- `BACKWARDS_COMPATIBILITY.txt`_

.. _Upgrading Plone 3.x to 4.0: http://plone.org/documentation/manual/upgrade-guide/version/upgrading-plone-3-x-to-4.0/referencemanual-all-pages
.. _`Migrating a Product to Plone 4.0`: http://maurits.vanrees.org/weblog/archive/2009/10/migrating-a-product-to-plone-4.0
.. _`BACKWARDS_COMPATIBILITY.txt`: http://dev.plone.org/plone/browser/Plone/trunk/docs/BACKWARDS_COMPATIBILITY.txt

=====================================================
Standardwerte, Vokabularien und Autovervollständigung
=====================================================

Standardwerte
=============

Oft vereinfacht es die Bedienung deutlich, wenn in Feldern Standardwerte eingetragen werden. Diese Werte werden im Hinzufügen-Formular gesetzt.

In unserem Beispiel sollen die Standardwerte für den Beginn und das Ende einer Veranstaltung eine Woche in der Zukunft liegen. Hierzu fügen wir in ``registration.py`` folgendes hinzu::

 import datetime
 ...
 @form.default_value(field=IRegistration['start'])
 def startDefaultValue(data):
     # To get hold of the folder, do: context = data.context
     return datetime.datetime.today() + datetime.timedelta(7)

 @form.default_value(field=IRegistration['end'])
 def endDefaultValue(data):
     # To get hold of the folder, do: context = data.context
     return datetime.datetime.today() + datetime.timedelta(10)

Der *Decorator* kann ein oder mehrere Unterscheidungskriterien haben. Folgende Unterscheidungskriterien sind möglich:

``context``
 Der Kontexttyp, z.B. ein Interface
``request``
 Der Request-Tp, z.B. ein Layer Marker Interface
``view``
 Der Formulartyp, z.B. eine Formularinstanz oder ein Interface.
``field``
 Die Feld-Instanz oder das Interface eines Feldes

Neben dem ``default_value``-Decorator gibt es noch zwei weitere Decorators:

``widget``
 Der Widget-Typ, z.B. ein Interface
``widget_label``
 bietet ein dynamische Label für Widgets wobei es dieselben Unterscheidungskriterien zulässt wie ``default_value``.
``button_label``
 bietet dynamische Label für Tasten mit den Unterscheidungskriterien ``content, ``request``, ``form``, ``manager`` und ``button``.

In der Dokumentation zu `plone.directives.form`_ finden Sie weitere Informationen hierzu.

.. _`plone.directives.form`: http://pypi.python.org/pypi/plone.directives.form

Vokabularien
============

Vokabularien werden üblicherweise zusammen mit Auswahlfeldern verwendet. Um nur eine Auswahl zuzulassen, kann das ``Choise``-Feld direkt verwendet werden::

 class IMySchema(form.Schema):
     myChoice = schema.Choice(...)

Für Multiple-Choice-Felder können ``List``, ``Tuple``, ``Set`` oder ``Frozenset`` mit ``value_type=schema.Choice`` verwendet werden, also z.B.::

 class IMySchema(form.Schema):
     myList = schema.List(
         title=u"My list",
         value_type=schema.Choice(values=['red', 'green', 'blue', 'yellow']))

Ein ``Choice``-Feld kann eines der folgenden Argumente erhalten:

- Werte aus einer Liste statischer Werte
- Werte aus einer Quelle, die mit ``IContextSourceBinder`` oder einer ``ISource``-Intanz angegeben werden
- Werte können aus einem Vokabular stammen, das als ``ÌVocabulary``-Instanz oder als Name eines ``IVocabularyFactory``-Utility angegeben wird

``term``
 Eintrag in ein Vokabular
``token``
 ASCII-Zeichenkette, die beim Abschicken eines Formulars übermittelt wird um den Term eindeutig zu identifizieren.
``value``
 Der aktuelle Wert, der in einem Objekt gespeichert wird
``title``
 Übersetzbare Unicode-Zeichenkette

Verfügbare Vokabularien
-----------------------

In Plone werden Ihnen bereits eine ganze Reihe von Vokabularien in ``plone.app.vocabularies`` zur Verfügung gestellt. Die gebräuchlichsten sind:

``plone.app.vocabularies.AvailableContentLanguages``
 Eine Liste aller verfügbaren Sprachen
``plone.app.vocabularies.SupportedContentLanguages``
 Eine Liste aller aktuell unterstützten Sprachen
``plone.app.vocabularies.Roles``
 Die in der Site verfügbaren Rollen
``plone.app.vocabularies.PortalTypes``
 Eine Liste der im Portal Types Tool registrierten Artikeltypen
``plone.app.vocabularies.ReallyUserFriendlyTypes``
 Eine Liste derjenigen Artikeltypen, die für Nutzer von Bedeutung sind
``plone.app.vocabularies.Workflows``
 Eine Liste aller Arbeitsabläufe
``plone.app.vocabularies.WorkflowStates``
 Eine Liste aller Arbeitsablaufstadien
``plone.app.vocabularies.WorkflowTransitions``
 Eine Liste aller Übergänge zwischen Arbeitsablaufstadien

Mit ``plone.principalsource`` steht uns ein weiteres Paket mit verschiedenen Vokabularien bereit, das zur Auswahl von Nutzern und Gruppen hilfreich ist:

``plone.principalsource.Users``
 Eine Liste aller Nutzer
``plone.principalsource.Groups``
 Eine Liste aller Gruppen
``plone.principalsource.Principals``
 Eine Liste aller Berechtigungen für Nutzer und Gruppen

Statische Vokabularien
----------------------

Hier ein Beispiel für ein statisches Vokabular::

 from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

 organisers = SimpleVocabulary(
     [SimpleTerm(value=u'vsc', title=_(u'Veit Schiele Communications')),
      SimpleTerm(value=u'zopyx', title=_(u'Zopyx Limited'))]
     )

 organiser = schema.Choice(
             title=_(u"Organiser"),
             vocabulary=organisers,
             required=False,
         )

Dynamische Vokabularien
-----------------------

Statische Vokabularien sind in zweierlei Hinsicht beschränkt: zum einen sind sie hartkodiert in Python, zum anderen werden die gespeicherten Werte nicht getrennt von den Labels gespeichert.

Ein dynamische Vokabular kann nun erzeugt werden indem ein sog. *Context Source Binder* verwendet wird. Ein solcher kann einfach aufgerufen werden durch eine Funktion oder ein Objekt mit einer ``__call__``-Methode, die das ``IContextSourceBinder``-Interface zusammen mit einem Kontext-Argument bereitstellt. Der Aufruf soll ein Vokabular ausgeben, das am einfachsten zu bekommen ist, wenn die ``SimpleVocabulary``-Klasse aus ``zope.schema`` verwendet wird.

Im folgenden nun ein Beispiel für eine Funktion, die alle Nutzer einer bestimmten Gruppe zurückgibt::

 from zope.schema.interfaces import IContextSourceBinder
 from zope.schema.vocabulary import SimpleVocabulary
 from Products.CMFCore.utils import getToolByName

 @grok.provider(IContextSourceBinder)
 def possibleOrganisers(context):
     acl_users = getToolByName(context, 'acl_users')
     group = acl_users.getGroupById('organisers')
     terms = []

     if group is not None:
         for member_id in group.getMemberIds():
             user = acl_users.getUserById(member_id)
             if user is not None:
                 member_name = user.getProperty('fullname') or member_id
                 terms.append(SimpleVocabulary.createTerm(member_id, str(member_id), member_name))

    return SimpleVocabulary(terms)

Parametriesierte Vokabularien
=============================

Das obige Beispiel kann erweitert werden indem der Gruppenname aus der Funktion herausgenommen wird und sich dann für jedes Feld unabhängig setzen lässt.  Hierfür wird dann ``IContextSourceBinder`` in eine eigene Klasse ausgelagert, die mit dem Gruppennamen initialisiert wird::

 class GroupMembers(object):
     """Context source binder to provide a vocabulary of users in a given
     group.
     """

     grok.implements(IContextSourceBinder)

     def __init__(self, group_name):
         self.group_name = group_name

     def __call__(self, context):
         acl_users = getToolByName(context, 'acl_users')
         group = acl_users.getGroupById(self.group_name)
         terms = []

         if group is not None:
             for member_id in group.getMemberIds():
                 user = acl_users.getUserById(member_id)
                 if user is not None:
                     member_name = user.getProperty('fullname') or member_id
                     terms.append(SimpleVocabulary.createTerm(member_id, str(member_id), member_name))

         return SimpleVocabulary(terms)

Benannte Vokabularien
---------------------

Sollen Vokabularien nicht nur im Kontext verfügbar sein sondern als Komponenten, werden sog. *Named Vocabularies* erstellt. Diese werden als *named utilities* registriert werden und sind anschließend in einem Schema mit ihrem Namen referenziert werden. Damit lassen sich Vokabularien in eigenständigen Paketen erstellen.

VDEX-Vokabularien
-----------------

`collective.vdexvocabulary`_ erlaubt die Verwendung von `IMS VDEX`_-Vokabularien und bietet darüberhinaus noch weitere Vorteile wie:

- ``i18n``-Unterstützung, wie sie im IMS VDEX-Standard definiert ist.
- Unterstützung für Sortierung auch von Unicode-Zeichen. sofern `zope.ucol`_ installiert ist
- Einfache Registrierung mit ``zcml``
- Relationen wie sie im IMS VDEX-Standard spezifiziert sind

.. _`collective.vdexvocabulary`: http://pypi.python.org/pypi/collective.vdexvocabulary
.. _`IMS VDEX`: http://en.wikipedia.org/wiki/IMS_VDEX
.. _`zope.ucol`: http://pypi.python.org/pypi/zope.ucol

``collective.elephantvocabulary``
---------------------------------

`collective.elephantvocabulary`_ ist ein Wrapper für ``zope.schema``-Vokabularien wodurch diese keinen ihre Einträge mehr vergessen.

.. _`collective.elephantvocabulary`: http://pypi.python.org/pypi/collective.elephantvocabulary/

Autovervollständigung
=====================

``plone.formwidget.autocomplete`` erweitert ``z3c.formwidget.query`` um ein nutzerfreundlicheres Interface für Felder bereitzustellen, bei dem nach der Eingabe von wenigen Zeichen bereits die möglichen Werte angezeigt werden.

Das Widget wird bereits mit ``plone.app.dexterity`` mitgeliefert, sodass wir es einfach z.B.  in ``registration.py`` verwenden können, mit::

     form.widget(organiser=AutocompleteFieldWidget)
     organiser = schema.Choice(
             title=_(u"Organiser"),
             vocabulary=u"plone.principalsource.Users",
             required=False,
         )

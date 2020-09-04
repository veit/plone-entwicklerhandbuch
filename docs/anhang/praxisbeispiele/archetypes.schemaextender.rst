=========================
archetypes.schemaextender
=========================

archetypes.schemaextender erlaubt das Erweitern, Ändern und Löschen von Feldern eines Archetypes-Schema.

`archetypes.schemaextender
<http://pypi.python.org/pypi/archetypes.schemaextender>`_ erlaubt, Archetypes-
Schemas dynamisch mit Adaptern zu erweitern. Dies kann verwendet werden um neue
Felder hinzuzufügen, Felder oder Fieldsets neu anzuordnen etc.

So sind dann auch drei verschiedene Adapter verfügbar:

``ISchemaExtender``
 erlaubt das Hinzufügen neuer Felder zu einem Schema.
``IOrderableSchemaExtender``
 erlaubt neue Felder hinzuzufügen und Felder neu anzuordnen, ist jedoch
 deutlich kostspieliger als ``ISchemaExtender``.
``IBrowserLayerAwareExtender``
 verwendet ``plone.browserlayer`` sodass der Extender nur verfügbar ist sofern
 ein Layer registriert wurde. Damit lässt sich die Schemaerweiterung von Plone-
 Artikeltypen auf eine Site begrenzen.
``ISchemaModifier``
 erlaubt auf niedrigschwelligem Niveau die Manipulation von Schemas.

Beispiel
========

#. Zunächst wird ``archetypes.schemaextender`` als Abhängigkeit unseres Produkts
   in ``vs/registration/configure.setup.py`` registriert::

    install_requires=[
        'setuptools',
        ...
        'archetypes.schemaextender',
    ],

#. Anschließend wird in ``vs/registration/interfaces.py`` das entsprechende
   Interface definiert::

    from plone.theme.interfaces import IDefaultPloneLayer

    class IVSRegistrationExtenderLayer(IDefaultPloneLayer):
        """A Layer Specific to VSRegistrationExtender"""

#. Dieser Layer wird nun registriert in
   ``vs/registration/profiles/default/browserlayer.xml`` mit::

    <layers>
        <layer name="vs.registration"
               interface="vs.registration.interfaces.IVSRegistrationExtenderLayer" />
    </layers>

#. Dann wird ein neues Paket hinzugefügt::

    $ mkdir extender
    $ touch extender/__init__.py

#. Anschließend wird es in die Konfiguration eingeschlossen indem in ``vs/registration/configure.zcml`` folgende Zeile hinzugefügt wird::

    <include package=".extender" />

#. Nun wird der Extender selbst registriert in
   ``vs/registration/extender/configure.zcml``::

    <include package="archetypes.schemaextender" />
    <adapter factory=".teaser.TeaserExtender"
             provides="archetypes.schemaextender.interfaces.ISchemaExtender"
             for="Products.ATContentTypes.interfaces.IATEvent" />

#. Nun wird die Klasse ``TeaserExtender`` in ``vs/registration/extender/teaser.py`` erstellt::

    class TeaserExtender(object):
        """ teaser fields """

        implements(ISchemaExtender, IBrowserLayerAwareExtender)
        # bind this extender to the browser layer
        layer = VSRegistrationExtenderLayer
        fields = [TeaserField('teaserImage',
                                default=False,
                                storage = AnnotationStorage(migrate=True),
                                swallowResizeExceptions=zconf.swallowImageResizeExceptions.enable,
                                pil_quality=zconf.pil_config.quality,
                                pil_resize_algo=zconf.pil_config.resize_algo,
                                max_size=config.TEASER_MAX_DIMENSION,
                                sizes=config.TEASER_SIZES,
                                widget=atapi.ImageWidget(
                                    label=u"Teaser image",
                                    label_msgid='label_teaser_image',
                                    i18n_domain='plone',
                                    ),
                                 schemata='Teaser',
                                 ),
                ]

        def __init__(self, context):
            self.context = context

        def getFields(self):
            return self.fields

Die vollständige Datei können Sie sich hier anschauen: :download:`teaser.py`.

Feldreihenfolge ändern
======================

#. Der hierfür notwendige Adapter  wird in
   ``vs/registration/extender/configure.zcml`` konfiguriert::

    <adapter
        factory=".extender.VSRegistrationExtender"
        provides="archetypes.schemaextender.interfaces.IOrderableSchemaExtender" />

#. Nun wird die Klasse ``TeaserExtender`` in ``vs/registration/extender/teaser.py``
   erweitert::

    from archetypes.schemaextender.interfaces import IOrderableSchemaExtender, IBrowserLayerAwareExtender
    ...
    class TeaserExtender(object):
        implements(IOrderableSchemaExtender, IBrowserLayerAwareExtender)
        ...
        def fiddle(object, schema):
        def getOrder(self, order):
            do = order['default']

            # place teaser at the very top
            do.remove('teaser')
            do.insert(0, 'teaser')
            return order

Ändern eines bestehenden Schemas
================================

#. Ein bestehendes Schema lässt sich ändern, indem zunächst ein Adapter
   konfiguriert wird in ``vs/registration/extender/configure.zcml``::

    <adapter
        factory=".teaser.TeaserExtender"
        provides="archetypes.schemaextender.interfaces.ISchemaModifier" />

#. Nun wird die Klasse ``TeaserExtender`` in ``vs/registration/extender/teaser.py``
   erweitert::

    from archetypes.schemaextender.interfaces import IOrderableSchemaExtender, IBrowserLayerAwareExtender, ISchemaModifier
    ...
    def fiddle(object, schema):
        schema['image'].widget.visible = {'edit':'invisible','view':'invisible'}
        return schema

.. seealso::
    * `Plone Documentation Team: archetypes.schemaextender <http://plone.org/documentation/manual/developer-manual/using-archgenxml/3rdparty/archetypes.schemaextender>`_
    * `archetypes/schemaextender/usage.txt <http://dev.plone.org/archetypes/browser/archetypes.schemaextender/trunk/archetypes/schemaextender/usage.txt>`_

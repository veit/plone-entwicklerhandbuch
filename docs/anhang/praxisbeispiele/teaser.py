from zope.component import adapts
from zope.interface import implements
from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.field import ExtensionField
from Products.Archetypes import atapi
from Products.ATContentTypes.interfaces.event import IATEvent
from Products.ATContentTypes.configuration import zconf
from Products.Archetypes.atapi import AnnotationStorage

from .. import config


class TeaserField(ExtensionField, atapi.ImageField):
    """ image field """


class TeaserExtender(object):
    """ teaser fields """

    implements(ISchemaExtender)
    fields = [
        TeaserField(
            "teaserImage",
            default=False,
            storage=AnnotationStorage(migrate=True),
            swallowResizeExceptions=zconf.swallowImageResizeExceptions.enable,
            pil_quality=zconf.pil_config.quality,
            pil_resize_algo=zconf.pil_config.resize_algo,
            max_size=config.TEASER_MAX_DIMENSION,
            sizes=config.TEASER_SIZES,
            widget=atapi.ImageWidget(
                label=u"Teaser image",
                label_msgid="label_teaser_image",
                i18n_domain="plone",
            ),
            schemata="Teaser",
        ),
    ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields

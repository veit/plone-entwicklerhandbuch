======================
Image Field hinzufügen
======================

Als Änderungsanforderung kam die Darstellung eines Fotos für Registration.

Definieren des Interfaces
=========================

Das Interface wird in ``registration/interfaces.py`` erweitert::

 from zope.interface import Interface
 from Products.ATContentTypes.interface.image import IImageContent
 ...

 class IRegistration(Interface, IImageContent):
     ...

Schemadefinition
================

Das Schema wird in ``content/registration.py`` definiert::

 RegistrationSchema = folder.ATFolderSchema.copy() + atapi.Schema((
     ...
     atapi.ImageField('image',
                primary=True,
                languageIndependent=True,
                storage = AnnotationStorage(migrate=True),
                swallowResizeExceptions = zconf.swallowImageResizeExceptions.enable,
                pil_quality = zconf.pil_config.quality,
                pil_resize_algo = zconf.pil_config.resize_algo,
                max_size = zconf.ATImage.max_image_dimension,
                sizes= {'large'   : (768, 768),
                        'preview' : (400, 400),
                        'mini'    : (200, 200),
                        'thumb'   : (128, 128),
                        'tile'    :  (64, 64),
                        'icon'    :  (32, 32),
                        'listing' :  (16, 16),
                       },
                validators = (('checkImageMaxSize', V_REQUIRED)),
                widget = ImageWidget(
                         description = 'Image for this registration',
                         label= _(u'label_image', default=u'Image'),
                         show_content_type = False,)),

     ), marshall=PrimaryFieldMarshaller()
     )
 ...
 RegistrationSchema['image'].storage = atapi.AnnotationStorage()

Anschließend wird das neue Feld implementiert::

 class Registration(folder.ATFolder):
     """Contains multiple registrants
     """
     implements(IRegistration)
     ...

**Anmerkung:** Wenn das Feld nicht ``image`` heisst, sollten zusätzlich neue *getter*- und *setter*-Methoden zur Verfügung gestellt werden. Hierzu können Sie sich z.B. in *ATContentTypes* ``getImage`` und ``setImage`` anschauen.

Adapter für ``IImageContent`` schreiben
=======================================

Der Adapter wird implementiert in ``content/registration.py``::

 from zope.interface import implements
 ...
 from zope.publisher.interfaces import IPublishTraverse
 from ZPublisher.BaseRequest import DefaultPublishTraverse

 ...

 @adapter(IRegistration)
 class ImageTraverser(DefaultPublishTraverse):

     implements(IPublishTraverse)

     def __init__(self, context, request):
         self.context = context
         self.request = request

     def publishTraverse(self, request, name):
         if name.startswith('image'):
             field = self.context.getField('image')
             image = None
             if name == 'image':
                 image = field.getScale(self.context)
             else:
                 scalename = name[len('image_'):]
                 if scalename in field.getAvailableSizes(self.context):
                     image = field.getScale(self.context, scale=scalename)
             if image is not None and not isinstance(image, basestring):
                 # image might be None or '' for empty images
                 return image
         else:
             return super(ImageTraverser, self).publishTraverse(request, name)

Anschließend wird der Adapter konfiguriert in der Datei ``content/configure.zcml``::

 <adapter
  for="Products.ATContentTypes.interface.image.IImageContent zope.publisher.interfaces.http.IHTTPRequest"
  factory=".registration.ImageTraverser"
  provides="zope.publisher.interfaces.IPublishTraverse" />

Erstellen eines Views
=====================

#. Zunächst wird der *View* registriert in ``browser/configure.zcml``::

    <browser:page
        for="Products.ATContentTypes.interface.image.IImageContent"
        class=".imagesupport.ImageView"
        permission="zope2.View"
        name="img_view"
        allowed_interface="..interfaces.IRegistration"
    />

    <browser:page
        for="Products.ATContentTypes.interface.image.IImageContent"
        name="fullscreen"
        class=".views.FullscreenView"
        permission="zope2.View"
    />
    <browser:page
        for="..interfaces.IRegistration"
        name="view"
        class=".registration.RegistrationView"
        permission="zope2.View"
    />

#. Anschließend wird der *View* implementiert wobei zunächst die Datei ``browser/imagesupport.py`` angelegt wird mit folgendem Inhalt::

    from zope.interface import implements
    from Products.CMFCore.utils import getToolByName
    from Products.Five.browser import BrowserView
    import urllib

    class ImageView(BrowserView):

        def __init__(self, context, request):
            self.context = context
            self.request = request

        def tag(self, **kwargs):
            """ tag """
            return self.context.getField('image').tag(self.context , **kwargs)

        def getImageSize(self, scale=None):
            """ image size """
            field = self.context.getField('image')
            return field.getSize(self.context,scale=scale)

        def hasImage(self):
            """ image size
            """
            field = self.context.getField('image')
            return field.get_size(self.context)

#. Anschließend wird noch der ``FullscreenView`` in ``browser/registration.py`` angegeben::

    ...

    class FullscreenView(BrowserView):
        """
        """
        __call__ = ViewPageTemplateFile('fullscreen_view.pt')


#. Nun kopieren wir uns das PageTemplate ``parts/plone/CMFPlone/skins/plone_content/image_view_fullscreen.pt`` in ``src/vs.registration/vs/registration/browser/`` und ändern es folgendermaßen ab::

    ...
    <div class="visualWrapper"
       tal:define="img_view context/@@img_view">
        <a href=""
           tal:attributes="href request/HTTP_REFERER"
           tal:condition="request/HTTP_REFERER">
            <span i18n:translate="label_back_to_site">
                Back to site
            </span>
            <br />
            <tal:block replace="structure img_view/tag" />
        </a>
        <a href=""
           tal:attributes="href here/portal_url"
           tal:condition="not: request/HTTP_REFERER">
            <span i18n:translate="label_home">
                Home
            </span>
            <br />
            <tal:block replace="structure img_view/tag"  />
        </a>
    </div>

#. Schließlich ergänzen wir auch noch ``browser/registration.pt``::

    ...
    <div metal:fill-slot="main">
           <tal:main-macro
               metal:define-macro="main"
               tal:define="img_view context/@@img_view;
    ...
    <span tal:condition="img_view/hasImage" tal:omit-tag="">
        <a href=""
            class="discreet"
            tal:attributes="href string:$here_url/fullscreen">
            <tal:block replace="structure python: img_view.tag(scale='preview')" />
            <br />
            <span class="visualNoPrint">
                <img src="" alt="" tal:replace="structure here/search_icon.gif" />
                <span i18n:translate="label_click_to_view_full_image" i18n:domain="plone">
                    Click to view full-size image&hellip;
                </span>
            </span>
        </a>
    </span>

===================
JSON-Im- und Export
===================

JSON (JavaScript Object Notation) ist gut geeignet um die Inhalte aus Plone im-
und exportieren zu können. `collective.jsonmigrator
<https://github.com/collective/collective.jsonmigrator>`_ kann ggf. diese
Azfgabe erleichtern.

Alternativ lässt sich auch einfach ein eigener View schreiben zum Export im JSON-Format::

    import os
    import base64

    try:
        import json
    except ImportError:
        # Python 2.5/Plone 3.3 use simplejson
        import simplejson as json

    from Products.Five.browser import BrowserView
    from Products.CMFCore.interfaces import IFolderish
    from DateTime import DateTime

    # Private attributes for the export list
    EXPORT_ATTRIBUTES = ["portal_type", "id"]

    class ExportFolderAsJSON(BrowserView):
        """
        Exports the current context folder as JSON.
        """

        def convert(self, value):
            """
            Convert value to more JSON friendly format.
            """
            if isinstance(value, DateTime):
                # Zope DateTime
                return value.ISO8601()
            elif hasattr(value, "isBinary") and value.isBinary():
                return None

                # FileField and ImageField payloads are binary
                # as OFS.Image.File object
                data = getattr(value.data, "data", None)
                if not data:
                    return None
                return base64.b64encode(data)
            else:
                return value

        def grabData(self, obj):
            """
            Export schema data as dictionary object.
            Binary fields are encoded as BASE64.
            """
            data = {}
            for field in obj.Schema().fields():
                name = field.getName()
                value = field.getRaw(obj)
                print "%s" % (value.__class__)

                data[name] = self.convert(value)
            return data

        def grabAttributes(self, obj):
            data = {}
            for key in EXPORT_ATTRIBUTES:
                data[key] = self.convert(getattr(obj, key, None))
            return data

        def export(self, folder, recursive=False):
            """
            Export content items.
            Possible to do recursively nesting into the children.
            :return: list of dictionaries
            """

        array = []
            for obj in folder.listFolderContents():
                data = self.grabData(obj)
                data.update(self.grabAttributes(obj))

                if recursive:
                    if IFolderish.providedBy(obj):
                        data["children"] = self.export(obj, True)
                array.append(data)
            return array

        def __call__(self):
            """
            """
            folder = self.context.aq_inner
            data = self.export(folder)
            pretty = json.dumps(data, sort_keys=True, indent='    ')
            self.request.response.setHeader("Content-type", "application/json")
            return pretty

===============================
wildcard.fixpersistentutilities
===============================

wildcard.fixpersistentutilities ist ein Python-Package, das das einfache Entfernen von Local Persistent Utilities ermöglicht. Damit lassen sich p4a, Singing & Dancing, LinguaPlone etc.  einfach beseitigen.

`wildcard.fixpersistentutilities <http://pypi.python.org/pypi/wildcard.fixpersistentutilities/>`_ stellt folgende Features bereit:

- Entfernen von *adapters*
- Entfernen von *subscribers*
- Entfernen von  *provided interfaces*
- Entfernen von *provided interfaces*

  Dies ist z.B. hilfreich beim Entfernen von `collective.flowplayer <http://pypi.python.org/pypi/collective.flowplayer/>`_.

Das Paket sollte nie in produktiven Umgebungen eingesetzt werden. Auch sollten Sie vorher immer eine Sicherungskopie Ihrer ZODB erstellt haben. Um das Paket dann nutzen zu können, fügen Sie einfach der URL Ihrer Plone-Site-Root ``@@fix-persistent-utilities`` hinzu. Anschließend können Sie alle registrierten Utilities Ihrer Website durchsuchen und ggf. entfernen.

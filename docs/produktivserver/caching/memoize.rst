=======
Memoize
=======

Decorators zum Caching der Werte von Funktionen und Methoden.

Der generische ``memoize``-Decorator verwendet das ``GenericCache``-Modul als
Storage. Üblicherweise enthält es maximal tausend Objekte, die maximal eine
Stunde gecached werden.

``view`` und ``instance``
=========================

``view`` und ``instance`` sind zwei Cache-Decorators, die festgelegte cache keys
und storages haben. Hier ein Beispiel für den ``instance``-Decorator::

 from plone.memoize import instance

 class MyClass(object):

    @instance.memoize
    def some_function(self, arg1, arg2):
        ...

Wird die Funktion ``some_function()`` das erste Mal aufgerufen, wird der
zurückgegebene Wert gespeichert. Anschließend wird bei Aufrufen mit den gleichen
Argumenten die gecachte Version ohne erneute Berechnung ausgeliefert.

Mit dem ``view``-Decorator wird für denselben Zope3-View im selben Kontext
gecached, z.B. mit::

 from plone.memoize import view

 class MyView(BrowserView):

     @view.memoize
     def some_function(self, arg1, arg2):
         ...

Schließlich kann mit ``@view.memoize_contextless`` das Caching des Views
unabhängig vom Kontext veranlasst werden. Dabei muss die Anfrage jedoch zwingend
``zope.annotation`` verwenden.

Marshalling von Schlüsseln und Parametern
=========================================

Das Marshallers-Modul bietet mehrere Marshaller. Für Beispiele schauen Sie sich
am besten die Docstrings in `marshallers.py
<http://dev.plone.org/plone/browser/plone.memoize/trunk/plone/memoize/marshallers.py>`_
an.

``volatile``-Modul
==================

Das ``volatile``-Modul definiert einen Decorator, der uns Angaben darüber
erlaubt, wie der cache key berechnet wird und wo er gespeichert wird.

Hier ein einfaches Beispiel für das Caching eines Five Views mit ``volatile``-
Caching im ``ram``-Modul::

 from Products.Five import BrowserView
 from plone.memoize import ram

 def _render_cachekey(method, self, brain):
     return (brain.getPath(), brain.modified)

 class View(BrowserView):
     @ram.cache(_render_cachekey)
     def render(self, brain):
         obj = brain.getObject()
         view = obj.restrictedTraverse('@@obj-view')
         return view.render()

Die Ergebnisse der ``render``-Methode werden über Anfragen hinweg und unabhängig
vom Nutzer gecached. Der Cache wird den Angaben in ``_render_cachekey``
entsprechend aktualisiert sobald sich das Änderungsdatum  oder der Pfad des
Brains ändern.

Sollen die Werte der Funktion nur für maximal eine Stunde gespeichert werden,
kann derselbe Decorator verwendet werden::

 from time import time
 ...
 class View(BrowserView):
     @ram.cache(lambda *args: time() // (60 * 60))
     ...

Weitere Beispiele und Erläuterungen des ``volatile``-Decorator finden Sie in
`volatile.py
<http://dev.plone.org/plone/browser/plone.memoize/trunk/plone/memoize/volatile.py>`_.

Unterstützung für ``memcached``
===============================

`memcached <http://memcached.org/>`_ ist ein *distributed memory caching
system*, das ebenfalls von ``plone.memoize`` unterstützt wird. Hier ein
einfaches Beispiel, wie ein solches *Utility* in der ``caching.py`` definiert
werden kann::

 from zope.interface import directlyProvides
 import zope.thread
 from plone.memoize.interfaces import ICacheChooser
 from plone.memoize.ram import MemcacheAdapter
 import os
 import memcache

 thread_local = zope.thread.local()

 def choose_cache(fun_name):
     global servers

     client=getattr(thread_local, "client", None)
     if client is None:
         servers=os.environ.get(
             "MEMCACHE_SERVER", "127.0.0.1:11211").split(",")
         client=thread_local.client=memcache.Client(servers, debug=0)

     return MemcacheAdapter(client)

 directlyProvides(choose_cache, ICacheChooser)

Anschließend wird die bestehende Konfiguration überschrieben, sodass unser neues
Utility für das ``ICacheChooser``-Interface verwendet wird. Dies wird in der
``overrides.zcml``-Datei angegeben::

 <configure
         xmlns="http://namespaces.zope.org/zope">

     <utility
         component=".caching.choose_cache"
         provides="plone.memoize.interfaces.ICacheChooser"
         />

 </configure>

Weitere Informationen zu ``memcached`` erhaltet Ihr in `Python + Memcached: Efficient Caching in Distributed Applications <https://julien.danjou.info/python-memcached-efficient-caching-in-distributed-applications/>`_.

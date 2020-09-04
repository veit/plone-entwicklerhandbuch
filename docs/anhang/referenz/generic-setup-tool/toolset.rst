=======
Toolset
=======

Mit der ``toolset.xml``-Datei lassen sich *Portal Tools* instantiieren oder entfernen, z.B.::

 <?xml version="1.0"?>
 <tool-setup>
   <required tool_id="portal_foo" class="dotted.path.to.Foo" />
   <forbidden tool_id="portal_bar" />
 </tool-setup>

In diesem Beispiel wird ``portal_foo`` instantiiert mit der Klasse ``Foo``. Zudem wird das ``portal_bar``-Tool entfernt sofern vorhanden.

.. note::
    Die ``toolset.xml``-Datei kann nicht nur im Paket verwendet werden, das das jeweilige Tool bereitstellt sondern ist vor allem auch für Policy-Pakete gedacht.

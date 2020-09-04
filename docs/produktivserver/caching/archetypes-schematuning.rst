=======================
archetypes.schematuning
=======================

archetypes.schematuning bietet Caching für die Archetypes-Schemata. `archetypes.schematuning`_ verwendet `plone.memoize`_ um die Archetypes-Schema-Methoden des ``BaseObject`` zu cachen. Üblicherweise werden diese faktorisiert und für jede Verbindung entsprechend modifiziert. So werden in einer normalen Plone-Site beim Zugriff auf ein ATDocument-Schema durchschnittlich 80 Requests benötigt. Mit ``archetypes.schematuning`` können solche Zugriffe durchschnittlich um das 18-fache beschleunigt werden.

Für Anwendungen, die auf Archetypes aufsetzen und das Schema dynamisch ändern, steht mit ``invalidateSchema`` eine Methode zur Verfügung, die das alte Schema aus dem Cache löscht. Hierzu müssen diese Anwendungen jedoch entsprechend angepasst werden.

.. _`archetypes.schematuning`: http://pypi.python.org/pypi/archetypes.schematuning
.. _`plone.memoize`: memoize.html

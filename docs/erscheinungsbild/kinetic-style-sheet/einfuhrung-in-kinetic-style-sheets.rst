Einführung in Kinetic Style Sheets
==================================

In Plone funktionieren alle Anwendungen ohne JavaScript, und JavaScript wird ausschließlich zur Verbesserung des User Interfaces verwendet. Darüberhinaus wird vermieden, JavaScript direkt in eine Seite einzufügen und viele Aufgaben lassen sich ohne selbst JavaScript schreiben zu müssen, erledigen.

Beim Aufruf einer  Plone-Seite mit KSS läuft folgende Sequenz ab:

#. KSS-Dateien, die in die Seite mit einem ``<link />``-Tag eingebunden sind, werden analysiert.
#. Dabei werden die im KSS definierten Aktionen an nutzerseitige Ereignisse gebunden, z.B. das Klicken auf einen Schalter.
#. Tritt ein solches Ereigns ein, wird die verknüpfte Aktion ausgeführt. Dies kann ein einfacher Effekt auf Nutzerseite sein, häufig jedoch wird eine asynchrone Anfrage an den Server gestellt werden.
#. Eine serverseitige Aktion führt anwendungsspezifische Operationen durch.
#. Die serverseitige Anwendung verknüpft die Antwort mit einem oder mehreren Befehlen und sendet alles gemeinsam an den Client. Befehle werden mit PlugIns verfügbar gemacht, wobei diverse PlugIns bereits mit Plone mitkommen, so z.B. das Ändern von Text oder das Aktualisieren von Portlets.
#. Der Client führt die Befehle aus.


.. note::
    Mit `firekiss.xpi`_ steht eine Erweiterung fpr firebug zur Verfügung, mit der sich KSS-Dateien untersuchen lassen.

.. note::
    Wie eigene KSS-PlugIns geschrieben werden, wird hier nicht Thema sein. Sie erhalten jedoch weitere Informationen zu KSS unter http://kssproject.org.

.. _`firekiss.xpi`: http://kssproject.org/download/firekiss.xpi/

.. http://wiki.zope.org/grok/NewbieKSSTutorial
.. http://kssproject.org/docs/tutorial/simple-kss
.. http://plone.org/documentation/how-to/kss-on-plone-3.1
.. http://kssproject.org/docs/how-to/refreshing-content-with-kss
.. http://maurits.vanrees.org/weblog/archive/2008/09/translations-of-portal-status-messages-in-kss
.. http://www.netsight.co.uk/blog/2009/1/16/simple-scripting-with-kss

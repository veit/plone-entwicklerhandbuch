============
Clock-Server
============

Um einen Clock-Server zu konfigurieren kann z.B. folgendes angegeben werden::

 zope-conf-additional =
     <clock-server>
         method /mysite/do_stuff
         period 60
         user admin
         password secret
         host localhost
     </clock-server>

Für jeden ``clock-server``-Abschnitt kann angegeben werden, welcher Nutzer die angegebene Methode aufrufen darf. Im einzelnen:

``method``
 Pfadangabe von Zope root zu einer ausführbaren Zope-Methode (Python-Skript, externe Methode etc.) Die Methode muss keine Argumente erhalten.
``period``
 Sekunden zwischen jedem Aufruf der Methode. Üblicherweise wird mindestens ``30`` angegeben.
``user``
 ein Zope-Nutzername
``password``
 Das Passwort dieses Zope-Nutzers
``host``
 Der Name des Host, der im Header eines Requests als ``Host:`` angegeben wird. Dies kann bei in Zope angegebenen *virtual host rules* nützlich sein.

Um zu überprüfen, ob der ``clock-server`` läuft, starten Sie die Instanz oder den ZEO-Client im Vordergrund und schauen, ob eine ähnliche Meldung wie die folgende ausgegeben wird::

 2009-03-03 19:57:38 INFO ZServer Clock server for "/mysite/do_stuff" started (user: admin, period: 60)

**Anmerkung:** Ein Clock-Server sollte immer nur für einen ZEO-Client angegeben werden.

Weitere Informationen erhalten Sie unter `Clock and asyncronous tasks <http://collective-docs.readthedocs.org/en/latest/misc/asyncronoustasks.html>`_.

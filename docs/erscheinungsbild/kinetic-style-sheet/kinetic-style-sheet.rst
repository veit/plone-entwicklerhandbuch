===================
Kinetic Style Sheet
===================

#. Zunächst erstellen wir die KSS-Datei ``registration.kss``::

    #confirm-registrant input:click {
        evt-click-preventdefault: true;
        action-server:confirmRegistrant;
        confirm-registrant: kssAttr('confirm');
    }

   Die erste Zeile identifiziert ein ``input``-Feld in einem Knoten mit der ID ``confirm-registrant``. Um zu gewährleisten, dass das Formular nicht wie üblich abgeschickt wird, setzen wir ``evt-click-preventdefault`` auf ``true``. Stattdessen soll die serverseitige Aktion ``confirmRegistrant`` ausgeführt werden wobei der Parameter ``confirm`` übergeben wird.

#. Anschließend wird die Datei ``registration.kss`` als Browser-Ressource in ``browser/configure.zcml`` registriert::

    <browser:resource
        name="registration.kss"
        file="registration.kss"
        />

#. Die KSS-Datei wird nun in die Seite mit folgendem Tag eingebunden::

    <link rel="kinetic-stylesheet"
          type="text/css"
          href="http://localhost:8080/mysite/++resource++registration.kss" />

   Häufig empfiehlt es sich jedoch, die KSS-Datei in der *KSS-Registry* anzumelden. Die Anmeldung erfolgt dann im Profil ``src/vs.registration/vs/theme/profiles/default/kssregistry.xml`` mit::

    <?xml version="1.0"?>
    <object name="portal_kss" meta_type="KSS Registry">
     <kineticstylesheet
         cacheable="True"
         compression="safe"
         cookable="True"
         enabled="1"
         expression=""
         id="registration.kss"/>
    </object>

   Wird nun der *import step* in ``portal_setup`` durchlaufen oder das ``vs.registration``-Produkt neu installiert, sollte der Eintrag mit ``++resource++registration.kss`` in ``portal_kss`` eingetragen sein.

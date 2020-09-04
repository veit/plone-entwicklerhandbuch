Performance-Tests
=================

`zope-testbrowser`_
 Mit ``zope-testbrowser`` lassen sich auch Performance-Tests durchführen. Dabei lässt sich für jedes Browser-Objekt angeben, wieviel Zeit jeder Request benötigte. Dies kann verwendet werden,  um für einen Request eine tolerierbare Antwortzeit festzulegen. Dabei sollte jedoch nicht ``lastRequestSeconds`` verwendet werden, da dies unterschiedliche Zeiteinstellungen der Maschinen mitberücksichtigt, sondern ``lastRequestPystones``::

  >>> browser.open('http://localhost:8080/mysite/')
  >>> browser.lastRequestPystones < 5
  True

.. _`zope-testbrowser`: http://pypi.python.org/pypi/zope.testbrowser

`funkload`_
 erlaubt es komplexe Tests mit komplexen Zyklen zu schreiben und gibt ansehnliche Reporte aus.

 .. seealso::

    - `Connexions Developers Blog: Switching from Squid to Varnish (and getting some nice benchmarking tools along the way)`_
    - `Tarek Ziadé: Funkload + Fabric = quick and dirty distributed load system`_

.. _`funkload`: http://funkload.nuxeo.org/
.. _`Connexions Developers Blog: Switching from Squid to Varnish (and getting some nice benchmarking tools along the way)`: http://devblog.cnx.org/2010/12/switching-from-squid-to-varnish-and.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+ConnexionsRhaptosDeveloperBlog+%28Connexions+Rhaptos+Developer+Blog%29
.. _`Fabric`: http://docs.fabfile.org
.. _`Tarek Ziadé: Funkload + Fabric = quick and dirty distributed load system`: http://tarekziade.wordpress.com/2010/12/09/funkload-fabric-quick-and-dirty-distributed-load-system/

`jMeter <http://jmeter.apache.org/>`_
    Sie können Performance-Tests für Ihr Diazo-Theme erstellen mit JMeter

    #. Installation::

        $ sudo apt-get install jmeter

    #. Erstellen eines Testplans

       Nachdem Sie JMeter gestartet haben, z.B. durch die Eingabe von
       ``jmeter `` in der Konsole, sehen Sie einen leeren Testplan.

       Ein Testplan besteht mindestens aus den folgenden Elementen:

       #. *Thread Group*
          Dies ist das Wurzelelement eines Testplans. Es simuliert die Nutzer,
          als die Anfragen ausgeführt werden. Dabei simuliert jeder Thread einen
          Nutzer.

       #. *HTTP Request Default*
           Die Standardwerte für alle HTTP-Requests innerhalb einer *Thread
           Group*.

       #. *HTTP Request*
           Eine Stichprobe (Sampler), die verwendet werden kann um die Zeit für eine
           Antwort an eine bestimmte URL zu messen.
       #. Aggregate Graph
           Statistiken zu den *HTTP Request* können als aggregierte Graphen
           dargestellt werden.

    .. seealso::

        * `Getting Started with jMeter
          <https://plone-performance-testing.readthedocs.io/en/latest/jmeter/getting-started-with-jmeter.html>`_

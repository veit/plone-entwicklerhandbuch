=========
Chameleon
=========

Chameleon ist eine HTML/XML-Template-Engine, die mit der Standardinstallation von Plone 5 mitkommt, jedoch auch als Zusatzprodukt für Plone 4 installiert werden kann.

`Chameleon <https://pypi.python.org/pypi/Chameleon>`_ vereinfacht das Einfügen
von Variablen erheblich, z.B. kann nun anstat::

    <a tal:attributes="href href" tal:content="text" />

folgendes verwendet werden::

    <a href="${href}">${text}</a>

Zudem lassen sich mit der ``__html__``-Methode einfach Strings einfügen ohne
dass diese *escaped* werden müssten, z.B.::

    class Markup(object):
        def __init__(self, s):
            self.s = s

        def __html__(self):
            return s

Anschließend kann eine Instanz dieser Klasse verwendet werden um einen String
einzufügen::

    from chameleon.utils import Markup
    form.status = Markup('<div class="note">Note</div>')

Beachten Sie jedoch, dass Sie nun selbst verantwortlich sind für das *Escaping*
unerwünschter Nutzereingaben.

.. seealso::

   * `Chameleon documentation <https://chameleon.readthedocs.org/en/latest/>`_

.. `Simplify your TAL with these 2 weird tricks
   <http://glicksoftware.com/blog/chameleon-tricks>`_
   `Magic templates in Plone 5 <http://www.starzel.de/blog/magic-templates-in-plone-5>`_

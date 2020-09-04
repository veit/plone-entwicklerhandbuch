==================
Python 3-Migration
==================

Requirements
============

* Alle Third-Party-Add-Ons sollten sowohl Python 2 wie auch Python 3 unterstützen.

  Eine Übersicht, welche Add-Ons in `Collective
  <https://github.com/orgs/collective/>`_ bereits auf Python 3 aktualisiert wurden,
  findet ihr in `Python 3 porting state for Plone add-ons
  <https://github.com/orgs/collective/projects/1>`_.

* Zur Python-3-Migration verwenden wir `six <https://six.readthedocs.io/>`_ und
  `modernize <https://pypi.python.org/pypi/modernize>`_.

  sie können installiert werden mit::

    $ python3 -m venv py3env
    $ cd py3env
    $ ./bin/pip install modernize six

``precompiler``
===============

Zusätzlich verwenden wir `plone.recipe.precompiler
<https://github.com/plone/plone.recipe.precompiler>`_ um Syntaxfehler zu finden. Er
kann mit Buildout installiert werden, indem in der ``py3.cfg``-Datei folgendes
angegeben wird::

    parts += precompiler
    ...
    [precompiler]
    recipe = plone.recipe.precompiler
    eggs = ${instance:eggs}
    compile-mo-files = true

``precompile`` wird jedes Mal ausgeführt, wenn ihr Bbuildout ausführt. Wenn ihr nur ``precompile`` ausführen möchtet, könnt ihr dies mit::

    $ bin/buildout -c py3.cfg  install precompiler

``python-modernize``
====================

``python-modernize`` bereitet Python-2-Code automatisch für die Python-3-Portierung
vor. Dabei weist euch ``python-modernize`` auf Probleme hin, die nicht automatisch
gelöst werden können.

Mit ``bin/python-modernize -x libmodernize.fixes.fix_import  src/my.package`` könnt
ihr euch anzeigen lassen, welche Änderungen ``modernize`` an eurem Plone-Add-on
``my.package`` vornehmen würde.

.. note::
    Ihr könnt ``python-modernize`` u.a. mit folgenden Optionen aufrufen:

    ``-x``
        schließt bestimmte `Fixers
        <https://python-modernize.readthedocs.io/en/latest/fixers.html>`_ aus.
    ``-l``
        listet euch alle verfügbaren *Fixers* auf.

.. note::
    Im Cheat Sheet `Writing Python 2-3 compatible code
    <http://python-future.org/compatible_idioms.html>`_ erhaltet ihr einen Überblick,
    wie sich die Syntax von Python 2 zu Python 3 ändert.


* Wir verwenden die ``py3.cfg`` aus dem Plone-5.2-Branch von `vs_buildut
  <https://github.com/veit/vs_buildout>`_::

    $ bin/buildout -c py3.cfg

Starten der Plone-Instanz
=========================

::

    $ bin/wsgi.py

Häufige Probleme beim Starten sind:

* ``Class Advice``
* Relative Imports
* Syntax Error beim Import von ``async``

Testen
======

Neben dem manuellen Testen solltet ihr automatisiert Testen mit::

    $ bin/test --all -s my.package

Alternativ könnt ihr den Testrunner automatisch den Python-Debugger starten lassen
mit::

    $ bin/test -s my.package -D

Aktualisieren der Metainformationen
===================================

Aktualisiert die ``classifiers`` in ``setup.py`` aktualisiert::

    classifiers=[
        ...
        "Framework :: Plone :: 5.2",
        ...
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        ...
    ],

Häufige Probleme
================

Strings: Text vs. Bytes
-----------------------

Meist wird in Plone Text verwendet und nur in sehr seltenen Fällen Bytes.

Versucht den Code so zu ändern, dass ihr mit Beenden der Python 2-Unterstützung
einfach nur das``if``-Statement löschen müsst, z.B.::

    if six.PY2 and isinstance(value, six.text_type):
        value = value.encode('utf8')
    do_something(value)

Dabei könnt Ihr Hilfsmethoden verwenden wie ``safe_text``, ``safe_bytes``, ``safe_unicode`` und ``safe_encode``, z.B.::

    from Products.CMFPlone.utils import safe_unicode
    ...
    obj = self.context.unrestrictedTraverse(
        safe_unicode(item['_path'].lstrip('/')), None)

``python-modernize`` ändert ebenfalls nicht ``from StringIO import StringIO`` obwohl
der Import nur in Python-2 funktioniert. Für Python-3 müsst ihr überprüfen, ob es
sich um Text- oder Binärdaten handelt und die import-Anweisung entsprechend
schreiben::

    from six import StringIO

oder::

    from six import BytesIO

Weitere Informationen findet ihr im `The Conservative Python 3 Porting Guide
<https://portingguide.readthedocs.io/en/latest/strings.html>`_.

.. Siehe auch
    * `Best practices for making code compatible with Python2 and Python3
      <https://github.com/plone/Products.CMFPlone/issues/2184>`_

================================
ZopeSkel – Standardeinstellungen
================================

Hierzu können Sie die Datei ``.zopeskel`` in Ihrem Home-Verzeichnis anlegen, z.B. mit::

 $ ./bin/zopeskel --make-config-file > ~/.zopeskel

Die ``.zopeskel``-Datei kann dann z.B. so aussehen::

    [DEFAULT]
    author_email = kontakt@veit-schiele.de
    license_name = BSD
    master_keywords = Web Python Zope

    [[plone_basic]]
    expert_mode = all
    namespace_package = vs
    add_profile = True
    keywords = %(master_keywords)s Plone
    url = https://github.com/veit/

- Sie können im ``[DEFAULT]``-Abschnitt bestimmte Werte angeben, die für eine spezifische Vorlage wieder überschrieben werden können. So ist z.B. im  ``[DEFAULT]``-Abschnitt als Lizenz ``BSD`` angegeben, diese wird jedoch im ``[plone3_theme]``-Abschnitt für diese Vorlage wieder überschrieben.
- Sie können auch Angaben aus dem ``[DEFAULT]``-Abschnitt in spezifischen Vorlagen erweitern unter Verweis auf die ``master``-Liste.

.. note::

   Im Gegensatz zum ``paster create``-Aufruf kann das ``zopeskel``-Skript nicht mit dem
   Argument ``--svn-repository`` aufgerufen werden um ein Paket an einer bestimmten Stelle
   eines SVN-Repository zusammen mit der Verzeichnishierarchie ``trunk/``, ``tags/`` und
   ``branches/`` zu erstellen.

============================================
ZopeSkel – Verfügbare Vorlagen und Variablen
============================================

Um eine Liste mit allen verfügbaren Vorlagen (Templates) und ausführlichen Beschreibungen zu erhalten, geben sie folgendes ein::

 $ ./bin/zopeskel --list

 Plone Development
 -----------------

 archetype: A Plone project that uses Archetypes content types

    This creates a Plone project that uses Archetypes content types. It
    has local commands that will allow you to add content types and to
    add fields to your new content types.
 ...

Um nun ein Projekt aus einer dieser Vorlagen zu erstellen, wird ZopeSkel folgendermaßen aufgerufen::

 $ ./bin/zopeskel <template> <output-name>

also z.B.::

 $ cd src/
 $ ../bin/zopeskel archetype vs.registration

Es können auch noch weitere Variablen neben dem Projektnamen mitgegeben werden, z.B.::

 $ ../bin/zopeskel archetype vs.registration author_email=kontakt@veit-schiele.de

Dies ist gut geeignet sofern Pakete skriptgesteuert erstellt werden sollen. Eine vollständige Liste der Variablen erhalten Sie mit::

 $ ./bin/paster create -t <template-name> --list-variables

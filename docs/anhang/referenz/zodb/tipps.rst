=====
Tipps
=====

- Beim Lesen der ``Data.fs`` sollte nicht gleichzeitig geschrieben werden.

  - Vermeiden Sie ``setDefault``.
  - Inplace-Migrationen sollten vermeiden werden.
- Verwenden Sie skalierbare Datenstrukturen wie ``BTrees``.

.. seealso::
    * `ZODB-Tutorial`_
    * `ZODB programming guide`_
    * `The ZODB Book`_

.. _`ZODB-Tutorial`: http://www.zodb.org/documentation/tutorial.html
.. _`ZODB programming guide`: http://www.zodb.org/documentation/guide/index.html
.. _`The ZODB Book`: http://www.zodb.org/zodbbook/

======================
Einführung in die ZODB
======================

Relationale Datenbanken
 sind gut geeignet, eine große Anzahl homogener Daten zu verwalten. Sie sind jedoch wenig geeignet um hierarchische Daten abzubilden.

 ORMs
  wie SQLAlchemy erlauben ein objektorientiertes Arbeiten wobei die Daten in einer relationalen Datenbank gespeichert werden. Die Restriktionen relationeller Datenmodelle bleiben jedoch auch hier erhalten.

Hierarchische Datenbanken
  z.B. LDAP oder ein Dateisystem sind sehr viel besser geeignet zur Speicherung flexibler hierarchischer Strukturen, wie sie von Content Management Systemen im allgemeinen gefordert werden. Diese Datenbankenbeherrschen jedoch im allgemeinen jedoch keine transaktionalen Semantiken.
ZODB
 ist transparent bei der persistenten Speicherung von Python-Objektem.

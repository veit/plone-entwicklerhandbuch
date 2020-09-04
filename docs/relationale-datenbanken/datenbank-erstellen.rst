===================
Datenbank erstellen
===================

In diesem Beispiel verwenden wir MySQL 5.0 mit InnoDB-Tabellen, die grundlegenden Konzepte lassen sich jedoch leicht auch auf andere relationale Datenbanken übertragen.

Hier das Skript zur Definition der Tabelle ``registration`` und einiger Beispieldaten::

 create database if not exists registration;
 use registration;

 -- Occurrences
 create table if not exists occurrence (
     occurrence_key integer unsigned not null auto_increment primary key,
     registration_key char(4) not null,
     registrant_key char(4) not null,
     occurrence_time datetime not null,
     vacancies integer unsigned not null,
     index showing_registration_key(registration_key),
     index showing_registrant_key(registrant_key),
     index showing_occurrence_time(occurrence_time),
     index showing_vacancies(vacancies)
 ) engine=InnoDB;

 -- Reservations
 create table if not exists reservation (
     reservation_key integer unsigned not null auto_increment primary key,
     occurrence_key integer unsigned not null,
     num_reservations tinyint unsigned not null,
     customer_name varchar(64) not null,
     index reservation_num_reservations(num_reservations),
     foreign key(occurrence_key)
         references occurrence(occurrence_key)
             on update restrict
             on delete restrict
 ) engine=InnoDB;

Für unser Beispiel wird der Zugang zu MySQL durch ``root`` ohne Passwort ermöglicht. Für Produktivsysteme sollte jedoch selbstverständlich ein Passwort vergeben werden.

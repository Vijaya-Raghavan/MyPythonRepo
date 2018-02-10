
CREATE SEQUENCE risk_id_seq START 1;
CREATE SEQUENCE prop_type_id_seq START 1;
CREATE SEQUENCE risk_prop_id_seq START 1;

create table risk(id integer primary key, name varchar(100) unique not null);

create table prop_type(id integer primary key, type varchar(50) unique not null);
insert into prop_type values(nextval('prop_type_id_seq'), 'TEXT');
insert into prop_type values(nextval('prop_type_id_seq'), 'NUMBER');
insert into prop_type values(nextval('prop_type_id_seq'), 'DATE');
insert into prop_type values(nextval('prop_type_id_seq'), 'ENUM');
insert into prop_type values(nextval('prop_type_id_seq'), 'BOOLEAN');

create table risk_prop(id integer primary key, risk_id integer references risk(id) not null, prop_name varchar(50) not null, prop_type_id integer references prop_type(id) not null, prop_desc varchar(1000), prop_constraint varchar(200), prop_default_val varchar(200));
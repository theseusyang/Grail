drop table IF EXISTS edge;
create table edge(src int, dest int);
insert into edge values(1,2);
insert into edge values(1,3);
insert into edge values(3,4);
insert into edge values(2,4);
insert into edge values(4,5);
select * from edge;

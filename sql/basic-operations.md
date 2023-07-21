# Basic operations on a database

In SQL (Structured Query Language), different types of commands are used to interact with databases and manage data. These commands are 
categorized into four main groups based on their functionality: DDL, DML, DCL, and TCL. Additionally, there is a subset called DQL, which 
is not an official category but is commonly used to refer to commands used for querying data. Let's explain each category:

The crud operation refers to:
crud - create, retrive (select), update and delete


In sql, the 4 main categories for querying data are:
 - DDL: create, alter, drop, truncate
 - DML: insert, update, delete,
 - TCL: start transaction, savepoint, rollback, commit, set constraint [o]
 - DCL: grant, revoke
 - DQL: select

## DDL (Data Definition Language):
DDL commands are used to define and manage the structure of the database. They are responsible for creating, altering, and dropping 
database objects like tables, views, indexes, and schemas. DDL commands do not manipulate the data itself but rather modify the 
database's structure and schema.

create - 
1. create a database - create database <db_name>;
2. create a table - create table <table_name> (<column name> <type>(<field length/size>));
3. create new table from existing_table.
create table new_table_name
(select * from existing_table);

desc <table_name>;
use <schema_name>;

alter - 
1. Rename table - 
alter table <table_name> rename to <new_table_name>;

2. Add column - 
alter table table_name add (column_name type(size),column_name type(size));
-- use, (comma) with to add multiple columns

3. Rename column - 
alter table <table_name> rename column <old_column_name> to <new_column_name>; 
-- use, (comma) with full rename column to change multiple columns
alter table table_name   
change old_column_name1 new_column_name1 data type,  
change old_column_name2 new_column_name2 data type;

5. modify datatype - 
alter table <table_name> modify column <column_name> <new_type/(new_size),
						 modify column <column_name> <new_type/(new_size)>;



-- alter used to add/modify/drop indexes/constarints.

drop -
1. drop table - drop table if exists table_name;
2. drop column - alter table table_name drop column column_name;


rename -
1. rename table - rename table table_name to new_table_name;
3. rename column - alter table table_name rename column old_column_name to new_column_name;

truncate -
1. truncate table - truncate table table_name;

comment - 
1. create table with comment - create table <table_name> (<column name> <type>(<field length/size>)) comment = '<comment description>';
2. add a comment to an existing table. - alter table <table_name> comment = '<comment description>';
3. drop a comment - alter table <table_name> comment = ''; -- leave it empty
4. update a comment to an existing table. - alter table <table_name> comment = '<updated comment description>';
5. display a comment - show table status where name = '<table_name>';

-- ****************************dql****************************

select - 
1. select all from table - select * from <table_name/view_name>;
2. select specific columns from table - select <list of columns - column1 , column2, column3> from <table_name/view_name>;
3. select using where clause - select * from <table_name/view_name> where <condition>; -- displays the records based on the given condition.
4. select using distinct - select distinct <column_name>, <list of columns> from <table_name>; -- gives the list unique values
5. select using and - select * from <table_name/view_name> where <condition> and <condition>; -- you can use more conditions under where caluse
6. select using or - select * from <table_name/view_name> where <condition> or <condition>; -- you can use more conditions under where caluse
7. select uisng in - select * from <table_name/view_name> where <column_name> in <list of values seperated by commas>; -- display's the list of values seperated by commas.
8. select uisng not in - select * from <table_name/view_name> where <column_name> not in <range/set of values>; -- display's the list of excluding values seperated by commas.
9. select uisng between/not between  - select * from <table_name/view_name> where <column_name> between/not between <value> and <value>; -- used to display the range of values, mostly in dates and numbers.
10. select uisng like - select * from <table_name/view_name> where <column_name> like <value with or without wild chars>; -- pattren matching will be done here. wild chars are %, _
11. select uisng limit - select * from <table_name/view_name> limit <range to be selected>; -- user to select the range, example 2[offest],4[range] or 2[range] - offset is optional. 
12. select uisng is null - select * from <table_name/view_name> where <column_name> is null; -- dispalys the records with null vaues.
13. select uisng is not null - select * from <table_name/view_name> where <column_name> is not null; -- dispalys the records with out null vaues.
14. select uisng order by - select * from <table_name/view_name> where <condition> order by <column_name/s>; -- dispalys the records in give oreder [asc-default/desc].
15. select uisng group by - select * from <table_name/view_name> where <condition> group by <column_name/s>; -- groups the columns based on the list of columns we mention.
16. select uisng having - select * from <table_name/view_name> where <condition> group by <column_name/s> having <condition>; -- additional condition on group by, works similar to where clause
17. select using rollup - select <list of columns with agg functions> from <table_name> group by <column_name/s> with rollup; -- get's the total sum values along with the group sum values listed on the group by caluse.
18. select as - select <column_name> as <new_column_name> from <table_name>; -- column names can be renamed as per our requirement while retrival(just for the sinle execution/display).


## DML

**Insert**

1. insert one into all columns - insert into <table_name> values (<list of values seperated by commas>); -- inserting one record into all columns, no need to list the columns
2. insert one into specific columns - insert into <table_name> (<list of columns seperated by commas>) values (<list of values seperated by commas>); -- inserting one record into speacific columns, need to list the columns
3. insert multiple rows into all columns - insert into <table_name> values (<list of values seperated by commas>),(<list of values seperated by commas>),(<list of values seperated by commas>),(<list of values seperated by commas>);-- inserting multiple record into all columns, no need to list the columns
4. insert multiple rows into specific columns- insert into <table_name> (<list of columns seperated by commas>) values (<list of values seperated by commas>),(<list of values seperated by commas>),(<list of values seperated by commas>),(<list of values seperated by commas>),(<list of values seperated by commas>); -- inserting multiple record into specific columns, need to list the columns

```
INSERT INTO Employee
SELECT 1, 'Mike', 3000,'2020-6-7'
UNION ALL
SELECT 2, 'Ellen', 35000,'2020-8-7'
```

7. insert into select - insert into table_name (<list of columns>)<select statement>; --select <*/list of columns> from <old_table_name>;
insert into students12 (id,s_name)
(select id,s_name from students1);

**Update**
1. update single value - update <table_name> set <column_name> = <value> where <condition>;
2. update multiple values - update <table_name> set <column_name> = <value>, <column_name_1> = <value_1>
							where <condition>;
3. update multiple records with multiple values - update <table_name>

```
set <column to be updated> = (
case 
	when <column to be compared>  = <value> then <value to be updated>
    when <column to be compared>  = <value> then <value to be updated>
    when <column to be compared>  = <value> then <value to be updated>
	when <column to be compared>  = <value> then <value to be updated>
    end);
```
		
**Delete**
1. delete a row - delete from <table_name> where <condition> or/and <condition>;
2. delete multiple rows - delete from <table_name> where <condition> or/and <condition>;


## DCL 
- will be handles by dba's

- grant , revoke -  database admins


- `grant` - grant the permission to the users on specific objects (schema);
- `revoke` - revoke the permission to the users on specific objects (schema);


## sub-query

- `subquery` - (query within query) - select <column names> from table_name where column (= or <> or in or not in) (select column_name from <table_name> where <conditions>)



## TCL

-->> transcation => <execute statements> savepoint/s, rollback (to savepoints), commit.

start transaction;
savepoint <savepoint_name>;
rollback to <savepoint_name>;
commit;

tcl

set autocommit=0;

```
create table students
(s_id int,
s_name varchar(25));

insert into students
values(1,'aishu'),
(2,'hari'),
(3,'sumair');

select * from students;

insert into students
values(12,'aishu');
rollback;
```

## Table Copy

- create a table and insert teh recors into the table by using the select statement. 

1. create table <table_name> as (select (*/list of columns) from table_name);
2. insert into <table_name> select (*/list of columns) from table_name;


## Joins

the joins available in mysql are,

- inner join -  
- cross join - 
- inner straight_join - 
- cross straight_join - 
- left join - 
- right join - 
- left outer join - 
- right outer join - 
- natural join table_factor - 
- natural inner left join - 
- natural inner right join - 
- natural outer join - 

4 types - inner,left,right,cross 

- inner join - joins based on the comparison condition and displays only the matching columns.

select <column/s> from <table_name1> inner join <table_name2> on/where/using <join condition>;

- left join - joins based on the comparison condition and displays all rows from left table and the matching columns from right table.

select <column/s> from <table_name1> left join <table_name2> on/where/using <join condition>;

- right join - joins based on the comparison condition and displays all rows from right table and the matching columns from left table.

select <column/s> from <table_name1> right join <table_name2> on/where/using <join condition>;

- cross join - doesn't have a join condition and it displayed cartesian product of both tables. 

select <column/s> from <table_name1> cross join <table_name2>;


## Union

- union/union all - the column count should match (union - duplications is not allowed/ union all - duplications is allowed)

```
select (*/list of columns) from table_name union 
select (*/list of columns) from table_name;

select (*/list of columns) from table_name union all
select (*/list of columns) from table_name;
``` 
 
## exclude 

 
constraints
functions
sub query
 

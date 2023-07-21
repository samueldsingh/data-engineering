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

**Drop**
1. drop table - drop table if exists table_name;
2. drop column - alter table table_name drop column column_name;


**Rename**
1. rename table - rename table table_name to new_table_name;
3. rename column - alter table table_name rename column old_column_name to new_column_name;

truncate -
1. truncate table - truncate table table_name;

**Comment** 
1. create table with comment - create table <table_name> (<column name> <type>(<field length/size>)) comment = '<comment description>';
2. add a comment to an existing table. - alter table <table_name> comment = '<comment description>';
3. drop a comment - alter table <table_name> comment = ''; -- leave it empty
4. update a comment to an existing table. - alter table <table_name> comment = '<updated comment description>';
5. display a comment - show table status where name = '<table_name>';


## DQL

**Select** 
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

1. INSERT ONE INTO ALL COLUMNS: `INSERT INTO <TABLE_NAME> VALUES (<LIST OF VALUES SEPERATED BY COMMAS>);`  Inserting one record into all columns, No need to list the columns.

2. INSERT ONE INTO SPECIFIC COLUMNS - `INSERT INTO <TABLE_NAME> (<LIST OF COLUMNS SEPERATED BY COMMAS>) VALUES (<LIST OF VALUES SEPERATED BY COMMAS>);`. Inserting one record into speacific columns, Need to list the columns

3. INSERT MULTIPLE ROWS INTO ALL COLUMNS: `INSERT INTO <TABLE_NAME> VALUES (<LIST OF VALUES SEPERATED BY COMMAS>),(<LIST OF VALUES SEPERATED BY COMMAS>),(<LIST OF VALUES SEPERATED BY COMMAS>),(<LIST OF VALUES SEPERATED BY COMMAS>);`. Inserting Multiple record into all columns, No need to list the columns

4. INSERT MULTIPLE ROWS INTO SPECIFIC COLUMNS: `INSERT INTO <TABLE_NAME> (<LIST OF COLUMNS SEPERATED BY COMMAS>) VALUES (<LIST OF VALUES SEPERATED BY COMMAS>),(<LIST OF VALUES SEPERATED BY COMMAS>),(<LIST OF VALUES SEPERATED BY COMMAS>),(<LIST OF VALUES SEPERATED BY COMMAS>),(<LIST OF VALUES SEPERATED BY COMMAS>);`. Inserting Multiple record into specific columns, Need to list the columns

5. INSERT USING IMPORT. Import the records from the exported csv file

6. INSERT IGNORE: `INSERT IGNORE INTO <TABLE_NAME> VALUES (<LIST OF VALUES SEPERATED BY COMMAS>);`. Ignore case helps to bypass the erros during the execution. 

7. INSERT INTO SELECT: `INSERT INTO <TABLE_NAME> (<LIST OF COLUMNS>)<SELECT STATEMENT>;`. SELECT <*/LIST OF COLUMNS> FROM <OLD_TABLE_NAME>;


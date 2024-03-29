
# Basic operations on a database

In SQL (Structured Query Language), different types of commands are used to interact with databases and manage data. These commands are 
categorized into four main groups based on their functionality: DDL, DML, DCL, and TCL. Additionally, there is a subset called DQL, which 
is not an official category but is commonly used to refer to commands used for querying data. Let's explain each category:

In sql, the 4 main categories for querying data are:
1. DDL: create, alter, drop, truncate
2. DML: insert, update, delete,
3. TCL: start transaction, savepoint, rollback, commit, set constraint [o]
4. DCL: grant, revoke
5. DQL: select


## 1. DDL (Data Definition Language):
DDL commands are used to define and manage the structure of the database. They are responsible for creating, altering, and dropping database objects like tables, views, indexes, and schemas. DDL commands do not manipulate the data itself but rather modify the database's structure and schema.


Common DDL commands include:
- `CREATE`: Used to create database objects like tables, views, indexes, etc.
- `ALTER`: Used to modify the structure of existing database objects.
- `DROP`: Used to remove the whole database or table indexes, data, and more
- `TRUNCATE`: Used to remove all rows from a table (similar to `DELETE`, but faster).


### 1. CREATE

Use **CREATE** command to perform the following operations:

i. CREATE a DATABASE - `CREATE DATABASE <DB_NAME>;`

ii. CREATE a TABLE - `CREATE TABLE <TABLE_NAME> (<COLUMN NAME> <TYPE>(<Field Length/SIZE>));`

iii. CREATE a VIEW - `CREATE {OR REPLACE} VIEW <VIEW_NAME> AS <SELECT STATMENT>;`


**i. Create a database**

```
CREATE DATABASE SampleDB;
```

Double-click the db name in the SCHEMAS list in the sidebar to set the db to default db.


**ii. Create a tables (Schema)**

```
CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(100),
    salary DECIMAL(10, 2)
);
```


**iii. Create a view:**

- In MySQL, a view is a virtual table that is derived from the result of a SELECT query. It does not store data itself but represents a stored query that can be used as if it were a real table.
- Views allow you to simplify complex queries, encapsulate logic, and provide an additional layer of security by restricting direct access to underlying tables.

- Some key points about views in MySQL are:

Definition (query using  SELECT, INSERT, UPDATE, and DELETE statements), simplify complex queries (views once created for complex query stays unaffected), data abstraction (underlying complexity of the tables are hidden), security (limit users' access to specific columns or rows), Read-Only and Updatable Views (can be either read-only or updatable), performance (do not store data; they are merely stored queries.slight performance overhead).


```
CREATE VIEW EmployeeDetails AS
SELECT emp_id, first_name, last_name, department, salary
FROM Employees
WHERE department = 'HR';
```

The `CREATE VIEW` statement is used to create a virtual table in a database based on the result of a `SELECT` statement. This virtual table, known as a view, allows you to retrieve and manipulate data from multiple tables or queries as if it were a single table. The `OR REPLACE` option allows you to update an existing view if it already exists with the same name.

Here are examples of using the `CREATE VIEW` and `CREATE OR REPLACE VIEW` commands:

**Example 1: Creating a View**

Suppose you have a database with a `Customers` table and an `Orders` table, and you want to create a view that displays customer names along with their total order amounts.

```sql
CREATE VIEW CustomerOrderSummary AS
SELECT c.first_name, c.last_name, SUM(o.total_amount) AS total_spent
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id;
```

In this example, the `CustomerOrderSummary` view is created based on the result of the `SELECT` statement. The view will display customer names and their total order amounts.

**Example 2: Replacing an Existing View**

Suppose you want to update the `CustomerOrderSummary` view with additional information. You can use the `CREATE OR REPLACE VIEW` command.

```sql
CREATE OR REPLACE VIEW CustomerOrderSummary AS
SELECT c.first_name, c.last_name, SUM(o.total_amount) AS total_spent, COUNT(o.order_id) AS order_count
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id;
```

In this example, the `CREATE OR REPLACE VIEW` command updates the existing `CustomerOrderSummary` view with the new `SELECT` statement that includes both total order amounts and the count of orders for each customer.

After creating or updating a view, you can query the view just like you would a regular table. Views are particularly useful when you need to simplify complex queries, restrict access to certain columns, or provide a consistent interface to data for users or applications.


**iv. Explain DESC <TABLE_NAME> and USE <schema_name>**

The MySQL command `DESC <TABLE_NAME>;` is used to retrieve information about the columns (field names) and their data types of a specific table in the currently selected database. The `USE <schema_name>;` command is used to select or switch to a particular database or schema. 


Example:
```
DESC employeedetails
```

```
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| emp_id      | int(11)      | NO   | PRI | NULL    |       |
| first_name  | varchar(50)  | YES  |     | NULL    |       |
| last_name   | varchar(50)  | YES  |     | NULL    |       |
| department  | varchar(100) | YES  |     | NULL    |       |
| salary      | decimal(10,2)| YES  |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+
```

The `DESC employees`; command provides information about each column in the `employees` table. It shows the column name, data type, whether the column allows NULL values, if the column is part of the primary key (PRI), default value, and any extra information.


The `USE company_db`; command selects the `company_db` database, and all subsequent queries will be executed within this database until another database is selected.

In summary, the `DESC <TABLE_NAME>;` command is used to describe the structure of a specific table, and the `USE <schema_name>;` command is used to switch to a particular database before executing queries on its tables.


### 2. ALTER

- In SQL, the `ALTER` command is used to modify the structure of an existing database object, such as a table, view, or database itself.
- It allows you to add, modify, or delete columns, change data types, rename objects, and perform various other changes to adapt the database schema to evolving requirements.

The `ALTER` command is versatile and provides several subcommands that are specific to the type of object being altered. The main subcommands used with `ALTER` are:

1. `ALTER TABLE`: Used to modify the structure of a table.
2. `ALTER VIEW`: Used to modify the definition of a view.
3. `ALTER DATABASE`: Used to modify database-level properties and settings.

Here are some common uses of the `ALTER` command for each subcommand:

1. ALTER TABLE NAME (RENAME) - `ALTER TABLE <TABLE_NAME> RENAME TO <NEW_TABLE_NAME>;`
2. ALTER TABLE : ADD COLUMN - `ALTER TABLE <TABLE_NAME> ADD <COLUMN_NAME> <TYPE(SIZE)>;`. Use, (COMMA) with to Add Multiple Columns
3. ALTER TABLE : RENAME COLUMN - `ALTER TABLE <TABLE_NAME> RENAME COLUMN <OLD_COLUMN_NAME> TO <NEW_COLUMN_NAME>;`. Use, (COMMA) with full RENAME COLUMN to Change multiple Columns
4. ALTER TABLE : DROP COLUMN - `ALTER TABLE <TABLE_NAME> DROP COLUMN <COLUMN_NAME>;`
5. ALTER TABLE : MODIFY THE TYPE/SIZE OF COLUMN - `ALTER TABLE <TABLE_NAME> MODIFY COLUMN <COLUMN_NAME> <NEW_TYPE/(NEW_SIZE)>;`
6. ALTER VIEW - `ALTER VIEW <VIEW_NAME> AS <SELECT STATMENT>;` -- Later
7. ALTER VIEW (RENAME) - `ALTER TABLE <VIEW_NAME> RENAME TO <NEW_VIEW_NAME>;` -- Not Working
	or RENAME TABLE <OLD_VIEW_NAME> to <NEW_VIEW_NAME>;

1. `ALTER TABLE`:

   - Adding a new column:
     ```sql
     ALTER TABLE table_name
     ADD column_name datatype;
     ```

   - Modifying a column's data type:
     ```sql
     ALTER TABLE table_name
     MODIFY column_name new_datatype;
     ```

   - Renaming a column:
     ```sql
     ALTER TABLE table_name
     CHANGE old_column_name new_column_name datatype;
     ```

   - Deleting a column:
     ```sql
     ALTER TABLE table_name
     DROP COLUMN column_name;
     ```

   - Adding a primary key:
     ```sql
     ALTER TABLE table_name
     ADD PRIMARY KEY (column_name);
     ```

2. `ALTER VIEW`:

   - Modifying the definition of a view:
     ```sql
     ALTER VIEW view_name AS
     SELECT column1, column2, ...
     FROM table_name
     WHERE condition;
     ```

3. `ALTER DATABASE`:

   - Modifying database-level properties (e.g., character set or collation):
     ```sql
     ALTER DATABASE database_name
     CHARACTER SET utf8mb4
     COLLATE utf8mb4_unicode_ci;
     ```

   - Setting default collation for a database:
     ```sql
     ALTER DATABASE database_name
     COLLATE collation_name;
     ```

**Collation** is a set of rules that determine how string comparison and sorting are performed for character data in a database. Collation settings can be specified at the database, table, or column level, and they significantly impact how string comparisons and sorting are handled in your SQL queries. 

It's important to note that not all alterations may be allowed, depending on the specific database management system and the existing constraints or dependencies within the database. Also, some database systems might have additional specific subcommands or restrictions for certain alterations.

Before using the `ALTER` command, make sure to back up your data and review the potential consequences of the changes, as some alterations might affect the existing data or require additional maintenance steps.


More examples of using the `ALTER` command for various operations:

**1. ALTER TABLE NAME (RENAME):**

```sql
-- Assuming we have a table named "employees" and we want to rename it to "staff"
ALTER TABLE employees RENAME TO staff;
```

**2. ALTER TABLE: ADD COLUMN (with multiple columns):**

```sql
-- Assuming we have a table named "students" and we want to add two new columns: "age" (INT) and "address" (VARCHAR)
ALTER TABLE students ADD age INT, ADD address VARCHAR(100);
```

**3. ALTER TABLE: RENAME COLUMN (with multiple columns):**

```sql
-- Assuming we have a table named "employees" and we want to rename the columns "fname" to "first_name" and "lname" to "last_name"
ALTER TABLE employees RENAME COLUMN fname TO first_name, RENAME COLUMN lname TO last_name;
```

**4. ALTER TABLE: DROP COLUMN:**

```sql
-- Assuming we have a table named "products" and we want to drop the column "obsolete"
ALTER TABLE products DROP COLUMN obsolete;
```

**5. ALTER TABLE: MODIFY THE TYPE/SIZE OF COLUMN:**

```sql
-- Assuming we have a table named "orders" and we want to change the data type of the "quantity" column to DECIMAL(8,2)
ALTER TABLE orders MODIFY COLUMN quantity DECIMAL(8,2);
```

**6. ALTER VIEW:**

```sql
-- Assuming we have a view named "high_salary_employees" and we want to change its definition to include employees with salaries above 50000
ALTER VIEW high_salary_employees AS
SELECT emp_id, first_name, last_name, salary
FROM employees
WHERE salary > 50000;
```

**7. ALTER VIEW (RENAME) - Note that renaming a view directly using `ALTER VIEW` is not supported in MySQL. Instead, you can use the `RENAME TABLE` command:**

```sql
-- Assuming we have a view named "old_view" and we want to rename it to "new_view"
RENAME TABLE old_view TO new_view;
```

These are some examples of using the `ALTER` command in MySQL to modify tables and views, including renaming, adding, modifying, and dropping columns, as well as modifying the definition of views. Always be cautious when using the `ALTER` command, as it can have significant impacts on the database structure and data. Ensure you have a backup of your data before performing any alterations.


### 3. DROP 

In SQL, the `DROP` command is used to remove or delete database objects, such as tables, views, indexes, or even entire databases. It permanently deletes the specified object from the database, and the data and structure associated with that object are no longer available.

Examples of using the `DROP` command:
1. DROP TABLE: `DROP TABLE {IF EXISTS} <TABLE_NAME>;`
2. DROP COLUMN: `ALTER TABLE <TABLE_NAME> DROP COLUMN <COLUMN_NAME>;`
3. DROP VIEW: `DROP VIEW {IF EXISTS} <VIEW_NAME>;`

The syntax for the `DROP` command varies depending on the type of object you want to drop. Here are some common uses of the `DROP` command:

**1. DROP TABLE:**

```sql
-- Example 1: Basic DROP TABLE command
DROP TABLE employees;
```

This command will permanently delete the table named `employees` along with all its data and associated objects (e.g., indexes, triggers, constraints).

```sql
-- Example 2: DROP TABLE with IF EXISTS
DROP TABLE IF EXISTS customers;
```

This command will check if the table named `customers` exists before attempting to drop it. If the table exists, it will be dropped; otherwise, it will do nothing, avoiding an error if the table does not exist.

**2. DROP COLUMN:**

```sql
-- Example: Drop a column named 'age' from the table 'employees'
ALTER TABLE employees DROP COLUMN age;
```

This command will remove the column named `age` from the table `employees`. Be cautious when dropping columns, as any data stored in that column will be lost.

**3. DROP VIEW:**

```sql
-- Example 1: Basic DROP VIEW command
DROP VIEW sales_view;
```

This command will delete the view named `sales_view` from the database. The view itself is just a saved query, and dropping it will not delete any actual data.

```sql
-- Example 2: DROP VIEW with IF EXISTS
DROP VIEW IF EXISTS customer_info_view;
```

This command will check if the view named `customer_info_view` exists before attempting to drop it. If the view exists, it will be dropped; otherwise, it will do nothing, avoiding an error if the view does not exist.

**4. Drop an Index:**

```sql
DROP INDEX index_name ON table_name;
```
This command deletes the specified index associated with a table. Indexes are used to improve the performance of queries, and dropping an index will not affect the table's data but might impact query performance.

**4. Drop a Database:**
```sql
DROP DATABASE database_name;
```
This command permanently removes the specified database and all its objects, including tables, views, procedures, and more. Be extremely cautious when using this command, as all data in the database will be lost.

Remember, using the `DROP` command is irreversible, and it permanently deletes database objects. Always ensure that you have a proper backup before performing any `DROP` operation, especially in a production environment. Be cautious when using the `DROP` command to avoid accidental data loss.

It's important to note that the `DROP` command is a powerful and potentially dangerous operation, so it should be used with care. Always make sure to have proper backups before performing any `DROP` operation, especially when dealing with critical data.

Always double-check the object name before executing the `DROP` command, as it is not reversible, and once an object is dropped, it cannot be recovered unless you have a backup of the database.


### 4. RENAME 

In SQL, the `RENAME` command is not a standard SQL command. The reason for this is that SQL databases have different implementations and features, and there is no single standardized way to rename database objects like tables, columns, or views across all database management systems (DBMS).

However, some specific database management systems provide their own ways to rename objects. Let's look at the examples of renaming tables and columns for different popular DBMS:

1. MySQL:
MySQL does not have a direct `RENAME` command, but you can use the `ALTER TABLE` command to rename a table or a column:

Rename a Table:
```sql
ALTER TABLE old_table_name RENAME TO new_table_name;
```

Rename a Column:
```sql
ALTER TABLE table_name CHANGE old_column_name new_column_name data_type;
```

2. PostgreSQL:
PostgreSQL also does not have a specific `RENAME` command. Instead, you can use the `ALTER TABLE` command to rename a table or a column:

Rename a Table:
```sql
ALTER TABLE old_table_name RENAME TO new_table_name;
```

Rename a Column:
```sql
ALTER TABLE table_name RENAME COLUMN old_column_name TO new_column_name;
```

3. SQL Server (Microsoft SQL Server):
SQL Server provides the `sp_rename` system stored procedure to rename objects:

Rename a Table:
```sql
EXEC sp_rename 'old_table_name', 'new_table_name';
```

Rename a Column:
```sql
EXEC sp_rename 'table_name.old_column_name', 'new_column_name', 'COLUMN';
```

It's important to note that renaming database objects should be done with caution, especially in production environments. Renaming objects might have implications on dependent queries, views, stored procedures, and application code. Always make sure to have proper backups and test thoroughly before performing any renaming operations.

Additionally, since there is no standardized `RENAME` command in SQL, it's recommended to consult the specific documentation of your database management system for the correct syntax and procedures for renaming objects in your particular DBMS.

Give examples of using RENAME command using the given:
1. RENAME TABLE: `RENAME TABLE <TABLE_NAME> to <NEW_TABLE_NAME>;`
2. RENAME VIEW: `RENAME TABLE <VIEW_NAME> to <NEW_VIEW_NAME>;`
3. RENAME COLUMN: `ALTER TABLE <TABLE_NAME> RENAME COLUMN <OLD_COLUMN_NAME> TO <NEW_COLUMN_NAME>;`

In most database management systems, including MySQL, PostgreSQL, and SQL Server, there is no specific `RENAME` command for directly renaming tables, views, or columns. Instead, you can use the `ALTER TABLE` command to rename a table or a column.

Here are the correct examples for renaming tables, views, and columns:

1. RENAME TABLE (MySQL):
To rename a table in MySQL, you can use the `ALTER TABLE` statement with the `RENAME` keyword:

```sql
-- Rename table 'old_table_name' to 'new_table_name'
ALTER TABLE old_table_name RENAME new_table_name;
```

2. RENAME TABLE (PostgreSQL):
To rename a table in PostgreSQL, you can use the `ALTER TABLE` statement with the `RENAME TO` clause:

```sql
-- Rename table 'old_table_name' to 'new_table_name'
ALTER TABLE old_table_name RENAME TO new_table_name;
```

3. RENAME TABLE (SQL Server):
SQL Server does not have a direct `RENAME TABLE` command. Instead, you can use the `sp_rename` system stored procedure:

```sql
-- Rename table 'old_table_name' to 'new_table_name'
EXEC sp_rename 'old_table_name', 'new_table_name';
```

4. RENAME VIEW (MySQL, PostgreSQL, SQL Server):
Views are not directly renamed using a `RENAME` command. Instead, you can create a new view with the desired name and recreate its definition based on the existing view's query:

```sql
-- Create a new view 'new_view_name' based on the existing view 'old_view_name'
CREATE VIEW new_view_name AS SELECT * FROM old_view_name;

-- Drop the old view if needed
DROP VIEW old_view_name;
```

5. RENAME COLUMN (MySQL, PostgreSQL, SQL Server):
To rename a column in a table, you can use the `ALTER TABLE` command with the `RENAME COLUMN` clause:

```sql
-- Rename column 'old_column_name' to 'new_column_name' in 'table_name'
ALTER TABLE table_name RENAME COLUMN old_column_name TO new_column_name;
```

Please note that the syntax and specific features might vary slightly between different database management systems. Always refer to the documentation of your particular DBMS for the correct syntax and options for renaming database objects.

### 5. TRUNCATE - (DROP+CREATE)

In SQL, the `TRUNCATE` command is used to quickly and efficiently remove all rows from a table, effectively resetting the table to its original state. Unlike the `DELETE` command, which removes individual rows and can be time-consuming for large tables, the `TRUNCATE` command is much faster and uses less transaction log space because it works by deallocating the data pages containing the table's rows.

Important points to note about the `TRUNCATE` command:

1. The `TRUNCATE` command is typically used with tables, not with views or other database objects.
2. It is a DDL (Data Definition Language) command, which means it implicitly commits the current transaction, and you cannot use it within a transaction or as part of a larger transaction.
3. Unlike the `DELETE` command, `TRUNCATE` does not log individual row deletions. It deallocates the data pages in which the rows are stored, making it faster and using less transaction log space.

The syntax for the `TRUNCATE` command is straightforward:

```sql
TRUNCATE TABLE table_name;
```

Example:

Suppose we have a table called `employees` with the following data:

```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50)
);

INSERT INTO employees (id, name, department)
VALUES
    (1, 'John', 'Engineering'),
    (2, 'Jane', 'HR'),
    (3, 'Alice', 'Marketing');
```

Now, let's use the `TRUNCATE` command to remove all rows from the `employees` table:

```sql
TRUNCATE TABLE employees;
```

After executing the `TRUNCATE` command, the `employees` table will be empty, and all data will be removed from the table. However, the table structure and column definitions will remain intact.

Keep in mind that since `TRUNCATE` is a DDL command, it cannot be rolled back or undone. Once the `TRUNCATE` command is executed, the data in the table is permanently deleted. If you need to keep a backup of the data or perform a more selective removal, consider using the `DELETE` command instead.

Give example for the given TRUNCATE command:
1. TRUNCATE TABLE - TRUNCATE TABLE <TABLE_NAME>;

Sure, here's an example of using the `TRUNCATE TABLE` command in SQL:

Suppose we have a table called `students` with the following data:

```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
);

INSERT INTO students (id, name, age)
VALUES
    (1, 'Alice', 25),
    (2, 'Bob', 22),
    (3, 'Charlie', 20);
```

Now, let's use the `TRUNCATE TABLE` command to remove all rows from the `students` table:

```sql
TRUNCATE TABLE students;
```

After executing the `TRUNCATE TABLE` command, the `students` table will be empty, and all data will be removed from the table. The table structure with its columns and primary key definition will remain intact, but all rows will be deleted.

Keep in mind that the `TRUNCATE TABLE` command is a fast and efficient way to remove all data from a table. However, it is essential to use it with caution, as the operation cannot be rolled back, and all data will be permanently deleted from the table. Make sure to have proper backups before performing the `TRUNCATE TABLE` command, especially in a production environment.

### 6. COMMENT

In SQL, the comment command is used to add comments within SQL code. Comments are non-executable lines that provide explanatory notes, reminders, or documentation within the SQL script. These comments are ignored by the database engine during query execution and do not affect the result of the query.

There are two types of comments in SQL:

1. Single-line comments: These comments start with `--` and continue until the end of the line. Anything written after `--` on the same line will be treated as a comment.

Example of a single-line comment:
```sql
-- This is a single-line comment
SELECT column1, column2 FROM table_name;
```

2. Multi-line comments: These comments are enclosed between `/*` and `*/` and can span multiple lines.

Example of a multi-line comment:
```sql
/*
This is a multi-line comment.
It can span several lines, and everything inside will be treated as a comment.
*/
SELECT column1, column2 FROM table_name;
```

Comments are useful for several reasons:

1. Code Documentation: Comments provide explanations for the purpose of queries or the rationale behind specific code blocks, making it easier for others (and your future self) to understand the code.

2. Code Testing: By commenting out parts of a query, you can temporarily exclude them from execution. This allows you to test different parts of a query without permanently removing them from the script.

3. Code Clarity: Comments help improve the readability of complex queries by breaking them down into smaller, more manageable parts.

It's essential to use comments in SQL scripts to improve code quality and maintainability. However, it's also crucial not to over-comment, as too many comments can clutter the code and make it harder to read. Balancing clear explanations with concise and well-organized code is key.

Give examples of using COMMENT command with the following:

1. CREATE TABLE WITH COMMENT: `CREATE TABLE <TABLE_NAME> (<COLUMN NAME> <TYPE>(<Field Length/SIZE>)) COMMENT = '<Comment description>';`
2. ADD A COMMENT TO AN EXISTING TABLE: `ALTER TABLE <TABLE_NAME> COMMENT = '<Comment description>';`
3. DROP A COMMENT: `ALTER TABLE <TABLE_NAME> COMMENT = '';` -- Leave it Empty
4. UPDATE A COMMENT TO AN EXISTING TABLE:  `ALTER TABLE <TABLE_NAME> COMMENT = '<Updated comment description>';`


In SQL, the syntax for adding, updating, and dropping comments on a table varies depending on the database management system being used. Here are examples for each case using MySQL:

1. CREATE TABLE WITH COMMENT:

```sql
-- Create a table 'students' with a comment describing the table
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
) COMMENT = 'Table to store student information';
```

In this example, the `CREATE TABLE` statement creates a table named `students` with columns `id`, `name`, and `age`. The `COMMENT` option is used to add a comment describing the purpose of the table.

2. ADD A COMMENT TO AN EXISTING TABLE:

```sql
-- Add a comment to an existing table 'employees'
ALTER TABLE employees COMMENT = 'Table to store employee records';
```

In this example, the `ALTER TABLE` statement is used to add a comment to an existing table named `employees`.

3. DROP A COMMENT:

```sql
-- Drop the comment from the 'students' table
ALTER TABLE students COMMENT = '';
```

In this example, the `ALTER TABLE` statement is used to remove the comment from the `students` table by setting it to an empty string.

4. UPDATE A COMMENT TO AN EXISTING TABLE:

```sql
-- Update the comment for the 'products' table
ALTER TABLE products COMMENT = 'Table to store product information and inventory';
```

In this example, the `ALTER TABLE` statement is used to update the comment for an existing table named `products`.

Please note that the syntax for adding, updating, and dropping comments may differ in other database management systems. Always refer to the specific documentation of your database system for the correct syntax and options for adding, updating, and dropping comments on tables.


## 2. DML (Data Manipulation Language):
DML commands are used to manipulate data within the database. They allow you to insert, update, and delete data in the database tables.

DML stands for "Data Manipulation Language" in SQL (Structured Query Language). It is a subset of SQL commands used to interact with and manipulate data stored in relational databases. DML commands primarily deal with inserting, updating, deleting, and retrieving data from database tables. Some of the key DML commands include:

1. SELECT: The SELECT statement is used to retrieve data from one or more database tables. It allows you to specify the columns you want to retrieve, filter data based on conditions using the WHERE clause, and sort the result using the ORDER BY clause.

Example:
```sql
SELECT first_name, last_name FROM employees WHERE department = 'HR' ORDER BY last_name;
```

2. INSERT: The INSERT statement is used to add new rows (records) into a table. It specifies the table name and the values for each column to be inserted.

Example:
```sql
INSERT INTO employees (first_name, last_name, department, age) VALUES ('John', 'Doe', 'IT', 30);
```

3. UPDATE: The UPDATE statement is used to modify existing data in a table. It allows you to change the values of one or more columns for selected rows based on a specified condition.

Example:
```sql
UPDATE employees SET department = 'Finance' WHERE age > 40;
```

4. DELETE: The DELETE statement is used to remove rows from a table based on specified conditions.

Example:
```sql
DELETE FROM employees WHERE department = 'HR';
```

DML commands are essential for managing data in a relational database. They allow you to add, modify, and remove data, as well as retrieve information for reporting and analysis. It's crucial to use DML commands with care, especially the DELETE statement, as they can have a significant impact on the data in the database. Always make sure to have proper backups and test queries before executing them, especially in a production environment.

Example of a DML command:
```sql
INSERT INTO students (id, name, age)
VALUES (1, 'John Doe', 25);
```

1. SELECT: Retrieve data from a table.

Suppose we have a table named `employees` with columns `id`, `first_name`, `last_name`, and `department`.

```sql
-- Example: Retrieve all employees' names and departments from the 'employees' table.
SELECT first_name, last_name, department FROM employees;
```

2. INSERT: Add new rows (records) into a table.

```sql
-- Example: Insert a new employee into the 'employees' table.
INSERT INTO employees (first_name, last_name, department) VALUES ('John', 'Doe', 'IT');
```

3. UPDATE: Modify existing data in a table.

```sql
-- Example: Update the department of an employee with ID 101.
UPDATE employees SET department = 'Finance' WHERE id = 101;
```

4. DELETE: Remove rows from a table.

```sql
-- Example: Delete all employees from the 'employees' table who are in the 'HR' department.
DELETE FROM employees WHERE department = 'HR';
```

5. MERGE (In some database systems like Oracle):

```sql
-- Example: Merge data from 'source_table' into 'target_table' based on a matching condition.
MERGE INTO target_table AS t
USING source_table AS s
ON t.id = s.id
WHEN MATCHED THEN
    UPDATE SET t.column1 = s.column1, t.column2 = s.column2
WHEN NOT MATCHED THEN
    INSERT (id, column1, column2) VALUES (s.id, s.column1, s.column2);
```

6. UPSERT (In some database systems like PostgreSQL and MySQL with ON DUPLICATE KEY UPDATE):

```sql
-- Example: Insert or update data in 'employees' table based on the unique constraint of 'id'.
INSERT INTO employees (id, first_name, last_name, department)
VALUES (101, 'John', 'Doe', 'Finance')
ON DUPLICATE KEY UPDATE department = VALUES(department);
```

Remember that the syntax and availability of certain commands may vary slightly between different database management systems (DBMS). Always refer to the specific documentation of your DBMS for the correct syntax and usage of DML commands.

Give examples for the following DML commands:

**SELECT -** 
1. SELECT ALL FROM TABLE: `SELECT * FROM <TABLE_NAME/VIEW_NAME>;`
2. SELECT SPECIFIC COLUMNS FROM TABLE: `SELECT <LIST of COLUMNS - COLUMN1 , COLUMN2, COLUMN3> FROM <TABLE_NAME/VIEW_NAME>;`
3. SELECT USING WHERE CLAUSE: `SELECT * FROM <TABLE_NAME/VIEW_NAME> WHERE <CONDITION>;` -- Displays the records based on the given condition.
4. SELECT USING DISTINCT: `SELECT DISTINCT <COLUMN_NAME>, <LIST OF COLUMNS> FROM <TABLE_NAME>;` -- Gives the list Unique Values
5. SELECT USING AND: `SELECT * FROM <TABLE_NAME/VIEW_NAME> WHERE <CONDITION> AND <CONDITION>;` -- You can use more conditions under where caluse
6. SELECT USING OR: `SELECT * FROM <TABLE_NAME/VIEW_NAME> WHERE <CONDITION> OR <CONDITION>;` -- You can use more conditions under where caluse
7. SELECT USING IN: `SELECT * FROM <TABLE_NAME/VIEW_NAME> WHERE <COLUMN_NAME> IN <LIST OF VALUES SEPERATED BY COMMAS>;` -- Display's the List of Values seperated by commas.
8. SELECT USING NOT IN: `SELECT * FROM <TABLE_NAME/VIEW_NAME> WHERE <COLUMN_NAME> NOT IN <RANGE/SET OF VALUES>;` -- Display's the List of excluding values seperated by commas.
9. SELECT USING BETWEEN/NOT BETWEEN: `SELECT * FROM <TABLE_NAME/VIEW_NAME> WHERE <COLUMN_NAME> BETWEEN/NOT BETWEEN <VALUE> AND <VALUE>;` -- Used to display the range of values, Mostly in dates and numbers.
10. SELECT USING LIKE: `SELECT * FROM <TABLE_NAME/VIEW_NAME> WHERE <COLUMN_NAME> LIKE <VALUE WITH OR WITHOUT WILD CHARS>;` -- pattren matching will be done here. WILD CHARS are %, _
11. SELECT USING LIMIT: `SELECT * FROM <TABLE_NAME/VIEW_NAME> LIMIT <RANGE TO BE SELECTED>;` -- user to select the range, Example 2[offest],4[range] or 2[range] - Offset is optional. 
12. SELECT USING IS NULL: `SELECT * FROM <TABLE_NAME/VIEW_NAME> WHERE <COLUMN_NAME> IS NULL;` -- Dispalys the records with null vaues.
13. SELECT USING IS NOT NULL: `SELECT * FROM <TABLE_NAME/VIEW_NAME> WHERE <COLUMN_NAME> IS NOT NULL;` -- Dispalys the records with out null vaues.
14. SELECT USING ORDER BY: `SELECT * FROM <TABLE_NAME/VIEW_NAME> WHERE <CONDITION> ORDER BY <COLUMN_NAME/S>;` -- Dispalys the records in give oreder [Asc-default/Desc].
15. SELECT USING GROUP BY: `SELECT * FROM <TABLE_NAME/VIEW_NAME> WHERE <CONDITION> GROUP BY <COLUMN_NAME/S>;` -- Groups the columns based on the list of columns we mention.
16. SELECT USING HAVING: `SELECT * FROM <TABLE_NAME/VIEW_NAME> WHERE <CONDITION> GROUP BY <COLUMN_NAME/S> HAVING <CONDITION>;` -- additional condition on group by, works similar to where clause
17. SELECT USING ROLLUP: `SELECT <LIST OF COLUMNS WITH AGG FUNCTIONS> FROM <TABLE_NAME> GROUP BY <COLUMN_NAME/S> WITH ROLLUP;` -- Get's the total sum values along with the group sum values listed on the group by clause.

The ROLLUP clause in SQL is used to generate subtotals and grand totals for aggregated data. It's often used in combination with the GROUP BY clause to create a hierarchical summary of data. Let's consider an example using a hypothetical sales database with a "sales" table containing information about sales transactions. The table might have columns such as "product_category," "region," "year," and "sales_amount."

Here's an example of using the ROLLUP clause to generate subtotals and grand totals for sales amounts based on product categories and regions:

```sql
SELECT product_category, region, year, SUM(sales_amount) AS total_sales
FROM sales
GROUP BY ROLLUP (product_category, region, year);
```

In this example, the query calculates the total sales amounts for various combinations of product categories, regions, and years using the ROLLUP clause. The result will include rows that represent subtotals and grand totals.

The output might look something like this:

```
product_category | region | year | total_sales
-----------------+--------+------+------------
Electronics      | East   | 2021 | 25000
Electronics      | East   | 2022 | 30000
Electronics      | East   |      | 55000  -- Subtotal for Electronics and East
Electronics      | West   | 2021 | 18000
Electronics      | West   | 2022 | 22000
Electronics      | West   |      | 40000  -- Subtotal for Electronics and West
Electronics      |        |      | 95000  -- Grand Total for Electronics

Clothing         | East   | 2021 | 15000
Clothing         | East   | 2022 | 17000
Clothing         | East   |      | 32000  -- Subtotal for Clothing and East
Clothing         | West   | 2021 | 12000
Clothing         | West   | 2022 | 14000
Clothing         | West   |      | 26000  -- Subtotal for Clothing and West
Clothing         |        |      | 58000  -- Grand Total for Clothing

                |        |      | 153000 -- Grand Total for all categories and regions
```

In this output, you can see subtotals for each product category within each region, as well as grand totals for each category and region combination and an overall grand total for all categories and regions.

The ROLLUP clause is a powerful tool for creating hierarchical summaries and gaining insights from aggregated data.

18. SELECT AS: `SELECT <COLUMN_NAME> AS <NEW_COLUMN_NAME> FROM <TABLE_NAME>;` -- Column names can be renamed as per our requirement while retrival(Just for the sinle execution/Display).



**INSERT -**
1. INSERT ONE INTO ALL COLUMNS: `INSERT INTO <TABLE_NAME> VALUES (<LIST OF VALUES SEPERATED BY COMMAS>);` Inserting one record into all columns, No need to list the columns.

2. INSERT ONE INTO SPECIFIC COLUMNS - `INSERT INTO <TABLE_NAME> (<LIST OF COLUMNS SEPERATED BY COMMAS>) VALUES (<LIST OF VALUES SEPERATED BY COMMAS>);`. Inserting one record into speacific columns, Need to list the columns

3. INSERT MULTIPLE ROWS INTO ALL COLUMNS: `INSERT INTO <TABLE_NAME> VALUES (<LIST OF VALUES SEPERATED BY COMMAS>),(<LIST OF VALUES SEPERATED BY COMMAS>),(<LIST OF VALUES SEPERATED BY COMMAS>),(<LIST OF VALUES SEPERATED BY COMMAS>);`. Inserting Multiple record into all columns, No need to list the columns

4. INSERT MULTIPLE ROWS INTO SPECIFIC COLUMNS: `INSERT INTO <TABLE_NAME> (<LIST OF COLUMNS SEPERATED BY COMMAS>) VALUES (<LIST OF VALUES SEPERATED BY COMMAS>),(<LIST OF VALUES SEPERATED BY COMMAS>),(<LIST OF VALUES SEPERATED BY COMMAS>),(<LIST OF VALUES SEPERATED BY COMMAS>),(<LIST OF VALUES SEPERATED BY COMMAS>);`. Inserting Multiple record into specific columns, Need to list the columns

5. INSERT USING IMPORT. Import the records from the exported csv file

6. INSERT IGNORE: `INSERT IGNORE INTO <TABLE_NAME> VALUES (<LIST OF VALUES SEPERATED BY COMMAS>);`. Ignore case helps to bypass the erros during the execution. 

7. INSERT INTO SELECT: `INSERT INTO <TABLE_NAME> (<LIST OF COLUMNS>)<SELECT STATEMENT>;`. SELECT <*/LIST OF COLUMNS> FROM <OLD_TABLE_NAME>;

**1. INSERT ONE INTO ALL COLUMNS:**  Inserting one record into all columns, No need to list the columns.

The INSERT INTO statement is used to add new rows (records) into a table in a database.

```
INSERT INTO Employees (emp_id, first_name, last_name, department_id)
VALUES (3, 'Michael', 'Johnson', 101);
```

**2. INSERT ONE INTO SPECIFIC COLUMNS:** Inserting one record into speacific columns, Need to list the columns

Here's an example of using the INSERT INTO statement to insert data into specific columns of a hypothetical `Customers` table:

```
INSERT INTO Customers (first_name, last_name, email)
VALUES ('Michael', 'Johnson', 'michael@example.com');
```

**3. INSERT MULTIPLE ROWS INTO ALL COLUMNS:** Inserting Multiple record into all columns, No need to list the columns

Here's an example of using the `INSERT INTO` statement to insert multiple rows into all columns of a hypothetical `Orders` table:

```
INSERT INTO Orders VALUES
(3, 101, '2023-08-01', 120.00),
(4, 103, '2023-08-05', 300.00),
(5, 102, '2023-08-10', 180.00);
```

**4. INSERT MULTIPLE ROWS INTO SPECIFIC COLUMNS**: Inserting Multiple record into specific columns, Need to list the columns 

Here's an example of using the INSERT INTO statement to insert multiple rows into specific columns of a hypothetical Products table:

```
INSERT INTO Products (product_id, product_name, category, price) VALUES
(3, 'Tablet', 'Electronics', 300),
(4, 'Headphones', 'Accessories', 50),
(5, 'Camera', 'Electronics', 600);
```

**5. INSERT USING IMPORT**: Import the records from the exported csv file

**6. INSERT IGNORE**: Ignore case helps to bypass the erros during the execution.

`INSERT IGNORE INTO <TABLE_NAME> VALUES (<LIST OF VALUES SEPERATED BY COMMAS>);`

The `INSERT IGNORE` statement is used in MySQL to insert data into a table. If a duplicate key error occurs while inserting data, the `IGNORE` keyword prevents the error from causing the entire statement to fail. Instead, the statement continues to execute, ignoring the duplicate key error and skipping the insertion of duplicate rows.

Here's an example of using the `INSERT IGNORE` statement to insert data into a hypothetical `Customers` table:

**Customers Table:**
| customer_id | first_name | last_name | email              |
|-------------|------------|-----------|--------------------|
| 1           | John       | Smith     | john@example.com  |
| 2           | Jane       | Doe       | jane@example.com  |

Inserting new customer records with potential duplicates:

```sql
INSERT IGNORE INTO Customers (customer_id, first_name, last_name, email)
VALUES
(3, 'Michael', 'Johnson', 'michael@example.com'),
(1, 'Alex', 'Brown', 'alex@example.com'); -- Duplicate customer_id
```

After executing this SQL statement, the `Customers` table will be updated as follows:

| customer_id | first_name | last_name | email              |
|-------------|------------|-----------|--------------------|
| 1           | John       | Smith     | john@example.com  |
| 2           | Jane       | Doe       | jane@example.com  |
| 3           | Michael    | Johnson   | michael@example.com|

In this example:
- The `INSERT IGNORE` statement specifies the `Customers` table as the target table.
- The `VALUES` keyword is followed by a list of sets of values, each enclosed in parentheses and separated by commas.
- The first set of values is inserted as a new record since it doesn't conflict with existing records.
- The second set of values contains a duplicate `customer_id` (1), but the `IGNORE` keyword prevents the error from stopping the insertion process. The duplicate row is ignored.

Please note that the behavior of `INSERT IGNORE` is specific to MySQL. Other databases may have similar functionality using different syntax or options.

**7. INSERT INTO SELECT**: `INSERT INTO <TABLE_NAME> (<LIST OF COLUMNS>)<SELECT STATEMENT>;`. SELECT <*/LIST OF COLUMNS> FROM <OLD_TABLE_NAME>;

Certainly! The `INSERT INTO ... SELECT` statement allows you to insert data into a table by selecting it from another table or using a `SELECT` query. This is useful for copying data from one table to another or transforming data before insertion. Here's the syntax:

```sql
INSERT INTO target_table (column1, column2, ...)
SELECT column1, column2, ...
FROM source_table
WHERE condition;
```

Here's an example using a hypothetical `NewCustomers` table and an existing `Customers` table:

**Customers Table:**
| customer_id | first_name | last_name |
|-------------|------------|-----------|
| 1           | John       | Smith     |
| 2           | Jane       | Doe       |

**NewCustomers Table:**
| customer_id | first_name | last_name |
|-------------|------------|-----------|

Copying data from `Customers` to `NewCustomers`:

```sql
INSERT INTO NewCustomers (customer_id, first_name, last_name)
SELECT customer_id, first_name, last_name
FROM Customers;
```

After executing this SQL statement, the `NewCustomers` table will be updated to match the `Customers` table:

| customer_id | first_name | last_name |
|-------------|------------|-----------|
| 1           | John       | Smith     |
| 2           | Jane       | Doe       |

In this example:
- The `INSERT INTO NewCustomers` statement specifies the target table as `NewCustomers`.
- The column list specifies the columns in `NewCustomers` that you want to populate.
- The `SELECT` statement retrieves data from the `Customers` table.
- The selected columns from `Customers` match the columns specified in the `INSERT INTO` statement.

This allows you to insert data from one table into another table using a single `INSERT INTO ... SELECT` statement. You can also apply transformations, filtering, or aggregations within the `SELECT` statement before inserting the data.

**UPDATE**

1. UPDATE SINGLE VALUE: `UPDATE <TABLE_NAME> SET <COLUMN_NAME> = <VALUE> WHERE <CONDITION>;`

2. UPDATE MULTIPLE VALUES [in Single row]: `UPDATE <TABLE_NAME> SET <COLUMN_NAME> = <VALUE>, <COLUMN_NAME_1> = <VALUE_1>, <COLUMN_NAME_2> = <VALUE_2> <etc...> WHERE <CONDITION>;`

3. UPDATE MULTIPLE RECORDS WITH MULTIPLE VALUES: `UPDATE <TABLE_NAME>`

```
SET <COLUMN TO BE UPDATED> = (
CASE 
    WHEN <COLUMN TO BE COMPARED>  = <VALUE> THEN <VALUE TO BE UPDATED>
    WHEN <COLUMN TO BE COMPARED>  = <VALUE> THEN <VALUE TO BE UPDATED>
    WHEN <COLUMN TO BE COMPARED>  = <VALUE> THEN <VALUE TO BE UPDATED>
    WHEN <COLUMN TO BE COMPARED>  = <VALUE> THEN <VALUE TO BE UPDATED>
END);
```

Example:
```
UPDATE students
SET score = (
    CASE 
        WHEN student_id = 101 THEN 95
        WHEN student_id = 102 THEN 80
        WHEN student_id = 103 THEN 85
        WHEN student_id = 104 THEN 92
    END)
WHERE student_id IN (101, 102, 103, 104);
```
		
**DELETE**
1. DELETE A ROW: `DELETE FROM <TABLE_NAME> WHERE <CONDITION> or/and <CONDITION>;`
2. DELETE MULTIPLE ROWS: `DELETE FROM <TABLE_NAME> WHERE <CONDITION> or/and <CONDITION>;`



## 3. DCL (Data Control Language):

- DCL stands for "Data Control Language" in SQL (Structured Query Language).
- DCL commands are used to control access to data and manage database objects' permissions within a relational database.
- These commands primarily deal with defining and managing user privileges and access rights to the database objects, ensuring data security and integrity.
- By granting or revoking privileges, database administrators can control who can perform various operations on the database objects, ensuring that sensitive data remains protected and only authorized users have appropriate access.
- It's crucial to carefully manage user permissions and privileges to maintain data integrity and prevent unauthorized access to critical data.
- Database administrators must regularly review and adjust privileges to meet security requirements and adhere to the principle of least privilege, giving users only the minimum level of access they need to perform their tasks.
- The two main DCL commands are: `GRANT` and `REVOKE`.

1. GRANT: The GRANT command is used to give specific privileges and permissions to users or roles. Privileges include the ability to perform certain actions on database objects, such as SELECT, INSERT, UPDATE, DELETE, and more.

Example:
```sql
-- Grant SELECT and INSERT privileges on the 'employees' table to a user 'user1'
GRANT SELECT, INSERT ON employees TO user1;
```


2. REVOKE: The REVOKE command is used to remove specific privileges from users or roles. It revokes previously granted privileges, restricting their access to certain actions on the database objects.

Example:
```sql
-- Revoke the UPDATE privilege on the 'products' table from a user 'user2'
REVOKE UPDATE ON products FROM user2;
```


In this example, the `REVOKE` command is used to remove the `UPDATE` privilege on the `products` table from a user named `user2`. This means that `user2` will no longer be able to modify existing records in the `products` table.

3. GRANT with OPTION:

```sql
-- Example: Grant SELECT privilege on the 'sales' table to a user 'user3' with the option to grant it further to others.
GRANT SELECT ON sales TO user3 WITH GRANT OPTION;
```

In this example, the `GRANT` command is used to give the `SELECT` privilege on the `sales` table to a user named `user3`. Additionally, the `WITH GRANT OPTION` allows `user3` to further grant the `SELECT` privilege to other users or roles.

4. REVOKE with CASCADE:

```sql
-- Example: Revoke all privileges on the 'inventory' table from a user 'user4' and cascade the revoke to objects depending on it.
REVOKE ALL PRIVILEGES ON inventory FROM user4 CASCADE;
```

In this example, the `REVOKE` command is used to remove all privileges on the `inventory` table from a user named `user4`. The `CASCADE` option ensures that the revoke action cascades to objects depending on the `inventory` table, removing permissions from dependent objects as well.

Remember that the syntax and availability of DCL commands may vary slightly between different database management systems (DBMS). Always refer to the specific documentation of your DBMS for the correct syntax and usage of DCL commands. Additionally, be cautious when granting or revoking privileges to ensure data security and adhere to the principle of least privilege.


## 4. TCL (Transaction Control Language):

- TCL stands for "Transaction Control Language" in SQL (Structured Query Language).
- TCL commands are used to manage transactions within a relational database. Transactions are a sequence of one or more SQL statements that are executed as a single unit of work.
- The primary goal of TCL commands is to ensure the integrity and consistency of data when multiple statements need to be executed together as a single logical operation.
- There are three main TCL commands in SQL: `COMMIT`, `ROLLBACK` and `SAVEPOINT`.

1. `COMMIT`: The COMMIT command is used to **permanently save the changes made within a transaction to the database**. When a COMMIT is executed, all the changes made by the statements within the transaction are written to the database, and the transaction is completed successfully.

Example:
```sql
-- Example: Commit the changes made within the current transaction.
COMMIT;
```

2. `ROLLBACK`: The ROLLBACK command is used to **undo the changes made within a transaction and return the database to its original state**. When a ROLLBACK is executed, all the changes made by the statements within the transaction are discarded, and the transaction is aborted.

Example:
```sql
-- Example: Rollback the changes made within the current transaction.
ROLLBACK;
```

3. `SAVEPOINT`: The `SAVEPOINT` command is used to set a point within a transaction to which you can later rollback if needed. SAVEPOINTs are useful when you want to undo only part of the changes made within a transaction without rolling back the entire transaction.

Example:
```sql
-- Example: Create a SAVEPOINT named 'sp1' within the current transaction.
SAVEPOINT sp1;
```

Transactions are essential for maintaining data integrity and consistency in a database. By using TCL commands like COMMIT and ROLLBACK, you can ensure that the changes made by a series of SQL statements are either permanently committed or entirely rolled back, depending on the success or failure of the transaction as a whole.

It's essential to use TCL commands judiciously and to handle transactions appropriately, especially when dealing with critical data operations or concurrent access to the database. Proper use of transactions helps prevent data corruption and ensures that the database remains in a valid and consistent state at all times.

TCL commands are used to manage transactions within the database. A transaction is a sequence of one or more database operations that need to be executed as a single unit of work, ensuring data consistency and integrity.



Example of a TCL command:
```sql
BEGIN; -- Start a transaction
UPDATE employees SET salary = salary + 500 WHERE department = 'HR';
SAVEPOINT sp1; -- Set a savepoint
UPDATE employees SET salary = salary + 300 WHERE department = 'Finance';
ROLLBACK TO sp1; -- Rollback to the savepoint
COMMIT; -- End the transaction and save changes
```

More examples of using TCL (Transaction Control Language) commands in SQL:

1. COMMIT:

```sql
-- Example: Commit the changes made within the current transaction.
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE account_id = 101;
UPDATE accounts SET balance = balance + 100 WHERE account_id = 102;
COMMIT;
```

In this example, we use the `COMMIT` command to permanently save the changes made within the transaction. The transaction starts with the `BEGIN TRANSACTION` statement and includes two `UPDATE` statements that debit $100 from account 101 and credit $100 to account 102. The `COMMIT` command ensures that both `UPDATE` statements are successfully executed as a single unit of work. If there are no errors, the changes are committed to the database.

2. ROLLBACK:

```sql
-- Example: Rollback the changes made within the current transaction.
BEGIN TRANSACTION;
UPDATE inventory SET quantity = quantity - 5 WHERE product_id = 201;
UPDATE orders SET status = 'FAILED' WHERE order_id = 301;
ROLLBACK;
```

In this example, we use the `ROLLBACK` command to undo the changes made within the transaction. The transaction starts with the `BEGIN TRANSACTION` statement and includes two `UPDATE` statements that decrement the inventory quantity for product 201 and mark order 301 as 'FAILED.' However, something went wrong, and we want to cancel both updates and restore the database to its original state.

3. SAVEPOINT:

```sql
-- Example: Use a SAVEPOINT to set a point within the transaction.
BEGIN TRANSACTION;
UPDATE employees SET salary = salary * 1.1 WHERE department = 'IT';
SAVEPOINT sp1;
UPDATE employees SET salary = salary * 1.05 WHERE department = 'HR';
ROLLBACK TO SAVEPOINT sp1;
COMMIT;
```

In this example, we use the `SAVEPOINT` command to create a point named 'sp1' within the transaction. The transaction includes two `UPDATE` statements that increase the salary for employees in the IT department and HR department. However, after the second update, we decide to rollback to the 'sp1' savepoint to cancel the changes made to the HR department's salaries. The `COMMIT` command saves the changes made to the IT department's salaries, and the database is updated accordingly.

Remember that TCL commands are essential for managing transactions and ensuring data integrity. It's crucial to use them judiciously to maintain the consistency and validity of the data in the database. Additionally, the specific syntax and behavior of TCL commands may vary between different database management systems (DBMS). Always refer to the documentation of your specific DBMS for the correct usage of TCL commands.


4. AUTOCOMMIT
- In the context of Transaction Control Language (TCL) in SQL, `AUTOCOMMIT` refers to a feature that automatically commits each SQL statement as soon as it is executed.
- When `AUTOCOMMIT` is enabled, every individual SQL statement forms a transaction, and that transaction is automatically committed (permanently saved to the database) as soon as the statement is executed successfully.
- By default, most database management systems have `AUTOCOMMIT` enabled. It means that when you execute an SQL statement, such as an `INSERT`, `UPDATE`, or `DELETE`, the changes are immediately made permanent in the database without the need to explicitly commit the transaction.

For example, in a typical scenario with `AUTOCOMMIT` enabled:

```sql
-- Enable AUTOCOMMIT (It's usually enabled by default)
SET AUTOCOMMIT ON;

-- Execute an SQL statement
INSERT INTO employees (emp_id, emp_name) VALUES (101, 'John');

-- The above statement is automatically committed and changes are saved to the database.
```

However, in some situations, you may want to manage transactions manually by disabling `AUTOCOMMIT`. This allows you to group multiple SQL statements into a single transaction and explicitly control when the transaction should be committed or rolled back.

To disable `AUTOCOMMIT`, you can use the following command:

```sql
SET AUTOCOMMIT OFF;
```

After disabling `AUTOCOMMIT`, you need to explicitly commit the transaction using the `COMMIT` command or roll back the transaction using the `ROLLBACK` command.

```sql
-- Disable AUTOCOMMIT
SET AUTOCOMMIT OFF;

-- Start a transaction
BEGIN;

-- Execute multiple SQL statements
INSERT INTO employees (emp_id, emp_name) VALUES (101, 'John');
UPDATE employees SET emp_name = 'Alice' WHERE emp_id = 101;

-- Commit the transaction
COMMIT;
```

In summary, `AUTOCOMMIT` in TCL allows SQL statements to be automatically committed as soon as they are executed, making each statement its own transaction. If you need more control over transactions, you can disable `AUTOCOMMIT` and manually manage transactions using `COMMIT` and `ROLLBACK` commands.



## 5. DQL (Data Query Language):

DQL commands are used to query and retrieve data from the database. Although not an official SQL category, DQL is commonly used to refer to commands used for data retrieval.

Common DQL commands include:
- `SELECT`: Used to retrieve data from one or more database tables.

Example of a DQL command:
```sql
SELECT id, name, age FROM students WHERE age > 20;
```

In summary, SQL commands are categorized into DDL, DML, DCL, and TCL based on their respective purposes: defining and managing the database structure, manipulating data, controlling user access and permissions, and managing transactions. Additionally, DQL commands are used to query and retrieve data from the database. Understanding these categories is essential for effectively managing databases and performing various data operations in SQL.


## 6. SUB-QUERY

- A subquery, also known as a nested query or inner query, is a query that is embedded within another SQL query.
- Subqueries are used to retrieve data from one or more tables based on the results of another query. They can be a powerful tool for performing complex queries and data manipulation in SQL.
- Subqueries are used to break down complex tasks into smaller steps and are often employed within SELECT, INSERT, UPDATE, and DELETE statements.

- The syntax for using a sub-query is:
``` 
SELECT <COLUMN NAMES> FROM TABLE_NAME WHERE COLUMN (= or <> or IN or NOT IN) (SELECT COLUMN_NAME FROM <TABLE_NAME> WHERE <CONDITIONS>)
```

Let's look at an example to understand how subqueries work:

Consider a database with two tables: `employees` and `departments`.

Table: employees

| emp_id | emp_name | emp_salary | dept_id |
|--------|----------|------------|---------|
| 101    | John     | 50000      | 1       |
| 102    | Alice    | 45000      | 2       |
| 103    | Bob      | 60000      | 1       |
| 104    | Mary     | 55000      | 3       |

Table: departments

| dept_id | dept_name |
|---------|-----------|
| 1       | IT        |
| 2       | HR        |
| 3       | Finance   |

Example 1: Simple Subquery

Suppose we want to retrieve the names of employees who work in the "IT" department. We can achieve this using a subquery as follows:

```sql
SELECT emp_name
FROM employees
WHERE dept_id = (SELECT dept_id FROM departments WHERE dept_name = 'IT');
```

In this example, the subquery `(SELECT dept_id FROM departments WHERE dept_name = 'IT')` retrieves the department ID for the "IT" department. The outer query then selects the `emp_name` from the `employees` table for those employees whose `dept_id` matches the result of the subquery.

Example 2: Subquery with Aggregate Function

Let's find the average salary of employees in the "Finance" department:

```sql
SELECT AVG(emp_salary) AS avg_salary
FROM employees
WHERE dept_id = (SELECT dept_id FROM departments WHERE dept_name = 'Finance');
```

In this example, the subquery `(SELECT dept_id FROM departments WHERE dept_name = 'Finance')` gets the department ID for the "Finance" department. The outer query then uses this department ID to calculate the average salary of employees in that department using the `AVG()` aggregate function.

These are just a few simple examples of how subqueries can be used in SQL. Subqueries can be nested within each other or combined with other SQL clauses like `IN`, `NOT IN`, `EXISTS`, `ALL`, `ANY`, etc., to perform more complex data retrieval and manipulation tasks.



## 7. TABLE COPY

- Table copy in SQL refers to the process of duplicating the data and structure of an existing table to create a new table.
- This is often done when you want to work with a copy of the original data without modifying the original table.
- Table copy can be useful for various purposes, such as creating backup copies, performing data analysis, or testing changes without affecting the original data.

There are different ways to copy a table in SQL, depending on the database management system (DBMS) you are using. Here, I'll provide examples for two common ways to copy a table:

1. Using CREATE TABLE AS SELECT (CTAS):

The `CREATE TABLE AS SELECT` (CTAS) statement allows you to create a new table based on the results of a SELECT query. It copies both the data and the structure of the original table to the new table.

For example, let's say we have a table called `employees` with columns `emp_id`, `emp_name`, and `emp_salary`, and we want to create a copy of this table:

```sql
CREATE TABLE employees_copy AS
SELECT * FROM employees;
```

In this example, the `employees_copy` table will be created with the same columns and data as the `employees` table.

2. Using INSERT INTO SELECT:

Another way to copy a table is to use the `INSERT INTO SELECT` statement. This method allows you to insert data from an existing table into a new table with the same structure.

```sql
CREATE TABLE employees_copy (
    emp_id INT,
    emp_name VARCHAR(50),
    emp_salary DECIMAL(10, 2)
);

INSERT INTO employees_copy
SELECT * FROM employees;
```

In this example, we first create an empty table called `employees_copy` with the same structure as the `employees` table. Then, we use the `INSERT INTO SELECT` statement to insert data from the `employees` table into the new table.

Both methods achieve the same result of copying the data and structure of the original table to a new table. The choice between them depends on your specific requirements and the database system you are using.

Give examples of the following commands:
1. CREATE TABLE <TABLE_NAME> AS (SELECT (*/LIST OF COLUMNS) FROM TABLE_NAME);
2. INSERT INTO <TABLE_NAME> SELECT (*/LIST OF COLUMNS) FROM TABLE_NAME;


Here are examples of the given SQL commands:

1. `CREATE TABLE <TABLE_NAME> AS (SELECT (*/LIST OF COLUMNS) FROM TABLE_NAME);`

Example: Creating a new table called `employees_copy` with a subset of columns from the `employees` table:

```sql
CREATE TABLE employees_copy AS
SELECT emp_id, emp_name, emp_salary
FROM employees;
```

In this example, the `employees_copy` table will be created with columns `emp_id`, `emp_name`, and `emp_salary`, and it will contain the same data as the `employees` table, but only for the selected columns.

2. `INSERT INTO <TABLE_NAME> SELECT (*/LIST OF COLUMNS) FROM TABLE_NAME;`

Example: Inserting data into the `employees_copy` table from the `employees` table:

```sql
INSERT INTO employees_copy (emp_id, emp_name, emp_salary)
SELECT emp_id, emp_name, emp_salary
FROM employees;
```

In this example, the `employees_copy` table must already exist with the same structure as the `employees` table. The `INSERT INTO SELECT` statement copies the data from the `employees` table into the `employees_copy` table for the specified columns.

These examples demonstrate how to use `CREATE TABLE AS SELECT` and `INSERT INTO SELECT` to copy data from an existing table into a new table or a table with an already defined structure. The difference between the two lies in whether you are creating a new table or inserting data into an existing one.


## 8. JOINS

In SQL, a join is a mechanism that allows you to combine rows from two or more tables based on related columns. Joins are fundamental for querying and retrieving data from multiple tables in a relational database. They help establish relationships between tables and provide a way to access data across different tables using a single query.


### 4 TYPES - INNER,LEFT,RIGHT,CROSS 

- `INNER JOIN`: The most common type of join. It returns only the rows where there is a match in both tables based on the specified condition.

`SELECT <COLUMN/S> FROM <TABLE_NAME1> INNER JOIN <TABLE_NAME2> ON/WHERE/USING <JOIN CONDITION>;`

We'll use a simple scenario of `INNER JOIN` with two tables: `Customers` and `Orders`.

**Customers Table:**
| customer_id | first_name | last_name |
|-------------|------------|-----------|
| 1           | John       | Smith     |
| 2           | Jane       | Doe       |
| 3           | Michael    | Johnson   |

**Orders Table:**
| order_id | customer_id | order_date | total_amount |
|----------|-------------|------------|--------------|
| 101      | 1           | 2023-04-15 | 150.00       |
| 102      | 2           | 2023-04-20 | 200.00       |

Now, let's use an `INNER JOIN` to retrieve the customer's first name, last name, order ID, order date, and total amount for customers who have placed orders:

```sql
SELECT Customers.first_name, Customers.last_name, Orders.order_id, Orders.order_date, Orders.total_amount
FROM Customers
INNER JOIN Orders ON Customers.customer_id = Orders.customer_id;
```

In this query:
- We use the `INNER JOIN` clause to combine the `Customers` and `Orders` tables based on the matching `customer_id` column.
- The `ON` keyword specifies the condition for joining the tables (`Customers.customer_id = Orders.customer_id`).
- The `SELECT` statement retrieves the first name, last name from the `Customers` table, and order ID, order date, and total amount from the `Orders` table.

The output will look like:

| first_name | last_name | order_id | order_date | total_amount |
|------------|-----------|----------|------------|--------------|
| John       | Smith     | 101      | 2023-04-15 | 150.00       |
| Jane       | Doe       | 102      | 2023-04-20 | 200.00       |

In this output, we can see the information for customers who have placed orders, where the data from both tables is combined based on the common `customer_id` column.

- `LEFT JOIN` or (`LEFT OUTER JOIN`): Returns all the rows from the left table and the matching rows from the right table. If there is no match in the right table, NULL values are returned for the columns from the right table.

`SELECT <COLUMN/S> FROM <TABLE_NAME1> LEFT JOIN <TABLE_NAME2> ON/WHERE/USING <JOIN CONDITION>;`

In SQL, `LEFT JOIN` and `LEFT OUTER JOIN` are essentially the same and can be used interchangeably. Both of these phrases refer to the same type of join operation. The `OUTER` keyword is optional and doesn't change the functionality of the join.

Both `LEFT JOIN` and `LEFT OUTER JOIN` perform the following operation:

- They retrieve all records from the left table (the table mentioned before the `LEFT JOIN` clause) and the matching records from the right table (the table mentioned after the `LEFT JOIN` clause).
- If there is no match for a record in the left table, the columns from the right table will contain NULL values.

We'll use `LEFT JOIN` and `LEFT OUTER JOIN` to give the same result:

Assume we have two tables, `Customers` and `Orders`:

**Customers Table:**
| customer_id | first_name | last_name |
|-------------|------------|-----------|
| 1           | John       | Smith     |
| 2           | Jane       | Doe       |

**Orders Table:**
| order_id | customer_id | total_amount |
|----------|-------------|--------------|
| 101      | 1           | 150.00       |
| 102      | 3           | 200.00       |

Using `LEFT JOIN`:
```sql
SELECT Customers.first_name, Customers.last_name, Orders.order_id, Orders.total_amount
FROM Customers
LEFT JOIN Orders ON Customers.customer_id = Orders.customer_id;
```

Using `LEFT OUTER JOIN`:
```sql
SELECT Customers.first_name, Customers.last_name, Orders.order_id, Orders.total_amount
FROM Customers
LEFT OUTER JOIN Orders ON Customers.customer_id = Orders.customer_id;
```

In both cases, the result will be:

| first_name | last_name | order_id | total_amount |
|------------|-----------|----------|--------------|
| John       | Smith     | 101      | 150.00       |
| Jane       | Doe       | NULL     | NULL         |

As you can see, both `LEFT JOIN` and `LEFT OUTER JOIN` return the same result, where all records from the left table (`Customers`) are returned along with matching records from the right table (`Orders`). If there's no match in the right table, the columns from the right table will contain NULL values.

- `RIGHT JOIN` or ((`RIGHT OUTER JOIN`): ): Similar to the LEFT JOIN, but returns all the rows from the right table and the matching rows from the left table.

`SELECT <COLUMN/S> FROM <TABLE_NAME1> RIGHT JOIN <TABLE_NAME2> ON/WHERE/USING <JOIN CONDITION>;`

We'll perform a `RIGHT JOIN` using the same example with the `Customers` and `Orders` tables:

**Customers Table:**
| customer_id | first_name | last_name |
|-------------|------------|-----------|
| 1           | John       | Smith     |
| 2           | Jane       | Doe       |

**Orders Table:**
| order_id | customer_id | total_amount |
|----------|-------------|--------------|
| 101      | 1           | 150.00       |
| 102      | 3           | 200.00       |

Using `RIGHT JOIN` (which is also known as `RIGHT OUTER JOIN`):

```sql
SELECT Customers.first_name, Customers.last_name, Orders.order_id, Orders.total_amount
FROM Customers
RIGHT JOIN Orders ON Customers.customer_id = Orders.customer_id;
```

Expected Result:

| first_name | last_name | order_id | total_amount |
|------------|-----------|----------|--------------|
| John       | Smith     | 101      | 150.00       |
| NULL       | NULL      | 102      | 200.00       |

In this `RIGHT JOIN` example:
- All records from the right table (`Orders`) are returned along with matching records from the left table (`Customers`).
- If there's no match in the left table, the columns from the left table will contain NULL values.

In this specific example, since there's no customer with `customer_id` 3 in the `Customers` table, the resulting record has NULL values for `first_name` and `last_name` from the `Customers` table.

- `CROSS JOIN`: Returns the Cartesian product of two tables, i.e., all possible combinations of rows from both tables.

`SELECT <COLUMN/S> FROM <TABLE_NAME1> CROSS JOIN <TABLE_NAME2>;`

A `CROSS JOIN`, also known as a Cartesian product, combines each row from one table with every row from another table. It doesn't require any specific conditions for joining; it simply creates all possible combinations of rows from both tables. Here's an example using two simple tables: `Colors` and `Sizes`.

**Colors Table:**
| color_id | color_name |
|----------|------------|
| 1        | Red        |
| 2        | Blue       |

**Sizes Table:**
| size_id | size_name |
|---------|-----------|
| 1       | Small     |
| 2       | Medium    |

Using `CROSS JOIN`:
```sql
SELECT Colors.color_name, Sizes.size_name
FROM Colors
CROSS JOIN Sizes;
```

Expected Result:

| color_name | size_name |
|------------|-----------|
| Red        | Small     |
| Red        | Medium    |
| Blue       | Small     |
| Blue       | Medium    |

In this example:
- The `CROSS JOIN` combines every row from the `Colors` table with every row from the `Sizes` table.
- The result is a combination of all possible colors and sizes.

Keep in mind that `CROSS JOIN` can generate a large number of rows if both tables have many records. It's important to use it with caution and ensure it's used appropriately for your specific use case.

- `FULL JOIN (or FULL OUTER JOIN)`: Returns all the rows from both tables, along with the matching rows. If there is no match in either table, NULL values are returned for the columns from the table without a match.

Let's perform a `FULL JOIN` (also known as a `FULL OUTER JOIN`) using an example with two tables: `Customers` and `Orders`.

**Customers Table:**
| customer_id | first_name | last_name |
|-------------|------------|-----------|
| 1           | John       | Smith     |
| 2           | Jane       | Doe       |
| 3           | Michael    | Johnson   |

**Orders Table:**
| order_id | customer_id | total_amount |
|----------|-------------|--------------|
| 101      | 1           | 150.00       |
| 102      | 2           | 200.00       |

Using `FULL JOIN` (or `FULL OUTER JOIN`):

```sql
SELECT Customers.first_name, Customers.last_name, Orders.order_id, Orders.total_amount
FROM Customers
FULL JOIN Orders ON Customers.customer_id = Orders.customer_id;
```

Expected Result:

| first_name | last_name | order_id | total_amount |
|------------|-----------|----------|--------------|
| John       | Smith     | 101      | 150.00       |
| Jane       | Doe       | 102      | 200.00       |
| Michael    | Johnson   | NULL     | NULL         |

In this example:
- The `FULL JOIN` combines all records from both the `Customers` and `Orders` tables.
- If there's a match, the columns from both tables are combined based on the matching `customer_id`.
- If there's no match for a customer in the `Orders` table or an order in the `Customers` table, the respective columns will contain NULL values.

The result includes all customers and their orders, and customers without orders or orders without customers.

- `SELF JOIN`: A self join is a type of SQL join operation in which a table is joined with itself. In other words, you treat a single table as if it were two separate tables and then perform a regular join operation between these two "virtual" tables. A self join is often used to establish relationships between rows within the same table based on related columns.

```
SELECT alias1.column_name, alias2.column_name
FROM table_name alias1
JOIN table_name alias2 ON alias1.join_condition = alias2.join_condition;
```

Let's perform a self join using an example with the `Employees` table, where we'll find the manager for each employee. Here's the data:

**Employees Table:**
| emp_id | first_name | last_name | manager_id |
|--------|------------|-----------|------------|
| 1      | John       | Smith     | NULL       |
| 2      | Jane       | Doe       | 1          |
| 3      | Michael    | Johnson   | 1          |
| 4      | Emily      | Brown     | 2          |

Using a self join to find employees and their managers:

```sql
SELECT e1.first_name AS employee, e2.first_name AS manager
FROM Employees e1
LEFT JOIN Employees e2 ON e1.manager_id = e2.emp_id;
```

Expected Result:

| employee | manager  |
|----------|----------|
| John     | NULL     |
| Jane     | John     |
| Michael  | John     |
| Emily    | Jane     |

In this example:
- We use a self join by creating two aliases (`e1` and `e2`) of the `Employees` table.
- The `LEFT JOIN` condition links the employee's `manager_id` with the manager's `emp_id`.
- The query retrieves the first name of employees and the first name of their respective managers.

The result shows employees along with their corresponding managers. John has no manager (`manager_id` is NULL), and the other employees have managers based on their `manager_id`.

- `NATURAL JOIN`: A `NATURAL JOIN` is a type of join operation that automatically matches columns with the same name from two tables. It's a shorthand way to join tables based on columns that share the same name without explicitly specifying the columns to join on. Here's an example using two simple tables: `Employees` and `Departments`.

**Employees Table:**
| emp_id | first_name | last_name | department_id |
|--------|------------|-----------|---------------|
| 1      | John       | Smith     | 101           |
| 2      | Jane       | Doe       | 102           |
| 3      | Michael    | Johnson   | 101           |
| 4      | Emily      | Brown     | 103           |

**Departments Table:**
| department_id | department_name |
|---------------|-----------------|
| 101           | HR              |
| 102           | Finance         |
| 103           | Marketing       |

Using `NATURAL JOIN`:

```sql
SELECT emp_id, first_name, last_name, department_name
FROM Employees
NATURAL JOIN Departments;
```

Expected Result:

| emp_id | first_name | last_name | department_name |
|--------|------------|-----------|-----------------|
| 1      | John       | Smith     | HR              |
| 2      | Jane       | Doe       | Finance         |
| 3      | Michael    | Johnson   | HR              |

In this example:
- The `NATURAL JOIN` automatically matches columns with the same name (`department_id`) in both tables (`Employees` and `Departments`).
- It performs an inner join based on the matched columns.
- The resulting table includes only the matched rows, and the duplicate column (`department_id`) is removed from the output.

Please note that the use of `NATURAL JOIN` might be limited in certain scenarios, especially when working with more complex database schemas or when columns have the same name but different meanings in the context of the tables. It's important to carefully consider the use of `NATURAL JOIN` and ensure that it aligns with your data and query requirements.

The other available `JOINS` in MYSQL are:

- INNER STRAIGHT_JOIN
- CROSS STRAIGHT_JOIN
- NATURAL JOIN table_factor
- NATURAL INNER LEFT JOIN
- NATURAL INNER RIGHT JOIN
- NATURAL OUTER JOIN



## 9. UNION

The UNION function in SQL is used to combine the result sets of two or more SELECT queries into a single result set, removing duplicate rows. It's particularly useful when you want to merge data from different tables or queries that have the same structure.

The basic syntax of the UNION operation is as follows:

```sql
SELECT columns FROM table1
UNION
SELECT columns FROM table2;
```

Key points to understand about the UNION function:

1. **Column Matching:** The SELECT statements within the UNION operation must have the same number of columns, and the corresponding columns must have compatible data types.

2. **Duplicate Removal:** By default, the UNION operation removes duplicate rows from the result set. If you want to include duplicates, you can use the UNION ALL keyword.

3. **Order of Results:** The order of rows in the result set is not guaranteed to be in any specific order unless you use an ORDER BY clause.

Here's a simple example to illustrate how UNION works:

Suppose you have two tables: "Employees" and "Contractors." Both tables have the same structure with columns "first_name" and "last_name."

```sql
-- Query 1
SELECT first_name, last_name
FROM Employees

UNION

-- Query 2
SELECT first_name, last_name
FROM Contractors;
```

In this example, the result of the UNION operation will combine the first names and last names from both the "Employees" and "Contractors" tables, removing any duplicates. If you use UNION ALL instead of UNION, duplicates will be retained.

Keep in mind that the columns and their data types must match between the SELECT statements. If they don't, you might need to use aliases or convert data types as needed.

UNION is a powerful tool for combining data from different sources and simplifying the process of querying and retrieving merged results.

In SQL, the `UNION` operator is used to combine the result sets of two or more `SELECT` queries into a single result set. The `UNION` operator removes duplicate rows from the final result set, making it useful for combining data from different tables or for merging data from similar tables.

There are a few key points to note about the `UNION` operator:

1. The number of columns and their data types in all the `SELECT` queries must be the same. If the column names are not the same, you can use aliases to ensure the column names in the final result set are clear.

2. The order of the columns in the `SELECT` queries must also be the same.

Syntax:
```
SELECT column1, column2, ...
FROM table1
UNION
SELECT column1, column2, ...
FROM table2;
```

Example:

Consider two tables: `employees` and `contractors`.

Table: employees

| emp_id | emp_name | dept_id |
|--------|----------|---------|
| 1      | John     | 101     |
| 2      | Alice    | 102     |
| 3      | Bob      | 101     |

Table: contractors

| emp_id | emp_name | dept_id |
|--------|----------|---------|
| 101    | Dave     | 103     |
| 102    | Eve      | 102     |
| 103    | Grace    | 101     |

Example: Using UNION

```sql
SELECT emp_id, emp_name, dept_id
FROM employees
UNION
SELECT emp_id, emp_name, dept_id
FROM contractors;
```

In this example, the `UNION` operator is used to combine the result sets of two `SELECT` queries from the `employees` and `contractors` tables. The final result set will contain all distinct rows from both tables, excluding any duplicate rows. The column names and data types are the same in both `SELECT` queries, which allows them to be combined using the `UNION` operator.

The result will be:

| emp_id | emp_name | dept_id |
|--------|----------|---------|
| 1      | John     | 101     |
| 2      | Alice    | 102     |
| 3      | Bob      | 101     |
| 101    | Dave     | 103     |
| 102    | Eve      | 102     |
| 103    | Grace    | 101     |

As you can see, the `UNION` operator merges the data from both tables, ensuring that duplicate rows are removed, and presents a single combined result set.
 


## 10. CASE, WHEN, END:

In SQL, the `CASE` expression is used for conditional logic. It allows you to perform different actions based on conditions within a query. The `CASE` expression can be used in both the `SELECT` and `UPDATE` statements to determine values or perform actions based on specified conditions.

The general syntax of the `CASE` expression is as follows:

```sql
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    ...
    ELSE default_result
END
```

Here's when the `CASE` expression is commonly used:

1. **In the SELECT Statement:** The `CASE` expression is often used in the `SELECT` statement to create computed columns or customize the output of the query. It allows you to transform data based on different conditions. For example, you can use it to assign labels or categories to data, calculate new values, or create conditional aggregations.

2. **In the UPDATE Statement:** The `CASE` expression can also be used in the `UPDATE` statement to conditionally modify values in a column. This is useful when you want to update specific rows based on certain conditions. You can use the `CASE` expression in combination with the `SET` clause to determine the new value to assign to a column based on different conditions.

3. **In Other SQL Statements:** The `CASE` expression can also be used in other SQL statements where conditional logic is required. For example, it can be used within the `WHERE` clause to filter rows based on conditions, or in combination with other statements to achieve specific outcomes.

Remember that the `CASE` expression allows you to evaluate multiple conditions and return different values based on those conditions. The `CASE` expression ends with `END`, indicating the conclusion of the conditional logic.

A simple example of using the `CASE` expression in a `SELECT` statement:

```sql
SELECT
    customer_name,
    CASE
        WHEN registration_date < '2023-01-01' THEN 'OLD'
        ELSE 'NEW'
    END AS "Registration Status"
FROM customers;
```

In this example, the `CASE` expression determines the "Registration Status" based on the registration date of customers. If the registration date is before January 1, 2023, the status is 'OLD', otherwise, it's 'NEW'.

Let's look at more examples of using the `CASE` expression with both the `SELECT` and `UPDATE` commands:

**Example 1: Using CASE in SELECT:**

Assume you have a `Students` table with columns `student_id`, `first_name`, `last_name`, and `grade`. You want to categorize students based on their grades:

```sql
SELECT
    student_id,
    first_name,
    last_name,
    grade,
    CASE
        WHEN grade >= 90 THEN 'A'
        WHEN grade >= 80 THEN 'B'
        WHEN grade >= 70 THEN 'C'
        ELSE 'D'
    END AS grade_category
FROM Students;
```

In this example, the `CASE` expression categorizes students based on their grades into 'A', 'B', 'C', or 'D' categories.

**Example 2: Using CASE in UPDATE:**

Assume you have a `Employees` table with columns `employee_id`, `first_name`, `last_name`, and `years_of_service`. You want to update the `salary` column based on years of service:

```sql
UPDATE Employees
SET salary = 
    CASE
        WHEN years_of_service >= 5 THEN salary * 1.1
        ELSE salary
    END;
```

In this example, the `CASE` expression increases the salary by 10% for employees with 5 or more years of service.

**Example 3: Using CASE with Multiple Conditions:**

Assume you have an `Orders` table with columns `order_id`, `order_date`, and `order_status`. You want to identify orders as 'On Time', 'Delayed', or 'Pending' based on their order status and order date:

```sql
SELECT
    order_id,
    order_date,
    order_status,
    CASE
        WHEN order_status = 'Shipped' AND order_date <= '2023-08-31' THEN 'On Time'
        WHEN order_status = 'Shipped' AND order_date > '2023-08-31' THEN 'Delayed'
        ELSE 'Pending'
    END AS delivery_status
FROM Orders;
```

In this example, the `CASE` expression categorizes orders into different delivery statuses based on their order status and order date.

Remember that the `CASE` expression is a powerful tool for implementing conditional logic within SQL queries. It allows you to handle various scenarios and customize the output or perform actions based on conditions.

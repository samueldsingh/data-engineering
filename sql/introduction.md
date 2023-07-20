8i7# Introduction

## 1. What is DBMS and RDBMS?

DBMS (Database Management System):

A Database Management System (DBMS) is a software system that allows users to interact with a database. It provides a set of tools and functionalities to store, retrieve, update, and manage data efficiently and securely. The main purpose of a DBMS is to provide an organized and structured way to manage data, ensuring data integrity, consistency, and security. Some key features of a DBMS include:

1. Data Organization: DBMS provides methods to organize data into tables, rows, and columns, creating a structured representation of data.

2. Data Retrieval: Users can query the database to retrieve specific data based on certain conditions using SQL (Structured Query Language).

3. Data Manipulation: DBMS allows users to insert, update, and delete data in the database, ensuring data integrity and consistency.

4. Data Security: DBMS provides access control mechanisms to secure data from unauthorized access and ensure data privacy.

5. Data Concurrency: DBMS handles multiple user access to the data concurrently, preventing conflicts and maintaining data consistency.

6. Data Recovery: DBMS has built-in mechanisms for data backup and recovery, protecting data from accidental loss or corruption.

RDBMS (Relational Database Management System):

RDBMS is a type of DBMS that manages data in a relational database model. In the relational model, data is organized into tables with rows and columns, and relationships between tables are established using keys. The key feature of RDBMS is the ability to enforce relationships and constraints between tables through the use of primary keys, foreign keys, and other integrity constraints. Some popular RDBMSs include MySQL, PostgreSQL, Oracle, Microsoft SQL Server, and SQLite.

Key characteristics of RDBMS:

1. Tabular Structure: Data is represented in tables, where each table consists of rows (records) and columns (attributes).

2. Data Integrity: RDBMS enforces integrity constraints such as primary keys, unique keys, foreign keys, and check constraints to maintain data accuracy and consistency.

3. SQL Support: RDBMS uses SQL to perform operations on data, making it easy for users to interact with the database.

4. Normalization: RDBMS encourages data normalization to eliminate data redundancy and improve data integrity.

5. ACID Properties: RDBMS follows ACID properties (Atomicity, Consistency, Isolation, Durability) to ensure data transactions are reliable and recoverable.

6. Data Relationships: RDBMS allows the establishment of relationships between tables using keys, enabling efficient data retrieval through joins.

In summary, both DBMS and RDBMS are software systems used to manage data, but RDBMS is a specific type of DBMS that follows the relational model, providing structured data organization and enforcing data relationships through keys and integrity constraints.

## 2. Examples of DBMS and RDBMS:

Here are examples of both DBMS and RDBMS:

DBMS (Database Management System):

1. MongoDB: MongoDB is a popular NoSQL database management system that stores data in a flexible JSON-like format called BSON (Binary JSON). It is designed for handling large volumes of unstructured or semi-structured data and is commonly used in modern web applications.

2. Couchbase: Couchbase is a NoSQL database management system that supports both document-oriented and key-value data models. It is known for its high performance and scalability and is used in applications that require fast data access and low-latency response times.

3. Redis: Redis is an in-memory data structure store that can function as a database, cache, and message broker. It is widely used for caching frequently accessed data and supporting real-time data analytics.

RDBMS (Relational Database Management System):

1. MySQL: MySQL is an open-source relational database management system known for its speed, reliability, and ease of use. It is widely used in web applications and is the default database for popular content management systems like WordPress.

2. PostgreSQL: PostgreSQL is an advanced open-source relational database management system that supports a wide range of features, including custom data types, full-text search, and geospatial data. It is known for its extensibility and adherence to SQL standards.

3. Oracle Database: Oracle Database is a commercial relational database management system developed by Oracle Corporation. It is one of the most popular RDBMS used in enterprise applications and large-scale systems, known for its scalability and high performance.

4. Microsoft SQL Server: SQL Server is a relational database management system developed by Microsoft. It is commonly used in Windows-based environments and integrates well with Microsoft's development tools and products.

5. SQLite: SQLite is a lightweight, serverless, and self-contained relational database management system. It is commonly used in mobile applications, embedded systems, and as a local database for desktop applications.

6. IBM Db2: Db2 is a family of data management products developed by IBM. It is known for its integration with IBM's mainframe systems and is used in enterprise-level applications.

These examples represent a small subset of the many database management systems available, each with its own strengths and best-suited use cases. The choice of a particular DBMS or RDBMS depends on the specific requirements of the application, the complexity of data, scalability needs, and other factors.


## 3. Explain what are ACID properties
ACID properties are a set of four key characteristics that ensure the reliability and consistency of transactions in a database system. These properties are essential for maintaining data integrity and providing a robust environment for data management. The term "ACID" stands for Atomicity, Consistency, Isolation, and Durability. Let's explore each of these properties in detail:

1. Atomicity:
Atomicity ensures that a transaction is treated as a single, indivisible unit of work. It means that either all the operations within a transaction are successfully completed, or none of them are. If any part of the transaction fails, the entire transaction is rolled back, and the database is left unchanged. This property ensures that the database remains in a consistent state, and partial updates are not allowed.

2. Consistency:
Consistency guarantees that a transaction brings the database from one consistent state to another consistent state. In other words, the database must adhere to a set of predefined rules or constraints before and after a transaction. If a transaction violates any of these rules, the entire transaction is rolled back, and the database remains unchanged. Consistency ensures that data remains accurate and valid throughout the transaction.

3. Isolation:
Isolation ensures that concurrent transactions are executed independently of each other. It prevents interference between transactions and ensures that each transaction sees the database in a consistent state. Transactions are executed as if they were the only ones running on the system, even when multiple transactions are happening simultaneously. This property prevents issues like data corruption and ensures data integrity even in a multi-user environment.

4. Durability:
Durability guarantees that once a transaction is committed, its effects are permanent and will survive any subsequent system failures, such as power outages or crashes. The changes made by a committed transaction are stored in non-volatile memory (usually disk storage) and remain in the database even in the event of a system failure. This property ensures that data is not lost, providing a high level of reliability and recoverability.

The ACID properties are crucial for maintaining data integrity, consistency, and reliability in database management systems. These properties ensure that transactions are executed reliably and that the database remains in a consistent and accurate state even in the presence of failures or concurrent access by multiple users.


## 4. Explain the differences betweeen database and a schema
Database and schema are related concepts in the field of database management, but they refer to different aspects of organizing and managing data:

**1. Database:**
A database is a collection of related data that is organized and structured to be stored, accessed, and managed efficiently. It can be thought of as a container that holds tables, views, procedures, and other objects that represent data and define its relationships. Databases are designed to manage large volumes of data and provide a structured way to store, retrieve, update, and delete information.

In the context of database management systems (DBMS), a database is a physical or logical container that stores data in files on disk or in-memory structures. Databases can be relational (RDBMS), NoSQL, graph-based, or other types, each offering specific data storage and retrieval mechanisms suited to different use cases.

For example, you might have a database named "CompanyDB" that contains tables for employees, departments, and projects, all related to the operations of a company.

**2. Schema:**
A schema, on the other hand, defines the structure and organization of the database. It is a *logical blueprint* that outlines the layout of the database, including the tables, their columns, data types, relationships, and constraints. The schema provides a clear definition of how data is stored and how different pieces of information are related to each other.

In a relational database management system (RDBMS), a schema is a collection of database objects, including tables, views, indexes, stored procedures, and other elements that define the database structure. A schema can be considered as a namespace that groups related database objects together.

For example, within the "CompanyDB" database, you might have different schemas like "HumanResources" and "Finance," each containing tables and views related to their respective departments.

In summary, a database is a container that holds related data, while a schema is a logical blueprint that defines the structure and organization of the database. The schema provides a way to organize and categorize the database objects, making it easier to manage and maintain the data within the database.


## 5. Explain DDL, DML, DCL, TCL and DQL.

In SQL (Structured Query Language), different types of commands are used to interact with databases and manage data. These commands are categorized into four main groups based on their functionality: DDL, DML, DCL, and TCL. Additionally, there is a subset called DQL, which is not an official category but is commonly used to refer to commands used for querying data. Let's explain each category:

**1. DDL (Data Definition Language):**
DDL commands are used to define and manage the structure of the database. They are responsible for creating, altering, and dropping database objects like tables, views, indexes, and schemas. DDL commands do not manipulate the data itself but rather modify the database's structure and schema.


Common DDL commands include:
- `CREATE`: Used to create database objects like tables, views, indexes, etc.
- `ALTER`: Used to modify the structure of existing database objects.
- `DROP`: Used to delete database objects from the database.
- `TRUNCATE`: Used to remove all data from a table (similar to `DELETE`, but faster).


**Examples:**


**CREATE**

Use **CREATE** command to perform the following operations:
a. CREATE a DATABASE - CREATE DATABASE <DB_NAME>;
b. CREATE a TABLE - CREATE TABLE <TABLE_NAME> (<COLUMN NAME> <TYPE>(<Field Length/SIZE>));
c. CREATE a VIEW - CREATE {OR REPLACE} VIEW <VIEW_NAME> AS <SELECT STATMENT>;


**a. Create a database**

```
CREATE DATABASE SampleDB;
```

Double-click the db name in the SCHEMAS list in the sidebar to set the db to default db.


**b. Insert tables**

```
CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(100),
    salary DECIMAL(10, 2)
);
```


**c. Create a view:**

In MySQL, a view is a virtual table that is derived from the result of a SELECT query. It does not store data itself but represents a stored query that can be used as if it were a real table. Views allow you to simplify complex queries, encapsulate logic, and provide an additional layer of security by restricting direct access to underlying tables. Some key points about views in MySQL are:

Definition (query using  SELECT, INSERT, UPDATE, and DELETE statements), simplify complex queries (views once created for complex query stays unaffected), data abstraction (underlying complexity of the tables are hidden), security (limit users' access to specific columns or rows), Read-Only and Updatable Views (can be either read-only or updatable), performance (do not store data; they are merely stored queries.slight performance overhead).


```
CREATE VIEW EmployeeDetails AS
SELECT emp_id, first_name, last_name, department, salary
FROM Employees
WHERE department = 'HR';
```


**Explain DESC <TABLE_NAME> and USE <schema_name>**

The MySQL command `DESC <TABLE_NAME>;` is used to retrieve information about the columns (field names) and their data types of a specific table in the currently selected database. The `USE <schema_name>;` command is used to select or switch to a particular database or schema. 


Example:
```
DESC employeedetails
```



The `DESC employees`; command provides information about each column in the `employees` table. It shows the column name, data type, whether the column allows NULL values, if the column is part of the primary key (PRI), default value, and any extra information.


The `USE company_db`; command selects the `company_db` database, and all subsequent queries will be executed within this database until another database is selected.

In summary, the DESC <TABLE_NAME>; command is used to describe the structure of a specific table, and the USE <schema_name>; command is used to switch to a particular database before executing queries on its tables.

**ALTER**

*-- ALTER USED TO ADD/MODIFY/DROP INDEXES/CONSTARINTS.*

In SQL, the `ALTER` command is used to modify the structure of an existing database object, such as a table, view, or database itself. It allows you to add, modify, or delete columns, change data types, rename objects, and perform various other changes to adapt the database schema to evolving requirements.

The `ALTER` command is versatile and provides several subcommands that are specific to the type of object being altered. The main subcommands used with `ALTER` are:

a. `ALTER TABLE`: Used to modify the structure of a table.
b. `ALTER VIEW`: Used to modify the definition of a view.
c. `ALTER DATABASE`: Used to modify database-level properties and settings.

Here are some common uses of the `ALTER` command for each subcommand:

a. `ALTER TABLE`:

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

b. `ALTER VIEW`:

   - Modifying the definition of a view:
     ```sql
     ALTER VIEW view_name AS
     SELECT column1, column2, ...
     FROM table_name
     WHERE condition;
     ```

c. `ALTER DATABASE`:

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

It's important to note that not all alterations may be allowed, depending on the specific database management system and the existing constraints or dependencies within the database. Also, some database systems might have additional specific subcommands or restrictions for certain alterations.

Before using the `ALTER` command, make sure to back up your data and review the potential consequences of the changes, as some alterations might affect the existing data or require additional maintenance steps.

Use **ALTER** to perform the following operations:

a. ALTER TABLE NAME (RENAME) - ALTER TABLE <TABLE_NAME> RENAME TO <NEW_TABLE_NAME>;
b. ALTER TABLE : ADD COLUMN - ALTER TABLE <TABLE_NAME> ADD <COLUMN_NAME> <TYPE(SIZE)>;
-- Use, (COMMA) with to Add Multiple Columns
c. ALTER TABLE : RENAME COLUMN - ALTER TABLE <TABLE_NAME> RENAME COLUMN <OLD_COLUMN_NAME> TO <NEW_COLUMN_NAME>; -- Use, (COMMA) with full RENAME COLUMN to Change multiple Columns
d. ALTER TABLE : DROP COLUMN - ALTER TABLE <TABLE_NAME> DROP COLUMN <COLUMN_NAME>;
e. ALTER TABLE : MODIFY THE TYPE/SIZE OF COLUMN - ALTER TABLE <TABLE_NAME> MODIFY COLUMN <COLUMN_NAME> <NEW_TYPE/(NEW_SIZE)>;
f. ALTER VIEW - ALTER VIEW <VIEW_NAME> AS <SELECT STATMENT>; -- Later
g. ALTER VIEW (RENAME) - ALTER TABLE <VIEW_NAME> RENAME TO <NEW_VIEW_NAME>; -- Not Working
	or RENAME TABLE <OLD_VIEW_NAME> to <NEW_VIEW_NAME>;

Here are examples of using the `ALTER` command for various operations:

a. ALTER TABLE NAME (RENAME):

```sql
-- Assuming we have a table named "employees" and we want to rename it to "staff"
ALTER TABLE employees RENAME TO staff;
```

b. ALTER TABLE: ADD COLUMN (with multiple columns):

```sql
-- Assuming we have a table named "students" and we want to add two new columns: "age" (INT) and "address" (VARCHAR)
ALTER TABLE students ADD age INT, ADD address VARCHAR(100);
```

c. ALTER TABLE: RENAME COLUMN (with multiple columns):

```sql
-- Assuming we have a table named "employees" and we want to rename the columns "fname" to "first_name" and "lname" to "last_name"
ALTER TABLE employees RENAME COLUMN fname TO first_name, RENAME COLUMN lname TO last_name;
```

d. ALTER TABLE: DROP COLUMN:

```sql
-- Assuming we have a table named "products" and we want to drop the column "obsolete"
ALTER TABLE products DROP COLUMN obsolete;
```

e. ALTER TABLE: MODIFY THE TYPE/SIZE OF COLUMN:

```sql
-- Assuming we have a table named "orders" and we want to change the data type of the "quantity" column to DECIMAL(8,2)
ALTER TABLE orders MODIFY COLUMN quantity DECIMAL(8,2);
```

f. ALTER VIEW:

```sql
-- Assuming we have a view named "high_salary_employees" and we want to change its definition to include employees with salaries above 50000
ALTER VIEW high_salary_employees AS
SELECT emp_id, first_name, last_name, salary
FROM employees
WHERE salary > 50000;
```

g. ALTER VIEW (RENAME) - Note that renaming a view directly using `ALTER VIEW` is not supported in MySQL. Instead, you can use the `RENAME TABLE` command:

```sql
-- Assuming we have a view named "old_view" and we want to rename it to "new_view"
RENAME TABLE old_view TO new_view;
```

These are some examples of using the `ALTER` command in MySQL to modify tables and views, including renaming, adding, modifying, and dropping columns, as well as modifying the definition of views. Always be cautious when using the `ALTER` command, as it can have significant impacts on the database structure and data. Ensure you have a backup of your data before performing any alterations.


DROP -
1. DROP TABLE - DROP TABLE {IF EXISTS} <TABLE_NAME>;
2. DROP COLUMN - ALTER TABLE <TABLE_NAME> DROP COLUMN <COLUMN_NAME>;
3. DROP VIEW -  DROP VIEW {IF EXISTS} <VIEW_NAME>;

RENAME -
1. RENAME TABLE - RENAME TABLE <TABLE_NAME> to <NEW_TABLE_NAME>;
2. RENAME VIEW - RENAME TABLE <VIEW_NAME> to <NEW_VIEW_NAME>;
3. RENAME COLUMN - ALTER TABLE <TABLE_NAME> RENAME COLUMN <OLD_COLUMN_NAME> TO <NEW_COLUMN_NAME>;

TRUNCATE - (DROP+CREATE)
1. TRUNCATE TABLE - TRUNCATE TABLE <TABLE_NAME>;

COMMENT - 
1. CREATE TABLE WITH COMMENT - CREATE TABLE <TABLE_NAME> (<COLUMN NAME> <TYPE>(<Field Length/SIZE>)) COMMENT = '<Comment description>';
2. ADD A COMMENT TO AN EXISTING TABLE. - ALTER TABLE <TABLE_NAME> COMMENT = '<Comment description>';
3. DROP A COMMENT - ALTER TABLE <TABLE_NAME> COMMENT = ''; -- Leave it Empty
4. UPDATE A COMMENT TO AN EXISTING TABLE. - ALTER TABLE <TABLE_NAME> COMMENT = '<Updated comment description>';

**2. DML (Data Manipulation Language):**
DML commands are used to manipulate data within the database. They allow you to insert, update, and delete data in the database tables.

Common DML commands include:
- `INSERT`: Used to add new records into a table.
- `UPDATE`: Used to modify existing records in a table.
- `DELETE`: Used to remove records from a table.

Example of a DML command:
```sql
INSERT INTO students (id, name, age)
VALUES (1, 'John Doe', 25);
```

**3. DCL (Data Control Language):**
DCL commands are used to manage the access and permissions of database objects. They control the authorization of users and define their privileges on the database.

Common DCL commands include:
- `GRANT`: Used to give users specific privileges on database objects.
- `REVOKE`: Used to revoke previously granted privileges.

Example of a DCL command:
```sql
GRANT SELECT, INSERT ON students TO user1;
```

**4. TCL (Transaction Control Language):**
TCL commands are used to manage transactions within the database. A transaction is a sequence of one or more database operations that need to be executed as a single unit of work, ensuring data consistency and integrity.

Common TCL commands include:
- `COMMIT`: Used to permanently save changes made by a transaction.
- `ROLLBACK`: Used to undo the changes made by a transaction and revert the database to its previous state.
- `SAVEPOINT`: Used to set a savepoint within a transaction, allowing partial rollback.

Example of a TCL command:
```sql
BEGIN; -- Start a transaction
UPDATE employees SET salary = salary + 500 WHERE department = 'HR';
SAVEPOINT sp1; -- Set a savepoint
UPDATE employees SET salary = salary + 300 WHERE department = 'Finance';
ROLLBACK TO sp1; -- Rollback to the savepoint
COMMIT; -- End the transaction and save changes
```

**5. DQL (Data Query Language):**
DQL commands are used to query and retrieve data from the database. Although not an official SQL category, DQL is commonly used to refer to commands used for data retrieval.

Common DQL commands include:
- `SELECT`: Used to retrieve data from one or more database tables.

Example of a DQL command:
```sql
SELECT id, name, age FROM students WHERE age > 20;
```

In summary, SQL commands are categorized into DDL, DML, DCL, and TCL based on their respective purposes: defining and managing the database structure, manipulating data, controlling user access and permissions, and managing transactions. Additionally, DQL commands are used to query and retrieve data from the database. Understanding these categories is essential for effectively managing databases and performing various data operations in SQL.

```MySQL password : sam@1234```


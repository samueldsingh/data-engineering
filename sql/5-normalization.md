
## Dimensional modelling

Dimensional modeling is an adaptation of the relational model specifically for data warehouses. It’s optimized for OLAP type of 
queries that aim to analyze rather than update. To do this, it uses the star schema. The schema of a dimensional model tends to be 
easy to interpret and extend. 

**Elements of dimensional modeling**
Dimensional models are made up of two types of tables: fact and dimension tables. What the fact table holds is decided by the business use-case. 
It contains records of a key metric, and this metric changes often. Fact tables also hold foreign keys to dimension tables. Dimension tables 
hold descriptions of specific attributes and these do not change as often.

**Star schema**
The star schema is the simplest form of the dimensional model. Some use the terms “star schema” and “dimensional model” interchangeably. 
The star schema is made up of two tables: fact and dimension tables. **Fact tables** hold records of metrics that are described 
further by **dimension tables**.

**Snowflake schema**
The snowflake schema is an extension of the star schema. The fact table is the same, but the way the dimension tables are structured is different
and the dimension tables are split up into even more tables.

**Same fact table, different dimensions**
The star schema extends one dimension, while the snowflake schema extends over more than one dimension. This is because the dimension tables are normalized.

**What is normalization?**
Normalization is a technique that divides tables into smaller tables and connects them via relationships. The goal is to reduce redundancy and 
increase data integrity. So how does this happen? The basic idea is to **identify repeating groups of data and create new tables for them**.

**Adding foreign keys**
Foreign key references are essential to both the snowflake and star schema. When creating either of these schemas, correctly setting up the 
foreign keys is vital because they connect dimensions to the fact table. They also enforce a one-to-many relationship, because unless 
otherwise specified, a foreign key can appear more than once in a table and primary key can appear only once.

**Why would we want to normalize a database?**
Normalization saves space. Denormalized structure enables a lot of data redundancy.

Normalization ensures better data integrity through its design. First, it enforces data consistency. Data entry can get messy, and at times 
people will fill out fields differently. Secondly, because duplicates are reduced, modification of any data becomes safer and simpler. 
Lastly, since tables are smaller and organized more by object, its easier to alter the database schema.

**Pros and cons of normalization**
Then there are the pros and cons of normalization. Now normalization seems appealing, especially for database maintenance. However, normalization 
requires a lot more joins making queries more complicated, which can make indexing and reading of data slower. Deciding between normalization and 
denormalization comes down to how read- or write- intensive your database is going to be.

The goals of normalization are to:
- to be able to characterize the level of redundancy in a relational schema
- Provide mechanisms for transforming schemas in order to remove redundancy

Normalization is the process of organizing data in a relational database to reduce redundancy and improve data integrity. It involves dividing a database into two or more tables and defining relationships between the tables. Normalization follows a set of rules, often referred to as normal forms, to ensure data is organized efficiently.

**1NF (First Normal Form):**
- Eliminates repeating groups by putting each value in a column.
- Ensures that every column contains atomic (indivisible) values.
- Each row has a unique identifier (primary key).

Example:

Consider a table named "Students" with the following columns: StudentID (Primary Key), Name, Courses.
```
| StudentID | Name      | Courses                 |
|-----------|-----------|-------------------------|
| 1         | Alice     | Math, Physics           |
| 2         | Bob       | Chemistry               |
| 3         | Carol     | Math, Biology, History  |
```
This table violates 1NF because the "Courses" column contains a repeating group of values. It should be split into a separate table to achieve 1NF.

**2NF (Second Normal Form):**
- Meets all the requirements of 1NF.
- All non-key attributes are fully functionally dependent on the entire primary key (no partial dependencies).

Example:

Consider a table named "Orders" with the following columns: OrderID (Primary Key), ProductID (Partial Key), CustomerID (Partial Key), Quantity.
```
| OrderID | ProductID | CustomerID | Quantity |
|---------|-----------|------------|----------|
| 1       | A         | 101        | 5        |
| 2       | B         | 101        | 3        |
| 3       | A         | 102        | 2        |
| 4       | C         | 103        | 4        |
```
In this table, "ProductID" and "CustomerID" together form the primary key, but "Quantity" is dependent only on "ProductID," not on the entire key. This violates 2NF, and to achieve 2NF, we need to split the table into "OrderDetails" (OrderID, ProductID, Quantity) and "Customers" (CustomerID, CustomerName) tables.

**3NF (Third Normal Form):**
- Meets all the requirements of 2NF.
- All non-key attributes are functionally dependent only on the primary key (no transitive dependencies).

Example:

Consider a table named "Employees" with the following columns: EmployeeID (Primary Key), DepartmentID, DepartmentName, ManagerName.
```
| EmployeeID | DepartmentID | DepartmentName | ManagerName |
|------------|--------------|-----------------|-------------|
| 101        | 1            | HR              | John        |
| 102        | 2            | Sales           | Mary        |
| 103        | 1            | HR              | John        |
| 104        | 3            | Finance         | Jane        |
```
In this table, "ManagerName" is dependent on "DepartmentName," which is not part of the primary key. This represents a transitive dependency and violates 3NF. To achieve 3NF, we need to split the table into "Employees" (EmployeeID, DepartmentID) and "Departments" (DepartmentID, DepartmentName, ManagerName) tables.


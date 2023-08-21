
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
further by **dimension tables**. The fact table and the dimension table share a one to many relationship.

**Snowflake schema**

The snowflake schema is an extension of the star schema. The fact table is the same, but the way the dimension tables are structured is different
and the dimension tables are split up into even more tables. 

**Same fact table, different dimensions**

The star schema extends one dimension, while the snowflake schema extends over more than one dimension. This is because the dimension tables are normalized.

**What is normalization?**

Normalization is a technique that divides tables into smaller tables and connects them via relationships. The goal is to reduce redundancy and 
increase data integrity. So how does this happen? The basic idea is to **identify repeating groups of data and create new tables for them**.

**Adding foreign keys**

- Foreign key references are essential to both the snowflake and star schema. When creating either of these schemas, correctly setting up the 
foreign keys is vital because they connect dimensions to the fact table.
- They also enforce a one-to-many relationship, because unless 
otherwise specified, a foreign key can appear more than once in a table and primary key can appear only once.
- Foreign keys are added to ensure data consistency when new data is inserted into the database.

**Why would we want to normalize a database?**

Normalization saves space. Denormalized structure enables a lot of data redundancy.

Normalization ensures better data integrity through its design. First, it enforces data consistency. Data entry can get messy, and at times 
people will fill out fields differently. Secondly, because duplicates are reduced, modification of any data becomes safer and simpler. 
Lastly, since tables are smaller and organized more by object, its easier to alter the database schema.

**Difference between normalized and denormalized databases**:
- Normalization requires much more joins than denormalized tables considering they have more tables which means slower performance.
- Denormalized tables enable **data redundancy** whereas normalized table eliminates **data redundancy**.
- Normalization ensures better data integrity through its design. During data entry, duplicates can easily identified and reduced.
- Secondly, because duplicates are reduced, modification of any data becomes safer and simpler.
- Since tables are smaller and organized more by object, its easier to alter the database schema.
- Extending the snowflake schema while ensuring data consistency is much easier.

**Pros and cons of normalization**

Normalization seems appealing, especially for database maintenance. However, normalization 
requires a lot more joins making queries more complicated, which can make indexing and reading of data slower. Deciding between normalization and 
denormalization comes down to how read- or write- intensive your database is going to be.

OLTP is write-intensive meaning we’re updating and writing often. Normalization makes sense because we want to add data quickly and consistently.

OLAP is read-intensive because we’re running analytics on the data. This means we want to prioritize quicker read queries. Remember how much more joins the normalized query had over the denormalized query? OLAP should avoid that.

The goals of normalization are to:

- to be able to characterize the level of redundancy in a relational schema
- Provide mechanisms for transforming schemas in order to remove redundancy

Normalization is the process of organizing data in a relational database to reduce redundancy and improve data integrity. It involves dividing a database into two or more tables and defining relationships between the tables. Normalization follows a set of rules, often referred to as normal forms, to ensure data is organized efficiently.

**Different levels of normal form**:

There are different extents to which you can normalize. These are called normal forms. Below is a list of them from least to most normalized. Each has its own set of rules, and some build on top of each other. 

- First normal form (1NF)
- Second normal form (2NF)
- Third normal form (3NF)
- Elementary key normal form (EKNF)
- Boyce-Codd normal form (BCNF)
- Fourth normal form (4NF)
- Essential tuple normal form (ETF)
- Fifth normal form (5NF)
- Domain-key Normal Form (DKNF)
- Sixth normal form (6NF)

**1NF (First Normal Form):**

To comply with 1NF, each record must be unique and each cell must hold one value. After performing 1NF, all the records will be unique and each column will have one value.

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

Second Normal Form (2NF) is a database normalization concept that builds upon the foundation of the First Normal Form (1NF). It addresses certain types of data redundancy that can exist in a relational database table. The primary goal of 2NF is to eliminate partial dependencies between non-key attributes and primary key attributes.

A table is said to be in Second Normal Form (2NF) if it meets the following criteria:

1. It is already in First Normal Form (1NF).
2. All non-key attributes are functionally dependent on the entire primary key.

In simpler terms, 2NF ensures that each non-key attribute (attribute that is not part of the primary key) is fully functionally dependent on the entire primary key, rather than on only a part of the key.

Here's a brief explanation using an example:

Consider a table called "Orders" with columns `order_id`, `customer_id`, `product_id`, and `product_description`. The primary key is `order_id`, and the combination of `order_id` and `product_id` is a composite key.

| order_id | customer_id | product_id | product_description |
|----------|-------------|------------|---------------------|
| 1        | 101         | 001        | Product A           |
| 1        | 101         | 002        | Product B           |
| 2        | 102         | 001        | Product A           |

In this example, the table is not in 2NF because the `product_description` attribute is partially dependent on only the `product_id` part of the composite key. It means that the same product description can appear in multiple rows due to different customers, even though the product is the same.

To bring the table into 2NF, you could split the table into two separate tables: "Orders" and "Products," where the product information is stored separately, and the dependency between non-key attributes and the primary key is maintained.

2NF helps to further reduce data redundancy and anomalies in the database, contributing to better data integrity and maintainability. It's important to note that while striving for normalization is important, over-normalization can lead to increased complexity in query design and performance concerns. The appropriate level of normalization depends on the specific needs and characteristics of the data and the application.

**3NF (Third Normal Form):**

Third Normal Form (3NF) is a database normalization concept that builds upon the principles of First Normal Form (1NF) and Second Normal Form (2NF). It aims to eliminate transitive dependencies between non-key attributes and primary key attributes in a relational database table. The primary goal of 3NF is to further reduce data redundancy and ensure data integrity by removing undesirable dependencies.

A table is considered to be in Third Normal Form (3NF) if it satisfies the following conditions:

1. It is already in First Normal Form (1NF) and Second Normal Form (2NF).
2. All non-key attributes are functionally dependent only on the primary key.

In simpler terms, 3NF ensures that there are no transitive dependencies where non-key attributes depend on other non-key attributes within the same table.

Here's an example to help illustrate the concept:

Consider a table called "Employees" with columns `employee_id`, `department_id`, `department_name`, and `employee_name`. The primary key is `employee_id`.

| employee_id | department_id | department_name | employee_name |
|-------------|---------------|-----------------|---------------|
| 101         | 1             | HR              | John          |
| 102         | 2             | Finance         | Jane          |
| 103         | 1             | HR              | Alice         |

In this example, the table is not in 3NF because the `department_name` attribute depends on the `department_id`, which is not part of the primary key. There's a transitive dependency between `department_name` and `department_id`.

To bring the table into 3NF, you could create a separate table for departments and link it to the "Employees" table using the `department_id` as a foreign key. This eliminates the transitive dependency and ensures that each non-key attribute depends solely on the primary key.

3NF helps to further improve data integrity and reduce anomalies by minimizing redundancy and ensuring that non-key attributes have clear, direct dependencies on the primary key. Like other normalization forms, the decision to implement 3NF should be based on the specific characteristics and requirements of the data and the application.

**Data Anomalies**:

A database that isn’t normalized enough is prone to three types of anomaly errors: update, insertion, and deletion.

**Update anomaly**

An update anomaly is a data inconsistency that can arise when updating a database with redundancy.

**Insertion anomaly**

An insertion anomaly is when you are unable to add a new record due to missing attributes.

**Deletion anomaly**

A deletion anomaly happens when you delete a record and unintentionally delete other data. 

**Data anomalies**

The more normalized the database, the less prone it will be to these anomalies. For example, most 3NF tables can’t have an update, insertion, and deletion anomalies. This makes normalization sound great. But, don’t forget the downsides of normalization as well — those long queries.

**Difference between Normalized and Denormalized databases**:

Normalized and denormalized tables are two different approaches to designing a relational database schema. Each approach has its own advantages and disadvantages, and the choice between them depends on factors such as data integrity, query performance, and maintenance.

**Normalized Tables:**
Normalization is a database design technique that involves breaking down a table into smaller related tables to eliminate data redundancy and maintain data integrity. The aim is to reduce data duplication by organizing data into separate tables with well-defined relationships. The process involves dividing a table into multiple smaller tables and linking them using foreign keys.

Advantages of Normalized Tables:
- Reduced data redundancy: Data is stored only once, reducing the risk of inconsistencies.
- Improved data integrity: Updates and modifications are less likely to result in anomalies.
- Easier maintenance: Changes are made in one place, reducing the risk of errors.
- More efficient storage: Smaller tables require less storage space.

Disadvantages of Normalized Tables:
- More complex queries: Retrieving data often requires joining multiple tables, which can lead to complex queries.
- Performance issues: Joins can slow down query performance, especially in complex queries with large datasets.

**Denormalized Tables:**
Denormalization involves combining related tables into a single table to improve query performance by reducing the need for joins. This approach sacrifices some level of data redundancy and integrity for the sake of faster querying.

Advantages of Denormalized Tables:
- Improved query performance: Fewer joins result in faster query execution.
- Simplified queries: Complex joins are reduced or eliminated, making queries simpler to write.
- Better suited for read-heavy applications: Applications with more frequent read operations benefit from faster retrieval.

Disadvantages of Denormalized Tables:
- Increased data redundancy: Data can be duplicated, leading to potential inconsistencies.
- Maintenance challenges: Updates and modifications need to be carefully managed to avoid inconsistencies.
- Larger storage requirements: Duplicated data requires more storage space.

**Choosing Between Normalized and Denormalized Tables:**
- Use normalized tables when data integrity and consistency are of utmost importance, such as in transactional systems.
- Use denormalized tables when read performance is a top priority, such as in reporting or analytics applications.
- Consider a hybrid approach: Depending on the specific requirements of your application, you might choose to denormalize certain tables for performance while keeping others normalized for data integrity.

It's important to note that there is no one-size-fits-all solution. The choice between normalized and denormalized tables should be made based on the specific needs of your application and the trade-offs you're willing to make between data integrity and performance.

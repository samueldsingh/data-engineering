
## Dimensional modelling

Dimensional modeling is an adaptation of the relational model specifically for data warehouses. It’s optimized for OLAP type of 
queries that aim to analyze rather than update. To do this, it uses the star schema. The schema of a dimensional model tends to be 
easy to interpret and extend. 

## 1. Elements of dimensional modeling

Dimensional models are made up of two types of tables: fact and dimension tables. What the fact table holds is decided by the business use-case. 
It contains records of a key metric, and this metric changes often. Fact tables also hold foreign keys to dimension tables. Dimension tables 
hold descriptions of specific attributes and these do not change as often.

**Star schema**

- The star schema is the simplest form of the dimensional model. Some use the terms “star schema” and “dimensional model” interchangeably. 
The star schema is made up of two tables: fact and dimension tables. 

- **Fact tables** hold records of metrics that are described further by **dimension tables**. The fact table and the dimension table share a one to many relationship.

**Snowflake schema**

The snowflake schema is an extension of the star schema. The fact table is the same, but the way the dimension tables are structured is different
and the dimension tables are split up into even more tables. 

**Same fact table, different dimensions**

The star schema extends one dimension, while the snowflake schema extends over more than one dimension. This is because the dimension tables are normalized.


## 2. What is normalization?

- Normalization is a technique that divides tables into smaller tables and connects them via relationships.
- The goal is to reduce redundancy and increase data integrity. So how does this happen? The basic idea is to **identify repeating groups of data and create new tables for them**.
- The aim is to reduce data duplication by organizing data into separate tables with well-defined relationships.
- The process involves dividing a table into multiple smaller tables and linking them using foreign keys.
- Normalization follows a set of rules, often referred to as normal forms, to ensure data is organized efficiently.


**Why would we want to normalize a database?**

- Normalization saves space. Denormalized structure enables a lot of data redundancy.
- Normalization ensures better data integrity through its design.
- First, it enforces data consistency. Data entry can get messy, and at times people will fill out fields differently.
- Secondly, because duplicates are reduced, modification of any data becomes safer and simpler. 
- Lastly, since tables are smaller and organized more by object, its easier to alter the database schema.

**Advantages and Disadvantages:**

Normalization seems appealing, especially for database maintenance. However, normalization 
requires a lot more joins making queries more complicated, which can make indexing and reading of data slower. Deciding between normalization and 
denormalization comes down to how read- or write- intensive your database is going to be.

OLTP is write-intensive meaning we’re updating and writing often. Normalization makes sense because we want to add data quickly and consistently.

OLAP is read-intensive because we’re running analytics on the data. This means we want to prioritize quicker read queries. Remember how much more joins the normalized query had over the denormalized query? OLAP should avoid that.


Advantages of Normalized Tables:
- Reduced data redundancy: Data is stored only once, reducing the risk of inconsistencies.
- Improved data integrity: Updates and modifications are less likely to result in anomalies.
- Easier maintenance: Changes are made in one place, reducing the risk of errors.
- More efficient storage: Smaller tables require less storage space.
- Eliminate data anomaly: Insert anomaly, Update anomaly, Delete anomaly.

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
- Data anomaly: like insert anomaly, update anomaly and delete anomaly are more frequent.


**Choosing Between Normalized and Denormalized Tables:**
- Use normalized tables when data integrity and consistency are of utmost importance, such as in transactional systems.
- Use denormalized tables when read performance is a top priority, such as in reporting or analytics applications.
- Use normalized tables when building simpler small scale applications that are easier to manage and when you want a flexible application that needs an update more often than required.
- If you want to ensure that data insert, updates and delete do not result in data inconsistencies, use normalization.
- Consider a hybrid approach: Depending on the specific requirements of your application, you might choose to denormalize certain tables for performance while keeping others normalized for data integrity.
- For reporting and analytics, where query performance is a primary concern, denormalized tables can significantly improve query response times by reducing the need for complex joins.
- Offline processing, where data is extracted, transformed and loaded, denormalized tables can speed up ETL process.
- When infrequent updates to the application is needed, use denormalized tables.

It's important to note that there is no one-size-fits-all solution. The choice between normalized and denormalized tables should be made based on the specific needs of your application and the trade-offs you're willing to make between data integrity and performance.

**Difference between normalized and denormalized databases**:

Normalized and denormalized databases are two contrasting approaches to designing the structure of a relational database. Each approach has its own advantages and trade-offs based on factors such as data integrity, query performance, and storage efficiency. Here's a comparison of normalized and denormalized databases:

**Normalized Databases:**

1. **Minimize Data Redundancy:** Normalized databases aim to eliminate data redundancy by organizing data into separate tables and linking them with relationships (foreign keys). Each piece of data is stored only once.

2. **Data Integrity:** Normalization helps maintain data integrity by reducing the chances of inconsistent or duplicate data. Updates are made in a single place, reducing the risk of anomalies.

3. **Flexibility:** Changes to data are easier to manage because modifications are typically localized to individual tables.

4. **Smaller Storage:** Normalized databases often require less storage space since data redundancy is minimized.

5. **Efficient Updates:** Updates to data in normalized databases are generally more efficient due to the smaller data size and fewer affected rows.

6. **Complex Joins:** Normalized databases may require multiple joins to retrieve related data, which can affect query performance.

**Denormalized Databases:**

1. **Data Redundancy:** Denormalized databases intentionally introduce controlled data redundancy by combining data from multiple tables into a single table. This can improve query performance but might lead to data integrity challenges.

2. **Query Performance:** Denormalization can lead to faster query performance since data is already consolidated in a single table, reducing the need for complex joins.

3. **Simplified Queries:** Queries can be simpler and require fewer joins in denormalized databases.

4. **Aggregation and Reporting:** Denormalization is often favored for reporting and analytics scenarios where complex queries need to be executed quickly.

5. **Data Anomalies:** Data anomalies like update, insert, and delete anomalies can occur more frequently in denormalized databases due to the redundancy.

6. **Maintenance Complexity:** Updates to data in denormalized databases can be more complex and may require changes in multiple places.

7. **Increased Storage:** Denormalized databases can require more storage space due to the redundancy.

In practice, the choice between normalized and denormalized databases depends on the specific requirements of the application. Normalization is typically favored for transactional systems where data integrity is critical. Denormalization is often used in data warehousing and reporting systems where query performance is a priority and where the risk of data anomalies can be managed.

It's important to strike a balance between normalization and denormalization based on the needs of the application, understanding that there might be cases where a combination of both approaches is appropriate.

## 3. Adding foreign keys

- Foreign key references are essential to both the snowflake and star schema. When creating either of these schemas, correctly setting up the 
foreign keys is vital because they connect dimensions to the fact table.
- They also enforce a one-to-many relationship, because unless 
otherwise specified, a foreign key can appear more than once in a table and primary key can appear only once.
- Foreign keys are added to ensure data consistency when new data is inserted into the database.


## 4. Different levels of normal form:

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

1NF is like tidying up your data. Imagine you have a table of records, and each record has multiple values in a single cell. In 1NF, you break down those values into separate cells. This way, each cell contains a single, atomic value. No more cramming multiple things into one cell.

- Eliminates repeating groups by putting each value in a column.
- Ensures that every column contains atomic (indivisible) values.
- Each row has a unique identifier (primary key).

Example:

For example, consider a table named "Students" with the following columns: StudentID (Primary Key), Name, Courses.

| Student | Subjects        |
|---------|-----------------|
| Alice   | Math, History   |
| Bob     | Science, Music  |

This table violates 1NF because the "Courses" column contains a repeating group of values. It should be split into a separate table to achieve 1NF.

After 1NF, you would have:
| Student | Subject  |
|---------|----------|
| Alice   | Math     |
| Alice   | History  |
| Bob     | Science  |
| Bob     | Music    |



**2NF (Second Normal Form):**

Second Normal Form (2NF) is a database normalization concept that builds upon the foundation of the First Normal Form (1NF). It addresses certain types of data redundancy that can exist in a relational database table. The primary goal of 2NF is to eliminate partial dependencies between non-key attributes and primary key attributes.

- 2NF is about making sure each piece of data is in the right place. Imagine you have a table with multiple attributes, and some attributes depend only on part of the primary key.
- In 2NF, you separate those attributes into a new table, linked by their shared key. This reduces redundancy and ensures data is stored logically.

A table is said to be in Second Normal Form (2NF) if it meets the following criteria:

1. It is already in First Normal Form (1NF).
2. All non-key attributes are functionally dependent on the entire primary key.

In simpler terms, 2NF ensures that each non-key attribute (attribute that is not part of the primary key) is fully functionally dependent on the entire primary key, rather than on only a part of the key.

Here's a brief explanation using an example:

For example, consider:
| Student | Course  | Instructor |
|---------|---------|------------|
| Alice   | Math    | Mr. Smith  |
| Bob     | Science | Mr. Johnson|
| Alice   | History | Mr. Smith  |

In 2NF, you'd create two tables:
**Students:**
| Student |
|---------|
| Alice   |
| Bob     |

**Courses:**
| Student | Course  | Instructor |
|---------|---------|------------|
| Alice   | Math    | Mr. Smith  |
| Bob     | Science | Mr. Johnson|
| Alice   | History | Mr. Smith  |

Another Example:

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

- 3NF is about avoiding data duplication. Imagine you have attributes that are determined by other attributes.
- In 3NF, you move those attributes to a new table, linked by their own unique key. This reduces redundancy and keeps the data accurate.

Example for 3NF:

For example, consider:
| Student | Major      | Advisor |
|---------|------------|---------|
| Alice   | Math       | Dr. Lee |
| Bob     | Science    | Dr. Smith|
| Alice   | History    | Dr. Lee |
| Bob     | Chemistry  | Dr. Smith|

In 3NF, you'd create two tables:
**Students:**
| Student |
|---------|
| Alice   |
| Bob     |

**Majors:**
| Major     | Advisor   |
|-----------|-----------|
| Math      | Dr. Lee   |
| Science   | Dr. Smith |
| History   | Dr. Lee   |
| Chemistry | Dr. Smith |


Another example:

Consider a table called "Employees" with columns `employee_id`, `department_id`, `department_name`, and `employee_name`. The primary key is `employee_id`.

| employee_id | department_id | department_name | employee_name |
|-------------|---------------|-----------------|---------------|
| 101         | 1             | HR              | John          |
| 102         | 2             | Finance         | Jane          |
| 103         | 1             | HR              | Alice         |

In this example, the table is not in 3NF because the `department_name` attribute depends on the `department_id`, which is not part of the primary key. There's a transitive dependency between `department_name` and `department_id`.

To bring the table into 3NF, you could create a separate table for departments and link it to the "Employees" table using the `department_id` as a foreign key. This eliminates the transitive dependency and ensures that each non-key attribute depends solely on the primary key.

3NF helps to further improve data integrity and reduce anomalies by minimizing redundancy and ensuring that non-key attributes have clear, direct dependencies on the primary key. Like other normalization forms, the decision to implement 3NF should be based on the specific characteristics and requirements of the data and the application.



In simpler terms, 1NF makes your data neat, 2NF ensures data is in the right place, and 3NF eliminates data duplication. These normal forms help organize data, prevent errors, and make databases more efficient and reliable.

## 5. Data Anomalies:

- Data anomalies are issues that occur in a database when the data doesn't behave as expected due to problems with the database's structure, organization, or integrity.
- These anomalies can lead to incorrect, inconsistent, or misleading information
- A database that isn’t normalized enough is prone to three types of anomaly errors: update, insertion, and deletion.

**Insertion anomaly**

- An insertion anomaly is when you are unable to add a new record due to missing attributes.
- This can happen when the database structure isn't well-designed and doesn't handle new data properly.

Example:

Suppose you have a table for customer orders that includes customer details. If a new customer places an order, but their details aren't available in the customer table yet, you might face an insertion anomaly because you can't add the order without the customer information.

**Update anomaly**

Update anomalies occur when updating data in the database leads to inconsistencies or unexpected changes in other parts of the database. This can happen if data is duplicated or stored inappropriately.

Example:
Continuing from the previous example, if you have multiple entries for the same customer in the customer table because their name was spelled differently, updating one entry to correct the name might not update the others. This inconsistency can lead to confusion and errors.

**Deletion anomaly**

A deletion anomaly happens when you delete a record and unintentionally delete other data. 

Example:
Suppose you have a database with a teacher's information stored alongside the classes they teach. If a teacher teaches only one class and you delete that class's entry, you might unintentionally delete the teacher's information as well. This could leave gaps in the data and cause confusion.

**Data anomalies**

The more normalized the database, the less prone it will be to these anomalies. For example, most 3NF tables can’t have an update, insertion, and deletion anomalies. This makes normalization sound great. But, don’t forget the downsides of normalization as well — those long queries.

Data anomalies are undesirable because they undermine the reliability and accuracy of the database. Proper database design, including normalization, can help prevent these anomalies by structuring the data in a way that ensures data integrity, consistency, and accurate relationships between tables.

## 5. What are the relationships in RDBMS:

In relational database management systems (RDBMS), relationships define how data in different tables are related or linked together. Relationships are established using keys, typically primary keys and foreign keys, to maintain data integrity and ensure accurate associations between records in different tables. There are three main types of relationships in RDBMS:

1. **One-to-One Relationship (1:1):**
In a one-to-one relationship, each record in one table is related to one and only one record in another table, and vice versa. This type of relationship is not very common due to the potential for data redundancy. One-to-one relationships are used when you need to split data into separate tables for organizational reasons without introducing data redundancy.

Example:
Consider a database for an organization. You might have an "Employees" table and a "ContactInfo" table. Each employee has a single contact information record, and each contact information record corresponds to a specific employee.

2. **One-to-Many Relationship (1:N):**
In a one-to-many relationship, a record in one table is related to one or more records in another table, but each record in the second table is related to only one record in the first table. This is the most common type of relationship in relational databases.

Example:
Using the same "Employees" table, you could have a "Projects" table. Each employee can be assigned to multiple projects, but each project is associated with only one employee.

3. **Many-to-Many Relationship (N:M):**
In a many-to-many relationship, multiple records in one table are related to multiple records in another table. To implement a many-to-many relationship, you typically use an intermediate table, often called a junction or linking table, to map the associations between the two tables.

Example:
Consider a university database with a "Students" table and a "Courses" table. Since each student can enroll in multiple courses, and each course can have multiple students, you would create an intermediate "Enrollments" table to track which students are enrolled in which courses.

These relationships help maintain data consistency, prevent data duplication, and allow for efficient querying and retrieval of related data. They're a fundamental concept in relational databases and are critical for building well-structured, normalized database schemas.

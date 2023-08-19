
# Examples of  creating a relational database

How do you define a database schema when creating a relational database? How do you structure a database by breaking the data into separate tables (relational database) and form relationships between them using indexes and then construct select queries by joining tables to retrieve your data?

You can create a database schema using a process known as *normalization*.  There are three different relationships in relational databases:
1. One to one relationship
2. One to many relationship
3. Many to many relationship

In a Relational Database Management System (RDBMS), there are several types of relationships that can exist between tables. These relationships help establish the structure and integrity of the database. Here are the common types of relationships and their uses:

1. **One-to-One (1:1) Relationship**:
   - Each row in the first table is associated with exactly one row in the second table, and vice versa.
   - Used when you want to break down a table into smaller, related tables for better organization.
   - Example: A "Person" table linked to a "Passport" table.

2. **One-to-Many (1:N) Relationship**:
   - Each row in the first table can be associated with multiple rows in the second table, but each row in the second table is associated with only one row in the first table.
   - Used to represent hierarchical relationships or when one entity can have multiple related entities.
   - Example: An "Author" table linked to multiple "Book" records.

3. **Many-to-Many (N:N) Relationship**:
   - Each row in the first table can be associated with multiple rows in the second table, and vice versa.
   - Achieved by introducing a third table (junction table or associative entity) that contains the primary keys of both related tables.
   - Used to model complex relationships between entities.
   - Example: A "Student" table linked to multiple "Course" records, and vice versa.

4. **Self-Referential Relationship**:
   - A type of relationship where rows in a table are related to other rows within the same table.
   - Used to represent hierarchical or recursive relationships within a single table.
   - Example: An "Employee" table with a foreign key referencing the "Manager" column in the same table.

These relationships help maintain data integrity, eliminate data duplication, and ensure efficient querying of data. Properly defining and implementing relationships is essential for maintaining a well-structured and easily maintainable database schema.

SQL can then be used to retrieve information using the table joins. 

Some optimization techniques like use of indexes and denormalization using triggers can be used to create a lightining fast database.

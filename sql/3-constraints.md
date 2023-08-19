# CONSTRAINTS IN SQL

In SQL, constraints are rules and conditions that are applied to the data in a database table. Constraints ensure data integrity and enforce specific rules 
on the values stored in the table columns. They help maintain the consistency, accuracy, and validity of the data in the database.

Commonly used constraints in SQL include:

1. **PRIMARY KEY** Constraint: Ensures that **each row in a table has a unique identifier, and it cannot have NULL values**. Typically, the primary key is
   used to uniquely identify each record in the table.


2. **UNIQUE** Constraint: Ensures that the **values in a specific column or a combination of columns are unique across all rows in the table**. It allows
  each value to appear only once in the column.


3. **FOREIGN KEY** Constraint: Establishes a relationship between two tables, where the values in one table's column must match the values in another
   table's primary key column. This constraint ensures referential integrity between related tables.


4. **NOT NULL** Constraint: Ensures that a column cannot have NULL values. It requires all rows in the table to have a value in that column.


5. **CHECK** Constraint: Allows you to specify a condition that must be satisfied for each row in the table. It restricts the values that can be inserted
   or updated in a specific column.


6. **DEFAULT** Constraint: Sets a default value for a column if no value is explicitly provided during an insert operation.

7. **INDEX** Constraint: An index is a database object that provides a quick lookup of data based on the values in one or more columns of a table. It acts like
   a roadmap that allows the database engine to find specific rows efficiently without having to scan the entire table.

8. **AUTO INCREMENT** Constraint: An auto-increment constraint, also known as an auto-incrementing or identity column, is a database feature that automatically
   generates a unique, incremental value for a column when a new row is inserted into a table. 

9. **ENUM** Constraint: An ENUM constraint is used to define a custom data type that represents **a set of predefined constant values for a column**. It allows you to
    specify that a column can only take one of the specified values, and any attempt to insert a value outside the predefined set will result in an error.

Examples of using constraints:

```sql
-- Creating a table with constraints
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    department VARCHAR(50),
    salary DECIMAL(10, 2) DEFAULT 0.00,
    hire_date DATE,
    CONSTRAINT emp_unique_name UNIQUE (emp_name),
    CONSTRAINT fk_department FOREIGN KEY (department) REFERENCES departments(dept_name),
    CONSTRAINT chk_salary CHECK (salary >= 0)
);
```

In this example, the `employees` table has multiple constraints defined:
- `PRIMARY KEY` ensures that each `emp_id` is unique and serves as the primary identifier for each employee.
- `NOT NULL` ensures that `emp_name` must have a value in every row.
- `UNIQUE` ensures that each `emp_name` is unique across all rows in the table.
- `FOREIGN KEY` establishes a relationship between the `department` column and the `dept_name` column in the `departments` table.
- `CHECK` ensures that the `salary` column must have a non-negative value.


Creating a table with all the constraints:

Sure! Here's an example of how you can create a table with various constraints in SQL, including PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, CHECK, DEFAULT, INDEX, AUTO_INCREMENT, and ENUM.

```sql
CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE NOT NULL,
    total_amount DECIMAL(10, 2),
    status ENUM('Pending', 'Shipped', 'Delivered') DEFAULT 'Pending',
    CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    CONSTRAINT chk_total_amount CHECK (total_amount > 0),
    INDEX idx_order_date (order_date),
    UNIQUE (order_id)
);

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    city VARCHAR(50),
    CONSTRAINT ck_city CHECK (city IN ('New York', 'Los Angeles', 'Chicago')),
    CONSTRAINT df_name DEFAULT 'Unknown' FOR first_name
);
```

In this example:
- The `Orders` table has a primary key `order_id` with AUTO_INCREMENT, a foreign key `customer_id` referencing the `Customers` table, a NOT NULL constraint on `order_date`, a CHECK constraint on `total_amount`, an ENUM column `status`, an INDEX on `order_date`, and a UNIQUE constraint on `order_id`.
- The `Customers` table has a primary key `customer_id`, NOT NULL constraints on `first_name` and `last_name`, a UNIQUE constraint on `email`, a CHECK constraint on `city`, and a DEFAULT constraint on `first_name`.

Please note that the specific syntax and supported features may vary depending on the database system you are using (e.g., MySQL, PostgreSQL, SQL Server). Make sure to adjust the data types, constraint names, and other details according to your database system's syntax.

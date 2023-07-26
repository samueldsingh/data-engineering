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

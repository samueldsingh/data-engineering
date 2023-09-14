# CONSTRAINTS IN SQL

In SQL, constraints are rules and conditions that are applied to the data in a database table. Constraints ensure data integrity and enforce specific rules 
on the values stored in the table columns. They help maintain the consistency, accuracy, and validity of the data in the database.

Commonly used constraints in SQL include:

1. **PRIMARY KEY** Constraint: Ensures that **each row in a table has a unique identifier, and it cannot have NULL values**. Typically, the primary key is
   used to uniquely identify each record in the table. It is a combination of a NOT NULL and UNIQUE constraint.


2. **UNIQUE** Constraint: Ensures that the **values in a specific column or a combination of columns are unique across all rows in the table**. It allows
  each value to appear only once in the column.


3. **FOREIGN KEY** Constraint: Establishes a relationship between two tables, where the values in one table's column must match the values in another
   table's primary key column. This constraint ensures referential integrity between related tables. It prevents actions that would destroy links between tables.


4. **NOT NULL** Constraint: Ensures that a column cannot have NULL values. It requires all rows in the table to have a value in that column.


5. **CHECK** Constraint: Allows you to specify a condition that must be satisfied for each row in the table. It restricts the values that can be inserted
   or updated in a specific column.


6. **DEFAULT** Constraint: Sets a default value for a column if no value is explicitly provided during an insert operation.

7. **INDEX** Constraint: Indexing used for easy and quick retrival. It allocates the row_id for each row. An index is a database object that provides a quick lookup of data based on the values in one or more columns of a table. It acts like a roadmap that allows the database engine to find specific rows efficiently without having to scan the entire table.

8. **AUTO INCREMENT** Constraint: An auto-increment constraint, also known as an auto-incrementing or identity column, is a database feature that automatically
   generates a unique, incremental value for a column when a new row is inserted into a table. 

9. **ENUM** Constraint: An ENUM constraint is used to define a custom data type that represents **a set of predefined constant values for a column**. It allows you to specify that a column can only take one of the specified values, and any attempt to insert a value outside the predefined set will result in an error.

Constraints can be used with several SQL commands, including:

1. **CREATE TABLE:** Constraints are often defined when creating a new table. They ensure that the data entered into the table adheres to specific rules.

2. **ALTER TABLE:** Constraints can also be added or modified after a table has already been created using the `ALTER TABLE` command.

3. **INSERT:** Constraints are checked when inserting new rows into a table to ensure that the data being inserted adheres to the defined rules.

4. **UPDATE:** Constraints are checked when updating existing rows in a table to maintain data integrity.

5. **DELETE:** Constraints can be used to prevent the deletion of rows that would violate data integrity rules.


## 1. NOT NULL

- Specifies that a column cannot have null values

```
-- Syntax :

CREATE TABLE <Table_Name>(
<Column_name_1> <Type> NOT NULL,
<Column_name_2> <Type>(<Limit>),
<Column_name_3> <Type>(<Limit>));

-- Example :

CREATE TABLE vikey_Company(
s_no INT NOT NULL,
name VARCHAR(30),
comments VARCHAR(100));

INSERT INTO vikey_Company VALUES ('1','Danny','This is for testing'); -- Positive case
INSERT INTO vikey_Company VALUES ('2','','This is for testing NOT NULL'); -- Positive case
INSERT INTO vikey_Company (name, comments) VALUES ('Sunny','This is for testing NOT NULL'); -- Negative case
```

## 2. UNIQUE

- A table can have more than one unique key. It's like a primary key but accepts one null value per column.

```
SELECT * FROM ranjeet_academy;

CREATE TABLE Ranjeet_Academy(
s_no INT,
s_name VARCHAR(30) UNIQUE,
s_city VARCHAR(20),
S_ph_no INT UNIQUE);

INSERT INTO Ranjeet_Academy VALUES ('1','Harsha','Bangalore','81448'); -- Correct values
INSERT INTO Ranjeet_Academy VALUES ('2','Vishnu','Bangalore','81448'); -- Repeat the ph_number 
INSERT INTO Ranjeet_Academy VALUES ('3','Harsha','Bangalore','86548'); -- Repeat the name
INSERT INTO Ranjeet_Academy VALUES ('4','','Bangalore','52345'); -- Null Value
INSERT INTO Ranjeet_Academy (s_no,s_city,S_ph_no)VALUES ('5','Bangalore','81468'); -- Skip Value
INSERT INTO Ranjeet_Academy VALUES ('6','','Bangalore','52345'); -- One more Null Value
```

## 3. CHECK

- Allows you to specify a condition that must be satisfied for each row in the table. It restricts the values that can be inserted or updated in a specific column.

```
CREATE TABLE Election_Data(
E_ID INT NOT NULL,
Voter_Name VARCHAR(30),
Voter_Age INT CHECK (Voter_Age>=18));

INSERT INTO Election_Data VALUES ('1','Danny','20'); -- Plus case
INSERT INTO Election_Data VALUES ('2','Sunny','18'); -- Equal case
INSERT INTO Election_Data VALUES ('3','Bunny','15'); -- Minus case
```

## 4. ENUM

- It allows the given listed values and null values.

```
CREATE TABLE Dheeraj_Sports(
s_no INT,
s_name VARCHAR(30),
s_city INT,
S_ph_no INT,
s_langues ENUM('Telugu','Tamil','Kannada','Hindi','English','Malayalam'));

INSERT INTO Dheeraj_Sports VALUES ('1','Malavika','002','354564646','Malayalam'); -- Postive
INSERT INTO Dheeraj_Sports VALUES ('2','Balaji','003','363566646','French'); -- Negative
INSERT INTO Dheeraj_Sports VALUES ('3','Sekhar','005','363546566',''); -- Empty Value
INSERT INTO Dheeraj_Sports (s_no, s_name, s_city, S_ph_no)VALUES ('3','Rushi','009','635656464'); -- Null Value
```

## 5. DEFAULT

- Default is used to replace the empty value with the given default value.

```
CREATE TABLE Vignesh_Biriyani(
Chef_ID_no INT NOT NULL,
Chef_name VARCHAR(30),
Chef_city VARCHAR(15) DEFAULT 'DINDIGUL');

INSERT INTO Vignesh_Biriyani VALUES ('1','Mani','Tiruvannamalai'); -- Postive case
INSERT INTO Vignesh_Biriyani VALUES ('2','Rushi',''); -- Null value
INSERT INTO Vignesh_Biriyani (Chef_ID_no, Chef_name) VALUES ('3','Balaji'); -- returns 'DINDIGUL'
```

## 6. INDEX 

- Indexing used for easy and quick retrival. it allocates the row_id for each row.

```
CREATE TABLE Malavika_Foods(
Item_ID INT,
Item_name VARCHAR(30),
city VARCHAR(30),
Item_Price INT,
index(item_name)
);

INSERT INTO Malavika_Foods values
('1','Puttu','BLR','198'),
('2','Appam','TRV','1248'),
('3','Vellappam','KOC','176'),
('4','Fish','HYD','36'),
('6','Kappa','KNR','287');

CREATE INDEX food_index ON malavika_foods(item_name);
DESC malavika_foods;

SELECT * FROM malavika_foods USE INDEX (food_index);
SELECT * FROM malavika_foods;
```

## 7. PRIMARY KEY 

- Used to identify each record in the table uniquely.

```
CREATE TABLE Sekhars_Blog(
Reader_ID INT PRIMARY KEY,
Reader_name VARCHAR(30),
Reader_city VARCHAR(3));

INSERT INTO Sekhars_Blog VALUES ('1','Mani','TRL'); -- Postive case
INSERT INTO Sekhars_Blog VALUES ('','Rushi','VZK'); -- Null value (Fails)
INSERT INTO Sekhars_Blog (Reader_name, Reader_city) VALUES ('Balaji', 'ERD'); -- No case (Fails)
```

## 8. AUTO_INCREMENT 

- Mainly used to generate the auto increment values.

```
CREATE TABLE Mr_Khan_Library(
s_ID INT AUTO_INCREMENT primary key,
s_name VARCHAR(30),
s_city varchar(25)
);

ALTER TABLE Mr_Khan_Library AUTO_INCREMENT = 100;
select * from Mr_Khan_Library;

INSERT INTO Mr_Khan_Library VALUES ('1','Mani','Tiruvannamalai'); -- Postive case
INSERT INTO Mr_Khan_Library VALUES ('','Rushi','Visakapatnam'); -- Null value (Fails)
INSERT INTO Mr_Khan_Library (s_name,s_city)VALUES ('Abhi','Hyderabad'); -- Skip the value (s_ID will be 100)
INSERT INTO Mr_Khan_Library VALUES ('-4','Harsha','Bangalore'); -- Negative case
INSERT INTO Mr_Khan_Library (s_name,s_city)VALUES ('Akhil','hyd');		-- (s_ID will be 101)
INSERT INTO Mr_Khan_Library (s_name,s_city)VALUES ('Akhil','hyd');		-- (s_ID will be 102)
```

## 9. Foreign Key Constraint

- Used to link multiple tables, The forign key of one table matches with primary key of another table.

```
SET FOREIGN_KEY_CHECKS=0;

CREATE TABLE Suchandan_Hotels (  
Dish_ID int NOT NULL,   
Dish_name varchar(15) PRIMARY KEY,   
Price INT
);

CREATE TABLE Bhaskar_Chats (  
Chat_ID int NOT NULL,   
Chat_name varchar(15),   
Price INT,
FOREIGN KEY (Chat_name) REFERENCES Suchandan_Hotels(Dish_name)
);

DESC Suchandan_Hotels;
DESC Bhaskar_Chats;

SELECT * FROM Suchandan_Hotels;
SELECT * FROM Bhaskar_Chats;


INSERT INTO Suchandan_Hotels VALUES 
('321','Pani Puri',100),
('342','Roti',150),
('374','Tea',99),
('384','Biriyani',500);

INSERT INTO Bhaskar_Chats VALUES 
('321','Pani Puri',30),
('342','Masala Puri',35),
('374','Samosa',20),
('384','Vada Pav',25);

INSERT INTO Suchandan_Hotels VALUES ('542','Butter Roti','200');
INSERT INTO Suchandan_Hotels VALUES ('842','Butter Roti','300'); -- Trying to insert duplicate value into primary key (Fails)

INSERT INTO Bhaskar_Chats VALUES ('543','Aloo Tikki','40');
INSERT INTO Bhaskar_Chats VALUES ('654','Aloo Tikki','20'); -- Trying to insert duplicate value into foreign key
```

## COMPOSITE KEYS

- A composite key is a candidate key that consists of two or more attributes (table columns) that together uniquely identify an entity occurrence (table row).

```
CREATE TABLE Employee (
    employee_id INT,
    department_id INT,
    employee_name VARCHAR(50),
    PRIMARY KEY (employee_id, department_id)
	);

drop table sports;
CREATE TABLE sports (
    sports_id varchar(5),
    Game VARCHAR(50),
    emp_id INT,
    dept_id INT,
    FOREIGN KEY (emp_id, dept_id) REFERENCES Employee(employee_id, department_id)
);

INSERT INTO Employee (employee_id, department_id, employee_name) VALUES
(1, 101, 'John Doe'),
(2, 102, 'Jane Smith'),
(3, 101, 'Michael Johnson'),
(4, 103, 'Emily Brown');

INSERT INTO sports (sports_id, Game, emp_id, dept_id) VALUES
(200, 'Football', 1, 101),
(201, 'Basketball', 1, 101),
(203, 'Tennis', 2, 102),
(204, 'Soccer', 2, 102);

INSERT INTO Employee (employee_id, department_id, employee_name) VALUES (5, 104, 'stormy');
INSERT INTO sports (sports_id, Game, emp_id, dept_id) VALUES (205, 'Football', 5, 104); -- trying to insert duplicates for child table.
INSERT INTO sports (sports_id, Game, emp_id, dept_id) VALUES (206, 'Football', 'null', 'null');-- null records -ve case (Fails)
INSERT INTO sports (sports_id, Game) VALUES (207, 'Football');-- no values +ve case (null is inserted)
```

## To find constraint information

```
SELECT * FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME = 'xyz';
```

## Using constraints with CREATE Table

Examples of using constraints:

```sql
Creating a table with constraints
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

Create a table with various constraints in SQL, including PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, CHECK, DEFAULT, INDEX, AUTO_INCREMENT, and ENUM.

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
- By giving constraints a name using the CONSTRAINT keyword, you make it easier to manage and reference them.

Please note that the specific syntax and supported features may vary depending on the database system you are using (e.g., MySQL, PostgreSQL, SQL Server). Make sure to adjust the data types, constraint names, and other details according to your database system's syntax.


## USING CONSTRAINTS WITH ALTER 

Use the `ALTER TABLE` command to add various constraints to an existing table named "Employees" in SQL, including PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, CHECK, DEFAULT, INDEX, AUTO_INCREMENT, and ENUM. Please note that the example provided assumes the table and related columns already exist.

```sql
-- Adding a PRIMARY KEY constraint
ALTER TABLE Employees
ADD PRIMARY KEY (employee_id);

-- Adding a FOREIGN KEY constraint
ALTER TABLE Employees
ADD CONSTRAINT fk_department
FOREIGN KEY (department_id) REFERENCES Departments(department_id);

-- Adding a UNIQUE constraint
ALTER TABLE Employees
ADD CONSTRAINT uk_email UNIQUE (email);

-- Adding a CHECK constraint
ALTER TABLE Employees
ADD CONSTRAINT chk_salary CHECK (salary > 0);

-- Adding an INDEX
ALTER TABLE Employees
ADD INDEX idx_last_name (last_name);

-- Adding an ENUM column
ALTER TABLE Employees
ADD COLUMN gender ENUM('Male', 'Female', 'Other');

-- Adding a DEFAULT constraint
ALTER TABLE Employees
ADD COLUMN status VARCHAR(20) DEFAULT 'Active';

-- Adding a NOT NULL constraint
ALTER TABLE Employees
MODIFY COLUMN first_name VARCHAR(50) NOT NULL;

-- Adding an AUTO_INCREMENT attribute (Assuming it's supported by the database)
ALTER TABLE Employees
MODIFY COLUMN employee_id INT AUTO_INCREMENT;
```

In this example:

- The `ALTER TABLE` command is used to modify the table schema.
- `employee_id` is added as the primary key using the `ADD PRIMARY KEY` constraint.
- A foreign key constraint `fk_department` is added to link the `department_id` column to the `Departments` table.
- A unique constraint `uk_email` is added to the `email` column to enforce uniqueness.
- The `first_name` column is modified to be `NOT NULL`.
- A `CHECK` constraint `chk_salary` is added to ensure that the salary is greater than 0.
- The `hire_date` column is set to have a default value of the current date.
- An index named `idx_last_name` is added to the `last_name` column.
- The `employee_id` column is modified to be auto-incremented.
- A new `gender` column of ENUM type is added.

Please note that the syntax might vary based on the specific database system you are using, and some constraints might not be supported in all systems. Always refer to the documentation of your database management system for the accurate syntax and supported constraints.

## Using constraints with INSERT command

Certainly! Below is an example that demonstrates using the mentioned constraints (`PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`, `CHECK`, `DEFAULT`, `INDEX`, `AUTO_INCREMENT`, and `ENUM`) with the `INSERT` command. This example assumes a simplified table named "Students" with various columns.

```sql
-- CREATE TABLE Students
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    age INT CHECK (age >= 18),
    department_id INT,
    email VARCHAR(100) UNIQUE,
    registration_date DATE DEFAULT CURRENT_DATE,
    INDEX idx_last_name (last_name)
);

-- INSERT data with constraints
INSERT INTO Students (first_name, last_name, gender, age, department_id, email)
VALUES ('John', 'Doe', 'Male', 20, 1, 'john.doe@example.com');

-- INSERT data with NULL values (assuming NULL is allowed)
INSERT INTO Students (first_name, last_name, gender)
VALUES ('Jane', 'Smith', 'Female');

-- INSERT data with default values
INSERT INTO Students (first_name, last_name, gender, age)
VALUES ('Alice', 'Johnson', 'Female', 22);

-- INSERT data that violates CHECK constraint
-- This will fail if age is less than 18

-- INSERT data with duplicate email (UNIQUE constraint violation)
-- This will fail if the email is already in use
```

In this example:

- A table named "Students" is created with various constraints (`PRIMARY KEY`, `UNIQUE`, `NOT NULL`, `CHECK`, `DEFAULT`, `ENUM`, `AUTO_INCREMENT`, `INDEX`).
- The `INSERT` command is used to add data that adheres to the defined constraints.
- You can see examples of inserting data with different combinations of constraints, including NULL values, default values, and data that violates constraints.

Please remember to adapt the column names, table names, and constraints according to your specific database schema and SQL dialect. Also, keep in mind that some constraints and features may not be supported in all database systems. Always refer to your database's documentation for accurate syntax and supported features.

## Using constraints with UPDATE command

Here's an example that demonstrates using the mentioned constraints (`PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`, `CHECK`, `DEFAULT`, `INDEX`, `AUTO_INCREMENT`, and `ENUM`) with the `UPDATE` command. This example assumes a simplified table named "Employees" with various columns.

```sql
-- CREATE TABLE Employees
CREATE TABLE Employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    department_id INT,
    email VARCHAR(100) UNIQUE,
    salary DECIMAL(10, 2) CHECK (salary > 0),
    hire_date DATE DEFAULT CURRENT_DATE,
    gender ENUM('Male', 'Female', 'Other') NOT NULL
);

-- INSERT data with constraints
INSERT INTO Employees (first_name, last_name, email, salary, gender)
VALUES ('John', 'Doe', 'john.doe@example.com', 50000.00, 'Male');

-- UPDATE data with constraints
UPDATE Employees
SET salary = 55000.00
WHERE employee_id = 1;

-- Attempt to UPDATE data violating CHECK constraint
-- This will fail if salary is set to a non-positive value

-- Attempt to UPDATE data violating UNIQUE constraint
-- This will fail if the email is already in use
```

In this example:

- A table named "Employees" is created with various constraints (`PRIMARY KEY`, `UNIQUE`, `NOT NULL`, `CHECK`, `DEFAULT`, `ENUM`, `AUTO_INCREMENT`).
- The `INSERT` command adds an employee with data that adheres to the defined constraints.
- The `UPDATE` command modifies an employee's salary, adhering to the constraints.
- You can see examples of using the `UPDATE` command to violate the `CHECK` constraint and the `UNIQUE` constraint. These attempts will fail due to the constraint violations.

As always, adapt the column names, table names, and constraints based on your specific database schema and SQL dialect. Constraints and features can vary between database systems, so consult your database's documentation for accurate syntax and supported features.

**Using constraints with DELETE command**:

Below is an example that demonstrates using the mentioned constraints (`PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`, `CHECK`, `DEFAULT`, `INDEX`, `AUTO_INCREMENT`, and `ENUM`) with the `DELETE` command. This example assumes a simplified table named "Employees" with various columns.

```sql
-- CREATE TABLE Employees
CREATE TABLE Employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    department_id INT,
    email VARCHAR(100) UNIQUE,
    salary DECIMAL(10, 2) CHECK (salary > 0),
    hire_date DATE DEFAULT CURRENT_DATE,
    gender ENUM('Male', 'Female', 'Other') NOT NULL
);

-- INSERT data with constraints
INSERT INTO Employees (first_name, last_name, email, salary, gender)
VALUES ('John', 'Doe', 'john.doe@example.com', 50000.00, 'Male');

-- DELETE data with constraints
DELETE FROM Employees
WHERE employee_id = 1;

-- Attempt to DELETE data with a FOREIGN KEY constraint
-- This will fail if the department_id is still referred to by other records

-- Attempt to DELETE data with a NOT NULL constraint
-- This will fail if the column value is set to NULL

-- Attempt to DELETE data with a CHECK constraint
-- This will fail if salary is less than or equal to 0
```

In this example:

- A table named "Employees" is created with various constraints (`PRIMARY KEY`, `UNIQUE`, `NOT NULL`, `CHECK`, `DEFAULT`, `ENUM`, `AUTO_INCREMENT`).
- The `INSERT` command adds an employee with data that adheres to the defined constraints.
- The `DELETE` command removes an employee's data.
- You can see examples of using the `DELETE` command to violate constraints such as the `FOREIGN KEY` constraint (if other records depend on the department), the `NOT NULL` constraint, and the `CHECK` constraint.

Always adjust the column names, table names, and constraints according to your specific database schema and SQL dialect. Constraints and features can vary between database systems, so refer to your database's documentation for accurate syntax and supported features.


**ASSIGNMENT**

1.	Create database

2. Create table accounts

```
2. Create table accounts
CREATE TABLE accounts (
account_no INT,
user_name VARCHAR(15),
bank_name VARCHAR (15),
email VARCHAR (20),
balance DECIMAL(10,2),
created_on DATETIME,
customer_id INT
);
```

3.	Columns account_no, user_name, bank_name, email, balance, created_on, customer_id

```
CREATE TABLE customer (
Customer_id INT,
first_name VARCHAR (15),
last_name VARCHAR (15),
DOB DATE,
address VARCHAR (50)
);
```

4.	Create table customer details
5.	Customer_id,first_name,last_name,DOB,address

6.	Add column phone_number to customer details and it should accept only 10 numbers, not more than or less than 10 numbers. (apply this on existing table)

```
-- ALTER TABLE customer
-- ADD phone_number VARCHAR(10) NOT NULL,
-- ADD CONSTRAINT check_ph_no_len CHECK (LENGTH(phone_number)=10);
```

7.	Apply default as currenttime on created_on field from accounts table(apply on existing table)

```
ALTER TABLE accounts
MODIFY created_on TIMESTAMP DEFAULT (CURRENT_TIMESTAMP);
```

8.	Create a new parent and child table with 5 records in it.


9. display customer_id,bank_name,email,phone_number(use joins)


10. use without joins

11.	How can you add a PRIMARY KEY constraint to the "emp_id" column of the "employees" table? 

```
ALTER TABLE employees
ADD PRIMARY KEY (employee_id);
```

12.	Explain the purpose of the UNIQUE constraint and how it differs from the PRIMARY KEY constraint.

- UNIQUE ensures that the values in a specific column or a combination of columns are unique across all rows in the table. 
- It allows each value to appear only once in the column. 
- PK also ensures that each row in a table has a unique identifier, and it cannot have NULL values.

13.	How do you add a UNIQUE constraint to the "email" column of the "employees" table to ensure email addresses are unique?

```
-- To add column, syntax is:
-- ALTER TABLE table
-- ADD [COLUMN] column_name column_definition [FIRST|AFTER existing_column];
```

```
-- ADD email column to "employees"
ALTER TABLE employees
ADD COLUMN email VARCHAR(25) AFTER department; 
ALTER TABLE employees 
ADD CONSTRAINT unique_email UNIQUE (email)
```

14. What is the FOREIGN KEY constraint, and how can you use it to establish a relationship between the "employees" and "departments" tables?

- A foreign key is a column or columns in a database that (e.g. table_1.column_a) that are linked to a column in a different table (table_2.column_b).
- The existence of a foreign key column establishes a foreign key constraint – a database rule that ensures that a value can be added or updated in column_a only if the same value already exists in column_b.

15.	How do you add a FOREIGN KEY constraint to the "department_id" column of the "employees" table, referencing the "department_id" column of the "departments" table?

```
ALTER TABLE Employees
ADD CONSTRAINT fk_department
FOREIGN KEY (department_id) REFERENCES Departments(department_id);
```

16.	Explain the concept of cascading referential integrity using the ON DELETE CASCADE option in a FOREIGN KEY constraint.

- Cascading referential integrity constraints define the actions to be taken when a record in a parent table (the table with the primary key) is deleted or updated.
- It helps maintain the integrity and consistency of data across related tables.
- One of the options to implement cascading referential integrity is using the ON DELETE CASCADE option in a FOREIGN KEY constraint. 
- Cascading is used with the drop command when we want to drop a parent table, even when a child table exists.

17. How do you enforce that the "age" column in the "employees" table must have values greater than or equal to 18 using the CHECK constraint?

```
ALTER TABLE Employees
ADD CONSTRAINT chk_age CHECK (age > 18);
```

18.	How can you use the DEFAULT constraint to set a default value of "Unknown" for the "department" column of the "employees" table?

```
ALTER TABLE Employees
ALTER department SET DEFAULT 'Unknown';
```

19. How do you create a composite PRIMARY KEY on the "emp_id" and "department_id" columns of the "employees" table?

```
ALTER TABLE employees
ADD CONSTRAINT pk_employee_department PRIMARY KEY (employee_id, department);
```

20. Explain the concept of multi-column UNIQUE constraint and how it ensures uniqueness across multiple columns.

- A multi-column UNIQUE constraint, also known as a composite UNIQUE constraint, is a database constraint that ensures the uniqueness of combinations of values across multiple columns in a table.
- a multi-column UNIQUE constraint enforces uniqueness for combinations of values in multiple columns. 
- This means that no two rows in the table can have the same combination of values in the specified columns

- 21.	How can you use the NOT NULL constraint to enforce that the "first_name" and "last_name" columns in the "employees" table must not contain NULL values?

```
ALTER TABLE employees
MODIFY COLUMN first_name VARCHAR(50) NOT NULL;

ALTER TABLE employees
MODIFY COLUMN last_name VARCHAR(50) NOT NULL;
```

22.	How do you remove the PRIMARY KEY constraint from the "emp_id" column of the "employees" table?

```
ALTER TABLE employees
DROP PRIMARY KEY;
```

23.	Explain the purpose of the INDEX constraint, and how can you add an index on the "department" column to improve query performance?

- Indexing makes columns faster to query by creating pointers to where data is stored within a database.
- Imagine you want to find a piece of information that is within a large database. If the data you are looking for is towards the very end, this query would take a long time to run.

```
ALTER TABLE employees
ADD INDEX idx_department (department);
```

24.	How do you drop the UNIQUE constraint from the "email" column of the "employees" table?

```
ALTER TABLE employees
DROP INDEX unique_email;
```

25.	How can you use the FOREIGN KEY constraint with the ON UPDATE CASCADE option to automatically update related records when the primary key is modified?

- You can use the FOREIGN KEY constraint with the ON UPDATE CASCADE option to automatically update related records in the child table when the primary key in the parent table is modified. 
- This is useful when you want to maintain referential integrity and ensure that changes in the primary key value propagate to the foreign key references in other tables. 


26.	How do you add a FOREIGN KEY constraint with the ON DELETE SET NULL option to set the "department_id" to NULL in the "employees" table if the referenced department is deleted?


27.	How can you add a CHECK constraint to ensure that the "age" column in the "employees" table must be between 18 and 60?

```
ALTER TABLE employees
ADD CONSTRAINT CHK_PersonAge CHECK (Age>=18 AND Age <=60);
```

28.	Explain the purpose of the PRIMARY KEY AUTO_INCREMENT attribute and how it works with the "emp_id" column.

- It designates a column (or a set of columns) as the primary key for a table. 
- It instructs the database to automatically generate a unique value for the primary key column whenever a new row is inserted into the table. 

29.	How do you alter the "department" column of the "employees" table to increase its maximum length from 20 to 50 characters?

```
ALTER TABLE employees
MODIFY COLUMN department VARCHAR(50);
```


30.	How can you use the FOREIGN KEY constraint with the ON DELETE RESTRICT option to prevent deletion of a department if it has associated employees in the "employees" table?


## JOINS

1. What is a JOIN in MySQL, and how does it work?

- Join statement is used for connecting data between several tables in a database based on the common fields in those tables.
- The same column name and data type are generally present in the tables being linked as common values.


2. Explain the differences between INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN in MySQL with examples.

- (INNER) JOIN: Returns records that have matching values in both tables
- LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table
- RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table
- FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table

3. How can you retrieve the first and last names of employees along with their corresponding department names using an INNER JOIN?

```
SELECT employees.first_name, employees.last_name, departments.department_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.department_id;
```

4. Write a SQL query to find the employees who do not belong to any department using a LEFT JOIN.

```
SELECT employees.first_name, employees.last_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.department_id
WHERE departments.department_id IS NULL;
```

5. How do you get a list of all departments and the number of employees in each department using an INNER JOIN and GROUP BY?

```
SELECT departments.department_name, COUNT(employees.employee_id) AS employee_count
FROM departments
INNER JOIN employees ON departments.department_id = employees.department_id
GROUP BY departments.department_name;
```

6. Explain the concept of self-join and provide an example of its usage in the "employee" table.

- A self-join is a type of SQL join where a table is joined with itself. In other words, you use the same table for both the left and right sides of the join operation. Self-joins are often used when you have a hierarchical or recursive relationship within a single table, such as in organizational structures or when modeling data with parent-child relationships.


Let's say you want to retrieve a list of employees along with their managers' names. You can use a self-join to accomplish this:

```
SELECT e.first_name AS employee_first_name,
       e.last_name AS employee_last_name,
       m.first_name AS manager_first_name,
       m.last_name AS manager_last_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.emp_id;
```

-- 7. Write a SQL query to find the employees who have the same department as Michael Johnson using a self-join.

```
SELECT e1.first_name, e1.last_name
FROM employees e1
JOIN employees e2 
ON e1.department = e2.department
WHERE e2.first_name = 'Monika' AND e2.last_name = 'Arora';
```

8. How can you use an OUTER JOIN to retrieve the employees and their respective department names, including employees without a department?

```
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id;
```

9. Write a SQL query to find the employees who have the same department as John Doe and Jane Smith using a self-join and an INNER JOIN.

```
-- Using a self-join with INNER JOIN
SELECT e1.first_name, e1.last_name, e1.department
FROM employees e1
INNER JOIN employees e2 ON e1.department = e2.department
WHERE (e2.first_name = 'Niharika' AND e2.last_name = 'Verma') OR (e2.first_name = 'Monika' AND e2.last_name = 'Arora');
```

10. Write a SQL query to find the second highest salary for each department along with the employees' names using a self-join and RANK() window function.

```
WITH RankedSalaries AS 
(
SELECT first_name, department, salary,
RANK() OVER (PARTITION BY department ORDER BY salary) AS salary_rank
FROM employees
)
SELECT rs.department, rs.first_name, rs.salary
FROM RankedSalaries rs
WHERE rs.salary_rank = 2;
```

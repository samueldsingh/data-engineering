# SQL Practice

## 1. Prepare table to practice sql skills

### i. Create sample table: Workers, Bonus, Title 

```
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),    
    salary DECIMAL(10, 2),
    joining_date DATETIME,
    department VARCHAR(100)
)
```

```
CREATE TABLE bonus (
    emp_ref_id INT,
    bonus_date DATETIME,
    bonus_amount INT
)
```

### ii. Insert values in the table

```
 INSERT INTO employees (worker_id, first_name, last_name, salary, joining_date, department)
 VALUES
     (1, 'Monika', 'Arora', 100000, '2014-02-20 9:00:00', 'HR'),
     (2, 'Niharika', 'Verma', 80000, '2014-06-11 9:00:00', 'Admin'),
     (3, 'Vishal', 'Singhal', 300000, '2014-02-20 9:00:00', 'HR'),
     (4, 'Amitabh', 'Singh', '500000', '2014-02-20 9:00:00', 'Admin'), 
     (5, 'Vivek', 'Bhati', 500000, '2014-06-11 9:00:00', 'Admin'),
     (6, 'Vipul', 'Diwan', 200000, '2014-06-11 9:00:00', 'Account'),
     (7, 'Satish', 'Kumar', 75000, '2014-01-20 9:00:00', 'Account'),
     (8, 'Geetika', 'Chauhan', 90000, '2014-04-11 9:00:00', 'Admin');
```

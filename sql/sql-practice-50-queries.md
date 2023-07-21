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

1. Write an SQL query to fetch “FIRST_NAME” from the employees table using the alias name <employee_name>.

```
SELECT first_name AS employee_name
FROM employees;
```

2. Write a SQL query to fetch “FIRST_NAME” from the Worker table in upper case.

```
SELECT UPPER(first_name) AS UPPER_CASE_FIRST_NAME
FROM employees;
```

3. Write an SQL query to fetch unique values of DEPARTMENT from the employees table.

```
SELECT DISTINCT department
FROM employees;
```

4. Write an SQL query to print the first three characters of first_name from the employees table.

```
SELECT LEFT(first_name, 3) AS first_three_chars
FROM employees;
```


5. Write an SQL query to find the position of the alphabet (‘a’) in the first name column ‘Amitabh’ from the employees table.

To find the position of the alphabet 'a' in the first name column 'Amitabh' from the "employees" table in SQL, you can use the `INSTR()` (MySQL) or `CHARINDEX()` (SQL Server) function, depending on the database system you are using.
 
```
SELECT INSTR(first_name, 'a') AS position_of_a
FROM employees
WHERE first_name = 'Amitabh';
```

6. Write an SQL query to print the first_name from the employees table after removing white spaces from the right side.

```
SELECT RTRIM(FIRST_NAME) AS trimmed_first_name
FROM employees;
```

7. Write an SQL query to print the DEPARTMENT from the Worker table after removing white spaces from the left side.

```
SELECT LTRIM(DEPARTMENT) AS trimmed_department
FROM employees;
```

8. Write an SQL query that fetches the unique values of DEPARTMENT from the Worker table and prints its length.

```
SELECT COUNT(DISTINCT department) AS department_count
FROM employees;
```

9. Write an SQL query to print the FIRST_NAME from the Worker table after replacing ‘a’ with ‘A’.

```
SELECT REPLACE(FIRST_NAME, 'a', 'A') AS modified_first_name
FROM Worker;
```

10. Write an SQL query to print the FIRST_NAME and LAST_NAME from the Worker table into a single column COMPLETE_NAME. A space char should separate them.

```
SELECT CONCAT(first_name, ' ', last_name) AS complete_name
FROM employees;
```

11. Write an SQL query to print all Worker details from the Worker table order by FIRST_NAME Ascending.


12. Write an SQL query to print all Worker details from the Worker table order by FIRST_NAME Ascending and DEPARTMENT Descending.


13. Write an SQL query to print details for Workers with the first names “Vipul” and “Satish” from the Worker table.


14. Write an SQL query to print details of workers excluding first names, “Vipul” and “Satish” from the Worker table.


15. Write an SQL query to print details of Workers with DEPARTMENT name as “Admin”.


16. Write an SQL query to print details of the Workers whose FIRST_NAME contains ‘a’.


17. Write an SQL query to print details of the Workers whose FIRST_NAME ends with ‘a’.


18. Write an SQL query to print details of the Workers whose FIRST_NAME ends with ‘h’ and contains six alphabets.


19. Write an SQL query to print details of the Workers whose SALARY lies between 100000 and 500000.


20. Write an SQL query to print details of the Workers who joined in Feb’2014.


21. Write an SQL query to fetch the count of employees working in the department ‘Admin’.


22. Write an SQL query to fetch worker names with salaries >= 50000 and <= 100000.


23. Write an SQL query to fetch the no. of workers for each department in descending order.


24. Write an SQL query to print details of the Workers who are also Managers.


25. Write an SQL query to fetch duplicate records having matching data in some fields of a table.


26. Write an SQL query to show only odd rows from a table.


27. Write an SQL query to show only even rows from a table.


28. Write an SQL query to clone a new table from another table.

 
29. Write an SQL query to fetch intersecting records of two tables.

 
30. Write an SQL query to show records from one table that another table does not have.

 
31. Write an SQL query to show the current date and time.

 
32. Write an SQL query to show the top n (say 10) records of a table.


33. Write an SQL query to determine the nth (say n=5) highest salary from a table.


34. Write an SQL query to determine the 5th highest salary without using the TOP or limit method.


35. Write an SQL query to fetch the list of employees with the same salary.


36. Write an SQL query to show the second-highest salary from a table.


37. Write an SQL query to show one row twice in the results from a table.


38. Write an SQL query to fetch intersecting records of two tables.


39. Write an SQL query to fetch the first 50% of records from a table.


40. Write an SQL query to fetch the departments that have less than five people in them.


41. Write an SQL query to show all departments along with the number of people in there.


42. Write an SQL query to show the last record from a table.


43. Write an SQL query to fetch the first row of a table.


44. Write an SQL query to fetch the last five records from a table.


45. Write an SQL query to print the name of employees having the highest salary in each department.

 
46. Write an SQL query to fetch three max salaries from a table.


47. Write an SQL query to fetch three min salaries from a table.

 
48. Write an SQL query to fetch nth max salaries from a table.

 
49. Write an SQL query to fetch departments along with the total salaries paid for each of them.

 
50. Write an SQL query to fetch the names of workers who earn the highest salary.



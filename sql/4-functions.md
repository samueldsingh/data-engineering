SQL functions are pre-defined or user-defined routines that accept zero or more arguments and return a value or a table result. They are used to perform various operations on data within an SQL database. SQL functions are categorized into several types based on their functionality. Let's dive into the details of SQL functions:

[SQL functions](https://blog.hubspot.com/website/mysql-functions#:~:text=MySQL%20functions%20are%20powerful%20tools,easy%2Dto%2Dnavigate%20databases.)

**1. Built-in (System) Functions:**
   These functions are provided by the database management system and are available for use without any additional setup.

   - **Scalar Functions:** These functions operate on a single input value and return a single output value. Examples include:
     - `CONCAT`: Concatenates two or more strings.
     - `LOWER`, `UPPER`: Converts a string to lowercase or uppercase.
     - `LEN`, `CHAR_LENGTH`: Returns the length of a string.
     - `ROUND`, `FLOOR`, `CEIL`: Perform rounding and ceiling/floor operations on numeric values.
    
   ```
-- CONCAT function to concatenate two strings
SELECT CONCAT('Hello', ' ', 'World');  -- Output: 'Hello World'

-- LEN function to get the length of a string
SELECT LEN('Database');  -- Output: 8

-- ROUND function to round a numeric value
SELECT ROUND(5.678);  -- Output: 6
   ```

   Other scalar functions:

Certainly! Here are examples of each of the SQL functions you mentioned:

- The `UCASE()` function converts a string to uppercase.

```sql
SELECT UCASE('hello world');  -- Output: 'HELLO WORLD'
```

- The `LCASE()` function converts a string to lowercase.

```sql
SELECT LCASE('Hello World');  -- Output: 'hello world'
```

- The `MID()` function extracts a substring from a string starting at a specified position.

```sql
SELECT MID('abcdef', 2, 3);  -- Output: 'bcd'
```

- The `LENGTH()` function returns the length of a string.

```sql
SELECT LENGTH('database');  -- Output: 8
```

- The `ROUND()` function rounds a numeric value to a specified number of decimal places.

```sql
SELECT ROUND(5.678, 1);  -- Output: 5.7
```

- The `NOW()` function returns the current date and time.

```sql
SELECT NOW();  -- Output: Current date and time
```


- The `FORMAT()` function formats a numeric value with a specified format.

```sql
SELECT FORMAT(1234567.89, 'C', 'en-US');  -- Output: '$1,234,567.89'
```

Please note that the availability and syntax of these functions may vary slightly based on the specific database system you are using. The examples provided are based on general SQL syntax.


   - **Aggregate Functions:** These functions operate on a set of values and return a single value. They are used with the `GROUP BY` clause for grouping and summarizing data. Examples include:
     - `SUM`, `AVG`, `MIN`, `MAX`, `STDDEV`, `VARIANCE`: Perform arithmetic operations on numeric values.
     - `COUNT`: Counts the number of rows or non-null values in a column.
     - `GROUP_CONCAT` (MySQL), `STRING_AGG` (PostgreSQL): Concatenates values from multiple rows into a single string.

```
-- SUM function to calculate the total of a column
SELECT SUM(salary) FROM employees;  -- Sum of salaries

-- COUNT function to count the number of rows
SELECT COUNT(*) FROM orders;  -- Number of orders

-- AVG function to calculate the average of a column
SELECT AVG(age) FROM customers;  -- Average age of customers

-- Calculate the standard deviation of salary for employees
SELECT STDDEV(salary) AS standard_deviation
FROM employees;

-- Calculate the variance of age for customers
SELECT VARIANCE(age) AS variance
FROM customers;

-- CONCAT all the product names for each order
SELECT order_id, GROUP_CONCAT(product_name ORDER BY product_name ASC SEPARATOR ', ') AS products
FROM orders
GROUP BY order_id;

SELECT order_id, STRING_AGG(product_name, ', ' ORDER BY product_name ASC) AS products
FROM orders
GROUP BY order_id;
```

   - **Date and Time Functions:** These functions operate on date and time values. Examples include:
     - `NOW`, `CURRENT_TIMESTAMP`: Returns the current date and time.
     - With `NOW`, 
     - With `CURRENT_TIMESTAMP`, the date and time is returned as `"YYYY-MM-DD HH-MM-SS" (string)` or as `YYYYMMDDHHMMSS.uuuuuu (numeric)`.
     - `DATEADD`, `DATEDIFF`: Performs date arithmetic operations.
     - `DATE_FORMAT`, `TO_CHAR`: Formats date and time values as strings.
     - `ADDTIME()` function adds a time interval to a time/datetime and then returns the time/datetime.

```
-- NOW function to get the current date and time
SELECT NOW();  -- Current date and time

-- The ADDDATE() function adds a time/date interval to a date and then returns the date.
SELECT ADDDATE(CURDATE(), INTERVAL 10 DAY);      # Output: 2023-09-10

-- DATEADD function to add days to a date. Same as ADDDATE() function
SELECT DATE_ADD(CURRENT_DATE(), INTERVAL 10 DAY);      # Output: Adds 10 days to the current date

-- Add 5 days, 2 hours, 10 minutes, 5 seconds, and 3 microseconds to a time and return the datetime:
SELECT ADDTIME(CURRENT_TIMESTAMP(), "5 2:10:5.000003");

-- DATE_FORMAT function to format date as a string
SELECT DATE_FORMAT('2023-08-04', '%Y-%m-%d');  -- Output: '2023-08-04'
```

**2. User-Defined Functions (UDFs):**
   Some database systems allow you to define your own functions using SQL or procedural languages like PL/SQL, T-SQL, or PL/pgSQL. UDFs can simplify complex queries and encapsulate business logic.

**3. Window Functions (Analytic Functions):**

[Window functions](https://en.wikipedia.org/wiki/Window_function_(SQL)) (also known as window analytic functions or windowed aggregates) is a function which uses values from one or multiple rows to return a value for each row. (This contrasts with an aggregate function, which returns a single value for multiple rows.) Window functions have an OVER clause; any function without an OVER clause is not a window function, but rather an aggregate or single-row (scalar) function. Unlike traditional aggregate functions like `SUM`, `AVG`, and `COUNT` that collapse multiple rows into a single result, window functions return a value for each row based on a specified window or range of rows.

Example:
As an example, here is a query which uses a window function to compare the salary of each employee with the average salary of their department (example from the PostgreSQL documentation):

```
SELECT depname, empno, salary, avg(salary) OVER (PARTITION BY depname) FROM empsalary;
```

Output is:
```
depname  | empno | salary |          avg          
----------+-------+--------+----------------------
develop   |    11 |   5200 | 5020.0000000000000000
develop   |     7 |   4200 | 5020.0000000000000000
develop   |     9 |   4500 | 5020.0000000000000000
develop   |     8 |   6000 | 5020.0000000000000000
develop   |    10 |   5200 | 5020.0000000000000000
personnel |     5 |   3500 | 3700.0000000000000000
personnel |     2 |   3900 | 3700.0000000000000000
sales     |     3 |   4800 | 4866.6666666666666667
sales     |     1 |   5000 | 4866.6666666666666667
sales     |     4 |   4800 | 4866.6666666666666667
(10 rows)
```

The `PARTITION BY` clause groups rows into partitions, and the function is applied to each partition separately. If the `PARTITION BY` clause is omitted (such as if we have an empty `OVER()` clause), then the entire result set treated as a single partition. For this query, the average salary reported would be the average taken over all rows.

Window functions are evaluated after aggregation (after the `GROUP BY` clause and non-window aggregate functions, for example).

Key features of window functions include:

1. **Partitioning:** Window functions can be partitioned by one or more columns, dividing the result set into distinct partitions. The calculation is then applied separately to each partition.

2. **Ordering:** Rows within each partition are ordered based on one or more columns. The ordering determines the sequence in which the calculations are performed.

3. **Window Frame:** A window frame defines the range of rows that are considered for the calculation. It can be specified using an OFFSET and RANGE or ROWS BETWEEN clause.

Window functions are extremely useful for generating reports, rankings, running totals, and performing complex analytical tasks directly within the SQL query. They help avoid the need for subqueries or self-joins in many cases and provide efficient ways to compute aggregations across rows without compromising individual row information.

Commonly used window functions include:

- `ROW_NUMBER()`: Assigns a unique integer to each row, based on the specified order within each partition.

Sure! Let's use the `ROW_NUMBER()` function in a practical example. Suppose we have a table named `orders` that stores information about customer orders. We want to assign a unique order number to each order within each customer's partition based on the order date.

Table: `orders`

| order_id | customer_id | order_date  |
|----------|-------------|-------------|
| 1        | 101         | 2023-08-01  |
| 2        | 101         | 2023-08-03  |
| 3        | 102         | 2023-08-02  |
| 4        | 102         | 2023-08-04  |
| 5        | 101         | 2023-08-05  |

We can use the `ROW_NUMBER()` function to assign a unique order number within each customer's partition based on the order date. The `PARTITION BY` clause divides the result set into partitions, and the `ORDER BY` clause specifies the order within each partition.

Here's the SQL query using the `ROW_NUMBER()` function:

```sql
SELECT 
    order_id, 
    customer_id, 
    order_date, 
    ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date) AS order_number
FROM orders;
```

The output of the query would be:

| order_id | customer_id | order_date  | order_number |
|----------|-------------|-------------|--------------|
| 1        | 101         | 2023-08-01  | 1            |
| 2        | 101         | 2023-08-03  | 2            |
| 5        | 101         | 2023-08-05  | 3            |
| 3        | 102         | 2023-08-02  | 1            |
| 4        | 102         | 2023-08-04  | 2            |

Explanation:
- For customer with `customer_id` 101, the orders are sorted by `order_date`. The first order (order_id 1) gets assigned the order number 1, the second order (order_id 2) gets assigned the order number 2, and so on.
- Similarly, for customer with `customer_id` 102, the orders are sorted by `order_date`. The first order (order_id 3) gets assigned the order number 1, and the second order (order_id 4) gets assigned the order number 2.

The `ROW_NUMBER()` function assigns a unique order number to each row within each customer's partition based on the specified order, providing a way to identify the sequence of orders for each customer.

- `RANK()`: Assigns a unique rank to each distinct value in the ordered partition, with gaps for duplicate values.

Suppose we have a table named `scores` that stores the scores of students in a quiz. We want to rank the students based on their scores, and in case of tie scores, we want to assign the same rank to those students and leave gaps for the next rank.

Table: `scores`

| student_id | score |
|------------|-------|
| 1          | 90    |
| 2          | 85    |
| 3          | 92    |
| 4          | 90    |
| 5          | 88    |
| 6          | 85    |

We can use the `RANK()` function to assign a unique rank to each distinct score within the ordered partition of students based on their scores. The `ORDER BY` clause specifies the order based on which the ranking is determined.

Here's the SQL query using the `RANK()` function:

```sql
SELECT 
    student_id, 
    score,
    RANK() OVER(ORDER BY score DESC) AS rank
FROM scores;
```

The output of the query would be:

| student_id | score | rank |
|------------|-------|------|
| 3          | 92    | 1    |
| 1          | 90    | 2    |
| 4          | 90    | 2    |
| 5          | 88    | 4    |
| 2          | 85    | 5    |
| 6          | 85    | 5    |

Explanation:
- The `RANK()` function assigns a unique rank to each distinct score within the ordered partition (the entire result set in this case) based on the descending order of scores.
- Since there are two students with a score of 90, they share the rank 2, and the next rank is skipped (gap). Similarly, there are two students with a score of 85, and they share the rank 5.
- The highest score (92) receives rank 1, and the scores are ranked in descending order.

The `RANK()` function provides a way to rank the values in a specific order, handling ties and leaving gaps for the next rank, as shown in the output.

- `DENSE_RANK()`: Assigns a rank to every row within its partition based on the ORDER BY clause. It assigns the same rank to the rows with equal values. If two or more rows have the same rank, then there will be no gaps in the sequence of ranked values.

The `DENSE_RANK()` function assigns a unique rank to each distinct value in the ordered partition, without leaving gaps for duplicate values.

Table: `scores`

| student_id | score |
|------------|-------|
| 1          | 90    |
| 2          | 85    |
| 3          | 92    |
| 4          | 90    |
| 5          | 88    |
| 6          | 85    |

Here's the SQL query using the `DENSE_RANK()` function:

```sql
SELECT 
    student_id, 
    score,
    DENSE_RANK() OVER(ORDER BY score DESC) AS dense_rank
FROM scores;
```

The output of the query would be:

| student_id | score | dense_rank |
|------------|-------|------------|
| 3          | 92    | 1          |
| 1          | 90    | 2          |
| 4          | 90    | 2          |
| 5          | 88    | 3          |
| 2          | 85    | 4          |
| 6          | 85    | 4          |

Explanation:
- The `DENSE_RANK()` function assigns a unique rank to each distinct score within the ordered partition (the entire result set in this case) based on the descending order of scores.
- Unlike the `RANK()` function, `DENSE_RANK()` does not leave gaps for duplicate values. So, both students with a score of 90 share the rank 2, and the next rank is 3 for the next distinct score.
- The highest score (92) receives rank 1, and the scores are ranked in descending order.

In this example, the `DENSE_RANK()` function assigns ranks without gaps for duplicate values, resulting in consecutive rank numbers.

- `SUM()`, `AVG()`, `MIN()`, `MAX()`: Perform calculations on a range of rows within a partition.
Certainly! Let's use the `SUM()`, `AVG()`, `MIN()`, and `MAX()` functions in a practical example. Suppose we have a table named `sales` that stores information about sales transactions, including the `product_id`, `sale_amount`, and `sale_date`. We want to calculate the total sales amount, average sale amount, minimum sale amount, and maximum sale amount for each product within a specified time period.

Table: `sales`

| product_id | sale_amount | sale_date  |
|------------|-------------|-------------|
| 1          | 100         | 2023-08-01  |
| 1          | 120         | 2023-08-02  |
| 2          | 150         | 2023-08-01  |
| 2          | 200         | 2023-08-03  |
| 1          | 80          | 2023-08-03  |

We can use the `SUM()`, `AVG()`, `MIN()`, and `MAX()` functions along with the `PARTITION BY` clause to calculate these aggregate values within each product's partition, considering only the sales within a specified time period (e.g., August 2023).

Here's the SQL query using these functions:

```sql
SELECT 
    product_id, 
    SUM(sale_amount) OVER(PARTITION BY product_id) AS total_sales,
    AVG(sale_amount) OVER(PARTITION BY product_id) AS avg_sale,
    MIN(sale_amount) OVER(PARTITION BY product_id) AS min_sale,
    MAX(sale_amount) OVER(PARTITION BY product_id) AS max_sale
FROM sales
WHERE sale_date BETWEEN '2023-08-01' AND '2023-08-31';
```

The output of the query would be:

| product_id | total_sales | avg_sale | min_sale | max_sale |
|------------|-------------|----------|----------|----------|
| 1          | 300         | 100      | 80       | 120      |
| 1          | 300         | 100      | 80       | 120      |
| 1          | 300         | 100      | 80       | 120      |
| 2          | 350         | 175      | 150      | 200      |

Explanation:
- The `SUM(sale_amount)` function calculates the total sales amount for each product within the specified time period.
- The `AVG(sale_amount)` function calculates the average sale amount for each product within the specified time period.
- The `MIN(sale_amount)` function calculates the minimum sale amount for each product within the specified time period.
- The `MAX(sale_amount)` function calculates the maximum sale amount for each product within the specified time period.
- The `PARTITION BY product_id` divides the calculation into separate partitions for each product.

In this example, the query provides a comprehensive summary of the sales performance for each product within the specified time period, including total sales, average sale, minimum sale, and maximum sale.

- `LEAD()`: Returns the value of the Nth row after the current row in a partition. It returns NULL if no subsequent row exists.

Sure! Let's use the `LEAD()` function in a practical example. Suppose we have a table named `employee_sales` that stores information about employee sales data, including the `employee_id`, `sale_amount`, and `sale_date`. We want to calculate the sale amount for the next day's sales for each employee within a specific time period.

Table: `employee_sales`

| employee_id | sale_amount | sale_date  |
|-------------|-------------|-------------|
| 1           | 100         | 2023-08-01 |
| 1           | 120         | 2023-08-02 |
| 1           | 80          | 2023-08-03 |
| 2           | 150         | 2023-08-01 |
| 2           | 200         | 2023-08-03 |
| 2           | 120         | 2023-08-04 |

We can use the `LEAD()` function to calculate the sale amount for the next day's sales for each employee within the specified time period.

Here's the SQL query using the `LEAD()` function:

```sql
SELECT 
    employee_id, 
    sale_amount,
    LEAD(sale_amount) OVER(PARTITION BY employee_id ORDER BY sale_date) AS next_day_sale
FROM employee_sales
WHERE sale_date BETWEEN '2023-08-01' AND '2023-08-03';
```

The output of the query would be:

| employee_id | sale_amount | next_day_sale |
|-------------|-------------|---------------|
| 1           | 100         | 120           |
| 1           | 120         | 80            |
| 2           | 150         | 200           |
| 2           | 200         | NULL          |

Explanation:
- The `LEAD(sale_amount)` function calculates the sale amount for the next day's sales for each employee within the specified time period.
- The `PARTITION BY employee_id` divides the calculation into separate partitions for each employee.
- The `ORDER BY sale_date` specifies the order based on which the next day's sale is determined.

In this example, the query provides the sale amount for each employee's next day's sales within the specified time period. Note that for the last row of employee 2, there's no subsequent row (next day) within the specified time period, so it returns `NULL`.

- `LAG()`: Returns the value of the Nth row before the current row in a partition. It returns NULL if no preceding row exists.

Sure! Let's use the `LAG()` function in a practical example. Suppose we have a table named `stock_prices` that stores daily stock prices for a particular stock, including the `stock_id`, `price`, and `date`. We want to calculate the change in stock price from the previous day for each stock within a specific time period.

Table: `stock_prices`

| stock_id | price | date       |
|----------|-------|------------|
| 1        | 100   | 2023-08-01 |
| 1        | 120   | 2023-08-02 |
| 1        | 80    | 2023-08-03 |
| 2        | 150   | 2023-08-01 |
| 2        | 200   | 2023-08-03 |
| 2        | 120   | 2023-08-04 |

We can use the `LAG()` function to calculate the change in stock price from the previous day's price for each stock within the specified time period.

Here's the SQL query using the `LAG()` function:

```sql
SELECT 
    stock_id, 
    price,
    LAG(price) OVER(PARTITION BY stock_id ORDER BY date) AS previous_day_price
FROM stock_prices
WHERE date BETWEEN '2023-08-02' AND '2023-08-04';
```

The output of the query would be:

| stock_id | price | previous_day_price |
|----------|-------|--------------------|
| 1        | 120   | 100                |
| 1        | 80    | 120                |
| 2        | 200   | 150                |
| 2        | 120   | 200                |

Explanation:
- The `LAG(price)` function calculates the price of the stock from the previous day for each stock within the specified time period.
- The `PARTITION BY stock_id` divides the calculation into separate partitions for each stock.
- The `ORDER BY date` specifies the order based on which the previous day's price is determined.

In this example, the query provides the change in stock price from the previous day's price for each stock within the specified time period. Note that for the first day of each stock, there's no preceding row (previous day) within the specified time period, so it returns `NULL`.

- `FIRST_VALUE()` and `LAST_VALUE()`: Access the value of the first or last row within a partition.

Sure! Let's use the `FIRST_VALUE()` and `LAST_VALUE()` functions in a practical example. Suppose we have a table named `orders` that stores information about customer orders, including the `order_id`, `customer_id`, and `order_date`. We want to find the first and last order dates for each customer within a specific time period.

Table: `orders`

| order_id | customer_id | order_date  |
|----------|-------------|-------------|
| 1        | 101         | 2023-08-01  |
| 2        | 101         | 2023-08-03  |
| 3        | 102         | 2023-08-02  |
| 4        | 102         | 2023-08-04  |
| 5        | 101         | 2023-08-05  |

We can use the `FIRST_VALUE()` and `LAST_VALUE()` functions to find the first and last order dates for each customer within the specified time period.

Here's the SQL query using these functions:

```sql
SELECT DISTINCT
    customer_id, 
    FIRST_VALUE(order_date) OVER(PARTITION BY customer_id ORDER BY order_date) AS first_order_date,
    LAST_VALUE(order_date) OVER(PARTITION BY customer_id ORDER BY order_date ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_order_date
FROM orders
WHERE order_date BETWEEN '2023-08-01' AND '2023-08-31';
```

The output of the query would be:

| customer_id | first_order_date | last_order_date |
|-------------|------------------|-----------------|
| 101         | 2023-08-01       | 2023-08-05      |
| 102         | 2023-08-02       | 2023-08-04      |

Explanation:
- The `FIRST_VALUE(order_date)` function calculates the first order date for each customer within the specified time period.
- The `LAST_VALUE(order_date) ... ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING` function calculates the last order date for each customer within the specified time period. The `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING` specifies that the window frame includes all rows within the partition.
- The `PARTITION BY customer_id` divides the calculation into separate partitions for each customer.

In this example, the query provides the first and last order dates for each customer within the specified time period. The `FIRST_VALUE()` function provides the first order date, and the `LAST_VALUE()` function provides the last order date for each customer.

- `CUME_DIST`: Calculates the cumulative distribution of a value in a set of values.

Sure! Let's use the `CUME_DIST()` function in a practical example. Suppose we have a table named `test_scores` that stores test scores for a group of students. We want to calculate the cumulative distribution of each student's test score within the group.

Table: `test_scores`

| student_id | test_score |
|------------|------------|
| 1          | 90         |
| 2          | 85         |
| 3          | 92         |
| 4          | 90         |
| 5          | 88         |
| 6          | 85         |

We can use the `CUME_DIST()` function to calculate the cumulative distribution of each student's test score within the group.

Here's the SQL query using the `CUME_DIST()` function:

```sql
SELECT 
    student_id, 
    test_score,
    CUME_DIST() OVER(ORDER BY test_score DESC) AS cumulative_distribution
FROM test_scores;
```

The output of the query would be:

| student_id | test_score | cumulative_distribution |
|------------|------------|-------------------------|
| 3          | 92         | 0.3333333333333333      |
| 1          | 90         | 0.8333333333333334      |
| 4          | 90         | 0.8333333333333334      |
| 5          | 88         | 1.0                     |
| 2          | 85         | 1.0                     |
| 6          | 85         | 1.0                     |

Explanation:
- The `CUME_DIST()` function calculates the cumulative distribution of each test score within the group.
- The `ORDER BY test_score DESC` specifies the order based on which the cumulative distribution is determined.
- The function returns a value between 0 and 1, representing the cumulative distribution of each test score relative to the other test scores in the group.

In this example, the query provides the cumulative distribution of each student's test score within the group. The highest test score (92) has a cumulative distribution of approximately 0.33, meaning that it is greater than approximately 33% of the other test scores in the group. Similarly, test scores of 90 have a cumulative distribution of approximately 83%, and test scores of 88 and 85 have a cumulative distribution of 100% since they are the lowest scores in the group.

- `PERCENT_RANK`: Calculates the percentile rank of a row in a partition or result set.

Let's use the `PERCENT_RANK()` function in a practical example. Suppose we have a table named `exam_scores` that stores exam scores for a group of students. We want to calculate the percentile rank of each student's exam score within the group.

Table: `exam_scores`

| student_id | exam_score |
|------------|------------|
| 1          | 90         |
| 2          | 85         |
| 3          | 92         |
| 4          | 90         |
| 5          | 88         |
| 6          | 85         |

We can use the `PERCENT_RANK()` function to calculate the percentile rank of each student's exam score within the group.

Here's the SQL query using the `PERCENT_RANK()` function:

```sql
SELECT 
    student_id, 
    exam_score,
    PERCENT_RANK() OVER(ORDER BY exam_score DESC) AS percentile_rank
FROM exam_scores;
```

The output of the query would be:

| student_id | exam_score | percentile_rank |
|------------|------------|-----------------|
| 3          | 92         | 0.2             |
| 1          | 90         | 0.4             |
| 4          | 90         | 0.4             |
| 5          | 88         | 0.6             |
| 2          | 85         | 0.8             |
| 6          | 85         | 0.8             |

Explanation:
- The `PERCENT_RANK()` function calculates the percentile rank of each exam score within the group.
- The `ORDER BY exam_score DESC` specifies the order based on which the percentile rank is determined.
- The function returns a value between 0 and 1, representing the percentile rank of each exam score relative to the other exam scores in the group.

In this example, the query provides the percentile rank of each student's exam score within the group. The highest exam score (92) has a percentile rank of 0.2, meaning that it is in the top 20% of the exam scores in the group. Similarly, exam scores of 90 have a percentile rank of 0.4, indicating they are in the top 40%, and exam scores of 88 and 85 have a percentile rank of 0.6 and 0.8, respectively, indicating they are in the top 60% and 80% of the exam scores in the group.

- `NTH_VALUE`: Returns value of argument from Nth row of the window frame

Certainly! Let's use the `NTH_VALUE()` function in a practical example. Suppose we have a table named `sales` that stores sales data for a group of products, including the `product_id`, `sales_amount`, and `sales_date`. We want to find the third highest sales amount for each product.

Table: `sales`

| product_id | sales_amount | sales_date  |
|------------|--------------|-------------|
| 1          | 100          | 2023-08-01  |
| 1          | 120          | 2023-08-02  |
| 1          | 80           | 2023-08-03  |
| 2          | 150          | 2023-08-01  |
| 2          | 200          | 2023-08-03  |
| 2          | 120          | 2023-08-04  |

We can use the `NTH_VALUE()` function to find the third highest sales amount for each product.

Here's the SQL query using the `NTH_VALUE()` function:

```sql
SELECT 
    product_id, 
    NTH_VALUE(sales_amount, 3) OVER(PARTITION BY product_id ORDER BY sales_amount DESC) AS third_highest_sales_amount
FROM sales;
```

The output of the query would be:

| product_id | third_highest_sales_amount |
|------------|---------------------------|
| 1          | 80                        |
| 1          | 100                       |
| 1          | 120                       |
| 2          | 120                       |
| 2          | 150                       |
| 2          | 200                       |

Explanation:
- The `NTH_VALUE(sales_amount, 3)` function calculates the third highest sales amount for each product.
- The `PARTITION BY product_id` divides the calculation into separate partitions for each product.
- The `ORDER BY sales_amount DESC` specifies the order based on which the third highest sales amount is determined.

In this example, the query provides the third highest sales amount for each product. The `NTH_VALUE()` function retrieves the sales amount at the third position in the ordered list of sales amounts for each product. Note that if there are fewer than three sales amounts for a product, the function may return a value from a different position in the list, or it may return `NULL` if there are not enough values to calculate the third highest sales amount.

- `NTILE(n)`: Divides rows into approximately equal parts (tiles) based on the specified integer n.

Sure! Let's use the `NTILE()` function in a practical example. Suppose we have a table named `employee_salaries` that stores salary information for a group of employees, including the `employee_id`, `salary`, and `department_id`. We want to divide employees into 4 groups based on their salaries, with each group having approximately equal numbers of employees.

Table: `employee_salaries`

| employee_id | salary | department_id |
|-------------|--------|---------------|
| 1           | 50000  | 1             |
| 2           | 60000  | 2             |
| 3           | 55000  | 1             |
| 4           | 70000  | 2             |
| 5           | 45000  | 1             |
| 6           | 80000  | 2             |

We can use the `NTILE()` function to divide employees into 4 groups based on their salaries.

Here's the SQL query using the `NTILE()` function:

```sql
SELECT 
    employee_id, 
    salary,
    department_id,
    NTILE(4) OVER(ORDER BY salary) AS salary_group
FROM employee_salaries;
```

The output of the query would be:

| employee_id | salary | department_id | salary_group |
|-------------|--------|---------------|--------------|
| 5           | 45000  | 1             | 1            |
| 1           | 50000  | 1             | 1            |
| 3           | 55000  | 1             | 2            |
| 2           | 60000  | 2             | 2            |
| 4           | 70000  | 2             | 3            |
| 6           | 80000  | 2             | 4            |

Explanation:
- The `NTILE(4)` function divides employees into 4 groups based on their salaries.
- The `ORDER BY salary` specifies the order based on which the employees are divided into salary groups.
- Each salary group contains approximately the same number of employees, with the lower salaries assigned to lower groups and the higher salaries assigned to higher groups.

In this example, the query provides the salary group for each employee based on their salary. The `NTILE()` function assigns each employee to one of four salary groups, ensuring that each group contains approximately an equal number of employees.


**4. String Functions:**
   These functions operate on string values and are often used for text manipulation and formatting. Examples include `SUBSTRING`, `LEFT`, `RIGHT`, `TRIM`, `REPLACE`.

```
-- SUBSTRING function to extract a substring
SELECT SUBSTRING('Hello World', 7);  -- Output: 'World'

-- TRIM function to remove leading and trailing spaces
SELECT TRIM('   Text   ');  -- Output: 'Text'

-- REPLACE function to replace a substring
SELECT REPLACE('Hello', 'H', 'J');  -- Output: 'Jello'
```

Other important string functions and the operations they perform are:

- `CONCAT`: Concatenate two or more strings into a single string
- `INSTR`: Return the position of the first occurrence of a substring in a string
- `LENGTH`: Get the length of a string in bytes and in characters
- `LEFT`: Get a specified number of leftmost characters from a string
- `LOWER`: Convert a string to lowercase
- `LTRIM`: Remove all leading spaces from a string
- `REPLACE`: Search and replace a substring in a string
- `RIGHT`: Get a specified number of rightmost characters from a string
- `RTRIM`: Remove all trailing spaces from a string
- `SUBSTRING`: Extract a substring starting from a position with a specific length.
- `TRIM`: Remove unwanted characters from a string.
- `UPPER`: Convert a string to uppercase
- `FIND_IN_SET`: Find a string within a comma-separated list of strings
- `FORMAT`: Format a number with a specific locale, rounded to the number of decimals
- `SUBSTRING_INDEX`: Return a substring from a string before a specified number of occurrences of a delimiter

Here are examples for the usage of the above string functions on the string, `Hello World`:

```
-- CONCAT - Concatenate two or more strings into a single string
SELECT CONCAT('Hello', ' ', 'World!') AS concatenated_string;		# Output: concatenated_string: Hello World!

-- INSTR - Return the position of the first occurrence of a substring in a string
SELECT INSTR('Hello World!', 'World') AS position;		# Output: position: 7	

-- LENGTH - Get the length of a string in bytes and in characters
SELECT LENGTH('Hello World!') AS length_bytes, CHAR_LENGTH('Hello World!') AS length_characters;	# Output: length_bytes: 12, length_characters: 12

-- LEFT - Get a specified number of leftmost characters from a string
SELECT LEFT('Hello World!', 5) AS leftmost_characters;		# Output: leftmost_characters: Hello

-- LOWER - Convert a string to lowercase
SELECT LOWER('Hello World!') AS lowercase_string;	# Output: lowercase_string: hello world!

-- LTRIM - Remove all leading spaces from a string
SELECT LTRIM('   Hello World!') AS trimmed_string;	# Output: trimmed_string: Hello World!

-- REPLACE - Search and replace a substring in a string
SELECT REPLACE('Hello World!', 'World', 'Universe') AS replaced_string;		# Output: replaced_string: Hello Universe!

-- RIGHT - Get a specified number of rightmost characters from a string
SELECT RIGHT('Hello World!', 6) AS rightmost_characters;	# Output: rightmost_characters: World!

-- RTRIM - Remove all trailing spaces from a string
SELECT RTRIM('Hello World!    ') AS trimmed_string;		# Output: trimmed_string: Hello World!

-- SUBSTRING - Extract a substring starting from a position with a specific length
SELECT SUBSTRING('Hello World!', 7, 5) AS extracted_substring;		# Output: extracted_substring: World

-- TRIM - Remove unwanted characters from a string
SELECT TRIM('   Hello World!   ') AS trimmed_string;		# Output: trimmed_string: Hello World!

-- UPPER - Convert a string to uppercase
SELECT UPPER('Hello World!') AS uppercase_string;		# Output: uppercase_string: HELLO WORLD!

-- FIND_IN_SET - Find a string within a comma-separated list of strings
SELECT FIND_IN_SET('apple', 'banana,apple,orange') AS position_in_list;		# Output: position_in_list: 2

-- FORMAT - Format a number with a specific locale, rounded to the number of decimals
SELECT FORMAT(12345.6789, 2, 'en_US') AS formatted_number;		# Output: formatted_number: 12,345.68

-- SUBSTRING_INDEX - Return a substring from a string before a specified number of occurrences of a delimiter
SELECT SUBSTRING_INDEX('apple,banana,orange', ',', 2) AS substring_before_second_comma;		# Output: substring_before_second_comma: apple,banana
```

**5. Mathematical Functions:**
   These functions perform mathematical operations on numeric values. Examples include `ABS`, `SQUARE`, `POWER`, `SQRT`.

```
-- ABS function to get the absolute value
SELECT ABS(-10);  -- Output: 10

-- POWER function to calculate power
SELECT POWER(2, 3);  -- Output: 8

-- SQRT function to calculate square root
SELECT SQRT(25);  -- Output: 5
```

Other common mathematical functions are:

- `ABS()`: Returns the absolute value of a number
- `CEIL()`: Returns the smallest integer value greater than or equal to the input number (n).
- `FLOOR()`: Returns the largest integer value not greater than the argument
- `MOD()`: Returns the remainder of a number divided by another
- `ROUND()`: Rounds a number to a specified number of decimal places.
- `POWER()`: Returns the argument raised to the specified power
- `TRUNCATE()`: Truncates a number to a specified number of decimal places
- `SQRT(n)`: Returns the square root of n
- `ACOS(n)`: Returns the arc cosine of n or null if n is not in the range -1 and 1.
- `ASIN(n)`: Returns the arcsine of n which is the value whose sine is n. It returns null if n is not in the range -1 to 1.
- `ATAN()`: Returns the arctangent of n.
- `ATAN2(n,m), ATAN(m,n)`: Returns the arctangent of the two variables n and m
- `CONV(n,from_base,to_base)`: Converts a number between different number bases
- `COS(n)`:	Returns the cosine of n, where n is in radians
- `COT(n)`: Returns the cotangent of n.
- `CRC32()`: Computes a cyclic redundancy check value and returns a 32-bit unsigned value
- `DEGREES(n)`: Converts radians to degrees of the argument n
- `EXP(n)`: Raises to the power of e raised to the power of n
- `LN(n)`: Returns the natural logarithm of n
- `LOG(n)`: Returns the natural logarithm of the first argument
- `LOG10()`: Returns the base-10 logarithm of the argument
- `LOG2()`: Returns the base-2 logarithm of the argument
- `PI()`: Returns the value of PI
- `POW()`: Returns the argument raised to the specified power
- `RADIANS()`: Returns argument converted to radians
- `RAND()`: Returns a random floating-point value
- `SIGN(n)`: Returns the sign of n that can be -1, 0, or 1 depending on whether n is negative, zero, or positive.
- `SIN(n)`: Returns the sine of n
- `TAN(n)`: Returns the tangent of n

Example operations of the above mathematical functions along with their output are:

```
-- ABS() - Returns the absolute value of a number
SELECT ABS(-5) AS absolute_value;

-- CEIL() - Returns the smallest integer value greater than or equal to the input number
SELECT CEIL(3.14) AS ceil_value;

-- FLOOR() - Returns the largest integer value not greater than the argument
SELECT FLOOR(3.14) AS floor_value;

-- MOD() - Returns the remainder of a number divided by another
SELECT MOD(10, 3) AS modulo_result;

-- ROUND() - Rounds a number to a specified number of decimal places
SELECT ROUND(3.14159, 2) AS rounded_value;

-- POWER() - Returns the argument raised to the specified power
SELECT POWER(2, 3) AS power_result;

-- TRUNCATE() - Truncates a number to a specified number of decimal places
SELECT TRUNCATE(3.14159, 2) AS truncated_value;

-- SQRT() - Returns the square root of n
SELECT SQRT(25) AS square_root;

-- ACOS() - Returns the arc cosine of n
SELECT ACOS(0.5) AS arc_cosine;

-- ASIN() - Returns the arcsine of n
SELECT ASIN(0.5) AS arc_sine;

-- ATAN() - Returns the arctangent of n
SELECT ATAN(1) AS arc_tangent;

-- ATAN2() - Returns the arctangent of two variables
SELECT ATAN2(1, 1) AS arc_tangent_2;

-- COS() - Returns the cosine of n
SELECT COS(0) AS cosine;

-- COT() - Returns the cotangent of n
SELECT COT(1) AS cotangent;

-- CRC32() - Computes a cyclic redundancy check value
SELECT CRC32('Hello World!') AS crc32_value;

-- DEGREES() - Converts radians to degrees
SELECT DEGREES(1.5708) AS degrees;

-- EXP() - Raises to the power of e raised to the power of n
SELECT EXP(1) AS exponent;

-- LN() - Returns the natural logarithm of n
SELECT LN(2.71828) AS natural_logarithm;

-- LOG() - Returns the natural logarithm of the first argument
SELECT LOG(10) AS logarithm;

-- LOG10() - Returns the base-10 logarithm of the argument
SELECT LOG10(100) AS base_10_logarithm;

-- LOG2() - Returns the base-2 logarithm of the argument
SELECT LOG2(8) AS base_2_logarithm;

-- PI() - Returns the value of PI
SELECT PI() AS pi_value;

-- RADIANS() - Returns argument converted to radians
SELECT RADIANS(180) AS radians;

-- RAND() - Returns a random floating-point value
SELECT RAND() AS random_value;

-- SIGN() - Returns the sign of n
SELECT SIGN(-5) AS sign_value;

-- SIN() - Returns the sine of n
SELECT SIN(0) AS sine;

-- TAN() - Returns the tangent of n
SELECT TAN(0) AS tangent;
```

Output is:
```
absolute_value: 5
ceil_value: 4
floor_value: 3
modulo_result: 1
rounded_value: 3.14
power_result: 8
truncated_value: 3.14
square_root: 5
arc_cosine: 1.0471975511966
arc_sine: 0.5235987755983
arc_tangent: 0.7853981633974
arc_tangent_2: 0.7853981633974
cosine: 1
cotangent: 0.64209261593433
crc32_value: 1414054756
degrees: 90
exponent: 2.718281828459
natural_logarithm: 0.99999932734728
logarithm: 2.302585092994
base_10_logarithm: 2
base_2_logarithm: 3
pi_value: 3.1415926535898
radians: 3.1415926535898
random_value: [random float]
sign_value: -1
sine: 0
tangent: 0
```

**6. Conversion Functions:**

- These functions converts a value into the specified datatype or character set. Examples include `CAST`, `CONVERT`.
- The syntax for cast is:
```
CAST(value AS datatype)
```

- The syntax for convert is:
```
CONVERT(value, type)
```

```
-- CAST function to convert a value to a specified data type
SELECT CAST('123' AS SIGNED);  -- Output: 123

-- Convert a value to a TIME datatype:
SELECT CAST("14:06:10" AS TIME);      -- Output: 14:06:10

-- Convert a value to a SIGNED datatype:
SELECT CAST(5-10 AS SIGNED);      -- Output: -5

-- Convert a value to CHAR datatype:
SELECT CONVERT(150, CHAR);      -- Output: 150

-- Convert a value to a TIME datatype:
SELECT CONVERT("14:06:10", TIME);      -- Output: 14:06:10

-- CONVERT function to change data type
SELECT CONVERT('2023-08-04', DATE);  -- Output: '2023-08-04'
```

**7. Conditional Functions:**

- Conditional statements in MySQL refer to the use of control structures to conditionally execute code based on certain conditions.
- These statements are primarily used within SQL queries and stored procedures to determine the flow of the program and perform different actions depending on whether a specified condition is true or false.
- Examples include `CASE`, `COALESCE`, `NULLIF`, `IFNULL` and `IF`.


**CASE**

The CASE statement goes through conditions and return a value when the first condition is met (like an IF-THEN-ELSE statement). So, once a condition is true, it will stop reading and return the result.

If no conditions are true, it will return the value in the ELSE clause.

If there is no ELSE part and no conditions are true, it returns NULL.

```
-- CASE statement to conditionally return values
SELECT 
    order_id,
    CASE
        WHEN order_amount > 1000 THEN 'High'
        WHEN order_amount > 500 THEN 'Medium'
        ELSE 'Low'
    END AS order_priority
FROM orders;
```

The following SQL will order the customers by City. However, if City is NULL, then order by Country:
```
SELECT CustomerName, City, Country FROM Customers
ORDER BY (CASE
WHEN City IS NULL THEN Country
ELSE City
END);
```

**COALESCE Function:**

The `COALESCE` function returns the first non-null expression from a list of expressions. It's often used to provide a fallback value when a column might be null.

Select first non-null value in a list
```sql
SELECT COALESCE(NULL, 1, 2, 'W3Schools.com');      # Output: 1
```

Example: Conside the table `employees` with the following data:

| id | first_name | last_name | salary   | hire_date  |
|----|------------|-----------|----------|------------|
| 1  | John       | Doe       | 50000.00 | 2020-03-15 |
| 2  | Jane       | Smith     | NULL     | 2021-01-10 |
| 3  | Michael    | Johnson   | 75000.00 | 2022-06-20 |

Suppose we want to retrieve the employee names and their salaries, but if the salary is null, we want to display "Salary not available". We can use COALESCE for this purpose:

```
SELECT 
    first_name, 
    last_name, 
    COALESCE(CAST(salary AS VARCHAR), 'Salary not available') AS formatted_salary
FROM employees;
```

The output would be:

```
| first_name | last_name | formatted_salary   |
|------------|-----------|--------------------|
| John       | Doe       | 50000.00           |
| Jane       | Smith     | Salary not available |
| Michael    | Johnson   | 75000.00           |
```

Suppose you have a table named `students` with columns `student_id`, `first_name`, and `last_name`. Some students have provided a middle name, while others have not. You want to display the full name for each student, including the middle name if available.

Table: students

| student_id | first_name | middle_name | last_name |
|------------|------------|-------------|-----------|
| 1          | John       | William     | Smith     |
| 2          | Mary       | NULL        | Johnson   |
| 3          | Robert     | Alexander   | Brown     |
| 4          | Emily      | NULL        | Davis     |

Using the `COALESCE` function:

```sql
SELECT student_id, COALESCE(middle_name, first_name) AS full_name
FROM students;
```

Expected Output:

| student_id | full_name     |
|------------|---------------|
| 1          | John William  |
| 2          | Mary          |
| 3          | Robert Alexander |
| 4          | Emily         |

In this example, the `COALESCE` function returns the middle name if it's available, otherwise, it returns the first name. The result is a full name for each student.

**NULLIF Function:**

- The `NULLIF` function compares two expressions and returns `null` if they are equal; otherwise, it returns the first expression.
- It's often used to handle cases where you want to replace a specific value with `NULL`.

Syntax:
```sql
NULLIF(expression1, expression2)
```

Example:
```sql
SELECT NULLIF("Hello", "world");      # Output: Hello
```

Let's consider the same employees table from the previous example, with the following data:

| id | first_name | last_name | salary   | hire_date  |
|----|------------|-----------|----------|------------|
| 1  | John       | Doe       | 50000.00 | 2020-03-15 |
| 2  | Jane       | Smith     | NULL     | 2021-01-10 |
| 3  | Michael    | Johnson   | 75000.00 | 2022-06-20 |

Suppose we want to retrieve the salaries of employees but replace any salary value of 75000.00 with NULL. We can use the NULLIF function for this purpose:

```
SELECT 
    first_name, 
    last_name, 
    NULLIF(salary, 75000.00) AS adjusted_salary
FROM employees;
```

In this query, we're using NULLIF to check if the salary column equals 75000.00. If it does, the function returns NULL; otherwise, it returns the actual value of the salary column.

The output of this query would be:
```
| first_name | last_name | adjusted_salary |
|------------|-----------|-----------------|
| John       | Doe       | 50000.00        |
| Jane       | Smith     | NULL            |
| Michael    | Johnson   | NULL            |
```

As you can see, the adjusted_salary column contains NULL values for employees whose salary was originally 75000.00, while the other salaries remain unchanged.



Suppose you have a table named `products` with columns `product_id`, `product_name`, and `discount_percentage`. Some products have a discount applied, while others do not. You want to display the discount percentage for each product, or "No discount" if there's no discount.

Table: products

| product_id | product_name | discount_percentage |
|------------|--------------|---------------------|
| 101        | Laptop       | 10                  |
| 102        | Smartphone   | NULL                |
| 103        | Headphones   | 5                   |
| 104        | Keyboard     | NULL                |

Using the `IFNULL` function:

```sql
SELECT product_id, IFNULL(discount_percentage, 'No discount') AS discount_info
FROM products;
```

Expected Output:

| product_id | discount_info |
|------------|---------------|
| 101        | 10            |
| 102        | No discount   |
| 103        | 5             |
| 104        | No discount   |

In this example, the `IFNULL` function returns the discount percentage if it's available, otherwise, it returns "No discount". The result provides clear information about the discount for each product.


**IFNULL Function:**

- The IFNULL() function returns a specified value if the expression is NULL.
- If the expression is NOT NULL, this function returns the expression.
- It's similar to the COALESCE function but specifically designed for cases where you want to handle NULL values with a fallback.

Syntax (MySQL):
```sql
IFNULL(expression1, expression2)
```

Example:
```sql
SELECT IFNULL("Hello", "W3Schools.com");      # Output: Hello
SELECT IFNULL(NULL, 500);      # Output: 500
```

Let's use the same employees table:

| id | first_name | last_name | salary   | hire_date  |
|----|------------|-----------|----------|------------|
| 1  | John       | Doe       | 50000.00 | 2020-03-15 |
| 2  | Jane       | Smith     | NULL     | 2021-01-10 |
| 3  | Michael    | Johnson   | 75000.00 | 2022-06-20 |

Suppose we want to retrieve the employee names along with their salaries, but for employees with NULL salaries, we want to display "Salary not available" instead. We can use the IFNULL function for this purpose:

```
SELECT 
    first_name, 
    last_name, 
    IFNULL(CAST(salary AS VARCHAR), 'Salary not available') AS formatted_salary
FROM employees;
```

In this query, we're using `IFNULL` to check if the salary column is `NULL`. If it is, we're casting it to a string and displaying "Salary not available". If it's not `NULL`, we're displaying the actual salary.

The output of this query would be similar to the output when using `COALESCE`:

| first_name | last_name | formatted_salary   |
|------------|-----------|--------------------|
| John       | Doe       | 50000.00           |
| Jane       | Smith     | Salary not available |
| Michael    | Johnson   | 75000.00           |


**ISNULL Function:**

The ISNULL() function returns 1 or 0 depending on whether an expression is NULL.

If expression is NULL, this function returns 1. Otherwise, it returns 0.

```
SELECT ISNULL("");      # Output: 0
SELECT ISNULL("Hello world!");      # Output: 0
```

Let's consider the same `employees` table and data as before:

```
| id | first_name | last_name | salary   | hire_date  |
|----|------------|-----------|----------|------------|
| 1  | John       | Doe       | 50000.00 | 2020-03-15 |
| 2  | Jane       | Smith     | NULL     | 2021-01-10 |
| 3  | Michael    | Johnson   | 75000.00 | 2022-06-20 |
```

Suppose we want to retrieve the employee names along with their salaries, but for employees with `NULL` salaries, we want to display "Salary not available" instead. We can use the `ISNULL` function for this purpose:

```sql
SELECT 
    first_name, 
    last_name, 
    ISNULL(CAST(salary AS VARCHAR), 'Salary not available') AS formatted_salary
FROM employees;
```

In this query, we're using `ISNULL` to check if the `salary` column is `NULL`. If it is, we're casting it to a string and displaying "Salary not available". If it's not `NULL`, we're displaying the actual salary.

The output of this query would be similar to the output when using `COALESCE` and `IFNULL`:

```
| first_name | last_name | formatted_salary   |
|------------|-----------|--------------------|
| John       | Doe       | 50000.00           |
| Jane       | Smith     | Salary not available |
| Michael    | Johnson   | 75000.00           |
```

Just like `IFNULL`, `ISNULL` is specific to certain database systems (Microsoft SQL Server and Sybase), whereas `COALESCE` is more widely supported across different database systems.

These conditional functions allow you to make your SQL queries more flexible and adaptive to different situations. They can be used to generate computed columns, handle null values, and create custom result sets based on conditions. Remember that the specific syntax and availability of these functions may vary depending on the database system you are using.

**8. Special Functions:**
   Some databases provide functions specific to their features. For example, PostgreSQL has JSON functions for working with JSON data, while MySQL has spatial functions for geographical data.


**9. Scalar vs. Table-Valued Functions:**
   - Scalar functions return a single value.
   - Table-valued functions return a table as a result.

SQL functions play a crucial role in database queries and data manipulation. They help optimize queries, encapsulate logic, and make complex operations more manageable. Each database system may have variations in syntax and function availability, so it's important to consult the documentation specific to your chosen database.

**10. Commonly used functions:**

Examples for each of the SQL functions along with sample outputs:

- **BIT_AND() - Bitwise AND:**

Suppose you have a table named `bitwise_values` with a column named `bits`:

| bits  |
|-------|
| 101   |
| 110   |
| 011   |
| 111   |

```sql
-- Calculate bitwise AND of values in the 'bits' column
SELECT BIT_AND(bits) AS result
FROM bitwise_values;
```

Output: `001`

- **BIT_OR() - Bitwise OR:**

Using the same `bitwise_values` table:

```sql
-- Calculate bitwise OR of values in the 'bits' column
SELECT BIT_OR(bits) AS result
FROM bitwise_values;
```

Output: `111`

- **BIT_XOR() - Bitwise XOR:**

Using the same `bitwise_values` table:

```sql
-- Calculate bitwise XOR of values in the 'bits' column
SELECT BIT_XOR(bits) AS result
FROM bitwise_values;
```

Output: `000`

- **GROUP_CONCAT() - Concatenate Values:**

Suppose you have a table named `products` with a column named `product_name`:

| product_name |
|--------------|
| Laptop       |
| Smartphone   |
| Tablet       |
| TV           |

```sql
-- Concatenate product names into a single string
SELECT GROUP_CONCAT(product_name SEPARATOR ', ') AS concatenated_names
FROM products;
```

Output: `Laptop, Smartphone, Tablet, TV`

- **JSON_ARRAYAGG() - Aggregate JSON Arrays:**

Using the same `products` table:

```sql
-- Create a JSON array of product names
SELECT JSON_ARRAYAGG(product_name) AS json_array
FROM products;
```

Output: `["Laptop", "Smartphone", "Tablet", "TV"]`

- **JSON_OBJECTAGG() - Aggregate JSON Objects:**

Suppose you have a table named `employee_salaries` with columns `employee_name` and `salary`:

| employee_name | salary |
|---------------|--------|
| Alice         | 50000  |
| Bob           | 60000  |
| Carol         | 55000  |

```sql
-- Create a JSON object of employee names and salaries
SELECT JSON_OBJECTAGG(employee_name, salary) AS json_object
FROM employee_salaries;
```

Output: `{"Alice": 50000, "Bob": 60000, "Carol": 55000}`

- **STDDEV_POP() - Population Standard Deviation:**

Suppose you have a table named `exam_scores` with a column named `score`:

| score |
|-------|
| 85    |
| 90    |
| 78    |
| 92    |

```sql
-- Calculate population standard deviation of exam scores
SELECT STDDEV_POP(score) AS population_stddev
FROM exam_scores;
```

Output: `5.31128874068349`

- **STDDEV_SAMP() - Sample Standard Deviation:**

Using the same `exam_scores` table:

```sql
-- Calculate sample standard deviation of exam scores
SELECT STDDEV_SAMP(score) AS sample_stddev
FROM exam_scores;
```

Output: `5.37360333735491`

- **VAR_POP() - Population Variance:**

Using the same `exam_scores` table:

```sql
-- Calculate population variance of exam scores
SELECT VAR_POP(score) AS population_variance
FROM exam_scores;
```

Output: `28.1666666666667`

- **VARP_SAM() - Sample Variance:**

Using the same `exam_scores` table:

```sql
-- Calculate sample variance of exam scores
SELECT VAR_SAMP(score) AS sample_variance
FROM exam_scores;
```

Output: `28.9166666666667`


**11. Specifiers**

In SQL, specifiers are placeholders or format codes used within certain functions to indicate how values should be formatted or interpreted. They provide instructions to the database on how to process and display data. Specifiers are often used in functions that deal with data formatting, such as date and time formatting, number formatting, and string formatting. They are typically represented with a percent symbol (%) followed by a letter or symbol that defines the format or behavior to be applied.

Here are some common examples of specifiers in SQL:

**Date and Time Specifiers:**
   - `%Y`: Year with century (e.g., 2023).
   - `%m`: Month (01-12).
   - `%d`: Day of the month (01-31).
   - `%H`: Hour (00-23).
   - `%M`: Minute (00-59).
   - `%S`: Second (00-59).

**Number Specifiers:**
   - `%d`: Decimal (integer) value.
   - `%f`: Floating-point value with decimal places.
   - `%e` or `%E`: Scientific notation for floating-point numbers.

**String Specifiers:**
   - `%s`: String value.
   - `%c`: Character value.

**Width and Precision Specifiers:**
   - `%n.m`: Specifies the minimum width (n) and precision (m) for formatting.

**Alignment Specifiers:**
   - `%[flags]`: Flags for formatting, like left-align, right-align, etc.

**Boolean Specifiers:**
   - `%b`: Boolean value (some databases).

**Other Specifiers:**
   - `%p`: AM/PM indicator (for time formatting).
   - `%r`: 12-hour time format (for time formatting).

Here's an example of using specifiers in a query to format a date and time:

```sql
SELECT
    CONCAT(DATE_FORMAT(order_date, '%Y-%m-%d'), ' ', DATE_FORMAT(order_time, '%H:%i:%S')) AS formatted_datetime
FROM orders;
```

In this example, `%Y-%m-%d` and `%H:%i:%S` are specifiers used with the `DATE_FORMAT` function to format the `order_date` and `order_time` columns, respectively.

It's important to note that specifiers might vary slightly among different database systems (e.g., MySQL, PostgreSQL, SQL Server). Always refer to the documentation of the specific database you are using to ensure accurate usage of specifiers.

Please note that the actual outputs may vary based on your data and the specific database system you are using. The examples provided use general SQL syntax.


Other specifiers and their meaning:
- `%a`: Three-characters abbreviated weekday name e.g., Mon, Tue, Wed, etc.
- `%b`: Three-characters abbreviated month name e.g., Jan, Feb, Mar, etc.
- `%c`: Month in numeric e.g., 1, 2, 3…12
- `%D`: Day of the month with English suffix e.g., 0th, 1st, 2nd, etc.
- `%d`: Day of the month with leading zero if it is 1 number e.g., 00, 01,02, …31
- `%e`: Day of the month without leading zero e.g., 1,2,…31
- `%f`: Microseconds in the range of 000000..999999
- `%H`: Hour in 24-hour format with leading zero e.g., 00..23
- `%h`:	Hour in 12-hour format with leading zero e.g., 01, 02…12
- `%I`: Same as %h
- `%i`: Minutes with leading zero e.g., 00, 01,…59
- `%j`: Day of year with leading zero e.g., 001,002,…366
- `%k`: Hour in 24-hour format without leading zero e.g., 0,1,2…23
- `%l`: Hour in 12-hour format without leading zero e.g., 1,2…12
- `%M`: Full month name e.g., January, February,…December
- `%m`: Month name with leading zero e.g., 00,01,02,…12
- `%p`: AM or PM, depending on other time specifiers
- `%r`: Time in 12-hour format hh:mm:ss AM or PM
- `%S`: Seconds with leading zero 00,01,…59
- `%s`: Same as %S
- `%T`: Time in 24-hour format hh:mm:ss
- `%U`: Week number with leading zero when the first day of week is Sunday e.g., 00,01,02…53
- `%u`: Week number with leading zero when the first day of week is Monday e.g., 00,01,02…53
- `%V`: Same as %U; it is used with %X
- `%v`:	Same as %u; it is used with %x
- `%W`: Full name of weekday e.g., Sunday, Monday,…, Saturday
- `%w`: Weekday in number (0=Sunday, 1= Monday,etc.)
- `%X`: Year for the week in four digits where the first day of the week is Sunday; often used with %V
- `%x`: Year for the week, where the first day of the week is Monday, four digits; used with %v
- `%Y`: Four digits year e.g., 2000 and 2001.
- `%y`: Two digits year e.g., 10,11,and 12.
- `%%`: Add percentage (%) character to the output

Example usage of the above specifiers and their output:
```
SELECT
    DATE_FORMAT('2023-08-04 14:30:45', '%a') AS abbreviated_weekday,
    DATE_FORMAT('2023-08-04 14:30:45', '%b') AS abbreviated_month,
    DATE_FORMAT('2023-08-04 14:30:45', '%c') AS month_numeric,
    DATE_FORMAT('2023-08-04 14:30:45', '%D') AS day_with_suffix,
    DATE_FORMAT('2023-08-04 14:30:45', '%d') AS day_with_leading_zero,
    DATE_FORMAT('2023-08-04 14:30:45', '%e') AS day_without_leading_zero,
    DATE_FORMAT('2023-08-04 14:30:45', '%f') AS microseconds,
    DATE_FORMAT('2023-08-04 14:30:45', '%H') AS hour_24h_with_leading_zero,
    DATE_FORMAT('2023-08-04 14:30:45', '%h') AS hour_12h_with_leading_zero,
    DATE_FORMAT('2023-08-04 14:30:45', '%I') AS hour_12h_same_as_h,
    DATE_FORMAT('2023-08-04 14:30:45', '%i') AS minutes_with_leading_zero,
    DATE_FORMAT('2023-08-04 14:30:45', '%j') AS day_of_year_with_leading_zero,
    DATE_FORMAT('2023-08-04 14:30:45', '%k') AS hour_24h_without_leading_zero,
    DATE_FORMAT('2023-08-04 14:30:45', '%l') AS hour_12h_without_leading_zero,
    DATE_FORMAT('2023-08-04 14:30:45', '%M') AS full_month_name,
    DATE_FORMAT('2023-08-04 14:30:45', '%m') AS month_with_leading_zero,
    DATE_FORMAT('2023-08-04 14:30:45', '%p') AS am_pm_indicator,
    DATE_FORMAT('2023-08-04 14:30:45', '%r') AS time_12h_format,
    DATE_FORMAT('2023-08-04 14:30:45', '%S') AS seconds_with_leading_zero,
    DATE_FORMAT('2023-08-04 14:30:45', '%s') AS same_as_S,
    DATE_FORMAT('2023-08-04 14:30:45', '%T') AS time_24h_format,
    DATE_FORMAT('2023-08-04 14:30:45', '%U') AS week_number_sunday_start,
    DATE_FORMAT('2023-08-04 14:30:45', '%u') AS week_number_monday_start,
    DATE_FORMAT('2023-08-04 14:30:45', '%V') AS same_as_U_with_X,
    DATE_FORMAT('2023-08-04 14:30:45', '%v') AS same_as_u_with_x,
    DATE_FORMAT('2023-08-04 14:30:45', '%W') AS full_weekday_name,
    DATE_FORMAT('2023-08-04 14:30:45', '%w') AS weekday_numeric,
    DATE_FORMAT('2023-08-04 14:30:45', '%X') AS year_week_sunday_start,
    DATE_FORMAT('2023-08-04 14:30:45', '%x') AS year_week_monday_start,
    DATE_FORMAT('2023-08-04 14:30:45', '%Y') AS year_full,
    DATE_FORMAT('2023-08-04 14:30:45', '%y') AS year_short,
    DATE_FORMAT('2023-08-04 14:30:45', '%%') AS percentage
```

Output is:
```
abbreviated_weekday: Thu
abbreviated_month: Aug
month_numeric: 8
day_with_suffix: 4th
day_with_leading_zero: 04
day_without_leading_zero: 4
microseconds: 000000
hour_24h_with_leading_zero: 14
hour_12h_with_leading_zero: 02
hour_12h_same_as_h: 02
minutes_with_leading_zero: 30
day_of_year_with_leading_zero: 216
hour_24h_without_leading_zero: 14
hour_12h_without_leading_zero: 2
full_month_name: August
month_with_leading_zero: 08
am_pm_indicator: PM
time_12h_format: 02:30:45 PM
seconds_with_leading_zero: 45
same_as_S: 45
time_24h_format: 14:30:45
week_number_sunday_start: 31
week_number_monday_start: 31
same_as_U_with_X: 31
same_as_u_with_x: 31
full_weekday_name: Thursday
weekday_numeric: 4
year_week_sunday_start: 2023
year_week_monday_start: 2023
year_full: 2023
year_short: 23
percentage: %
```

Commonly used date format strings:

- `%Y-%m-%d`: 2013-07-04
- `%e/%c/%Y`: 4/7/2013
- `%c/%e/%Y`: 7/4/2013
- `%d/%m/%Y`: 4/7/2013
- `%m/%d/%Y`: 7/4/2013
- `%e/%c/%Y %H:%i`: 4/7/2013 11:20
- `%c/%e/%Y %H:%i`: 7/4/2013 11:20
- `%d/%m/%Y %H:%i`: 4/7/2013 11:20
- `%m/%d/%Y %H:%i`: 7/4/2013 11:20
- `%e/%c/%Y %T`: 4/7/2013 11:20
- `%c/%e/%Y %T`: 7/4/2013 11:20
- `%d/%m/%Y %T`: 4/7/2013 11:20
- `%m/%d/%Y %T`: 7/4/2013 11:20
- `%a %D %b %Y`: Thu 4th Jul 2013
- `%a %D %b %Y %H:%i`: Thu 4th Jul 2013 11:20
- `%a %D %b %Y %T`: Thu 4th Jul 2013 11:20:05
- `%a %b %e %Y`: Thu Jul 4 2013
- `%a %b %e %Y %H:%i`: Thu Jul 4 2013 11:20
- `%a %b %e %Y %T`: Thu Jul 4 2013 11:20:05
- `%W %D %M %Y`: Thursday 4th July 2013
- `%W %D %M %Y %H:%i`: Thursday 4th July 2013 11:20
- `%W %D %M %Y %T`: Thursday 4th July 2013 11:20:05
- `%l:%i %p %b %e, %Y`: 7/4/2013 11:20
- `%M %e, %Y`: 4-Jul-13
- `%a, %d %b %Y %T`: hu, 04 Jul 2013 11:20:05


## 12. Comparision functions

Comparison functions in SQL are used to compare values and determine the relationship between them. These functions help in evaluating conditions and producing Boolean results (either `TRUE` or `FALSE`) based on the comparison outcomes. Comparison functions are fundamental for filtering data, creating conditions in queries, and controlling the flow of logic in SQL statements.

Here are some common comparison functions in SQL:

- **Equal (`=`):** This function checks if two values are equal.
   
   Example: `SELECT * FROM customers WHERE age = 25;`

- **Not Equal (`<>` or `!=`):** This function checks if two values are not equal.
   
   Example: `SELECT * FROM products WHERE price <> 0;`

- **Greater Than (`>`):** This function checks if the left value is greater than the right value.
   
   Example: `SELECT * FROM orders WHERE total_amount > 1000;`

- **Less Than (`<`):** This function checks if the left value is less than the right value.
   
   Example: `SELECT * FROM employees WHERE salary < 50000;`

- **Greater Than or Equal To (`>=`):** This function checks if the left value is greater than or equal to the right value.
   
   Example: `SELECT * FROM products WHERE stock_quantity >= 10;`

- **Less Than or Equal To (`<=`):** This function checks if the left value is less than or equal to the right value.
   
   Example: `SELECT * FROM customers WHERE registration_year <= 2020;`

- **IS NULL:** This function checks if a value is NULL.
   
   Example: `SELECT * FROM orders WHERE shipping_address IS NULL;`

- **IS NOT NULL:** This function checks if a value is not NULL.
   
   Example: `SELECT * FROM employees WHERE department IS NOT NULL;`

- **BETWEEN:** This function checks if a value is within a specified range (inclusive).
   
   Example: `SELECT * FROM products WHERE price BETWEEN 10 AND 50;`

- **NOT BETWEEN:** This function checks if a value is not within a specified range.
   
    Example: `SELECT * FROM customers WHERE age NOT BETWEEN 18 AND 30;`

- **IN:** This function checks if a value matches any value in a list.
   
    Example: `SELECT * FROM orders WHERE status IN ('Pending', 'Processing');`

- **NOT IN:** This function checks if a value does not match any value in a list.
   
    Example: `SELECT * FROM products WHERE category NOT IN ('Electronics', 'Clothing');`

- **LIKE:** This function checks if a value matches a pattern. It's often used with wildcard characters `%` (matches any sequence of characters) and `_` (matches a single character).
   
    Example: `SELECT * FROM employees WHERE last_name LIKE 'S%';`

- **NOT LIKE:** This function checks if a value does not match a pattern.
   
    Example: `SELECT * FROM products WHERE product_name NOT LIKE '%sale%';`

These comparison functions are crucial for constructing queries that retrieve specific data based on certain conditions. They allow you to filter and manipulate data according to the logical comparisons you want to make within your SQL statements.


When creating SQL queries, problem-solving have some recurring patterns. 

## Example 1:

You have a sales table with the following columns: SalesDate (date), ProductID (integer), and UnitsSold (integer). 
Each row in this table is unique. Write a SQL query to identify the products that have achieved 3 consecutive months of 
increasing unit sales based on the data in the table.

```
SalesDate   | ProductID | UnitsSold | PrevMonthUnitsSold | NextMonthUnitsSold
-----------------------------------------------------------------------------
2022-01-01  | 1         | 50        | NULL               | 60
2022-02-01  | 1         | 60        | 50                 | 75
2022-03-01  | 1         | 75        | 60                 | 70
2022-04-01  | 1         | 70        | 75                 | 80
2022-05-01  | 1         | 80        | 70                 | 90
2022-06-01  | 1         | 90        | 80                 | NULL
2022-01-01  | 2         | 100       | NULL               | 110
2022-02-01  | 2         | 110       | 100                | 120
2022-03-01  | 2         | 120       | 110                | 150
2022-04-01  | 2         | 150       | 120                | 140
2022-05-01  | 2         | 140       | 150                | 160
2022-06-01  | 2         | 160       | 140                | NULL
```

In order to have this above result, `LAG()` function will be used to get the previous month’s UnitsSold and the `LEAD()` function to get the 
next month’s `UnitsSold` for each row, partitioned by `ProductID` and ordered by `SalesDate`.

```
WITH sales_prev_next AS (
  SELECT 
    SalesDate,
    ProductID,
    UnitsSold,
    LAG(UnitsSold) OVER (PARTITION BY ProductID ORDER BY SalesDate) AS PrevMonthUnitsSold,
    LEAD(UnitsSold) OVER (PARTITION BY ProductID ORDER BY SalesDate) AS NextMonthUnitsSold
  FROM Sales
)
```

Then, we will select the distinct ProductID values where the current month’s UnitsSold is greater than the previous month’s UnitsSold and the next month’s 
UnitsSold is greater than the current month’s UnitsSold.

```
SELECT DISTINCT ProductID
FROM sales_prev_next
WHERE UnitsSold > PrevMonthUnitsSold 
AND NextMonthUnitsSold > UnitsSold;
```

You have a table named “Orders” with the following columns: id (integer), order_date (date), and order_total (decimal). Each row represents an order placed, 
including the order ID, order date, and the total amount of the order. Write an SQL query to display the records where there are 3 or more rows with 
consecutive IDs, and the order total is greater than or equal to $150 for each order.

```
Input: Orders table 
+----------+------------+--------------+
|  id      | order_date | order_total  |
+----------+------------+--------------+
| 1        | 2022-01-01 | 80.50        |
| 2        | 2022-01-02 | 120.75       |
| 3        | 2022-01-03 | 150.20       |
| 4        | 2022-01-04 | 200.00       |
| 5        | 2022-01-05 | 180.90       |
| 6        | 2022-01-06 | 150.40       |
| 7        | 2022-01-07 | 160.25       |
| 8        | 2022-01-09 | 110.60       |
| 9        | 2022-01-11 | 130.80       |
+----------+------------+--------------+

Output: 
+----------+------------+--------------+
| id       | order_date | order_total  |
+----------+------------+--------------+
| 3        | 2022-01-03 | 150.20       |
| 4        | 2022-01-04 | 200.00       |
| 5        | 2022-01-05 | 180.90       |
+----------+------------+--------------+
```

First, as mentioned in the previous approach to consecutive problems, I will use LAG() and LEAD() functions to fetch the previous and next id’s order totals. 
However, in this scenario, the comparison approach is different from the previous example. Instead of comparing the values of order totals with the previous 
and next id’s values, we will compare the 3 consecutive id’s order totals with a specific number to generate the expected outcome.

To simplify the process, let’s take id 5 as an example. In this case, we need to check whether the order totals of id 3, 4 and 5 satisfy the requirement 
of being greater than or equal to $150. Similarly, we also need to check the order totals of id 5, 6, and 7, as well as id 4, 5, and 6 to determine if 
they meet the condition. This approach allows us to identify three consecutive IDs where the order totals satisfy the requirement.

```
WITH tbl AS (
 SELECT
    id,
    order_date,
    order_total,
    LAG(order_total,1) OVER (ORDER BY id) AS prev_order_total,
    LEAD(order_table,1) OVER (ORDER BY id) AS next_order_total,
    LAG(order_total,2) OVER (ORDER BY id) AS prev_order_total2,
    LEAD(order_total,2) OVER (ORDER BY id) AS next_order_total2
  FROM Orders)
```

Here is the table result after applying LEAD() and LAG():

```
+----+------------+-------------+-------------------+-------------------+-------------------+-------------------+
| id | order_date | order_total | prev_order_total  | next_order_total  | prev_order_total2 | next_order_total2 |
+----+------------+-------------+-------------------+-------------------+-------------------+-------------------+
| 1  | 2022-01-01 | 80.50       | NULL              | 120.75            | NULL              | 150.20            |
| 2  | 2022-01-02 | 120.75      | 80.50             | 150.20            | NULL              | 200.00            |
| 3  | 2022-01-03 | 150.20      | 120.75            | 200.00            | 80.50             | 180.90            |
| 4  | 2022-01-04 | 200.00      | 150.20            | 180.90            | 120.75            | 130.40            |
| 5  | 2022-01-05 | 180.90      | 200.00            | 130.40            | 150.20            | 160.25            |
| 6  | 2022-01-06 | 130.40      | 180.90            | 160.25            | 200.00            | 110.60            |
| 7  | 2022-01-07 | 160.25      | 130.40            | 110.60            | 180.90            | 130.80            |
| 8  | 2022-01-09 | 110.60      | 160.25            | 130.80            | 130.40            | NULL              |
| 9  | 2022-01-11 | 130.80      | 110.60            | NULL              | 110.60            | NULL              |
+----+------------+-------------+-------------------+-------------------+-------------------+-------------------+
```

To obtain the three consecutive IDs with a total order greater than or equal to 150, the following conditions need to be satisfied:

```
SELECT  id 
    , order_date 
    , order_total
FROM tbl1
WHERE (order_total >= 150 AND next_order_total >= 150 AND prev_order_total >= 150)
OR (order_total >= 150 AND prev_order_total >= 150 AND prev_order_total2 >= 150)
OR (order_total >= 150 AND next_order_total >= 150 AND next_order_total2 >=150)
```

Last words…
LEAD() and LAG() are helpful when comparing values across consecutive rows or performing calculations based on the previous or next values. This can help identify changes, detect outliers, or track the progression of a variable over time. To sum up, these 2 functions simplify the process of accessing values from adjacent rows, eliminating the need for self-joins or subqueries. This leads to more concise and efficient SQL code.

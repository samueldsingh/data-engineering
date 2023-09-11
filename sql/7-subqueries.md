
## Why subqueries?
- Readability
- Subqueries are more flexible than joins, because they can handle different types of data and operations.
- Subqueries can also be used in places where joins are not allowed, such as in the SELECT, HAVING, or ORDER BY clauses. Joins, on the other hand, may have some limitations and restrictions, depending on the type of join and the database engine.

## What is a subquery?
- A subquery is a SELECT statement within another statement.
- A subquery is a SQL query nested inside a larger query.
- A subquery may occur in: A SELECT clause. A FROM clause. A WHERE clause.
- In MySQL subquery can be nested inside a SELECT, INSERT, UPDATE, DELETE statement or inside another subquery.
- A subquery is usually added within the WHERE Clause of another SQL SELECT statement.
- The inner query executes first before its parent query so that the results of the inner query can be passed to the outer query.

## Non correlated subquery

A noncorrelated subquery executes independently of the outer query. The subquery executes first, and then passes its results to the outer query

Example:
```
SELECT order_id, total_amount
FROM orders
WHERE total_amount > (SELECT AVG(total_amount) FROM orders);
```

## Correlated subquery

- Inner query references values from the outer query. 
- In other words, the inner query's execution is dependent on the values from the outer query. 
- Correlated subqueries are used to perform row-by-row processing and are often used in situations where you
  need to compare values between the outer and inner queries.

Example:
```
SELECT emp_id, emp_name
FROM employees e
WHERE salary > (SELECT AVG(salary) FROM salaries s WHERE s.department_id = e.department_id);
```

## 2 types of subquery

**1. Single row subquery:**
Returns zero or one row in results. Uses comparision operators like `<=`, `>=`, `!=`.

**2. Multiple row subquery:**
Returns one or more columns. Uses operator like `IN`, `ANY`, `ALL`.

## Difference between IN vs EXISTS

- `IN` selects a list of matching values, whereas `EXISTS` returns the Boolean value TRUE or FALSE.
- The `EXISTS` clause is faster than `IN` when the subquery results are very large.


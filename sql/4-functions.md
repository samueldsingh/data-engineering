SQL functions are pre-defined or user-defined routines that accept zero or more arguments and return a value or a table result. They are used to perform various operations on data within an SQL database. SQL functions are categorized into several types based on their functionality. Let's dive into the details of SQL functions:

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
     - `DATEADD`, `DATEDIFF`: Performs date arithmetic operations.
     - `DATE_FORMAT`, `TO_CHAR`: Formats date and time values as strings.

```
-- NOW function to get the current date and time
SELECT NOW();  -- Current date and time

-- DATEADD function to add days to a date
SELECT DATEADD(DAY, 7, '2023-08-01');  -- Adds 7 days to the given date

-- DATE_FORMAT function to format date as a string
SELECT DATE_FORMAT('2023-08-04', '%Y-%m-%d');  -- Output: '2023-08-04'
```

**2. User-Defined Functions (UDFs):**
   Some database systems allow you to define your own functions using SQL or procedural languages like PL/SQL, T-SQL, or PL/pgSQL. UDFs can simplify complex queries and encapsulate business logic.

**3. Window Functions (Analytic Functions):**
   These functions operate on a "window" of rows related to the current row. They are used with the `OVER` clause and are often used for analytical calculations. Examples include:
   - `ROW_NUMBER`, `RANK`, `DENSE_RANK`: Assigns unique numbers to rows within a window.
   - `LAG`, `LEAD`: Access values from previous or subsequent rows.
   - `SUM`, `AVG`, `MIN`, `MAX` with `OVER`: Perform calculations over a window of rows.

```
-- ROW_NUMBER function to assign row numbers
SELECT emp_name, salary, ROW_NUMBER() OVER (ORDER BY salary DESC) AS rank
FROM employees;

-- SUM function with OVER clause for running total
SELECT order_date, order_amount, SUM(order_amount) OVER (ORDER BY order_date) AS running_total
FROM orders;
```

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
SELECT CONCAT('Hello', ' ', 'World!') AS concatenated_string;

-- INSTR - Return the position of the first occurrence of a substring in a string
SELECT INSTR('Hello World!', 'World') AS position;

-- LENGTH - Get the length of a string in bytes and in characters
SELECT LENGTH('Hello World!') AS length_bytes, CHAR_LENGTH('Hello World!') AS length_characters;

-- LEFT - Get a specified number of leftmost characters from a string
SELECT LEFT('Hello World!', 5) AS leftmost_characters;

-- LOWER - Convert a string to lowercase
SELECT LOWER('Hello World!') AS lowercase_string;

-- LTRIM - Remove all leading spaces from a string
SELECT LTRIM('   Hello World!') AS trimmed_string;

-- REPLACE - Search and replace a substring in a string
SELECT REPLACE('Hello World!', 'World', 'Universe') AS replaced_string;

-- RIGHT - Get a specified number of rightmost characters from a string
SELECT RIGHT('Hello World!', 6) AS rightmost_characters;

-- RTRIM - Remove all trailing spaces from a string
SELECT RTRIM('Hello World!    ') AS trimmed_string;

-- SUBSTRING - Extract a substring starting from a position with a specific length
SELECT SUBSTRING('Hello World!', 7, 5) AS extracted_substring;

-- TRIM - Remove unwanted characters from a string
SELECT TRIM('   Hello World!   ') AS trimmed_string;

-- UPPER - Convert a string to uppercase
SELECT UPPER('Hello World!') AS uppercase_string;

-- FIND_IN_SET - Find a string within a comma-separated list of strings
SELECT FIND_IN_SET('apple', 'banana,apple,orange') AS position_in_list;

-- FORMAT - Format a number with a specific locale, rounded to the number of decimals
SELECT FORMAT(12345.6789, 2, 'en_US') AS formatted_number;

-- SUBSTRING_INDEX - Return a substring from a string before a specified number of occurrences of a delimiter
SELECT SUBSTRING_INDEX('apple,banana,orange', ',', 2) AS substring_before_second_comma;
```

The output is:

```
concatenated_string: Hello World!
position: 7
length_bytes: 12, length_characters: 12
leftmost_characters: Hello
lowercase_string: hello world!
trimmed_string: Hello World!
replaced_string: Hello Universe!
rightmost_characters: World!
trimmed_string: Hello World!
extracted_substring: World
trimmed_string: Hello World!
uppercase_string: HELLO WORLD!
position_in_list: 2
formatted_number: 12,345.68
substring_before_second_comma: apple,banana
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
   These functions convert values from one data type to another. Examples include `CAST`, `CONVERT`.

```
-- CAST function to convert a value to a different data type
SELECT CAST('123' AS INT);  -- Output: 123

-- CONVERT function to change data type
SELECT CONVERT('2023-08-04', DATE);  -- Output: '2023-08-04'
```

**7. Conditional Functions:**
   These functions evaluate conditions and return different values based on the outcome. Examples include `CASE`, `COALESCE`, `NULLIF`.

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


**12. Comparision Functions**

Comparison functions in SQL are used to compare values and determine the relationship between them. These functions help in evaluating conditions and producing Boolean results (either `TRUE` or `FALSE`) based on the comparison outcomes. Comparison functions are fundamental for filtering data, creating conditions in queries, and controlling the flow of logic in SQL statements.

Here are some common comparison functions in SQL:

1. **Equal (`=`):** This function checks if two values are equal.
   
   Example: `SELECT * FROM customers WHERE age = 25;`

2. **Not Equal (`<>` or `!=`):** This function checks if two values are not equal.
   
   Example: `SELECT * FROM products WHERE price <> 0;`

3. **Greater Than (`>`):** This function checks if the left value is greater than the right value.
   
   Example: `SELECT * FROM orders WHERE total_amount > 1000;`

4. **Less Than (`<`):** This function checks if the left value is less than the right value.
   
   Example: `SELECT * FROM employees WHERE salary < 50000;`

5. **Greater Than or Equal To (`>=`):** This function checks if the left value is greater than or equal to the right value.
   
   Example: `SELECT * FROM products WHERE stock_quantity >= 10;`

6. **Less Than or Equal To (`<=`):** This function checks if the left value is less than or equal to the right value.
   
   Example: `SELECT * FROM customers WHERE registration_year <= 2020;`

7. **IS NULL:** This function checks if a value is NULL.
   
   Example: `SELECT * FROM orders WHERE shipping_address IS NULL;`

8. **IS NOT NULL:** This function checks if a value is not NULL.
   
   Example: `SELECT * FROM employees WHERE department IS NOT NULL;`

9. **BETWEEN:** This function checks if a value is within a specified range (inclusive).
   
   Example: `SELECT * FROM products WHERE price BETWEEN 10 AND 50;`

10. **NOT BETWEEN:** This function checks if a value is not within a specified range.
   
    Example: `SELECT * FROM customers WHERE age NOT BETWEEN 18 AND 30;`

11. **IN:** This function checks if a value matches any value in a list.
   
    Example: `SELECT * FROM orders WHERE status IN ('Pending', 'Processing');`

12. **NOT IN:** This function checks if a value does not match any value in a list.
   
    Example: `SELECT * FROM products WHERE category NOT IN ('Electronics', 'Clothing');`

13. **LIKE:** This function checks if a value matches a pattern. It's often used with wildcard characters `%` (matches any sequence of characters) and `_` (matches a single character).
   
    Example: `SELECT * FROM employees WHERE last_name LIKE 'S%';`

14. **NOT LIKE:** This function checks if a value does not match a pattern.
   
    Example: `SELECT * FROM products WHERE product_name NOT LIKE '%sale%';`

These comparison functions are crucial for constructing queries that retrieve specific data based on certain conditions. They allow you to filter and manipulate data according to the logical comparisons you want to make within your SQL statements.

Certainly! Here are examples for both the `COALESCE` and `IFNULL` functions:

15. **COALESCE:**

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

16. **IFNULL:**

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

Both `COALESCE` and `IFNULL` offer convenient ways to handle NULL values and provide meaningful output in SQL queries.

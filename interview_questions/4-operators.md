# IV. Operators:
===============
## 1. Explain in detail about all operators 

In Python, operators are symbols or special characters that perform specific operations on one or more operands. They allow you to perform mathematical calculations, compare values, assign values, combine or modify values, and more. Here is an explanation of the different types of operators in Python:

1. Arithmetic Operators:
   - Arithmetic operators perform mathematical calculations on numeric operands.
   - Examples: `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division), `%` (modulus), `**` (exponentiation), `//` (floor division).

2. Assignment Operators:
   - Assignment operators are used to assign values to variables.
   - Examples: `=` (simple assignment), `+=` (add and assign), `-=` (subtract and assign), `*=` (multiply and assign), `/=` (divide and assign), `%=` (modulus and assign), `**=` (exponentiation and assign), `//=` (floor division and assign).

3. Comparison Operators:
   - Comparison operators compare two values and return a boolean result (`True` or `False`) based on the comparison.
   - Examples: `==` (equal to), `!=` (not equal to), `>` (greater than), `<` (less than), `>=` (greater than or equal to), `<=` (less than or equal to).

4. Logical Operators:
   - Logical operators perform logical operations on boolean values and return a boolean result.
   - Examples: `and` (logical AND), `or` (logical OR), `not` (logical NOT).

5. Bitwise Operators:
   - Bitwise operators perform operations on binary representations of integers.
   - Examples: `&` (bitwise AND), `|` (bitwise OR), `^` (bitwise XOR), `~` (bitwise NOT), `<<` (left shift), `>>` (right shift).

6. Identity Operators:
   - Identity operators compare the memory addresses of two objects to determine their identity.
   - Examples: `is` (is the same object), `is not` (is not the same object).

7. Membership Operators:
   - Membership operators check if a value is present in a sequence or collection.
   - Examples: `in` (is present in), `not in` (is not present in).

8. Unary Operators:
   - Unary operators perform operations on a single operand.
   - Examples: `-` (negation), `+` (unary plus), `not` (logical negation).

9. Ternary Operator:
   - The ternary operator (`x if condition else y`) is a shorthand way of writing an if-else statement in a single line.

These operators have different precedence and associativity rules, which determine the order of evaluation when multiple operators are used in an expression.

Understanding and using operators is crucial for performing various operations in Python, such as calculations, comparisons, logical operations, and more. By utilizing operators effectively, you can manipulate data, control program flow, and create complex expressions to achieve desired results in your code.

## 2. == vs is 

In Python, the `==` operator and the `is` operator are used for different purposes and have distinct behaviors:

1. `==` Operator (Equality Operator):
   - The `==` operator compares the values of two objects and checks if they are equal.
   - It evaluates to `True` if the values of the objects are the same, and `False` otherwise.
   - Example:
     ```python
     a = [1, 2, 3]
     b = [1, 2, 3]
     c = a

     print(a == b)  # True (values are equal)
     print(a == c)  # True (values are equal)
     print(b == c)  # True (values are equal)
     ```
   - In the example above, the `==` operator compares the values of the lists `a` and `b`, which contain the same elements. It returns `True` because the values are equal.

2. `is` Operator (Identity Operator):
   - The `is` operator checks if two objects refer to the same memory location or have the same identity.
   - It evaluates to `True` if the objects have the same identity, and `False` otherwise.
   - Example:
     ```python
     a = [1, 2, 3]
     b = [1, 2, 3]
     c = a

     print(a is b)  # False (different identities)
     print(a is c)  # True (same identity)
     print(b is c)  # False (different identities)
     ```
   - In the example above, the `is` operator checks the identity of the lists `a`, `b`, and `c`. It returns `True` for `a is c` because `a` and `c` refer to the same list object in memory.

In summary, the `==` operator compares the values of two objects, while the `is` operator checks if two objects have the same identity. The `==` operator checks for value equality, whereas the `is` operator checks for object identity. It's important to choose the appropriate operator based on the desired comparison or evaluation you need to perform.

## 3. and or operators. Explain 2 examples 

The `and` and `or` operators in Python are used to perform logical operations and combine boolean values. Here are two examples that demonstrate the usage of these operators:

1. Example using `and` operator:
```python
age = 25
is_student = True

if age >= 18 and is_student:
    print("You are eligible for a student discount.")
else:
    print("You are not eligible for a student discount.")
```
In this example, the `and` operator is used to combine two conditions: `age >= 18` and `is_student`. The `and` operator evaluates to `True` if both conditions are true. If the age is greater than or equal to 18 and the person is a student, the program prints "You are eligible for a student discount." Otherwise, it prints "You are not eligible for a student discount."

2. Example using `or` operator:
```python
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("It's time to relax and enjoy!")
else:
    print("Back to work!")
```
In this example, the `or` operator is used to combine two conditions: `is_weekend` and `is_holiday`. The `or` operator evaluates to `True` if at least one of the conditions is true. If it's either a weekend or a holiday, the program prints "It's time to relax and enjoy!" Otherwise, it prints "Back to work!"

The `and` operator requires both conditions to be true for the overall expression to be true, while the `or` operator only requires one of the conditions to be true. These operators are commonly used in conditional statements and boolean expressions to control the flow of the program based on specific conditions or combinations of conditions.

## 4. Operator precedence.

Operator precedence refers to the order in which operators are evaluated in an expression when multiple operators are present. It determines the grouping and execution order of operators based on their priority. Understanding operator precedence is important to ensure that expressions are evaluated correctly. 

In Python, operator precedence follows a specific set of rules. Here is a summary of the operator precedence hierarchy in descending order (from highest to lowest precedence):

1. Parentheses: `( )`
   - Parentheses are used to explicitly group expressions and override the default precedence.

2. Exponentiation: `**`
   - The exponentiation operator raises the left operand to the power of the right operand.

3. Unary Operators: `+x`, `-x`, `~x`
   - Unary operators perform operations on a single operand, such as negation, logical negation, or bitwise negation.

4. Multiplication, Division, Modulus, Floor Division: `*`, `/`, `%`, `//`
   - Multiplication (`*`), division (`/`), modulus (`%`), and floor division (`//`) operators have the same level of precedence and are evaluated from left to right.

5. Addition and Subtraction: `+`, `-`
   - Addition (`+`) and subtraction (`-`) operators have the same level of precedence and are evaluated from left to right.

6. Bitwise Shifts: `<<`, `>>`
   - Bitwise shift operators perform left shift (`<<`) and right shift (`>>`) operations on binary representations of integers.

7. Bitwise AND: `&`
   - The bitwise AND operator performs a bitwise AND operation on binary representations of integers.

8. Bitwise XOR: `^`
   - The bitwise XOR operator performs a bitwise XOR operation on binary representations of integers.

9. Bitwise OR: `|`
   - The bitwise OR operator performs a bitwise OR operation on binary representations of integers.

10. Comparison Operators: `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in`
    - Comparison operators compare values and return boolean results (`True` or `False`).

11. Logical NOT: `not`
    - The logical NOT operator performs logical negation on a boolean value.

12. Logical AND: `and`
    - The logical AND operator performs logical conjunction on boolean values.

13. Logical OR: `or`
    - The logical OR operator performs logical disjunction on boolean values.

It's important to note that parentheses can be used to override the default precedence and explicitly specify the order of evaluation in an expression.

Understanding the operator precedence rules helps in writing correct and readable expressions. It is recommended to use parentheses when there is ambiguity or to improve clarity, even if they are not strictly required by the precedence rules.


## 5. Subtract 2 numbers and print result program.
	- Write down all scenarios with different input values 

 Certainly! Here's a Python program that subtracts two numbers and prints the result:

```python
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = num1 - num2

print("The result of subtracting", num2, "from", num1, "is:", result)
```

Scenarios with different input values:

1. Positive numbers:
   - Input:
     ```
     Enter the first number: 10
     Enter the second number: 3
     ```
   - Output:
     ```
     The result of subtracting 3.0 from 10.0 is: 7.0
     ```

2. Negative numbers:
   - Input:
     ```
     Enter the first number: -5
     Enter the second number: -2
     ```
   - Output:
     ```
     The result of subtracting -2.0 from -5.0 is: -3.0
     ```

3. Zero as one of the numbers:
   - Input:
     ```
     Enter the first number: 0
     Enter the second number: 8
     ```
   - Output:
     ```
     The result of subtracting 8.0 from 0.0 is: -8.0
     ```

4. Decimal numbers:
   - Input:
     ```
     Enter the first number: 5.7
     Enter the second number: 2.3
     ```
   - Output:
     ```
     The result of subtracting 2.3 from 5.7 is: 3.4
     ```

5. Large numbers:
   - Input:
     ```
     Enter the first number: 1000000
     Enter the second number: 500000
     ```
   - Output:
     ```
     The result of subtracting 500000.0 from 1000000.0 is: 500000.0
     ```

These are just a few examples demonstrating different scenarios for subtracting two numbers. The program will subtract the second number from the first number and print the result.

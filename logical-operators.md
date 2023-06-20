## AND Operator
The `and` operator in Python is a logical operator that combines two conditions. It returns `True` if both conditions are `True`, otherwise it returns `False`.

Here are the rules for the and operator:

1. If the left operand is `False`, the and operator immediately evaluates to `False` without evaluating the right operand. This is known as **short-circuit evaluation**.

Example: `False` and `x` will always be `False`, regardless of the value of `x`.

2. If the left operand is `True`, the and operator evaluates the right operand and returns its value.

Example: `True` and `x` will evaluate to `x`, as the value of `x` determines the overall result.

3. If both operands are `True`, the `and` operator returns `True`.

Example: `True` and `True` will evaluate to `True`.

4. If either or both operands are `False`, the and operator returns `False`.

Example: `True` and `False` or `False` and `True` will evaluate to `False`.

In summary, the `and` operator requires both operands to be `True` in order to evaluate to `True`. If any operand is `False`, the result will be `False`.

```
1 ^ 1 = 1
1 ^ 0 = 0
0 ^ 1 = 0
0 ^ 0 = 0
```



##  Read three inputs, arrange in ascending , without if, for, while, sort
first_no = int(input("Enter the first number: "))
second_no = int(input("Enter the second number: "))
third_no = int(input("Enter the third number: "))

min = first_no * ( first_no <= second_no and first_no <= third_no) + second_no * (second_no <= first_no and second_no <= third_no) + third_no * (third_no <= first_no and third_no <= second_no)

max = first_no * ( first_no >= second_no and first_no >= third_no) + second_no * (second_no >= first_no and second_no >= third_no) + third_no * (third_no >= first_no and third_no >= second_no)

median = (first_no + second_no + third_no) - min - max

print("Ascending order: ", min, median, max)

Example: first_no = 7, second_no = 8, third_no =3

The execution of the expression, `1 * ( 1 <= 2 and 1 <= 3) + 2 * (2 <=1 and 2 <= 3) + 3 * (3 <= 1 and 3 <=2)` is as:

1. 1 * (1 <= 2 and 1 <= 3)
The expression inside the brackets is evaluated as follows:
- 1 <= 2 is True because 1 is less than or equal to 2.
- 1 <= 3 is True because 1 is less than or equal to 3.
- The logical AND operator 'and' evaluates to True if both conditions are True.

Therefore, the expression evaluates to 1 * True = 1.

1. 7 * (7 <= 8 and 7 <= 3)
The expression inside the brackets is evaluated as follows:
- 7 <= 8 is True because 7 is less than or equal to 8.
- 7 <= 3 is False because 7 is not less than or equal to 3.
- The logical AND operator 'and' evaluates to False because one of the conditions is False.

Therefore, the expression evaluates to 7 * False = 0.

2 * (8 <= 7 and 8 <= 3)
The expression inside the brackets is evaluated as follows:
- 8 <= 7 is False because 8 is not less than or equal to 7.
- 8 <= 3 is False because 8 is not less than or equal to 3.
- The logical AND operator 'and' evaluates to False if any of the conditions is False.

Therefore, the expression evaluates to 2 * False = 0.

3 * (3 <= 7 and 3 <= 8)
The expression inside the brackets is evaluated as follows:
3 <= 7 is False because 3 is not less than or equal to 1.
3 <= 8 is False because 3 is not less than or equal to 2.
The logical AND operator 'and' evaluates to False if any of the conditions is False.

Therefore, the expression evaluates to 3 * False = 0.

Finally, the result is the sum of the three expressions: 1 + 0 + 0 = 1.

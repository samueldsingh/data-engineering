

## What are functions?

In Python, a function is a block of reusable code that performs a specific task or set of tasks. It allows you to group related instructions together 
and execute them by calling the function name. Functions are a fundamental concept in programming, and they play a crucial role in organizing and 
modularizing code. Here are some key points about functions in Python:

1. Function Definition:
   - A function is defined using the `def` keyword, followed by the function name, parentheses `()`, and a colon `:` to indicate the start of the function body.
   - Example:

     ```
     def greet():
         print("Hello, World!")
     ```

2. Function Call:
   - To execute a function and run the code inside it, you need to call the function by using its name followed by parentheses `()`.
   - Example:

     ```
     greet()  # Output: "Hello, World!"
     ```

3. Function Parameters:
   - Functions can accept input values called parameters or arguments, which are defined inside the parentheses.
   - Parameters provide a way to pass data into the function for processing.
   - Example:

     ```
     def greet(name):
         print("Hello, " + name + "!")
     ```

4. Return Statement:
   - Functions can return a value using the `return` statement. The returned value can be assigned to a variable or used in other parts of the code.
   - Example:

     ```
     def add_numbers(a, b):
         return a + b
     ```

5. Function Documentation (Docstring):
   - Functions can include a docstring, which is a string that provides a description and details about the function's purpose, parameters, and return value.
   - Docstrings help document and explain the usage of the function for other developers or yourself.
   - Example:

     ```
     def greet(name):
         """
         This function greets a person by name.
         Parameters:
         - name: a string representing the person's name
         """
         print("Hello, " + name + "!")
     ```

6. Function Scope:
   - Variables defined within a function are local to that function and can only be accessed within its scope.
   - Global variables, defined outside any function, can be accessed from within functions.
   - Example:

     ```
     def calculate():
         num1 = 10  # local variable
         num2 = 5
         result = num1 + num2
         return result

     total = calculate()  # global variable
     ```

Functions provide several benefits, such as code reuse, modularity, readability, and maintainability. They allow you to break down complex tasks 
into smaller, manageable parts. By encapsulating code within functions, you can easily call and reuse the same functionality multiple times, leading 
to more efficient and organized programming.

What are the advantages of using functions:
- Avoids code duplication
- Achieves Code reusability
- When enhancements are required, we need "code changes" in only one place

## 2. What is the difference between arguments and parameters in a function
In the context of functions, "arguments" and "parameters" are related but distinct concepts. They refer to different things in the function definition 
and function call:

1. Parameters:
   - Parameters are the placeholders defined in the function declaration or definition. They specify the names and order of the values that a function expects to receive when it is called.
   - Parameters act as variables within the function's scope and are used to manipulate and process the input data.
   - Parameters are listed inside the parentheses `()` in the function definition.
   - Example:
     ```
     def greet(name, age):
         print("Hello, " + name + "! You are " + str(age) + " years old.")
     ```

2. Arguments:
   - Arguments are the actual values passed to a function when it is called. They represent the data or expressions that are supplied to the function for processing.
   - Arguments are passed inside the parentheses `()` in the function call.
   - Arguments are matched with the parameters based on their respective positions or explicitly specified using keyword arguments.
   - Example:
     ```
     greet("John", 30)  # "John" and 30 are the arguments
     ```

In summary, parameters are the variables defined in the function declaration, whereas arguments are the actual values or expressions passed to a function 
during its invocation. Parameters define the expected input structure, while arguments provide the specific data to be processed by the function. 
It's essential to ensure that the number and order of arguments match the parameters in the function definition to avoid errors.

## 3. Give examples of all arithmetic operations using functions

Here are examples of all arithmetic operations using functions in Python:

1. Addition (+):
   ```python
   def add(a, b):
       return a + b

   result = add(5, 3)
   print(result)  # Output: 8
   ```

2. Subtraction (-):
   ```python
   def subtract(a, b):
       return a - b

   result = subtract(7, 2)
   print(result)  # Output: 5
   ```

3. Multiplication (*):
   ```python
   def multiply(a, b):
       return a * b

   result = multiply(4, 3)
   print(result)  # Output: 12
   ```

4. Division (/):
   ```python
   def divide(a, b):
       return a / b

   result = divide(10, 2)
   print(result)  # Output: 5.0
   ```

5. Floor Division (//):
   ```python
   def floor_divide(a, b):
       return a // b

   result = floor_divide(10, 3)
   print(result)  # Output: 3
   ```

6. Modulo (%):
   ```python
   def modulo(a, b):
       return a % b

   result = modulo(10, 3)
   print(result)  # Output: 1
   ```

7. Exponentiation (**):
   ```
   def exponentiate(a, b):
       return a ** b

   result = exponentiate(2, 3)
   print(result)  # Output: 8
   ```

8. Negation (-):
   ```
   def negate(a):
       return -a

   result = negate(5)
   print(result)  # Output: -5
   ```

These examples demonstrate the different arithmetic operations (+, -, *, /, //, %, **, -) using custom functions. You can define these functions 
and use them to perform arithmetic calculations with different input values.

## 4. Explain return statement in Python:

The `return` statement in a function is used to specify the value or values that should be returned from the function when it is called. It allows you to send data back from the function to the code that called it. Here are some important points about the `return` statement in Python:

1. Returning a Single Value:
   - A function can return a single value using the `return` statement followed by the expression or variable representing the value to be returned.
   - Example:
     ```python
     def calculate_sum(a, b):
         return a + b

     result = calculate_sum(3, 5)
     print(result)  # Output: 8
     ```

2. Returning Multiple Values:
   - In Python, a function can also return multiple values as a tuple. Multiple values are separated by commas in the `return` statement.
   - The returned values can be assigned to multiple variables or accessed as elements of a tuple.
   - Example:
     ```python
     def get_name_and_age():
         name = "John"
         age = 30
         return name, age

     name, age = get_name_and_age()
     print(name)  # Output: "John"
     print(age)  # Output: 30
     ```

3. Early Termination:
   - When a `return` statement is encountered in a function, the execution of the function is immediately terminated, and control is transferred back to the calling code.
   - Any code or statements after the `return` statement within the function will not be executed.
   - Example:
     ```python
     def check_positive(number):
         if number < 0:
             return "Negative"
         else:
             return "Positive"

     result = check_positive(5)
     print(result)  # Output: "Positive"
     ```

4. Returning None:
   - If a function does not explicitly specify a `return` statement, it automatically returns `None`, which represents the absence of a value.
   - Example:
     ```python
     def say_hello():
         print("Hello")

     result = say_hello()
     print(result)  # Output: None
     ```

5. Conditional Returns:
   - A function can have multiple `return` statements, and the choice of which one to execute can be based on conditional statements or logical checks within the function.
   - Example:
     ```python
     def check_value(value):
         if value < 0:
             return "Negative"
         elif value == 0:
             return "Zero"
         else:
             return "Positive"

     result = check_value(10)
     print(result)  # Output: "Positive"
     ```

The `return` statement is crucial for providing the output or results of a function to the calling code. It allows you to pass back computed values, 
perform early termination, and handle various conditions within the function. Understanding how to use the `return` statement effectively enables you 
to write functions that encapsulate specific functionality and provide useful results to the rest of your program.

## 5. Give examples of printing the sum of two numbers with using return type and without using return type

Example: *Without return types*
``` 
def sum(n1, n2):
    result = n1 + n2  # Business Logic
    print("Addition is  :", result)  # Print it

print("SUM Operation : ", sum(10,20))
sum(10, 20)
```

The output is:
```
Addition is  : 30
SUM Operation :  None
Addition is  : 30
```

In *return type*, the sum function takes 2 responsibilities:
    1. Implementing the business logic
    2. Handling the end result/output

Example: *With return type*
``` 
print("--------With return type--------")
def sum(n1, n2):
    result = n1 + n2  # Business Logic
    return result     # return end value

print("SUM Operation : ", sum(10, 20))
print("---------------------------------")
output = sum(10, 20)
print("SUM Operation : ", output)
print("---------------------------------")
```

The output is:
```
--------With return type--------
SUM Operation :  30
---------------------------------
SUM Operation :  30
---------------------------------
```

## 6. Write a python to return the character count in a string.

```
str1 = 'abcabbcabac'

def get_charcount(st):
    di = {}
    for char in str1:
        if char not in di.keys():
            di[char] = 1
        else:
            di[char] += 1
    # print("Final char count : ", di)
    return di

ch_count = get_charcount(str1)
print("Final char count : ", ch_count)
```

The output is:
```
Final char count :  {'a': 4, 'b': 4, 'c': 3}
```

## 7. Function categories 
In python, the functions are usually of 4 types:
1. Function with parameters, with return type
2. Function with parameters, without return type
3. Function without parameters, with return type
4. Function without parameters, without return type

Let's look at the sum functionality for the 4 different categories:
1. Function with parameters, with return type
```
num1 = 10
num2 = 20

def sum(n1, n2):
    res = n1 + n2
    return res

print("Addition is : ", sum(num1, num2))  
```

The output is:
```
Addition is :  30
```

2. Function with parameters, without return type
```
num1 = 10
num2 = 20

def sum(n1, n2):
    res = n1 + n2
    print("Addition is : ", res)

sum(num1, num2)
print("Second cat : ", sum(num1, num2))
```

The output is:
```
Addition is :  30
Addition is :  30
Second cat :  None
```

3. Function without parameters, with return type
```
def sum():
    n1 = 10
    n2 = 20
    res = n1 + n2
    return res

output = sum()
print("Addition is : ", output)
```

The output is:
```
Addition is: 30
```

4. Function without parameters, without return type
```
def sum():
    n1 = 10
    n2 = 20
    res = n1 + n2
    print("Addition is : ", res)

sum()
print("Cat 4 : ", sum())
```

Output is:
```
Addition is :  30
Addition is :  30
Cat 4 :  None
```

## 8. Passing arguments in a function
There are 3 ways of passing arguments in a function:
1. Positional Arguments (Required arguments)
2. Default Arguments
3. Keyword Arguments (Named arguments)

1. Positional Arguments (Required arguments)
```
def sum(n1, n2, n3):
    print("In sum method : with vals :", n1, n2, n3)
    res = n1 + n2 + n3
    print("Sum is : ", res)

sum(10, 20, 30)
```

Output is:
```
In sum method : with vals : 10 20 30
Sum is :  60
```

Causes of TypeError:
1. sum(10, 20)            # TypeError: sum() missing 1 required positional argument: 'n3'3#
2. sum(10, 20, 30, 40)    # TypeError: sum() takes 3 positional arguments but 4 were given



2. Default Arguments
```
def sum(n1, n2, n3 = 1000):   # int float bool str  list tuple dict set
    res = n1 + n2 + n3
    print("Sum is : ", res)
```

**Scenarios:**
sum(10)          # # sum() missing 1 required positional argument: 'n2'
sum(10, 20)      # n3 = 1000
sum(10, 20, 30)  # n3 = 1000 will be overriden with 30

The output is:
```
Sum is :  1030
Sum is :  60
```

## Function Overloading:
When a function can be called in minimum two or more ways (based on the number of arguments)

Example:
```
def sum(n1, n2=500, n3=1000):
    res = n1 + n2 + n3
    print("Result : ", res)

# sum()
sum(10)
sum(150, 250)
sum(150, 250, 350)
# print("Zero argument    :", sum())
print("One argument     :", sum(10))
print("Two argument     :", sum(10, 20))
print("Three argument   :", sum(10, 20, 30))
#print("Extra arguments  :",sum(10,20,30,40))
```

The output will be:
```
Result :  1510
Result :  1400
Result :  750
Result :  1510
One argument     : None
Result :  1030
Two argument     : None
Result :  60
Three argument   : None
```

Example 2:
```
def sum(n1 = 100, n2 = 500, n3 = 1000):
    res = n1 + n2 + n3
    return res

print("Zero argument    :", sum())
print("One argument     :", sum(10))
print("Two argument     :", sum(10, 20))
print("Three argument   :", sum(10, 20, 30))
```

The output is:
```
Zero argument    : 1600
One argument     : 1510
Two argument     : 1030
Three argument   : 60
```

3. Keyword Arguments (Named arguments)

Usecase 1 : For code readability while calling function
Usecase 2 : If we don't want to maintain order while passing arguments
Usecase3 : If we want to pass argument only for specific parameter

```
def sum(n1=2000, n2, n3=1000):
    res = n1 + n2 + n3
    print("Sum is : ",res)
```

The output is:
```
SyntaxError: non-default argument follows default argument
```

Usecase 1 : For code readability while calling function

```
def get_order_info(mobile, ref_no, order_no, quantity, price):
    print("Order details :")
    print(order_no, ref_no, quantity, price, mobile)

get_order_info(mobile=8975435643,
               ref_no=9865432132,
               order_no=123,
               quantity=40,
               price=65876,
               )
```

The output is:
```
Order details :
123 9865432132 40 65876 8975435643
```

Usecase 2 : If we don't want to maintain order while passing arguments
```
def sum(n1, n2, n3):
    res = n1 + n2 + n3
    print("Sum1 is : ", res)

sum(10, 20, 30)           # 1.Positional/Required
sum(n1=10, n2=20, n3=30)  # UC1: code readability
sum(n2=20, n1=30, n3=10)  # UC2: don't want to maintain order
sum(n3=20, n1=30, n2=10)  # UC2: don't want to maintain order
```

The output is:
```
Sum1 is :  60
Sum1 is :  60
Sum1 is :  60
Sum1 is :  60
```

Usecase3 : If we want to pass argument only for specific parameter
```
def feedback(rating=10, comments=None):
    print(rating, comments)
```

The output is:
```
10 None
Feedback :  None
7 None
Feedback :  None
10 Good
Feedback :  None
1 Bad
Feedback :  None
1 Bad
Feedback :  None
1 Bad
Feedback :  None
```


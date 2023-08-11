
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



**1. Positional Arguments (Required arguments)**

Positional arguments are passed to a function based on their position or order.

The function receives the arguments in the same order they are passed when calling the function.

The number of positional arguments in the function call must match the number of parameters in the function definition.

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
1. sum(10, 20)            `# TypeError: sum() missing 1 required positional argument: 'n3'3#`
2. sum(10, 20, 30, 40)    `# TypeError: sum() takes 3 positional arguments but 4 were given`



**2. Default Arguments**

Default arguments in functions allow you to specify a default value for a parameter if no argument is provided when the function is called. This means that the function can be called with fewer arguments than the number of parameters it has.

```
def sum(n1, n2, n3 = 1000):   # int float bool str  list tuple dict set
    res = n1 + n2 + n3
    print("Sum is : ", res)
```

**Scenarios:**

sum(10)          `# # sum() missing 1 required positional argument: 'n2'`

sum(10, 20)      `# n3 = 1000`

sum(10, 20, 30)  `# n3 = 1000 will be overriden with 30`

The output is:
```
Sum is :  1030
Sum is :  60
```

**Function Overloading:**
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

**3. Keyword Arguments (Named arguments)**

Keyword arguments are passed to a function using the name of the parameter and the corresponding value. The order of keyword arguments doesn't matter as long as the parameter names are specified. Keyword arguments provide more flexibility and allow you to skip positional arguments or change their order.

Usecase 1 : For code readability while calling function

Usecase 2 : If we don't want to maintain order while passing arguments

Usecase 3 : If we want to pass argument only for specific parameter

```
def sum(n1=2000, n2, n3=1000):
    res = n1 + n2 + n3
    print("Sum is : ",res)
```

The output is:
```
SyntaxError: non-default argument follows default argument
```

**Usecase 1 : For code readability while calling function**

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

**Usecase 2 : If we don't want to maintain order while passing arguments**
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

**Usecase 3 : If we want to pass argument only for specific parameter**
```
def feedback(rating=10, comments=None):
    print(rating, comments)

print("Feedback : ", feedback())
print("Feedback : ", feedback(7))
print("Feedback : ", feedback(comments='Good'))  # Keyword Arguments
print("Feedback : ", feedback(1, "Bad"))
print("Feedback : ", feedback(rating=1, comments="Bad"))
print("Feedback : ", feedback(comments="Bad", rating=1))
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

## Global and local variables

In programming, global and local variables determine the scope and visibility of variables within a program. Here's an explanation of global and local variables with examples:

1. Global Variables:
   - Global variables are declared outside of any function or block and can be accessed throughout the program.
   - They have global scope, meaning they are visible to all functions and blocks within the program.
   - Global variables can be modified and accessed from any part of the program.
   - Example:

     ```python
     # Global variable
     global_var = 10

     def my_function():
         # Accessing global variable
         print(global_var)

     my_function()  # Output: 10
     ```

     In this example, `global_var` is a global variable defined outside of any function. It can be accessed from within the `my_function()` and its value is printed.

2. Local Variables:
   - Local variables are declared within a function or block and have local scope, meaning they are only visible within that specific function or block.
   - They are created when the function or block is entered and destroyed when it is exited.
   - Local variables cannot be accessed outside of the function or block in which they are defined.
   - Example:

     ```python
     def my_function():
         # Local variable
         local_var = 20
         print(local_var)

     my_function()  # Output: 20
     # Trying to access local_var here would result in an error
     ```

     In this example, `local_var` is a local variable defined within the `my_function()`. It can be accessed and printed from within the function, but any attempt to access it outside of the function would result in an error.

It's important to note that global and local variables can have the same name, but they are distinct and separate entities. If a local variable has the same name as a global variable, the local variable takes precedence within its scope, and any modifications or references to that variable will affect the local instance, not the global one.

```
message = 'Hello World'              # Global
def get_str_len(msg):                # msg -> local scope
    print("String is:", message)     # Global variable can be accessed from anywhere
    le = 0                           # le -> Local scope
    for char in msg:
        le += 1
    return le
```

The output is:
```
String is: Hello World
Length of given string: 11
```

Another example:

```
val = int(input("Enter value: "))
def find_square(num):
    res = num ** 2
    return res
out = find_square(val)
print("Square of value:", out)
```

The output is:

```
Enter value: 7
Square of value: 49
```

## Explain anonymous functions with example:

Anonymous functions, also known as lambda functions, are functions without a defined name. They are often used when you need a short, one-line function for a specific task. Here's an explanation of anonymous functions with an example:

In Python, you can define an anonymous function using the `lambda` keyword. The general syntax for a lambda function is `lambda arguments: expression`. The lambda function takes in one or more arguments, performs a computation using the expression, and returns the result.

Example:

```python
# Normal function to add two numbers
def add_numbers(x, y):
    return x + y

result = add_numbers(3, 5)
print(result)  # Output: 8

# Equivalent anonymous/lambda function to add two numbers
add_lambda = lambda x, y: x + y

result = add_lambda(3, 5)
print(result)  # Output: 8
```

In this example, we have a normal function `add_numbers(x, y)` that adds two numbers `x` and `y` and returns the result. The equivalent anonymous/lambda function `add_lambda` performs the same addition operation.

The lambda function is defined using the `lambda` keyword, followed by the arguments `x` and `y`, a colon `:`, and the expression `x + y`. The lambda function is assigned to the variable `add_lambda`.

Both the normal function `add_numbers` and the lambda function `add_lambda` can be called with the same arguments `(3, 5)`, and they produce the same output of `8`.

Lambda functions are commonly used when you need a simple, concise function definition for one-time use, such as in sorting, filtering, or mapping operations.

## Explain lambda, map, filter and reduce functions

Lambda functions, `map()`, `filter()`, and `reduce()` are powerful built-in functions in Python for working with iterables. Here's an explanation of each with examples:

Lambda Functions (Anonymous Functions):
- Lambda functions are anonymous functions without a defined name.
- They are defined using the `lambda` keyword and are typically used for short, one-line functions.
- Lambda functions can be used inline without the need for a separate function definition.
- Example:

```python
# Square using lambda function
square = lambda x: x ** 2
result = square(5)
print(result)  # Output: 25
```

**Map Function:**
- The `map()` function applies a given function to each element of an iterable and returns an iterator of the results.
- It takes two arguments: the function to apply and the iterable object.
- The result is an iterator, which can be converted into a list or other desired format.
- Example:

```python
numbers = [1, 2, 3, 4, 5]

# Square using map()
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]
```

**Another example of Lambda with map:**

```
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

final_list = list(map(lambda x: x ** 2, li))
print("Using map: ", final_list)
```

**Filter Function:**
- The `filter()` function constructs a new iterator by selecting elements from an iterable that satisfy a given condition (expressed as a lambda function or a regular function).
- It takes two arguments: the filtering function and the iterable object.
- The result is an iterator containing only the elements that passed the filtering condition.
- Example:

```python
numbers = [1, 2, 3, 4, 5]

# Filter even numbers using filter()
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]
```

**Another example of Lambda with filter:**
```
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

def filter_list(li1):
    li2 = []
    for val in li1:
        if val%2 == 0:
            li2.append(val)
    return li2
print("Even numbers1: ", filter_list(li))


print("Even numbers2: ", list(filter(lambda x: (x % 2 == 0), li)))

ev_list = list(filter(lambda x: (x % 2 == 0), li))
print("Even numbers3: ", ev_list)
```

The output is:
```
Even numbers1:  [22, 54, 62]
Even numbers2:  [22, 54, 62]
Even numbers3:  [22, 54, 62]
```

**Reduce Function:**
- The `reduce()` function applies a given function to the first two elements of an iterable, then to the result and the next element, and so on, reducing the iterable to a single value.
- It requires the `functools` module to be imported.
- Example:

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Summing all numbers using reduce()
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)  # Output: 15
```

In this example, `reduce()` is used to apply the lambda function `lambda x, y: x + y` to the list of numbers. The function sums the elements pairwise until a single value is obtained.

These functions (`map()`, `filter()`, and `reduce()`) are versatile tools for processing data in Python, and using lambda functions enables concise and flexible functional programming approaches.

**Example of lambda with reduce:**
```
li = [1,2,3,4,5,6,7,8,9,10]
squared_list = list(map(lambda x: x ** 2, li))
print(squared_list)
```

The output is:
```
Using map:  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

**Another example of lambda with reduce:**

```
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print("Reduce data ", sum)
```

The output is:
```
Using map:  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Reduce data  193
```


## Explain the scope of variable using LEGB rule

The LEGB rule is an acronym that stands for Local, Enclosing, Global, and Built-in. It describes the order in which Python searches for variables in different scopes. Here's an explanation of each scope:

1. Local (L) Scope:
   - Variables defined within a function have local scope.
   - They are only accessible within the function where they are defined.
   - Example:

     ```python
     def my_function():
         local_variable = 10
         print(local_variable)

     my_function()  # Output: 10
     # Trying to access local_variable here would result in an error
     ```

2. Enclosing (E) Scope:
   - This scope applies to nested functions, where each nested function has access to its own local variables and variables from outer functions.
   - Example:

     ```python
     def outer_function():
         outer_variable = 10

         def inner_function():
             print(outer_variable)

         inner_function()  # Output: 10

     outer_function()
     ```

     In this example, the inner function `inner_function()` has access to the `outer_variable` defined in the outer function `outer_function()`.

3. Global (G) Scope:
   - Variables defined at the top-level of a module or declared as global inside a function have global scope.
   - They are accessible from anywhere within the module.
   - Example:

     ```python
     global_variable = 10

     def my_function():
         print(global_variable)

     my_function()  # Output: 10
     ```

     In this example, `global_variable` is defined outside of any function, making it accessible within the `my_function()`.

4. Built-in (B) Scope:
   - This scope includes the built-in functions and modules available in Python by default, such as `print()`, `len()`, and `range()`.
   - These functions are globally accessible without the need for an import statement.
   - Example:

     ```python
     def my_function():
         print(len("Hello"))

     my_function()  # Output: 5
     ```

     In this example, `len()` is a built-in function that can be used directly without importing any module.

Python follows the LEGB rule to resolve variable names. When a variable is referenced, Python searches for it in the local scope first, then in any enclosing scopes, followed by the global scope, and finally in the built-in scope.

If a variable is found in the local scope, that value is used. If not found, Python moves to the next scope until the variable is found or if it reaches the built-in scope. If the variable is not found anywhere, a `NameError` will be raised.

## Memory allocation of functions

In Python, memory allocation for functions and related data structures, such as local variables, parameters, and return values, is managed dynamically by the Python runtime using the call stack and heap. Python provides automatic memory management through reference counting and a garbage collector, which helps manage memory allocation and deallocation. Here's how function memory allocation works in Python:

1. **Function Call Stack:**
   - When a function is called in Python, a new frame is created on the call stack to store the function's local variables, parameters, return address, and other bookkeeping information.
   - Each function call creates a new stack frame, and the frames are organized in a last-in-first-out (LIFO) manner.

2. **Local Variables and Parameters:**
   - Local variables declared within a function are stored in the function's stack frame.
   - Function parameters (arguments) are also stored in the function's stack frame.
   - These variables and parameters exist only within the scope of the function and are automatically deallocated when the function returns.

3. **Automatic Memory Management:**
   - Python uses reference counting to keep track of the number of references to an object. When an object's reference count drops to zero (no longer in use), Python's garbage collector automatically reclaims the memory occupied by the object.
   - The garbage collector detects cyclic references to prevent memory leaks.

4. **Heap Allocation (Objects):**
   - Complex data structures, such as objects created using classes, are allocated on the heap.
   - Python's `object` type and custom classes (created using `class` definitions) are examples of heap-allocated objects.
   - The memory for these objects is managed by Python's memory management system.

5. **Dynamic Memory Allocation:**
   - In Python, you don't need to explicitly allocate memory for objects or deallocate memory when objects are no longer needed. Python handles this automatically.
   - When you create objects using constructors or literals (e.g., lists, dictionaries, strings), Python dynamically allocates memory for the objects on the heap.

6. **Reference Counting and Circular References:**
   - Python's reference counting mechanism detects when an object is no longer accessible, and the associated memory is automatically reclaimed.
   - Circular references (references forming a cycle) are detected and managed using a garbage collector that identifies and collects unreachable objects.

In summary, Python's memory management system, including the use of the call stack, heap allocation for objects, automatic reference counting, and garbage collection, makes memory allocation and deallocation transparent to the programmer, leading to simplified memory management and reduced risk of memory leaks.

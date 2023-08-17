
## 1. What is a function

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

## 2. Why we need to write functions

Functions are a fundamental concept in programming, and they serve several important purposes:

1. **Modularization and Reusability:** Functions allow you to break down your code into smaller, modular pieces. This makes your code more organized and easier to manage. You can reuse functions across different parts of your codebase, reducing redundancy and promoting code reusability.

2. **Abstraction:** Functions allow you to abstract complex logic into simpler, named operations. This makes your code easier to read and understand, as you can give meaningful names to these operations.

3. **Code Organization:** Functions help organize your code by grouping related operations together. This improves the readability and maintainability of your codebase.

4. **Debugging and Testing:** When a function is well-defined, you can isolate and test it separately from the rest of your code. This simplifies the debugging process, as you can focus on one part of the code at a time.

5. **Solving Complex Problems:** Functions enable you to break down complex problems into smaller, manageable steps. Each function can handle a specific part of the problem, making the overall solution easier to develop and understand.

6. **Collaboration:** Functions facilitate collaboration among team members. When you define clear function interfaces, team members can work on different parts of a project concurrently and integrate their work seamlessly.

7. **Readability and Maintainability:** By using functions, you can give meaningful names to operations and encapsulate logic. This makes your code more readable and maintainable, even for people who didn't write the code initially.

8. **Code Testing:** Functions make it easier to write unit tests for specific functionality. You can test individual functions in isolation to ensure they work correctly.

9. **Scaling:** As your codebase grows, functions help manage complexity. They allow you to handle different components of your application separately, making it easier to scale and extend your code.

In summary, functions provide a structured and organized way to implement, manage, and maintain code. They contribute to code reusability, readability, modularization, and efficient problem-solving.

## 3. Define function and explain in detail

A function in programming is a self-contained block of code that performs a specific task. It is a fundamental building block in most programming languages and serves the purpose of grouping a set of statements together to accomplish a particular goal. Functions allow you to break down your code into smaller, manageable parts, making it more organized, readable, and maintainable.

Here's a detailed breakdown of the key aspects of a function:

1. **Function Declaration/Definition:** A function is defined using the `def` keyword, followed by the function name and a pair of parentheses. Any required parameters are placed inside the parentheses.

2. **Function Name:** The name of the function should be meaningful and indicative of the task it performs. Function names follow the same naming conventions as variable names.

3. **Parameters:** Parameters are values that are passed to the function when it is called. They act as placeholders for data that the function needs to perform its task. Parameters are defined within the parentheses in the function definition.

4. **Function Body:** The body of the function contains the set of statements that define the task the function performs. These statements are indented under the function definition.

5. **Return Statement:** Functions can return a value using the `return` statement. This value is the result of the function's operation. If no `return` statement is present, the function returns `None` by default.

6. **Function Call:** To execute a function and make it perform its task, you call it by using its name followed by parentheses. If the function has parameters, you provide the values for those parameters within the parentheses.

Here's an example of a simple Python function that calculates the sum of two numbers:

```python
def add_numbers(x, y):
    sum = x + y
    return sum

result = add_numbers(5, 7)  # Calling the function with arguments 5 and 7
print(result)  # Output: 12
```

In this example:
- `add_numbers` is the function name.
- `x` and `y` are the parameters.
- Inside the function body, the sum of `x` and `y` is calculated and returned using the `return` statement.
- When the function is called with arguments `5` and `7`, it returns the sum `12`.

Functions play a crucial role in making code modular, reusable, and organized. They allow you to break down complex tasks into smaller, manageable chunks, improving code readability and maintainability. Additionally, functions promote the concept of DRY (Don't Repeat Yourself) by enabling code reusability across different parts of your program.

## 4. State vs Behavior

In programming, particularly in the context of object-oriented programming (OOP), the concepts of "state" and "behavior" are fundamental when designing classes and objects. These concepts help define the characteristics and actions associated with objects.

1. **State:**
   State refers to the attributes or properties that an object can have. It defines the data associated with the object. These attributes hold information that describes the object's current condition. For example, if you're designing a class for a "Car," the state of a car object might include attributes like "color," "make," "model," "speed," and "fuel level." State is represented by instance variables (also called attributes or fields) in a class.

2. **Behavior:**
   Behavior refers to the actions or functions that an object can perform. It defines the operations or methods that the object can execute. These methods define the actions that the object can take and how it interacts with other objects. Using the same "Car" example, behaviors of a car object could include methods like "start_engine," "accelerate," "brake," and "refuel."

In essence, the state of an object represents its characteristics and the data it holds, while the behavior of an object represents its actions and the operations it can perform.

Functions, both in OOP and in general programming, can encapsulate both state and behavior:

- **State in Functions:**
  Functions can take parameters as inputs and use those parameters to perform operations or calculations. The values of the parameters are part of the state that influences how the function behaves. For example, a function that calculates the area of a rectangle might take the length and width as parameters, which are part of the state that defines the rectangle's dimensions.

- **Behavior in Functions:**
  Functions define the behavior or actions that can be performed on data. They encapsulate a sequence of steps that accomplish a specific task. For example, a function that sorts a list of numbers is defining a behavior that rearranges the elements in a specific order.

In OOP, classes encapsulate both state (instance variables) and behavior (methods) within a single entity. This encapsulation promotes modularity, reusability, and easier maintenance of code. By combining state and behavior, classes provide a powerful way to model real-world entities and their interactions in code.

## 5. Function types

In Python, functions can be categorized into different types based on their characteristics and how they are used. Here are some common types of functions:

1. **Built-in Functions:**
   These are pre-defined functions that are provided by the Python interpreter. They are readily available for use without requiring any additional imports or definitions. Examples include `print()`, `len()`, `range()`, `max()`, `min()`, and `sum()`.

2. **User-Defined Functions:**
   These functions are defined by the programmer to perform specific tasks. They provide modularity and code reusability by encapsulating a sequence of steps within a named block of code. User-defined functions are created using the `def` keyword followed by a function name, parameters, and a code block. Example:
   ```python
   def calculate_area(length, width):
       return length * width
   ```

3. **Anonymous Functions (Lambda Functions):**
   These are small, one-line functions defined using the `lambda` keyword. They are often used for simple tasks and are commonly passed as arguments to higher-order functions like `map()`, `filter()`, and `sorted()`. Example:
   ```python
   double = lambda x: x * 2
   ```

4. **Recursive Functions:**
   Recursive functions are functions that call themselves to solve a problem. They involve breaking down a problem into smaller instances of the same problem. A base case is essential to prevent infinite recursion. Example:
   ```python
   def factorial(n):
       if n == 0:
           return 1
       else:
           return n * factorial(n - 1)
   ```

5. **Higher-Order Functions:**
   Higher-order functions are functions that can take other functions as arguments or return functions as results. They enable functional programming paradigms. Example:
   ```python
   def apply_operation(operation, x, y):
       return operation(x, y)

   def add(a, b):
       return a + b

   result = apply_operation(add, 3, 5)  # Result: 8
   ```

6. **Generator Functions:**
   Generator functions use the `yield` keyword to create generator objects. They produce values lazily and are memory-efficient for handling large datasets. Example:
   ```python
   def generate_even_numbers(limit):
       for i in range(limit):
           if i % 2 == 0:
               yield i

   even_numbers = generate_even_numbers(10)
   ```

7. **Method Functions:**
   These are functions defined within a class and are associated with instances of the class. They can access instance attributes and other methods. Example:
   ```python
   class Circle:
       def __init__(self, radius):
           self.radius = radius

       def calculate_area(self):
           return 3.14 * self.radius * self.radius
   ```

8. **Static Methods:**
   Static methods are defined within a class but don't have access to instance attributes. They are bound to the class rather than instances and are called using the class name. Example:
   ```python
   class MathUtils:
       @staticmethod
       def add(a, b):
           return a + b
   ```

Each type of function has its own purpose and use case. Understanding these different function types allows you to write more organized and efficient code.

## 6. Function calling ways

In Python, functions can be called using different approaches depending on how the function is defined and what arguments it requires. Here are the various ways to call a function:

1. **Positional Arguments:**
   The most common way to call a function is by providing the arguments in the order they are defined in the function signature. For example:
   ```python
   def greet(name, age):
       print(f"Hello, {name}! You are {age} years old.")

   greet("Alice", 30)
   ```

2. **Keyword Arguments:**
   You can also call a function by specifying the arguments along with their corresponding parameter names. This approach makes the code more readable and allows you to pass arguments in any order. For example:
   ```python
   greet(age=25, name="Bob")
   ```

3. **Default Arguments:**
   Functions can have default values assigned to their parameters. If an argument is not provided during the function call, the default value will be used. This makes some arguments optional. For example:
   ```python
   def greet(name, age=18):
       print(f"Hello, {name}! You are {age} years old.")

   greet("Eve")           # Uses default age (18)
   greet("David", 40)     # Overrides default age
   ```

4. **Variable Length Arguments:**
   Functions can accept a variable number of arguments using the `*args` syntax. These arguments are collected into a tuple and can be accessed within the function. For example:
   ```python
   def print_arguments(*args):
       for arg in args:
           print(arg)

   print_arguments("apple", "banana", "cherry")
   ```

5. **Keyword Variable Length Arguments:**
   Functions can accept a variable number of keyword arguments using the `**kwargs` syntax. These arguments are collected into a dictionary and can be accessed within the function. For example:
   ```python
   def print_key_value_pairs(**kwargs):
       for key, value in kwargs.items():
           print(f"{key}: {value}")

   print_key_value_pairs(name="Alice", age=30, city="New York")
   ```

6. **Unpacking Arguments:**
   You can unpack the contents of a list or tuple to pass as arguments to a function using the `*` operator. For example:
   ```python
   numbers = [2, 4, 6]
   greet(*numbers)   # Equivalent to greet(2, 4, 6)
   ```

7. **Passing Functions as Arguments:**
   You can pass functions as arguments to other functions, which is common when working with higher-order functions. For example:
   ```python
   def apply_operation(operation, a, b):
       return operation(a, b)

   def add(x, y):
       return x + y

   result = apply_operation(add, 3, 5)
   ```

These different ways of calling functions provide flexibility and allow you to design your code to be more readable, modular, and maintainable.

## 7. How to print function name. Explain how a function will be loaded

To print the name of a function within the function itself, you can use the `__name__` attribute of the function object. This attribute holds the name of the function as a string. Here's how you can do it:

```python
def my_function():
    print("Function name:", my_function.__name__)

my_function()
```

When you run the above code, it will output:

```
Function name: my_function
```

Regarding how a function is loaded and executed in Python:

1. **Compilation:** When you define a function in your Python code, Python doesn't immediately execute it. Instead, it compiles the function definition into bytecode, which is a lower-level representation that the Python interpreter can understand.

2. **Function Object Creation:** When the interpreter encounters a function definition, it creates a function object in memory. This function object holds the compiled bytecode and other attributes, including the function's name, parameters, and any other details.

3. **Execution:** When you call a function by using its name followed by parentheses (e.g., `my_function()`), Python looks up the function object using the function name and then executes the bytecode associated with that function.

4. **Function Scope:** The function object has access to its local variables, arguments, and any variables defined in its enclosing scope. It also has access to global variables.

5. **Name Resolution:** The function's name is resolved in the current scope. If the function is defined locally, the local definition takes precedence. If not found locally, Python looks in the global scope.

6. **Loading and Caching:** Once a function is defined and compiled, Python caches its bytecode and function object for subsequent calls. This makes function calls efficient, as Python doesn't need to recompile the function each time it's called.

7. **Function Call:** When a function is called, Python creates a new local scope for that call. The parameters and any local variables defined within the function are accessible within this scope.

8. **Returning Control:** When the function completes its execution, either by reaching the end of the code or encountering a `return` statement, it returns control to the caller, and any return value is passed back as needed.

In summary, functions in Python are loaded when the code is compiled and executed, and they are treated as objects with attributes, including the `__name__` attribute, which allows you to access the function's name at runtime.

## 8. Parameter vs Argument

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
     greet("Sam", 26)  # "Sam" and 26 are the arguments
     ```

In summary, parameters are the variables defined in the function declaration, whereas arguments are the actual values or expressions passed to a function 
during its invocation. Parameters define the expected input structure, while arguments provide the specific data to be processed by the function. 
It's essential to ensure that the number and order of arguments match the parameters in the function definition to avoid errors.

## 9. Variable vs Value

In programming, both values and variables are fundamental concepts that play a crucial role in storing and manipulating data. Let's explore what each term means:

1. **Value:**
   A value is a specific piece of data, such as a number, string, boolean, or any other data type. Values are the building blocks of any program and represent actual information that the program works with. Examples of values include:

   - `42` (integer value)
   - `'Hello, world!'` (string value)
   - `True` (boolean value)
   - `3.14` (floating-point value)

   Values are constants, meaning they don't change during the course of a program's execution.

2. **Variable:**
   A variable is a named storage location that can hold a value. Variables allow you to give a meaningful name to a piece of data so that you can refer to it later in your program. Variables provide a way to store and manipulate data dynamically during the execution of a program. They act as placeholders for values.

   Variables are created by assigning a value to a name using the assignment operator (`=`). Once a variable is created, you can change its value, and the new value will replace the old one. Examples of variables include:

   ```python
   age = 25  # 'age' is the variable, and '25' is the value assigned to it
   name = 'Sam'  # 'name' is the variable, and 'Sam' is the value assigned to it
   is_student = True  # 'is_student' is the variable, and 'True' is the value assigned to it
   ```

   Variables provide a way to store data that can vary throughout the program's execution.

In essence, a value is the actual data, and a variable is a named container that can hold and represent a value. Values remain constant, while variables can be assigned and reassigned different values over the course of a program's execution.

## 10. Different ways of calling function



## 11. Function overloading

**Function Overloading:**
Function overloading allows defining multiple functions with the same name but different parameter lists. When a function can be called in minimum two or more ways (based on the number of arguments)

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

## 12. Anonymous function. Explain in detail

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

## 13. Lambda with map filter and reduce functions. Explain in detail with examples

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

## 14. Function memory allocation


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

## 15. Scope of variable. Explain about LEGB rule

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


## 16. Give examples of all arithmetic operations using functions

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

## 17. Explain return statement in Python:

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

## 18. Give examples of printing the sum of two numbers with using return type and without using return type

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

## 19. Write a python to return the character count in a string.

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

## 20. Function categories 
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

## 21. Passing arguments in a function
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

## 22. Global and local variables

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


## 27. Parameterized functions
Parameterized functions are functions that accept input (arguments) when they are called. The arguments provide data to the function allowing it to perform
specific actions or calculations based on the provided values. Parameterized functions make code more flexible and reusable by allowing the same function to be used with different input values.

A simple example of parameterized functions:
```
def greet(name):
    print("Hello,", name)

# Calling the greet function with different arguments
greet("Sam")  # Output: Hello, Sam
greet("Ben")    # Output: Hello, Ben
```

When defining the function, the parameter `name` is passed to the function `greet`. When the function name is called, an argument is provided for the parameter
`name` which allows the function to personalize the greeting for different names.

Parameterized functions can have multiple parameters, each separated by a comma, and can be used to pass different types of data, such as numbers, strings, lists, or even other functions, to the function for processing.

Parameterized functions can have different types of parameters based on their usage and behavior. 

In programming, parameterized functions can have different types of parameters based on their usage and behavior. Here are the common types of parameters in parameterized functions:

1. **Positional Parameters**:
   These are the most common type of parameters in functions. The order of the arguments passed during the function call matters. The values are assigned to parameters based on their position.

```python
def greet(name, age):
    return "Hello, " + name + ", you are " + str(age) + " years old."

message = greet("Sam", 30)  # Positional parameters
print(message)
```

2. **Keyword Parameters**:
   In keyword parameters, the arguments are passed using the parameter name, allowing you to specify the values for specific parameters regardless of their position.

```python
def greet(age, name):  
   return "Hello, " + name + ", you are " + str(age) + " years old."

print(greet(age=25,name="Sam"))
```

3. **Default Parameters**:
   Default parameters have predefined default values in the function definition. If the caller doesn't provide a value for a default parameter, the default value is used.

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"

# Calling the greet function with default and custom values
message_default = greet("Alice")  # Using the default 'greeting'
message_custom = greet("Bob", "Hi")  # Using a custom 'greeting'

# Printing the returned messages
print(message_default)
print(message_custom)
```

4. **Variable-Length Parameters**:
   Variable-length parameters allow a function to accept a variable number of arguments. In Python, you can use `*args` for variable-length positional arguments and `**kwargs` for variable-length keyword arguments.

```python
def employee_details(*args):

   if len(args) < 3:
        return "Insufficient details provided for an employee."

   # 'args' is a tuple containing the variable-length arguments
   name = args[0]
   designation = args[1]
   age = args[2]

   details = f"{name} is a/an {designation} who is {age} years old."
   return details

employee1 = employee_details("John", "Engineer", 30)
print(employee1)
```

5. Calling Functions from Lists or Dictionaries:
You can use the `*` operator to unpack a list or tuple and pass its elements as separate positional arguments to a function. Similarly, you can use the `**` operator to unpack a dictionary and pass its key-value pairs as keyword arguments.

```
data = ["Sam", 30]
greet(*data)  # Unpacking list

data_dict = {"name": "Sam", "age": 25}
greet(**data_dict)  # Unpacking dictionary
```

Interview functions:

1. What is a function
2. Why we need to write functions
3. Define function and explain in detail
4. State vs Behavior
5. Function types
6. Function calling ways
7. How to print function name. Explain how a function will be loaded
8. Parameter vs Argument
9. Variable vs Value
10. Different ways of calling function
11. Function overloading
12. Ananymous function. Explain in detail
13. Lambda with map filter and reduce functions. Explain in detail with examples
14. Function memory allocation
15. Scope of variable. Explain about LEGB rule

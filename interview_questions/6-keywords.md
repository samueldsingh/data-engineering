# VI. Keywords:
=====================
### 1. Explain all keywords with examples and areas of usage

- In Python, keywords are reserved words that have special meanings and are used to define the syntax and structure of the language. 
- These keywords cannot be used as variable names or identifiers because they are already predefined and have specific functionalities assigned to them.

- There are 35 keywords in Python:
```
False      class      finally    is         return
None       continue   for        lambda     try
True       def        from       nonlocal   while
and        del        global     not        with
as         elif       if         or         yield
assert     else       import     pass
break      except     in         raise
```

Keywords in Python are reserved words that have predefined meanings and cannot be used as variable names or identifiers. They serve specific purposes in the Python language and have predefined functionalities. Here is an explanation of all the keywords in Python along with examples and areas of usage:

1. False, True:
   - These keywords represent boolean values, False and True, respectively.
   - Example:
     ```python
     flag = True
     if flag:
         print("Flag is True")
     ```

2. None:
   - The keyword None represents the absence of a value or the null value.
   - Example:
     ```python
     result = None
     ```

3. and, or, not:
   - These keywords are used for logical operations. 'and' represents logical AND, 'or' represents logical OR, and 'not' represents logical NOT.
   - Example:
     ```python
     a = True
     b = False
     if a and b:
         print("Both a and b are true")
     ```

4. if, else, elif:
   - These keywords are used for conditional statements. 'if' is used for defining a condition, 'else' specifies the alternate path when the condition is not met, and 'elif' is used for defining additional conditions.
   - Example:
     ```python
     age = 18
     if age >= 18:
         print("You are an adult")
     elif age >= 13:
         print("You are a teenager")
     else:
         print("You are a child")
     ```

5. for, while, break, continue:
   - These keywords are used for looping and flow control. 'for' is used for iterating over a sequence, 'while' is used for creating a loop with a condition, 'break' is used to exit a loop prematurely, and 'continue' is used to skip the current iteration and move to the next one.
   - Example:
     ```python
     for i in range(5):
         if i == 3:
             break
         print(i)
     ```

6. def, return:
   - These keywords are used for defining and returning functions. 'def' is used to define a function, and 'return' is used to specify the return value from a function.
   - Example:
     ```python
     def add(a, b):
         return a + b
     ```

7. class, object:
   - These keywords are used for creating classes and objects in object-oriented programming. 'class' is used to define a class, and 'object' is the base class for all other classes in Python.
   - Example:
     ```python
     class Car:
         def __init__(self, make, model):
             self.make = make
             self.model = model

     myCar = Car("Toyota", "Camry")
     ```

8. import, from, as:
   - These keywords are used for importing modules and packages. 'import' is used to import an entire module, 'from' is used to import specific items from a module, and 'as' is used to provide an alias for imported modules or items.
   - Example:
     ```python
     import math
     from datetime import datetime as dt
     ```

9. try, except, finally:
   - These keywords are used for exception handling. 'try' is used to specify a block of code where exceptions may occur, 'except' is used to handle specific exceptions, and 'finally' is used to specify a block of code that will be executed regardless of whether an exception occurs or not.
   - Example:
     ```python
     try:
         result = 10 / 0
     except ZeroDivisionError:
         print("Error: Division by zero")
     finally:
         print("Cleanup code")
     ```

10. global, nonlocal:
    - These keywords are used for accessing variables in different scopes. 'global' is used to access global variables within a function, and 'nonlocal' is used to access variables in the enclosing (non-global) scope of nested functions.
    - Example:
      ```python
      count = 0

      def increment():
          global count
          count += 1

      increment()
      print(count)
      ```

These keywords are essential building blocks of the Python language and are used in various areas of programming, such as conditional statements, loops, functions, classes, exception handling, and module imports. Understanding their functionalities and proper usage is crucial for writing effective and readable Python code.

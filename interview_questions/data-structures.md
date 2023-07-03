IX. Data Structures:
=====================
        
### 1. What are CRUD operations.Explain in detail 
        
### 2. Sequence.Types. Operations on each sequence
            
### 3. HTTP Request methods for CRUD. Explain in detail 
HTTP (Hypertext Transfer Protocol) provides a set of request methods or verbs that define 
the intended action to be performed on a resource. These methods are often used in web 
development for implementing CRUD (Create, Read, Update, Delete) operations on resources. 
Here's a brief explanation of each HTTP request method in the context of CRUD:

1. GET:
The GET method is used to retrieve or read a representation of a resource from the server. It is idempotent, meaning that multiple identical requests should have the same effect as a single request. In CRUD, GET is typically used for retrieving existing resources.

2. POST:
The POST method is used to submit data to be processed by the server. It is non-idempotent, meaning that multiple identical requests may have different effects. In CRUD, POST is typically used for creating new resources.

3. PUT:
The PUT method is used to update or replace a resource on the server. It is idempotent, meaning that multiple identical requests should have the same effect as a single request. In CRUD, PUT is typically used for updating existing resources.

4. PATCH:
The PATCH method is used to partially update a resource on the server. It is not required to be idempotent. In CRUD, PATCH is also used for updating existing resources, but only modifying specific fields or properties.

5. DELETE:
The DELETE method is used to delete a resource from the server. It is idempotent, meaning that multiple identical requests should have the same effect as a single request. In CRUD, DELETE is used for deleting existing resources.

These HTTP request methods provide a standardized way of performing CRUD operations on resources over the web. When designing web applications, these methods are mapped to corresponding actions or endpoints to handle the desired operations on the server side.
     
### i. Numbers:
        
### 1. Types of numbers. Explain each use case 
In Python, there are several types of numbers that can be used for different purposes. Here are the commonly used number types and their use cases:

1. Integers (int):
Integers represent whole numbers without any fractional part. They are used for tasks that involve counting, indexing, or representing discrete quantities. Integers can be positive, negative, or zero.

2. Floating-Point Numbers (float):
Floating-point numbers represent real numbers with a fractional part. They are used for tasks that involve decimal values, measurements, or calculations requiring precision. Floating-point numbers can represent both small and large values.

3. Complex Numbers (complex):
Complex numbers are used to represent numbers with both real and imaginary parts. They are often used in mathematical calculations involving complex algebra, signal processing, or scientific computations.

4. Booleans (bool):
Booleans represent truth values and can only have two possible values: True or False. They are used for logical operations, conditionals, and control flow. Booleans are often the result of comparisons or logical operations.

5. Long Integers (long):
Long integers are used to represent arbitrarily large integers. They can handle numbers beyond the range of regular integers. Long integers are used when precision and large number handling is required, such as in cryptography or mathematical computations.

These different number types allow you to work with various kinds of data and perform different calculations and operations in Python. It's important to choose the appropriate number type based on the requirements of your specific task to ensure accurate results and efficient memory usage.    
        
        
### 2. type conversions
Type conversion, also known as type casting, is the process of converting a value from one data type to another in a programming language. In Python, you can perform various type conversions to manipulate and operate on data of different types. Here are some common type conversions in Python:

1. Implicit Type Conversion:
Implicit type conversion, also known as automatic type conversion, is performed automatically by Python when it is safe to do so. For example, if you perform arithmetic operations between different numeric types, Python will automatically convert the operands to a common type before performing the operation. This is called implicit type promotion. For instance:
```
a = 5
b = 2.5
c = a + b  # The integer 'a' is implicitly converted to a float before addition
```

2. Explicit Type Conversion:
Explicit type conversion, also known as explicit type casting, is performed manually by the programmer using built-in functions or constructors. It allows you to explicitly convert a value from one type to another. Some common explicit type conversion functions in Python include:
`int():` Converts a value to an integer.
`float():` Converts a value to a floating-point number.
`str():` Converts a value to a string.
`bool():` Converts a value to a boolean.
`list():` Converts a value to a list.
`tuple():` Converts a value to a tuple.
`set():` Converts a value to a set.
`dict():` Converts a value to a dictionary.

```
x = 10.5
y = int(x)  # Explicitly converts the float 'x' to an integer
```

3. Type Conversion using Constructors:
In addition to the explicit type conversion functions, some data types in Python have constructors that can be used to create objects of that type. These constructors can also be used for type conversion. For example, the `int()`, `float()`, `str()`, `list()`, `tuple()`, `set()`, and `dict()` constructors can be used to convert values to their respective types

```
a = "123"
b = int(a)  # Converts the string 'a' to an integer using the int() constructor
```

Type conversions are useful when you need to perform operations or manipulate data of different types. However, it's important to ensure that the conversion is valid and makes sense in the context of your program to avoid errors or unexpected behavior.
        
### 3. Explain different operations of boolean type
    
    
### ii. String:
        1. Explain about string. 
        2. Multi line string 
        3. String is Immutable.Explain in detail 
        4. CRUD Operations on String
        5. Sequence operations on String
        6. Memory allocation of String 
        7. Explain 10 important functions of String

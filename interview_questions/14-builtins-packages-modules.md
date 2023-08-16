
## 1. Importance of Package vs Module

In Python, both packages and modules play crucial roles in organizing and structuring code. They help manage code complexity, promote reusability, and improve code maintenance. However, they serve slightly different purposes:

**Module:**
- A module is a single file that contains Python code, including functions, classes, and variables.
- Modules are used to logically group related code together and make it easier to manage.
- Modules encourage code reusability by allowing you to import and use their contents in other modules or scripts.
- Example: If you have a module named `math_operations.py` with functions for various mathematical operations, you can import and use those functions in other parts of your code.

**Package:**
- A package is a collection of related modules organized in a directory structure.
- Packages help organize larger projects by grouping related modules into subdirectories, creating a hierarchical structure.
- Packages often contain an `__init__.py` file, which can be empty or contain initialization code for the package.
- Packages can include subpackages, which are subdirectories that themselves are packages.
- Example: If you have a package named `data_processing` with submodules `cleaning`, `transforming`, and `analyzing`, you can have a well-organized structure for data-related tasks.

**Importance of Packages and Modules:**
1. **Code Organization:** Both packages and modules help organize code, making it more manageable and understandable, especially in larger projects.
2. **Reusability:** Modules and packages allow you to encapsulate functionality that can be reused across different parts of your code or even in different projects.
3. **Encapsulation:** Modules and packages facilitate encapsulation, as you can control the visibility of variables and functions using public and private naming conventions.
4. **Collaboration:** When working with a team, modular code is easier to collaborate on and integrate into a larger project.
5. **Maintenance:** Modular code is easier to maintain and update. Changes in one module or package don't necessarily affect others.
6. **Avoiding Name Conflicts:** Modules and packages provide namespaces, which help avoid naming conflicts between different parts of your code.

In summary, both modules and packages are essential for structuring, organizing, and maintaining Python code. Modules allow you to encapsulate functionality within individual files, while packages extend this organization to directory structures, enabling even better code organization and separation of concerns.

## 2. file vs module

In Python, both "file" and "module" are related concepts, but they serve different purposes:

**File:**
A file in Python refers to a collection of data or information stored on a storage device, such as a hard drive. Files can contain various types of data, such as text, binary data, images, audio, and more. Python provides built-in functions and libraries to work with files, allowing you to read from and write to files.

**Module:**
A module in Python is a collection of functions, classes, and variables that can be used to perform specific tasks. Modules are used to organize code into reusable and maintainable units. They promote code reusability and modular programming. A module can be a single Python file containing Python code, and it can be imported into other Python scripts to use the functions, classes, and variables defined in that module.

Here's a more detailed explanation of both concepts:

**File:**
- A file is a storage entity that can hold various types of data.
- Files can be text files, binary files, or a combination of both.
- Examples of files include text documents, images, audio files, video files, etc.
- Python provides functions like `open()` to work with files, allowing you to read and write data to and from them.

Example of reading from a text file:

```python
# Open and read from a text file
with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)
```

**Module:**
- A module is a collection of related functions, classes, and variables.
- Modules promote code organization, reusability, and maintainability.
- Modules can be imported into other Python scripts using the `import` statement.
- Python comes with built-in modules (like `math`, `random`, `os`, etc.), and you can create your own custom modules.

Example of creating and using a custom module:

```python
# Example of a custom module named 'my_module.py'
def greet(name):
    return f"Hello, {name}!"

# Another script using the custom module
import my_module

message = my_module.greet("Sam")
print(message)  # Output: Hello, Sam!
```

In summary, a "file" is a storage entity that holds data, while a "module" is a collection of code elements that can be imported and used in other Python scripts.

## 3. package vs module

In Python, both packages and modules are fundamental concepts that help organize and structure your code in a more manageable way. Let's explore the differences between packages and modules:

**Module:**
A module is a single file that contains Python code. It can include functions, classes, and variables that can be used in other Python programs by importing the module. Modules are used to break down code into smaller, reusable components.

Example of a module named `my_module.py`:

```python
# my_module.py

def greet(name):
    return f"Hello, {name}!"
```

You can use the functions from the module in another Python script:

```python
import my_module

message = my_module.greet("Sam")
print(message)  # Output: Hello, Sam!
```

**Package:**
A package is a collection of related modules organized in a directory hierarchy. It includes a special file called `__init__.py` to indicate that the directory should be treated as a package. Packages allow you to create a structured namespace for your modules.

Example of a package structure:

```
my_package/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
```

You can access modules from a package using dot notation:

```python
from my_package import module1, subpackage.module3

result1 = module1.some_function()
result2 = subpackage.module3.another_function()
```

Key differences between packages and modules:

1. **Structure:**
   - A module is a single file containing code.
   - A package is a directory containing multiple modules and possibly subpackages.

2. **Use Cases:**
   - Modules are used to encapsulate related functions, classes, and variables for reuse.
   - Packages are used to organize and group related modules and subpackages.

3. **Namespace:**
   - Modules have their own namespace.
   - Packages provide a structured namespace for modules and subpackages.

4. **Importing:**
   - Modules are imported using their filename (without the `.py` extension).
   - Modules and submodules within a package are imported using dot notation.

In summary, modules provide a way to encapsulate code, while packages provide a way to organize and structure your modules within a directory hierarchy.

## 4. Builtin libraries. Explain about min 10 libraries in python

Built-in libraries in Python are modules and packages that are included with the Python programming language by default. These libraries provide a wide range of functionality and allow you to perform various tasks without having to install external packages. Here are 10 important built-in libraries in Python:

1. **math:**
   The `math` library provides various mathematical functions and constants. It includes functions for basic arithmetic operations, trigonometry, exponentiation, logarithms, and more.

   Example:
   ```python
   import math

   print(math.sqrt(25))  # Output: 5.0
   print(math.pi)        # Output: 3.141592653589793
   ```

2. **random:**
   The `random` library is used to generate random numbers. It provides functions to generate random integers, floating-point numbers, and to shuffle sequences.

   Example:
   ```python
   import random

   print(random.randint(1, 10))  # Generate a random integer between 1 and 10
   print(random.random())        # Generate a random floating-point number between 0 and 1
   ```

3. **datetime:**
   The `datetime` library is used for working with dates and times. It provides classes for date, time, datetime, timedelta, and more.

   Example:
   ```python
   from datetime import datetime, timedelta

   now = datetime.now()
   print(now)                       # Current date and time
   future_date = now + timedelta(days=7)
   ```

4. **os:**
   The `os` library provides functions for interacting with the operating system. It allows you to work with files, directories, and execute system commands.

   Example:
   ```python
   import os

   print(os.getcwd())               # Get current working directory
   os.mkdir("new_directory")        # Create a new directory
   ```

5. **sys:**
   The `sys` library provides functions and variables to interact with the Python interpreter. It's commonly used for command-line arguments and environment variables.

   Example:
   ```python
   import sys

   print(sys.argv)                  # Command-line arguments
   print(sys.version)               # Python version information
   ```

6. **re:**
   The `re` library is used for regular expressions. It allows you to work with patterns and perform pattern matching and substitution in strings.

   Example:
   ```python
   import re

   pattern = r'\d+'  # Match one or more digits
   result = re.findall(pattern, "123 abc 456")
   print(result)                    # Output: ['123', '456']
   ```

7. **json:**
   The `json` library is used for working with JSON (JavaScript Object Notation) data. It allows you to encode Python objects into JSON and decode JSON into Python objects.

   Example:
   ```python
   import json

   data = {'name': 'Sam', 'age': 26}
   json_string = json.dumps(data)   # Convert dictionary to JSON string
   ```

8. **collections:**
   The `collections` library provides additional data structures beyond the built-in types. It includes useful classes like `Counter`, `defaultdict`, and `deque`.

   Example:
   ```python
   from collections import Counter

   text = "hello"
   counter = Counter(text)
   print(counter)                   # Output: Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
   ```

9. **urllib:**
   The `urllib` library is used for working with URLs. It provides functions for fetching data from the internet, parsing URLs, and encoding/decoding query strings.

   Example:
   ```python
   from urllib.request import urlopen

   response = urlopen('https://www.example.com')
   html = response.read()
   ```

10. **csv:**
    The `csv` library provides classes for reading and writing CSV (Comma Separated Values) files. It simplifies the process of working with tabular data in plain text format.

    Example:
    ```python
    import csv

    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
    ```

These are just a few examples of the built-in libraries in Python. Python's standard library contains many more modules that provide various functionalities for different purposes.

## 5. from import vs import (Directly importing module vs importing specific function/class from module)

In Python, you can import modules using either the `import` statement or the `from ... import ...` statement. Both approaches allow you to use the functionality provided by the imported module, but they differ in how you access that functionality within your code.

1. **Importing the Entire Module:**
   When you use the `import` statement, you bring the entire module into your current namespace. You access the module's functions, classes, and variables using the module's name as a prefix.

   ```python
   import math

   result = math.sqrt(25)
   ```

   Here, the `math` module is imported, and you access its `sqrt` function using `math.sqrt()`.

2. **Importing Specific Function/Class from Module:**
   With the `from ... import ...` statement, you can selectively import specific functions, classes, or variables from the module directly into your namespace. This way, you don't need to use the module's name as a prefix when accessing them.

   ```python
   from math import sqrt

   result = sqrt(25)
   ```

   In this example, only the `sqrt` function is imported directly, and you can use it without the `math.` prefix.

Using `import`:
- Allows you to access any functionality in the module without needing to specify each function/class explicitly.
- Keeps the namespace clean and prevents naming conflicts.
- Provides clear visibility of the origin of functions or classes in your code.

Using `from ... import ...`:
- Allows you to use specific functions or classes without the need for the module's name as a prefix.
- Can lead to shorter and more readable code when dealing with specific functionalities.
- Be cautious with this approach to avoid naming conflicts if you import similarly named functions/classes from different modules.

In general, it's a good practice to use `import` when you need various functionalities from a module and `from ... import ...` when you only need specific ones. However, it's essential to strike a balance between keeping your code concise and avoiding potential naming conflicts.

## 6. Create 2 packages,modules inside it. Call function from first package inside second package module


## 7. __init__.py file in each package. Why. Importance


## 10. if __name__ == '__main__': What it means ?

The `if __name__ == '__main__':` construct is a common pattern used in Python scripts to determine whether the script is being run as the main program or if it's being imported as a module into another script. This construct allows you to write code that can be both used as a standalone script and as a module that can be imported into other scripts.

When you run a Python script, the interpreter assigns a special built-in variable called `__name__` to the script. If the script is the main program being executed, the value of `__name__` is set to `'__main__'`. If the script is being imported as a module into another script, the value of `__name__` is set to the name of the module (the filename without the `.py` extension).

Here's an example to illustrate its usage:

Consider a script named `my_script.py`:

```python
def add(a, b):
    return a + b

if __name__ == '__main__':
    print("Running as a standalone script.")
    result = add(5, 3)
    print("Result:", result)
```

If you run `my_script.py` directly (i.e., `python my_script.py`), you will see the output:

```
Running as a standalone script.
Result: 8
```

However, if you import `my_script` in another script:

```python
import my_script

result = my_script.add(10, 20)
print("Result from imported module:", result)
```

The output will be:

```
Result from imported module: 30
```

The `if __name__ == '__main__':` construct is useful because it allows you to include code that should only run when the script is run as the main program, while preventing that code from executing when the script is imported as a module. This is particularly helpful when you want to provide reusable modules that can be imported into other scripts without executing their main functionality.

## 11. Scope resolution

Scope resolution in Python refers to the process of determining which variable, function, or class definition is being referred to in a particular part of the code. Python uses a set of rules to resolve variable names to their respective definitions based on their scope. The concept of scope is crucial to understand how variables are accessed and manipulated in different parts of a program.

Python has four main levels of scope resolution:

1. **Local Scope:** Variables defined within a function are in the local scope. They are accessible only within that function. Local scope takes precedence over other scopes during name resolution.

2. **Enclosing Scope:** If a function is defined within another function, the inner function has access to variables from the outer function's scope. The outer function's scope is called the enclosing scope.

3. **Global Scope:** Variables defined at the top level of a script or module (outside any function) are in the global scope. They can be accessed from anywhere in the script.

4. **Built-in Scope:** This is the scope that contains all the built-in functions, such as `print()`, `len()`, etc. These functions can be accessed from any part of the code.

The scope resolution is determined by the LEGB rule:

- **L (Local):** Search for the name in the local scope (inside the current function).
- **E (Enclosing):** Search for the name in the enclosing scopes (if any), from inner to outer functions.
- **G (Global):** Search for the name in the global scope (at the top level of the script or module).
- **B (Built-in):** Search for the name in the built-in scope (containing built-in functions).

Python follows this order when looking up names. If a name is not found in the current scope, it will be searched in the enclosing scopes, then the global scope, and finally the built-in scope.

Here's an example to illustrate scope resolution:

```python
x = 10  # Global variable

def outer_function():
    y = 20  # Enclosing variable

    def inner_function():
        z = 30  # Local variable
        print(x)  # Accesses global variable
        print(y)  # Accesses enclosing variable
        print(z)  # Accesses local variable

    inner_function()

outer_function()
```

In this example, the innermost `inner_function` first searches for `z` in its local scope, then `y` in its enclosing scope, and finally `x` in the global scope.

Understanding scope resolution is essential to avoid naming conflicts and to ensure that variables are accessed correctly throughout your code.

## 12. Recursive import issue in python

A recursive import issue, also known as a circular import, occurs when two or more modules depend on each other in a way that one module imports the other, and the other module also imports the first one. This creates a loop in the import process, leading to potential problems and errors in your Python code.

Let's consider an example to illustrate the recursive import issue:

**module_a.py**
```python
# module_a.py
import module_b

def function_a():
    print("Function A")

module_b.function_b()
```

**module_b.py**
```python
# module_b.py
import module_a

def function_b():
    print("Function B")

module_a.function_a()
```

In this example, `module_a` imports `module_b`, and `module_b` imports `module_a`. When you try to run any of these modules, you'll encounter the recursive import issue.

This issue can lead to the following problems:

1. **Attribute Errors:** Since the modules are being imported before they are fully defined, attributes or functions may not be accessible, leading to attribute errors.

2. **Cyclic Dependencies:** Recursive imports create cyclic dependencies, making it difficult to manage and understand the flow of your code.

3. **Infinite Loop:** The imports create a loop, causing the interpreter to get stuck in an infinite loop while trying to resolve the imports.

To avoid recursive import issues:

1. **Restructure Your Code:** Consider reorganizing your code to remove circular dependencies. Splitting functionality into separate modules and designing a clear hierarchy can help.

2. **Import as Needed:** Instead of importing a module at the top level, import it only within functions or methods where it's actually used.

3. **Import Inside Functions:** Importing modules inside functions rather than at the module level can help avoid the circular import issue.

4. **Use Importing Techniques:** Use conditional imports or delayed imports using function calls to break the circular dependency.

For example:

**module_a.py**
```python
def function_a():
    from module_b import function_b
    print("Function A")
    function_b()
```

**module_b.py**
```python
def function_b():
    from module_a import function_a
    print("Function B")
    function_a()
```

By following these practices, you can prevent recursive import issues and create a more modular and maintainable codebase.

## 13. Explain the different files used in your project:

- **json**: It is the string version that can be read or written to a file. Python has a JSON module that will help converting the datastructures to JSON strings. The JSON module is mainly used to convert the python dictionary above into a JSON string that can be written into a file.

- **gzip**: Python's gzip module is the interface to GZip application. The gzip data compression algorithm itself is based on zlib module. The gzip module contains definition of GzipFile class along with its methods. It also caontains convenience function open(), compress() and decompress().

- **csv**: CSV (Comma Separated Values) is a simple file format used to store tabular data, such as a spreadsheet or database. A CSV file stores tabular data (numbers and text) in plain text. Each line of the file is a data record.

- **xwlt+**: This is a library for developers to use to generate spreadsheet files compatible with Microsoft Excel versions 95 to 2003. The package itself is pure Python with no dependencies on modules or packages outside the standard Python distribution.

- **base64**: Module is used to encode and decode data. First, the strings are converted into byte-like objects and then encoded using the base64 module. The below example shows the implementation of encoding strings isn't base64 characters. Example: import base64.

- **os**: The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc. You first need to import the os module to interact with the underlying operating system

- **sys**: The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment. It allows operating on the interpreter as it provides access to the variables and functions that interact strongly with the interpreter.

- **sentry**: Sentry's Python SDK enables automatic reporting of errors and exceptions as well as identifies performance issues in your application. Sentry's Python SDK includes powerful hooks that let you get more out of Sentry, and helps you bind data like tags, users, or contexts.	

- **flask**: Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. Flask is a micro web framework written in Python. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools

**Flask-RESTful:**

Flask-RESTful is an extension for Flask, a popular web framework for Python, that simplifies the process of building RESTful APIs (Application Programming Interfaces). RESTful APIs are used to expose your application's functionalities as a set of URLs that can be easily consumed by other applications or clients.

Flask-RESTful provides tools to create APIs quickly and efficiently by allowing you to define resources as Python classes. Each resource corresponds to a URL, and HTTP methods (GET, POST, PUT, DELETE, etc.) are mapped to methods within the resource class. It also handles input validation, serialization, and response formatting, making it easier to build robust APIs.

Here's a simple example of using Flask-RESTful to create a basic API:

```python
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run()
```

In this example, the `HelloWorld` class is a resource that handles HTTP GET requests at the root URL ("/"). The `get` method returns a JSON response with a simple message. Flask-RESTful handles the routing and serialization for you.

Flask-RESTful makes it convenient to build APIs with proper structure and adherence to REST principles, allowing you to focus on your application's logic rather than the intricacies of handling HTTP requests and responses.

**random**: Python Random module is an in-built module of Python which is used to generate random numbers. These are pseudo-random numbers means these are not truly random. This module can be used to perform random actions such as generating random numbers, print random a value for a list or string, etc.			

**request:** The requests module allows you to send HTTP requests using Python. The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).

**requests:** Requests is a Python Library that lets you send HTTP/1.1 requests, add headers, form data, multipart files, and parameters with simple Python dictionaries. It also lets you access the response data in the same way.

**Pickle Files:**

Pickle is a module in Python that provides a way to serialize (convert objects into byte streams) and deserialize (convert byte streams back into objects) complex data structures like dictionaries, lists, classes, etc. Pickle is often used for data persistence, data serialization, or transferring data between different Python programs.

**Serialization** is the process of converting complex data structures into a format that can be easily stored or transmitted, such as byte streams. **Deserialization** is the reverse process of converting the serialized data back into its original data structure.

Pickle is particularly useful when you want to store data in a file or transmit data between different systems while preserving the structure and type of the data. It's important to note that pickle files are specific to Python and may not be interoperable with other programming languages.

Here's a simple example of using pickle to serialize and deserialize data:

```python
import pickle

data = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Serialize the data and write it to a pickle file
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Deserialize the data from the pickle file
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
```

## 14. Explain serialization and deserialization

**Serialization** is the process of converting complex data structures or objects into a format that can be easily stored or transmitted. Serialization allows you to represent the data in a structured manner so that it can be reconstructed later. The serialized data can be saved to a file, sent over a network, or stored in a database. Serialization is commonly used in scenarios where data needs to be persisted or transferred between different systems or applications.

The primary purpose of serialization is to convert data into a format that can be easily stored or transmitted, while preserving its structure and type information. This allows the data to be reconstructed accurately when needed.

**Deserialization**, on the other hand, is the reverse process of serialization. It involves converting the serialized data back into its original data structure or object. Deserialization reconstructs the data based on the information stored in the serialized representation.

Serialization and deserialization are commonly used in various contexts, such as:

1. **Data Persistence**: Serialization is used to save the state of objects to a file, database, or other storage medium. This allows the objects to be restored later, even after the application has been closed or restarted.

2. **Network Communication**: Serialized data can be transmitted over a network between different systems. This is useful for communication between client-server applications or services.

3. **Caching**: Serialized data can be cached to improve performance. Cached data can be quickly retrieved and deserialized when needed.

4. **Distributed Systems**: In distributed systems, objects may need to be serialized and sent to other nodes for processing or storage.

5. **Data Exchange**: Serialized data can be exchanged between applications written in different programming languages, as long as both sides understand the serialization format.

Common formats for serialized data include JSON (JavaScript Object Notation), XML (eXtensible Markup Language), and binary formats like Pickle in Python or Protocol Buffers.

Example of Serialization and Deserialization using JSON:

```python
import json

# Data to be serialized
data = {'name': 'Sam', 'age': 26, 'city': 'Bangalore'}

# Serialization: Convert data to JSON format
serialized_data = json.dumps(data)

print(serialized_data)  # Output: {'name': 'Sam', 'age': 26, 'city': 'Bangalore'}

# Deserialization: Convert JSON data back to Python data structures
deserialized_data = json.loads(serialized_data)

print(deserialized_data)  # Output: {'name': 'Sam', 'age': 26, 'city': 'Bangalore'}
```

In this example, the `json.dumps()` function serializes the data to a JSON-formatted string, and the `json.loads()` function deserializes the JSON string back into Python data structures.

## 15. Collections, modules, classes, properties

1. `defaultdict`:
A `defaultdict` is a subclass of the built-in `dict` class. It provides a default value for the keys that are not present in the dictionary.

```python
from collections import defaultdict

# Create a defaultdict with int as default factory
word_count = defaultdict(int)

# Count the occurrences of words in a sentence
sentence = "This is a sample sentence for demonstration purposes"
for word in sentence.split():
    word_count[word] += 1

print(word_count)
# Output: defaultdict(<class 'int'>, {'This': 1, 'is': 1, 'a': 1, 'sample': 1, 'sentence': 1, 'for': 1, 'demonstration': 1, 'purposes': 1})
```

2. `OrderedDict`:
An `OrderedDict` is a dictionary subclass that maintains the order of elements based on the insertion order.

```python
from collections import OrderedDict

# Create an ordered dictionary
person_info = OrderedDict()
person_info['name'] = 'Sam'
person_info['age'] = 26
person_info['city'] = 'Bangalore'

print(person_info)
# Output: OrderedDict([('name', 'Sam'), ('age', 26), ('city', 'Bangalore')])
```

3. `namedtuple`:
A `namedtuple` is a subclass of a tuple that allows you to give names to each position in the tuple, making it more readable.

```python
from collections import namedtuple

# Create a named tuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 5)

print(p.x)  # Output: 3
print(p.y)  # Output: 5
```

4. `frozenset`:
A `frozenset` is an immutable version of a set. It is useful when you want to create a set that can be used as a dictionary key or an element of another set.

```python
# Create a frozenset
fruits = frozenset(["apple", "banana", "orange"])

# Use frozenset in a dictionary
fruit_dict = {fruits: "fruit set"}
print(fruit_dict)
# Output: {frozenset({'orange', 'banana', 'apple'}): 'fruit set'}
```

5. `Counter`:
A `Counter` is a dictionary subclass that counts the occurrences of elements in an iterable.

```python
from collections import Counter

# Create a Counter
colors = ["red", "blue", "green", "red", "blue", "red", "yellow"]
color_counter = Counter(colors)

print(color_counter)
# Output: Counter({'red': 3, 'blue': 2, 'green': 1, 'yellow': 1})
```

These data structures from the `collections` module provide additional functionality beyond the standard built-in data structures in Python.

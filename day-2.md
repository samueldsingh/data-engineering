# What is Python? What are the advantages and disadvantages of Python? Where is it used?

- It is a high level, object-oriented, interpreted and general purpose programming language known for its simplicity, readability, versatility and reuseability. 
- It is popular due to its clean and easy-to-understand syntax, which emphasizes code readability.
- It offers a wide range of built-in functions and libraries that make it efficient for various programming tasks.
- Python can be used for a wide range of applications, including web development, data analysis, scientific computing, artificial intelligence, machine learning, automation, and more. 
- Python programs consist of statements and expressions that define the logic and behavior of the program. 
- These programs can include control structures like loops and conditionals, data structures like lists and dictionaries, functions and classes for code organization and reusability, as well as modules and packages for code modularization and sharing.
- Its extensive standard library and third-party packages make it capable of handling a wide variety of programming tasks efficiently and effectively.

## Why Python is an Interpreted Language?
Python is often referred to as an interpreted language because it uses an interpreter to execute code directly, without the need for prior compilation into machine code. Here are a few reasons why Python is considered an interpreted language:

- Readability and Simplicity: Python emphasizes code readability and simplicity, and being an interpreted language aligns with these principles. Python code is written in a more human-readable format, which makes it easier for developers to write, understand, and modify.

- Dynamic Typing: Python is dynamically typed, meaning you **don't need to explicitly declare variable types**. The interpreter determines the type of a variable at runtime based on the assigned value. This flexibility is possible because the interpreter can evaluate and handle type information dynamically.

- Rapid Development: Interpreted languages like Python are known for their faster development cycle. Since there is no separate compilation step, developers can write code and immediately execute it. This facilitates faster iteration and prototyping, making Python suitable for rapid application development.

- Interactive Shell: Python provides an interactive shell, also known as a REPL (Read-Evaluate-Print Loop). The Python interpreter allows users to **interactively experiment with code, enter statements, and immediately see the results. This interactive nature is particularly useful for testing and exploring code snippets**.

Portability: Python's interpreted nature contributes to its portability. Python programs can run on any platform or operating system that has a compatible Python interpreter installed, without the need for recompilation. This enables code portability and simplifies the process of sharing and distributing Python applications.

While Python is primarily interpreted, it does have an optional compilation step. Python code can be compiled into bytecode, which is then executed by the interpreter. This bytecode compilation improves performance and enables distribution of compiled Python programs. However, this compilation step is transparent to the developer and handled automatically by the interpreter or tools like Just-In-Time (JIT) compilers.

## Entity, Attributes, Values, Datatypes

**Entity**: Represents real world object or concept that you want to model in your program. 
- It can be a person, a place, a thing, or an abstract concept. In programming, entities are typically represented as **objects or instances of classes**.

**Attributes**: Attributes are characteristics or properties associated with an entity. 
- They describe the state or features of an entity. 
- For example, if you have an entity representing a person, attributes could include name, age, height, and so on. 
- In Python, attributes can be represented as **variables or fields within a class or as properties associated with an object**.

**Values**: Values are the actual data assigned to attributes. They represent specific instances or data points for a given attribute. 
- For example, the attribute "name" of a person entity can have a value like "John," while the attribute "age" can have a value like 25. 
- Values can be of various types, such as numbers, strings, booleans, or more complex types like lists or dictionaries.

**Data Types**: Data types define the nature and behavior of values in a programming language. 
- In Python, data types specify the kind of data that a variable or attribute can hold. 
- Some commonly used data types in Python include:
```Numeric: int, float, string, boolean, 
Text Type: string (sequence of characters),
Boolean Types: bools (logical operations like True or False),
Sequence Types: List (ordered collection in square brackets), Tuple ( ordered collection in parenthesis), Range (sequence of numbers used in loops)
Mapping Type: Dictionary (collection of key-value pairs enclosed in curly braces)
Set Types: set (unordered collection of unique elements, enclosed in curly braces), frozenset (immutable sets)
Binary Types: bytes (sequence of bytes), bytearray (mutable sequence of bytes)
Other Types: NoneType (null value), complex (numbers with real and imaginary parts)
```

## 15 examples of an entity along with their attribute, value and data type
1. Car:
- Attributes: Model (string), year_of_make (int), Price (float)
- Vales: Hyndai i10, 2017, 700000.50

2. Weather:
- Attributes: date (string or datetime), temperature (float), humidity (float), is_rainy (boolean)
- Values: date = "30-03-2022", temperature = 28.5, humidity = 0.75, is_rainy = False

3. Restaurant:
- Attributes: name (string), cuisine_type (string), rating (float), is_open (boolean)
- Values: name = "Barbeque Nation", cuisine_type = "Italian", rating = 4.5, is_open = True

4. Computer:
- Attributes: brand (string), processor_speed (float), memory_capacity (integer), is_laptop (boolean)
- Values: brand = "HP Pavilion", processor_speed = 2.4, memory_capacity = 8, is_laptop = True

5. Event:
- Attributes: name (string), date (string or datetime), location (string), is_free (boolean)
- Values: name = "Music Concert", date = "2023-07-15", location = "Phoenix Mall", is_free = False

6. Product:
- Attributes: name (string), price (float), quantity (integer), is_available (boolean)
- Values: name = "iPhone 12", price = 70,000, quantity = 10, is_available = True

7. Student:
- Attributes: name (string), age (integer), grade (integer), is_enrolled (boolean)
- Values: name = "Samuel David Singh", age = 15, grade = 9, is_enrolled = True

8. Country:
- Attributes: name (string), population (integer), capital (string), is_developed (boolean)
- Values: name = "United States", population = 331000000, capital = "Washington, D.C.", is_developed = True

9. Employee:
- Attributes: name (string), age (integer), position (string), salary (float)
- Values: name = "Samuel", age = 30, position = "Manager", salary = 50000.0

10. Movie:
- Attributes: title (string), director (string), release_year (integer), rating (float)
- Values: title = "The Shawshank Redemption", director = "Frank Darabont", release_year = 1994, rating = 9.3

11. Animal:
- Attributes: name (string), avg_age (int), is_carnivore (boolean)
- Values: name = "Lion", avg_age = 5, is_carnivore = True

12. Customer:
- Attributes: name (string), age (integer), email (string), is_premium (boolean)
- Values: name = "Samuel", age = 35, email = "samuel@example.com", is_premium = True

13. Product:
- Attributes: name (string), price (float), quantity_available (integer), is_discounted (boolean)
- Values: name = "Smartphone", price = 20000.50, quantity_available = 50, is_discounted = False

14. Song:
- Attributes: title (string), artist (string), duration_seconds (integer), is_favorite (boolean)
- Example values: title = "Bohemian Rhapsody", artist = "Queen", duration_seconds = 355, is_favorite = True

15. Bank:
- Attributes: name (string), location (string), total_assets (float), is_international (boolean)
- Values: name = "HDFC", location = "Bangalore", total_assets = 5000000.0, is_international = True







## 1. Iterator protocol in python

The iterator protocol defines a standard way to produce a sequence of values (either finite or infinite), and potentially a return value when all values have 
been generated.
An object is an iterator when it implements a `next()` method with the following semantics: 
      
So while working with for loop on sequence, first iter method will be called on iterable object like string list etc., and iterator object will be created.

On iterator object, everytime next method will be called to get next element from sequence.

The iterator protocol in Python allows objects to be iterated or looped over. It defines the methods that need to be implemented in an object to make it iterable. Iterables are objects that can return an iterator, and iterators are objects that keep track of the current position during iteration.

The iterator protocol consists of two main methods: `__iter__()` and `__next__()`. Let's go through each of them:

1. **`__iter__()` Method:**
   This method is responsible for returning the iterator object itself. It's called when an iterable is used in a loop.

2. **`__next__()` Method:**
   This method is used to get the next item from the iterator. It should raise the `StopIteration` exception when there are no more items to be returned.

Here's an example of how to create a custom iterable and iterator using the iterator protocol:

```python
class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

class MyIterable:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        return MyIterator(self.limit)

# Using the custom iterable and iterator
my_iterable = MyIterable(5)
for value in my_iterable:
    print(value)
```

In this example, `MyIterable` is an iterable class that defines `__iter__()` to return an instance of `MyIterator`. The `MyIterator` class implements both `__iter__()` and `__next__()` methods to create a custom iterator. When the `for` loop is used on `my_iterable`, it creates an instance of `MyIterator` and iterates over its values.

The iterator protocol allows you to create custom iterable and iterator classes for more complex iterations, allowing you to control the behavior of your custom objects in loops and other iteration scenarios.

## 2. Generator protocol in python

Python provides a generator to create your own iterator function. A generator is a special type of function which does not return a single value, instead, 
it returns an iterator object with a sequence of values. In a generator function, a `yield` statement is used rather than a `return` statement. 
Values will be produced lazily in each iteration in generator using `yield` keyword.

The generator protocol in Python provides a convenient and memory-efficient way to create iterators. Generators allow you to iterate over a sequence of values without storing them all in memory at once. This is particularly useful for large datasets or when generating values on-the-fly.

Generators are implemented using functions with the `yield` keyword. When a generator function is called, it returns a generator iterator that can be used to iterate over the sequence of values produced by the `yield` statements in the function.

The generator protocol involves two key aspects:

1. **Generator Function:**
   A generator function is defined using the `def` keyword, just like a regular function. However, instead of using `return` to produce a value, you use the `yield` keyword. The function's state is saved between successive calls, allowing it to resume execution from where it left off.

2. **Generator Iterator:**
   When a generator function is called, it returns a generator iterator. This iterator implements the iterator protocol with `__iter__()` and `__next__()` methods. The `__next__()` method executes the generator function until it encounters a `yield` statement, at which point it returns the yielded value. The execution state of the generator function is then saved, and the function can be resumed from that point when the `__next__()` method is called again.

Here's an example of a generator function that generates Fibonacci numbers:

```python
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Using the generator to generate Fibonacci numbers
fibonacci = fibonacci_generator()
for _ in range(10):
    print(next(fibonacci))
```

In this example, the `fibonacci_generator()` function is a generator that yields Fibonacci numbers indefinitely. The generator iterator `fibonacci` is used in a loop to generate and print the first 10 Fibonacci numbers.

Generators provide an elegant and efficient way to work with sequences of values, especially when dealing with large or infinite datasets. They allow you to produce values one at a time and avoid loading all values into memory simultaneously.

for speed of execution:  we can use iterator which uses `iter` and `next` method calls interally
for memory management :  efficiency we can use generator 

## 3. iterator vs generator

Iterators and generators are related concepts in Python that provide ways to iterate over a sequence of values. However, they have some differences in terms of implementation and usage.

**Iterators:**
An iterator is an object that implements the iterator protocol, which includes the methods `__iter__()` and `__next__()`. Iterators are used to iterate over a sequence of values one at a time. They maintain the state of iteration internally and provide the next value whenever `__next__()` is called. Iterators are generally implemented using classes.

Here's an example of an iterator:

```python
class MyIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max_value:
            self.current += 1
            return self.current - 1
        else:
            raise StopIteration

# Using the iterator
my_iter = MyIterator(5)
for num in my_iter:
    print(num)
```

**Generators:**
Generators are a type of iterator that are implemented using functions with the `yield` keyword. They provide a more concise and memory-efficient way to create iterators. A generator function returns a generator iterator, and when the `yield` statement is encountered, the function's state is saved, allowing it to resume execution from that point.

Here's an example of a generator:

```python
def my_generator(max_value):
    current = 0
    while current < max_value:
        yield current
        current += 1

# Using the generator
gen = my_generator(5)
for num in gen:
    print(num)
```

**Differences:**

1. **Implementation:** Iterators are generally implemented using classes and require defining `__iter__()` and `__next__()` methods. Generators are implemented using functions with the `yield` keyword.

2. **Memory Efficiency:** Generators are more memory-efficient as they generate values on-the-fly and don't store all values in memory. Iterators can be memory-intensive if they store all values in memory at once.

3. **Conciseness:** Generators are often more concise since they don't require defining a separate class and methods.

4. **State:** In generators, the state is saved automatically when the `yield` statement is encountered. In iterators, you need to manage the state explicitly.

In summary, both iterators and generators provide ways to iterate over values, but generators offer a more convenient and memory-efficient approach, especially for large or infinite sequences of values.


## 4. What are decorators

Decorators in Python are a powerful and flexible way to modify or extend the behavior of functions or methods without changing their actual code. They allow you to wrap a function or method with additional functionality, such as logging, authorization, caching, or validation, by applying the decorator to the function definition.

Decorators are themselves functions that take another function as input and return a new function that often adds some behavior to the original function. They are often used to achieve aspects of metaprogramming and code reusability.

Here's a basic example of a decorator:

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

In this example:
- The `my_decorator` function is a decorator that takes a function `func` as an argument.
- Inside the decorator, a new function `wrapper` is defined, which adds some behavior before and after calling the original function.
- The `@my_decorator` syntax is used to apply the decorator to the `say_hello` function.
- When `say_hello()` is called, it is actually the `wrapper` function that gets executed, wrapping the original behavior of `say_hello`.

Decorators can also take arguments and be nested, allowing for more complex use cases. They are widely used in web frameworks like Flask and Django to add functionality to views and routes, among other things.

Here's another example of a decorator with arguments:

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(n=3)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
```

In this example:
- The `repeat` decorator takes an argument `n` that specifies the number of times the decorated function should be repeated.
- The `decorator` function inside `repeat` is returned and wraps the original function, allowing it to be called multiple times.
- The `@repeat(n=3)` syntax applies the decorator to the `say_hello` function and specifies that it should be repeated 3 times when called.

Decorators provide a clean and elegant way to enhance and customize the behavior of functions without modifying their core logic.

## 5. What are the different decorators. Explain in detail.

There are several built-in decorators in Python, each serving a specific purpose. Let's explore some of the common ones in detail:

1. **@staticmethod**: This decorator is used to define static methods within a class. Static methods don't have access to instance-specific data and are primarily used for utility functions that are related to the class but don't require access to instance attributes.

Example:

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

result = MathUtils.add(5, 3)
print(result)  # Output: 8
```

2. **@classmethod**: This decorator is used to define class methods within a class. Class methods take the class itself as their first parameter and are often used to create alternative constructors or to perform actions related to the class.

Example:

```python
class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create_person(cls, name):
        return cls(name)

person = Person.create_person("Alice")
print(person.name)  # Output: Alice
```

3. **@property**: This decorator is used to define a method as a property, allowing you to access it like an attribute. It's often used to implement getter methods and provide controlled access to class attributes.

Example:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            print("Radius must be positive.")

circle = Circle(5)
print(circle.radius)  # Output: 5
circle.radius = 3
print(circle.radius)  # Output: 3
```

4. **@abstractmethod**: This decorator is used to define abstract methods within an abstract base class. Abstract methods are declared in the base class but don't have an implementation. Subclasses of the base class are required to provide implementations for these methods.

Example:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area())  # Output: 78.5
```

5. **@classmethod vs @staticmethod**: Both decorators are used to define methods that don't operate on instance-specific data. However, `@classmethod` takes the class itself as its first parameter, allowing access to class-specific data and methods, whereas `@staticmethod` doesn't take any special parameter.

These are just a few examples of built-in decorators in Python. Decorators allow you to modify or enhance the behavior of functions or methods in a clean and organized way. You can also create your own custom decorators to suit specific needs in your code.

## 6. How decorators work internally?

Decorators in Python work by taking a function (or a method) as an argument, modifying or enhancing its behavior, and returning the modified function. They are applied using the `@decorator_name` syntax. Internally, decorators are essentially higher-order functions that take a function as input and return a new function.

Here's a simplified step-by-step explanation of how decorators work internally:

1. **Definition of Decorator Function**: A decorator is a regular Python function that accepts another function (or method) as an argument.

2. **Modification**: Inside the decorator function, you can modify or enhance the behavior of the input function. This can include adding extra functionality, altering its output, or executing some code before or after the input function is called.

3. **Returning a Function**: The decorator function returns a new function, often referred to as the "wrapped" function. This new function can include the modifications made by the decorator.

4. **Decorating a Function**: When you apply a decorator using the `@decorator_name` syntax above a function definition, you are essentially replacing the original function with the wrapped function returned by the decorator.

5. **Function Call**: When you call the decorated function, you are actually calling the wrapped function that was returned by the decorator. This means that the modifications or enhancements made by the decorator are applied.

Here's a simple example to illustrate how this works:

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # Call the original function
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()
```

In this example, the `my_decorator` function takes the `say_hello` function as an argument and returns a new function `wrapper`. When you decorate `say_hello` using `@my_decorator`, you replace the original `say_hello` function with the `wrapper` function. So, when you call `say_hello()`, you are actually calling the `wrapper` function, which adds some behavior before and after the original `say_hello` function is called.

This mechanism allows decorators to modify or enhance the behavior of functions in a flexible and reusable way without modifying their actual code.

## 7. Why do we need to use decorators

A decorator in Python is a function that takes another function as its argument, and returns yet another function. Decorators can be extremely useful as they allow the extension of an existing function,
without any modification to the original function source code. Before and after calling mtehod we can use decorator to provide additonal functionality for our method
at runtime or we can decide to call method or not at runtime using decorator.

Decorators are a powerful and flexible tool in Python that provide a way to modify or enhance the behavior of functions or methods without altering their original code. They offer several benefits and use cases:

1. **Code Reusability**: Decorators allow you to encapsulate common functionality or behavior and apply it to multiple functions. This promotes code reusability and reduces code duplication.

2. **Separation of Concerns**: Decorators help in keeping your codebase organized by separating different concerns. You can place specific functionality, such as logging, authentication, or caching, in decorators, ensuring that the main function focuses solely on its core purpose.

3. **Modularity and Maintainability**: By applying decorators to functions, you can enhance or modify their behavior in isolation without changing the underlying code. This promotes a modular and maintainable codebase.

4. **Aspect-Oriented Programming (AOP)**: Decorators enable you to implement AOP, a programming paradigm that focuses on separating cross-cutting concerns, such as logging and error handling, from the main logic.

5. **Readable Code**: Decorators allow you to keep the main logic of functions clean and focused, making the code easier to read, understand, and maintain.

6. **Dynamic Enhancements**: Decorators provide a dynamic way to add features or enhancements to functions. You can apply decorators conditionally or dynamically based on the requirements.

7. **Code Organization**: When dealing with a large codebase, decorators can help in organizing and centralizing common functionalities that need to be applied across multiple functions.

8. **Framework Development**: Decorators are widely used in building frameworks and libraries. They allow developers to extend and customize the behavior of framework functions without modifying the framework's core code.

Common use cases for decorators include:
- **Logging**: Adding logging statements before and after function calls to track their execution.
- **Caching**: Storing and reusing the results of expensive function calls to improve performance.
- **Authentication and Authorization**: Checking user authentication and permissions before allowing access to certain functions.
- **Validation**: Checking input parameters or return values for correctness.
- **Timing**: Measuring the time taken by a function to execute.
- **Error Handling**: Wrapping functions with try-except blocks to handle exceptions.
- **Memoization**: Caching function results to speed up computations.
- **Authorization**: Checking whether a user has the necessary permissions to execute a function.

Overall, decorators provide a clean and elegant way to modify or extend the behavior of functions in a flexible and reusable manner, making them an essential tool in Python programming.
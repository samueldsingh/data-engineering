
# Object Oriented Programming

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects, each representing a real-world entity or concept. It focuses on structuring code around objects that have data (attributes) and behavior (methods), and these objects interact with each other to perform tasks. OOP provides several key concepts to achieve this organization, including encapsulation, inheritance, polymorphism, and abstraction. Let's dive into each of these concepts in detail:

1. **Class:**
A class is a blueprint or template for creating objects. It defines the common attributes and behaviors that the objects of that class will have. A class is like a blueprint, and objects are instances of that blueprint.

Example:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof! Woof!")
```

In this example, we've defined a class `Dog` with attributes `name` and `age` and a method `bark()`.

2. **Object:**
An object is an instance of a class. It represents a specific occurrence of the entity defined by the class. Each object has its own set of attributes and can invoke methods defined in its class.

Example:

```python
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)
```

Here, `dog1` and `dog2` are two objects of the class `Dog`.

3. **Attributes:**
Attributes are variables that hold data within an object. They represent the characteristics or properties of the object.

Example:

```python
print(dog1.name)  # Output: "Buddy"
print(dog2.age)   # Output: 5
```

4. **Methods:**
Methods are functions defined within a class that define the behavior of the objects. They can access and modify the object's attributes.

Example:

```python
dog1.bark()  # Output: "Woof! Woof!"
```

5. **Encapsulation:**
Encapsulation is the principle of bundling data (attributes) and the methods that operate on that data within a single unit (i.e., the class). It hides the internal implementation details of the class from the outside, and access to the data is controlled through methods.

Example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        if new_age >= 0:
            self.age = new_age
```

In this example, we have encapsulated the `age` attribute and provided getter (`get_age()`) and setter (`set_age()`) methods to access and modify it.

6. **Inheritance:**
Inheritance is a mechanism where one class (child or subclass) can inherit attributes and behaviors from another class (parent or superclass). It promotes code reuse and allows creating specialized classes based on existing ones.

Example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print(f"{self.name} is studying.")

class CollegeStudent(Student):
    def __init__(self, name, age, college):
        super().__init__(name, age)
        self.college = college

    def study(self):
        print(f"{self.name} is studying in {self.college}.")
```

Here, `CollegeStudent` inherits from `Student`, and it overrides the `study()` method to provide a more specific implementation.

7. **Polymorphism:**
Polymorphism allows objects of different classes to be treated as objects of a common superclass. It allows a single interface to represent different types of objects. This can be achieved through method overriding or method overloading.

Example (method overriding):

```python
def perform_study(student):
    student.study()

student1 = Student("Alice", 20)
student2 = CollegeStudent("Bob", 22, "XYZ College")

perform_study(student1)  # Output: "Alice is studying."
perform_study(student2)  # Output: "Bob is studying in XYZ College."
```

Here, both `Student` and `CollegeStudent` have a `study()` method, and polymorphism allows us to call `perform_study()` with objects of different types.

8. **Abstraction:**
Abstraction is the process of simplifying complex reality by modeling classes that represent the essential features of an object. It focuses on what an object does rather than how it does it. Abstract classes and interfaces are used to achieve abstraction in some programming languages.

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
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

circle = Circle(5)
square = Square(4)

print(circle.area())  # Output: 78.5
print(square.area())  # Output: 16
```

Here, the `Shape` class is an abstract class representing a shape's essential characteristic – its area. It is not meant to be instantiated, but its subclasses, `Circle` and `Square`, implement the `area()` method to provide specific functionality.

Object-Oriented Programming helps in building more organized, modular, and extensible code. It is widely used in various programming languages like Python, Java, C++, and more to develop complex software systems with ease.


## Steps involved in creating a class

## Example 1
```
# Step1: Defining Class

class Employee:
  def __init__(self, emp_id, name, age):
    self.emp_id = emp_id
    self.name = name
    self.age = age
  
  def get_einfo(self):
    print("Employee Information : ", self.emp_id, self.name, self.age)
    
    
# Step 2 - Create object

sam = Employee(6, "samuel", 26)

# Step3: Method Call
sam.get_einfo()
# Employee.get_einfo(sam)
```

The output is:
```
Employee Information :  6 samuel 26
```

## Example 2

```

# Step1: Create Class
class Student:
  
    # State
    def __init__(self, sid, name, marks):
        self.sid = sid
        self.name = name
        self.marks = marks
        
    # Behavior
    def get_sinfo(self):
        print("Student Information: ", self.sid, self.name, self.marks)

    def update_marks(self, val):
        self.marks = val

    def del_marks(self):
        self.marks = None

# Step2: Create Object
samuel = Student(100, "samuel ", 65)

# Step3: Method Call
samuel.get_sinfo()

# update marks
samuel.update_marks(90)
samuel.get_sinfo()
samuel.del_marks()
samuel.get_sinfo()
```

The output is:
```
Student Information:  100 samuel  65
Student Information:  100 samuel  90
Student Information:  100 samuel  None
```

## Example 3

```

# Student class

class Student:
    # State
    def __init__(self, sid, name, marks):
        self.sid = sid
        self.name = name
        self.marks = marks
    # Behavior
    def get_sinfo(self):
        print("Student info : ", self.sid, self.name, self.marks)

    def get_result(self):
        if self.marks >= 35:
            print("Result : PASS : ", self.name)
        else:
            print("Result :FAIL  : ", self.name)

    def update_name(self):
        self.name = "Vigneshwaran Kanagaraj"



vignesh = Student(100, 'Vignesh K', 56)
print("Beore update : ", vignesh.get_sinfo())
vignesh.update_name()
print("After update : ", vignesh.get_sinfo())
```

The output is:
```
Student info :  100 Vignesh K 56
Beore update :  None
Student info :  100 Vigneshwaran Kanagaraj 56
After update :  None
```

## What are instance variables and class variables?

In object-oriented programming, instance variables and class variables are two types of variables used in classes to store data and maintain state. They have different scopes and behave differently during the lifetime of objects and classes.

1. Instance Variable:
Instance variables are variables that belong to each instance (object) of a class separately. Each object of the class has its own copy of instance variables, and the values of these variables can be unique for each object. They are defined within the `__init__` method of the class and are prefixed with the `self` keyword, which refers to the instance itself.

Example:

```python
class Car:
    def __init__(self, make, model):
        self.make = make   # instance variable
        self.model = model # instance variable

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Accord")

print(car1.make)  # Output: "Toyota"
print(car2.make)  # Output: "Honda"
```

In this example, `make` and `model` are instance variables of the `Car` class. Each instance of the class (e.g., `car1` and `car2`) has its own set of these variables.

2. Class Variable:
Class variables are variables that belong to the class itself, not to individual instances. They are shared among all instances of the class, meaning that any modification to the class variable will affect all instances of that class. Class variables are typically defined directly within the class, outside of any method, and they are not prefixed with the `self` keyword.

Example:

```python
class Car:
    wheels = 4  # class variable

    def __init__(self, make, model):
        self.make = make   # instance variable
        self.model = model # instance variable

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Accord")

print(car1.wheels)  # Output: 4
print(car2.wheels)  # Output: 4

Car.wheels = 6  # Changing the class variable for all instances

print(car1.wheels)  # Output: 6
print(car2.wheels)  # Output: 6
```

In this example, `wheels` is a class variable of the `Car` class. Both `car1` and `car2` share the same `wheels` value, and if we modify the `wheels` class variable, it will be reflected in all instances.

It's important to understand the distinction between instance variables and class variables, as they serve different purposes in the design of classes and objects. Instance variables represent unique properties of individual objects, while class variables represent properties shared among all instances of the class.

## What are instance methods and class methods

In Python, class methods and instance methods are two types of methods used within classes to perform operations on class-level and instance-level data, respectively. They are defined using decorators (`@classmethod` and `@staticmethod` for class methods) and can access different types of variables within the class.

1. Instance Methods:
Instance methods are the most common type of methods used in classes. They are bound to the instance of the class and can access and modify instance variables. Instance methods take the `self` parameter as the first argument, which represents the instance of the class itself. When calling an instance method on an object, Python automatically passes the instance as the first argument.

Example:

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def instance_method(self):
        print("Instance method called with value:", self.value)

obj = MyClass(42)
obj.instance_method()  # Output: "Instance method called with value: 42"
```

In this example, `instance_method` is an instance method of the `MyClass` class. It takes the `self` parameter, allowing it to access and use the instance variables (e.g., `self.value`).

2. Class Methods:
Class methods are methods that are bound to the class itself rather than to the instances. They use the `@classmethod` decorator and take the class as the first argument, often named `cls`. Class methods can be used to perform operations that are related to the class as a whole and not dependent on specific instance data.

Example:

```python
class MyClass:
    class_variable = 10

    def __init__(self, value):
        self.value = value

    @classmethod
    def class_method(cls):
        print("Class method called with class variable:", cls.class_variable)

obj = MyClass(42)
obj.class_method()  # Output: "Class method called with class variable: 10"
```

In this example, `class_method` is a class method of the `MyClass` class. It uses the `@classmethod` decorator and can access the class-level variable `class_variable` directly through `cls.class_variable`.

3. Static Methods:
While not specifically mentioned in your question, it's worth noting that there is another type of method called static methods. These methods do not require access to instance-specific or class-specific data. They are defined using the `@staticmethod` decorator and do not take the `self` or `cls` parameters. Static methods are mainly used when a method does not need access to instance data or class data and operates independently.

Example:

```python
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method")

MyClass.static_method()  # Output: "This is a static method"
```

In this example, `static_method` is a static method of the `MyClass` class. It does not require any instance-specific or class-specific data and can be called directly on the class.

To summarize, instance methods are used to operate on instance-specific data and require the `self` parameter, while class methods operate on class-level data and require the `cls` parameter. Static methods do not require access to instance or class data and are defined using the `@staticmethod` decorator.

## What are decorators in python?
In Python, decorators are a powerful and flexible way to modify or extend the behavior of functions or methods. They allow you to wrap a function inside another function, typically to add some additional functionality before or after the original function's execution.

Decorators are denoted by the `@decorator_name` syntax placed above the function definition. When a decorated function is called, the decorator is invoked first, and then the original function is executed with any modifications made by the decorator.

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

# Calling the decorated function
say_hello()
```

Output:
```
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```

In this example, `my_decorator` is a custom decorator function that takes another function `func` as an argument. The `wrapper` function is defined inside the decorator, which performs some actions before and after calling the original `func`.

When we decorate the `say_hello` function with `@my_decorator`, calling `say_hello()` is equivalent to calling `my_decorator(say_hello)()`. The `say_hello` function is replaced with the `wrapper` function returned by the decorator. Thus, when `say_hello()` is called, the behavior is modified by the `my_decorator`.

Decorators are widely used in Python to add functionalities like logging, timing, authentication, and more to functions without modifying their original code. You can stack multiple decorators on top of each other, and they will be applied in the order they are defined.

Python also provides some built-in decorators like `@staticmethod`, `@classmethod`, and `@property` for specific use cases, and you can create your own custom decorators to suit your needs.


## Explain default constructor and parameterized constructor

In object-oriented programming, constructors are special methods used to initialize objects when they are created from a class. In Python, there are two types of constructors: the default constructor and the parameterized constructor.

1. Default Constructor:
A default constructor is a constructor that is automatically created by Python if no constructor is explicitly defined in a class. It does not take any parameters and is used to create objects with default attribute values. The default constructor can be called using the class name, followed by parentheses, to create an instance of the class.

Example:

```python
class MyClass:
    def __init__(self):
        print("Default constructor called.")

obj = MyClass()  # Output: "Default constructor called."
```

In this example, `MyClass` has a default constructor, `__init__`, which is called when an object is created using `MyClass()`. Since no explicit constructor is defined, Python creates a default constructor with no parameters.

2. Parameterized Constructor:
A parameterized constructor is a constructor that takes one or more parameters and is explicitly defined in the class. It allows you to initialize the object with custom attribute values based on the arguments passed during object creation. This type of constructor is useful when you want to customize the object's state during instantiation.

Example:

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        print("Value:", self.value)

obj1 = MyClass(42)
obj2 = MyClass(99)

obj1.display_value()  # Output: "Value: 42"
obj2.display_value()  # Output: "Value: 99"
```

In this example, `MyClass` has a parameterized constructor, `__init__`, that takes a `value` parameter. When objects `obj1` and `obj2` are created, the constructor is called with the specified arguments, setting the `value` attribute of each object accordingly.

It's worth noting that in Python, you can also have both default and parameterized constructors in a class. When both constructors are defined, the parameterized constructor takes precedence, and the default constructor will not be automatically created. To create an object using the default constructor in such cases, you need to explicitly define the default constructor.

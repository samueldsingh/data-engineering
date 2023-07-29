
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
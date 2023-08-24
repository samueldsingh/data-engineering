
# Object Oriented Programming

## Interview Questions:

## 1. What is OOPs

- Object-Oriented Programming is a programming paradigm that uses objects, which are instances of classes, to structure and organize code.
- OOP is based on the concept of "objects" and "classes," and it focuses on the design and manipulation of objects to solve complex problems in a more modular and organized way.

Key concepts in OOP include:

1. **Classes:** Classes are blueprints or templates for creating objects. They define the attributes (data) and methods (functions) that the objects will have.

2. **Objects:** Objects are instances of classes. They represent real-world entities and encapsulate both data and behavior.

Let's see the key feautres of Object-Oriented Programming (OOP) with examples:

**1. Classes and Objects:**

- A class is a blueprint for creating objects. It defines the structure and behavior that the objects of the class will have.
- An object is an instance of a class.

Example: Let's consider a simple class called "Person" that represents a person with a name and age.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating objects (instances) of the Person class
person1 = Person("Sam", 26)
person2 = Person("Ben", 25)

# Accessing object attributes
print(person1.name)  # Output: Sam
print(person2.age)   # Output: 25
```

**2. Encapsulation:**

- Encapsulation is the practice of **bundling the data (attributes) and methods (functions) that operate on the data into a single unit (the class)**. 
- It provides control over access to the data and promotes data integrity.
- A class exhibits encapsulation by binding all the instance variables and methods into a single unit.
- Object exhibit encapsulation when fields are initialized inside objects and methods are accessed logically.

Example: In the "Person" class, we can encapsulate the `name` and `age` attributes by making them private and providing methods to access and update them.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name
    
    def set_age(self, age):
        if age > 0:
            self.age = age
            
    def get_age(self):
        return self.age

# Creating an object of the Person class
person = Person("Sam", 26)

# Accessing and updating attributes using methods
print(person.get_name())  # Output: Sam
person.set_age(22)
print(person.get_age())   # Output: 22
```

Encapsulation hides the internal details and state of an object from the outside, providing a controlled and consistent way to interact with the object's behavior.

**3. Inheritance:**

- Inheritance allows a new class (the derived or child class) to inherit properties and methods from an existing class (the base or parent class).
- The main advantage of inheritance is code reuseability.

Example: Let's create a "Student" class that inherits from the "Person" class.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name

# Define the Student class, inheriting from the Person class
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

# Create an object of the Student class
student = Student("Sam", 26, "123")

# Access attributes from the parent class
print(student.get_name())  # Output: Sam
print(student.student_id)  # Output: 123
```

Inheritance allows a new class (derived or subclass) to inherit properties and behavior from an existing class (base or superclass), promoting code reuse, extensibility and hierarchical organization.


**4. Polymorphism:**

- Polymorphism allows objects of different classes to be treated as objects of a common base class.
- It enables flexibility and allows a single interface to represent different types of objects.
- Polymorphism means having many forms. It means the same function name (but different signatures) being used for different types.
- Static polymorphism is achieved using method overloading and dynamic polymorphism is achieved using method overriding.

Use Case 1: **Method Overriding:** Inheritance and polymorphism enable you to override methods in derived classes, providing specific implementations while maintaining a common interface defined in the base class.

Use Case 2: **Interface Adherence:** Polymorphism allows multiple classes to adhere to a common interface (e.g., by implementing the same methods from an interface), making it easier to swap out different implementations as needed.

Example: We'll demonstrate polymorphism using a common method called "introduce" that works for both the "Person" and "Student" classes.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name

# Define the Student class, inheriting from the Person class
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

# Define the introduce function
def introduce(entity):
    print("Hello, my name is", entity.get_name())

# Create objects of the classes
person = Person("Sam", 26)
student = Student("Ben", 20, "123")

# Use the introduce function with different objects
introduce(person)   # Output: Hello, my name is Sam
introduce(student)  # Output: Hello, my name is Ben
```

In this example, the `introduce` function accepts objects of both the "Person" and "Student" classes, demonstrating polymorphism.

**5. Abstraction**

Abstraction is a fundamental concept in object-oriented programming (OOP) that allows you to focus on the essential features of an object while hiding the unnecessary implementation details. It simplifies the complexity of real-world entities by creating a model that only includes the relevant attributes and behaviors, making the code more manageable and understandable.

An abstract class is a class that cannot be instantiated and is meant to serve as a blueprint for other classes. It defines a set of abstract methods (methods without implementation) that must be implemented by its concrete subclasses. Abstract classes are used to enforce a specific structure or behavior in the subclasses, ensuring that certain methods are available in all derived classes.

Let's illustrate abstraction with an example:

```python
from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

# Concrete subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

# Concrete subclass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# Usage
circle = Circle(3)
rectangle = Rectangle(5, 10)

# Calling the abstract method on concrete objects
print("Area of circle:", circle.calculate_area())  # Output: Area of circle: 28.26
print("Area of rectangle:", rectangle.calculate_area())  # Output: Area of rectangle: 50
```

In this example, we define an abstract base class `Shape` with an abstract method `calculate_area()`. This method must be implemented in any concrete subclass derived from `Shape`. The concrete subclasses `Circle` and `Rectangle` inherit from `Shape` and provide their own implementations of the `calculate_area()` method.

Using abstraction, we create a common interface (the `calculate_area()` method) that all shapes should have, regardless of their specific implementation details. This allows us to treat instances of different shape classes uniformly while ensuring that each shape provides its own implementation of the `calculate_area()` method. The use of abstraction helps in maintaining a consistent structure and behavior across different subclasses, making the code more manageable and extensible.

OOP helps in structuring code, improving code reusability, making code more manageable, and modeling real-world relationships effectively. It's widely used in various programming languages such as Python, Java, C++, and many more. OOP is especially useful for designing and building large, complex systems, as it promotes modular development and reduces code duplication.

## 2. Why OOPs required

Object-Oriented Programming (OOP) is required for several reasons, mainly to improve code organization, reusability, and maintainability, especially in large and complex software systems. Here are some key reasons why OOP is essential:

1. **Modularity:** OOP promotes modular design by organizing code into reusable and manageable units (classes and objects). This modularity makes it easier to understand and maintain the code.

2. **Code Reusability:** OOP allows you to create classes that can be reused in different parts of the codebase. This reduces redundancy and promotes the reuse of existing components, leading to more efficient development.

3. **Encapsulation:** OOP encapsulates data and behavior within objects, making it easier to manage and control access to data. This helps in preventing unintended interference and improving data integrity.

4. **Abstraction:** OOP allows you to create abstract data types, which hide complex implementation details and only expose essential functionality. Abstraction helps in focusing on what an object does rather than how it does it.

5. **Inheritance:** Inheritance allows you to create new classes based on existing classes, inheriting their attributes and methods. This promotes code reuse and helps in modeling relationships between classes.

6. **Polymorphism:** Polymorphism allows objects of different classes to be treated as objects of a common base class. This promotes flexibility and allows a single interface to represent different types of objects.

7. **Readability and Maintainability:** OOP results in more readable and organized code, making it easier to understand and maintain over time. Changes in one part of the code are less likely to affect other parts, reducing the risk of introducing bugs.

8. **Scalability:** OOP supports building scalable systems by providing a structured way to manage and extend the codebase. As the system grows, OOP principles help maintain a high level of organization.

9. **Real-world Modeling:** OOP allows you to model real-world entities and relationships effectively. This makes the code more intuitive and easier to relate to real-world concepts.

10. **Collaboration:** OOP promotes a clear separation of concerns and can facilitate collaboration among developers. Different team members can work on different classes, making it easier to manage large codebases.

Overall, OOP is a powerful programming paradigm that provides a structured and efficient way to design and build software systems, making them more maintainable, reusable, and scalable.

## 3. Features of OOPs

Object-Oriented Programming (OOP) is a programming paradigm that emphasizes the use of objects and classes to structure code. Here are some key features of OOP:

1. **Classes and Objects:** OOP allows you to create classes, which are blueprints for creating objects. Objects are instances of classes, and they encapsulate both data (attributes) and behavior (methods).

2. **Encapsulation:** Encapsulation is the bundling of data and methods that operate on the data within a single unit (the class). It restricts access to the internal details of an object and provides control over data manipulation.

3. **Inheritance:** Inheritance allows a new class (the derived or child class) to inherit properties and methods from an existing class (the base or parent class). It promotes code reuse and the creation of hierarchies.

4. **Polymorphism:** Polymorphism allows objects of different classes to be treated as objects of a common base class. It enables the use of a single interface to represent various types of objects.

5. **Abstraction:** Abstraction involves creating abstract data types that represent essential features while hiding complex implementation details. It focuses on what an object does rather than how it does it.

6. **Modularity:** OOP promotes modular design by breaking down complex systems into smaller, manageable units (classes). This makes the code easier to understand, maintain, and reuse.

7. **Data Hiding:** OOP provides mechanisms for data hiding, which allows you to hide the implementation details of an object and expose only the necessary interfaces.

8. **Message Passing:** Objects communicate by sending messages to each other. Methods in one object can invoke methods in another object to perform specific tasks.

9. **Dynamic Binding:** Dynamic binding allows the selection of the appropriate method to execute at runtime based on the actual type of object being used. This enables flexibility and late binding.

10. **Overloading and Overriding:** OOP supports method overloading (defining multiple methods with the same name but different parameters) and method overriding (redefining a method in a derived class).

11. **Real-World Modeling:** OOP allows you to model real-world entities, relationships, and interactions, making the code more intuitive and easier to relate to real-world concepts.

These features collectively provide a powerful framework for designing and building software systems that are organized, maintainable, and scalable.

## 4. class vs object

In Object-Oriented Programming (OOP), "class" and "object" are fundamental concepts that play different roles in structuring code. Let's explore the differences between them:

**Class:**

1. **Blueprint:** A class is a blueprint or template for creating objects. It defines the structure and behavior that the objects of that class will have. It specifies the attributes (data) and methods (functions) that the objects can have.

2. **Definition:** A class is a user-defined data type in OOP. It defines a new type with its own characteristics.

3. **Abstraction:** A class represents a generalized concept, abstracting common features that a group of objects of that class will share.

4. **Static:** A class is a static concept in the sense that it doesn't hold actual data. It defines a template that can be used to create objects.

5. **Example:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print("Hello, my name is", self.name)
```

**Object:**

1. **Instance:** An object is an instance of a class. It is a concrete realization of the class blueprint, with actual data stored in its attributes.

2. **Creation:** Objects are created based on the definition of a class. You can create multiple objects from a single class, each with its own unique data.

3. **State:** An object has a state defined by its attributes. Attributes store the data associated with the object.

4. **Dynamic:** Objects are dynamic entities, and they can interact with each other by invoking methods defined in their class.

5. **Example:**
```python
# Creating objects from the Person class
person1 = Person("Sam", 26)
person2 = Person("Ben", 25)

# Accessing object attributes and methods
print(person1.name)         # Output: Sam
person2.introduce()         # Output: Hello, my name is Ben
```

In summary, a "class" defines the blueprint for creating objects, while an "object" is a specific instance of that class with its own data (attributes) and behavior (methods). Classes allow you to define the structure and behavior, while objects allow you to work with actual instances based on that definition.

## 5. class vs instance vs local variables. Explain in detail about usecase of each variable

**Class Variables:**

- A class variable (also called static variables) is a variable that belongs to the class as a whole, rather than to instances (objects) of the class. It is shared among all instances of the class.
- Class variables are defined within the class but outside any instance methods.
- As they are not bound to any instance of a class, they can be shared among all objects of a class.
- Modifying a class variables affects all the objects instance at the same time.
- Class variable can be used when working with shareable data, where we define class method, `cls` as the first parameter and we can access class parameters.

Use Case of Class Variables:
- **Shared Data:** Class variables are useful when you want to share data among all instances of a class. For example, you can use a class variable to keep track of the number of instances created for that class.
- **Constant Values:** Class variables can be used to store constant values that are the same for all instances of the class, like default configuration values.

Example:
```python
class Circle:
    # Class variable
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius * self.radius

# Usage
circle1 = Circle(5)
circle2 = Circle(7)
print(circle1.area())  # Output: 78.53975
print(circle2.area())  # Output: 153.93878
```

**Instance Variables:**

- An instance variable is a variable that belongs to a specific instance (object) of a class. Instance variables seperate copy is created in every instance (or object).
- Instance variables are referenced as `instancename.var`. Each instance can have its own set of instance variables. 
- Instance variables are usually defined within the constructor (`__init__` method) of the class.
- They are tied to the particular object instance of the class, hence the contents of an instance variable are completely independent from one object instance to the other.
- If we have to implement behavior uniquely on each object then we can use instance method with `self` as first parameter and after creating object we can call instance method so that object will be passed as argument to self paramter.
- If we want separate copy for each object, we can use instance variables.

Use Case of Instance Variables:
- **Object-specific Data:** Instance variables are used to store data that is specific to each instance. For example, if you're modeling different circles with different radii, each circle object should have its own radius as an instance variable.
- **State:** Instance variables represent the state of an object, storing attributes that define its current state.

Example:
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

# Usage
circle1 = Circle(5)
circle2 = Circle(7)
print(circle1.area())  # Output: 78.53975
print(circle2.area())  # Output: 153.93878
```

**Local Variables:**

A local variable is a variable defined within a specific scope, typically within a function or a method. It is accessible only within that specific scope and does not exist outside of it.

Use Case of Local Variables:
- **Temporary Data:** Local variables are often used to store temporary data or intermediate results within a function or method.
- **Encapsulation:** Local variables help encapsulate data and logic within a specific function, keeping the data hidden from other parts of the code.

Example:
```python
def calculate_area(radius):
    # Local variable
    pi = 3.14159
    return pi * radius * radius

# Usage
result = calculate_area(5)
print(result)  # Output: 78.53975
```

In summary, class variables are shared among all instances of a class, instance variables are specific to each instance, and local variables are used within a specific scope (typically a function) for temporary data or encapsulation. Each type of variable serves a distinct purpose in managing data within your program.

## 6. class vs instance vs static method. Explain in detail about usecase of each Method

**Class Methods:**

- A class method is a method that is bound to the class and not the instance (object) of the class. A class method cannot access data from any specific instance or object. It can access any class variable or static method.
- The class method defines the behavior of the class.
- It takes the class as its first argument (usually named `cls`) instead of the instance as parameter to know about the state of that class.
- Class methods can be called on the class itself, and they can access class-level variables.

Use Case of Class Methods:
1. **Factory Methods:** Class methods are often used to create alternate constructors for the class. These methods can create instances with specific properties without the need to directly call the constructor.
2. **Accessing Class-level Data:** Class methods can access and modify class-level variables, which can be useful for maintaining shared data across all instances.
3. **Utility Functions:** Class methods can be used to create utility functions that are related to the class but do not depend on instance-specific data.

Example:
```python
class Circle:
    pi = 3.14159  # Class variable

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius * self.radius

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)

# Usage
circle1 = Circle(5)
circle2 = Circle.from_diameter(10)
print(circle1.area())  # Output: 78.53975
print(circle2.area())  # Output: 78.53975
```

**Instance Methods:**

- An instance method defines the behavior of the object. It operates on an instance variable (object) of a class.
- It takes the instance as its first argument (usually named `self`). Instance methods can access instance variables and instance-specific data.
- Instance methods require an object of its class to be created before it can be called.
- To invoke an instance method, create an object of the class in which the method is defined.

Use Case of Instance Methods:
1. **Modifying Object State:** Instance methods are used to modify the state (attributes) of an object, providing behavior that operates on the instance's specific data.
2. **Object-specific Operations:** Instance methods often represent behaviors or actions that are related to the specific instance and involve the instance's data.
3. **Encapsulation:** Instance methods encapsulate the behavior and operations that are related to a specific object, keeping the logic associated with the instance in one place.

Example:
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

# Usage
circle = Circle(5)
print(circle.area())  # Output: 78.53975
```

**Static Methods:**

- The static method does not take any specific parameter.
- Static Method cannot access or modify the class state.
- Static methods do not know about class state. These methods are used to do some utility tasks by taking some parameters.
- To define a static method we use @staticmethod decorator.

A static method is a method that belongs to a class but does not have access to instance-specific data or the class itself as its first argument. It's a method that does not modify the state of the instance or class and does not depend on instance-specific data.

Use Case of Static Methods:
1. **Utility Functions:** Static methods are used for utility functions that are related to the class but do not require access to instance-specific or class-level data.
2. **Organization:** Static methods can be used to group functions that are logically related to the class, even though they do not require access to instance data.

Example:
```python
class MathUtils:
    @staticmethod
    def square(n):
        return n * n

# Usage
result = MathUtils.square(5)
print(result)  # Output: 25
```

In summary, class methods are useful for factory methods, accessing class-level data, and creating utility functions. Instance methods are used for modifying object state, performing object-specific operations, and encapsulating behavior. Static methods are appropriate for utility functions that are logically related to the class but do not depend on instance-specific data or the class itself. Each type of method serves a distinct purpose in managing behavior within a class.

## 7. Importance of init method

The `__init__` method in Python is a special method (also known as a constructor) that is automatically called when an object of a class is created. It plays a crucial role in initializing the attributes (data members) of the object. Here are the key reasons why the `__init__` method is important:

1. **Attribute Initialization:** The primary purpose of the `__init__` method is to initialize the attributes of the object. It allows you to set the initial values for the object's attributes, ensuring that each object starts with the desired state.

2. **Object-specific Data:** The `__init__` method allows you to specify values for the instance variables based on the arguments provided when creating the object. This enables you to create objects with specific characteristics and data.

3. **Encapsulation:** By defining attribute initialization within the `__init__` method, you encapsulate the process of setting the initial state of the object. This promotes clean and consistent object creation.

4. **Consistency:** The `__init__` method ensures that all objects created from the class start with the same set of attributes and default values, providing a consistent structure for all instances.

5. **Constructor Logic:** The `__init__` method can contain additional logic or checks that need to be performed when an object is created. This allows you to enforce constraints, validate input, or perform any necessary setup.

6. **Inheritance:** When a subclass is created, its `__init__` method can use the `super()` function to call the `__init__` method of the parent class. This allows the subclass to inherit and extend the initialization behavior of the parent class.

Example:
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14159 * radius * radius

# Creating a Circle object
circle1 = Circle(5)
print(circle1.radius)  # Output: 5
print(circle1.area)    # Output: 78.53975

# Creating another Circle object
circle2 = Circle(7)
print(circle2.radius)  # Output: 7
print(circle2.area)    # Output: 153.93878
```

In this example, the `__init__` method initializes the `radius` attribute, and based on the `radius`, it calculates and initializes the `area` attribute for each `Circle` object. This ensures that each `Circle` object has its own radius and area, encapsulating this logic within the class.

## 8. Importance of self

- `self` is a default variable that stores the memory address of the instance of the current class. `self` becomes the first method for the instance and constructor method.
- `self` is used to represent the instance of the class itself.
- With `self`, we can access the attribute and the method of the class in python.
- While calling instance method using object, first object will be passed as argument to the self parameter.

The `self` parameter is a crucial aspect of object-oriented programming (OOP) in Python. It is a convention used to refer to the instance of the class within its own methods. Understanding the importance of the `self` parameter is essential for properly working with instance variables and methods in Python classes. Here are the key reasons why the `self` parameter is important:

1. **Instance Reference:** `self` allows you to reference the instance of the class, which is essential for accessing and modifying instance-specific attributes (instance variables) and invoking instance methods.

2. **Data Isolation:** `self` ensures that the data within an object remains isolated and does not mix with the data of other instances. Each object has its own set of attributes, and `self` ensures that these attributes are unique to the instance.

3. **Method Invocation:** When you call an instance method within the class, you use `self` to refer to the current instance. This enables the method to operate on the data specific to that instance.

4. **Creating and Initializing Objects:** The `self` parameter is used in the `__init__` method (constructor) to initialize instance variables with the values passed during object creation. It allows you to set up the initial state of the object.

5. **Encapsulation:** By using `self`, you encapsulate the access to instance attributes and methods, making it clear that these attributes and methods belong to the object and are accessed through the instance.

6. **Method Chaining:** When methods of an object return `self`, it allows method chaining. This is a common pattern in Python libraries that allows you to call multiple methods on an object in a single line.

Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I'm {self.age} years old."

# Creating a Person object
person = Person("Sam", 26)

# Accessing instance attributes using self
print(person.introduce())  # Output: My name is Sam and I'm 26 years old.
```

In this example, the `self` parameter is used to access the `name` and `age` instance attributes within the `introduce` method. This allows the method to provide a personalized introduction based on the instance-specific data. The `self` parameter is essential for maintaining the connection between the object and its attributes/methods, enabling proper encapsulation and isolation of data.

## 9. object life cycle

The object life cycle in Python refers to the various stages an object goes through during its existence in a Python program, from creation to destruction. Understanding the object life cycle is essential for managing resources, memory, and ensuring proper behavior of your Python programs. Here are the key stages in the object life cycle:

1. **Creation (Instantiation):** The first stage is the creation of an object, also known as instantiation. This is typically done using a class constructor (the `__init__` method). At this stage, the object is created in memory, and its instance attributes are initialized.

2. **Usage:** Once an object is created, it can be used in various ways. You can access its attributes, invoke its methods, and perform operations using the object.

3. **Reference Counting:** Python uses a reference counting mechanism to keep track of the number of references to an object. When the reference count drops to zero (meaning there are no more references to the object), the object becomes eligible for garbage collection.

4. **Garbage Collection:** Python has an automatic garbage collector that periodically identifies and releases memory occupied by objects that are no longer reachable (i.e., objects with a reference count of zero). This process frees up memory and helps manage resources.

5. **Destruction (De-allocation):** When an object is no longer needed (i.e., its reference count reaches zero, or it goes out of scope), Python's garbage collector deallocates the memory occupied by the object. At this stage, the `__del__` method, if defined in the class, is called just before the object is destroyed.

It's important to note that the object life cycle is managed automatically by Python's memory management and garbage collection mechanisms. Developers generally don't need to explicitly manage the object's destruction, as Python takes care of it. However, there are cases where you may want to explicitly release resources or perform cleanup, and for that, you can define a `__del__` method in your class.

Example:
```python
class MyClass:
    def __init__(self, value):
        self.value = value
        print(f"Object created with value: {self.value}")

    def __del__(self):
        print(f"Object with value {self.value} destroyed")

# Creating objects
obj1 = MyClass(1)
obj2 = MyClass(2)

# Using objects
print(obj1.value)
print(obj2.value)

# Objects go out of scope, reference count drops to zero
del obj1
del obj2

# Python's garbage collector deallocates memory and calls __del__ method
```

In this example, the `MyClass` objects are created, used, and eventually go out of scope. Python's garbage collector automatically deallocates the memory occupied by these objects, and the `__del__` method is called just before destruction. The output will show the creation and destruction of the objects.

## 10. Constructor. Explain in detail

- The primary purpose of a constructor is to initialize the attributes (data members) of the object to a valid or desired initial state.
- A constructor is automatically called when an object (instance) of a class is created.
- A constructor is a special kind of method that Python calls when it instantiates an object using the definitions found in your class.
- Python relies on the constructor to perform tasks such as initializing (assigning values to) any instance variables that the object will need when it starts.
- In Python, the constructor is defined using the special method `__init__`.
- This method is automatically invoked when you create an object of the class. The `__init__` method can take parameters, and these parameters are used to provide initial values to the attributes of the object.

Key Points about Constructors:

1. **Automatic Invocation:** The `__init__` method is called automatically when an object of the class is created using the class constructor.

2. **Initialization:** The primary purpose of the constructor is to initialize the object's attributes. It ensures that the object starts with a consistent and valid state.

3. **Parameters:** The `__init__` method can take parameters that are used to provide values for the instance variables (attributes) of the object.

4. **Self Parameter:** The first parameter of the `__init__` method is `self`, which represents the instance being created. You use `self` to refer to instance variables and methods within the constructor.

5. **Attribute Initialization:** Inside the `__init__` method, you can use `self` to assign values to instance variables, setting up the initial state of the object.

Example:

```python
class Person:
    def __init__(self, name, age):
        # Initialize instance variables
        self.name = name
        self.age = age

# Creating objects using the constructor
person1 = Person("Sam", 30)
person2 = Person("Ben", 25)

# Accessing instance variables
print(person1.name)  # Output: Sam
print(person1.age)   # Output: 30
print(person2.name)  # Output: Ben
print(person2.age)   # Output: 25
```

In this example, the `Person` class has a constructor (`__init__` method) that takes `name` and `age` as parameters. When objects are created using the constructor, the `name` and `age` attributes of each object are initialized based on the values provided during object creation. The `self` parameter allows us to set the initial state of each object with specific data.

## 11. Constructor life cycle

The constructor life cycle refers to the sequence of events that occur when an object is created in an object-oriented programming language, such as Python. It involves the process of creating the object, initializing its attributes, and setting up its initial state. Let's break down the constructor life cycle into key stages:

1. **Object Creation:** The constructor is called during the creation of an object. It's the first step in the life cycle. When you create an object using the class constructor, the constructor method (`__init__`) is automatically invoked.

2. **Memory Allocation:** Memory is allocated to store the object's data (attributes). The constructor doesn't handle memory allocation directly; the runtime environment takes care of this.

3. **Attribute Initialization:** Inside the constructor, instance variables (attributes) are initialized to specific values. These values are typically provided as arguments to the constructor when the object is created.

4. **Self Parameter:** The constructor receives a special parameter called `self`, which refers to the newly created object. This allows you to set the initial values of the object's attributes.

5. **Setting Up Initial State:** The constructor ensures that the object starts with a consistent and valid state. It may perform additional setup tasks, such as calling other methods or setting default values.

6. **Object Ready for Use:** Once the constructor completes its execution, the object is fully created and initialized. It's now ready to be used in the program, and its attributes can be accessed and modified.

7. **Object Lifetime:** The object remains in memory until it goes out of scope (no longer accessible), at which point it becomes eligible for garbage collection. The `__del__` method (destructor) can be used to define any cleanup actions when the object is destroyed.

Example:

```python
class Person:
    def __init__(self, name, age):
        # Initialize instance variables
        self.name = name
        self.age = age
        print("Constructor called")

# Creating objects using the constructor
person1 = Person("Sam", 30)
person2 = Person("Ben", 25)

# Accessing instance variables
print(person1.name)  # Output: Sam
print(person2.name)  # Output: Ben
```

In this example, the constructor (`__init__`) initializes the `name` and `age` attributes of each `Person` object with values provided during object creation. The constructor is called automatically when objects are created, and it ensures that the objects start with the specified initial state.

## 12. Default vs Parameterized Constructor

**Default Constructor:**

A default constructor is a constructor that doesn't take any parameters, and it's provided by the language or implicitly defined in a class if you don't define any constructor explicitly. Its primary purpose is to initialize the object's attributes with default values. In Python, if you don't define a constructor (`__init__` method) in a class, the default constructor is used, which initializes the object without requiring any arguments.

Example of a default constructor:

```python
class Person:
    def __init__(self):
        self.name = "Unknown"
        self.age = 0

# Using the default constructor
person = Person()
print(person.name)  # Output: Unknown
print(person.age)   # Output: 0
```

In this example, the `Person` class has a default constructor that initializes the `name` attribute to "Unknown" and the `age` attribute to 0.

**Parameterized Constructor:**

A parameterized constructor is a constructor that accepts parameters and initializes the object's attributes based on the provided values. It allows you to customize the initial state of the object by passing arguments to the constructor. A parameterized constructor is useful when you want to create objects with specific initial values.

- Constructor overloading is achieved using default arguments (parameter in construction have predefined values), positional arguments (arguments are passed
  to construction in the order they are defined) and keyword arguments (pass values to constructor parameters by explicitly mentioning the parameter names followed by the values).

Example of a parameterized constructor:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Using the parameterized constructor
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1.name)  # Output: Sam
print(person1.age)   # Output: 30
print(person2.name)  # Output: Ben
print(person2.age)   # Output: 25
```

In this example, the `Person` class has a parameterized constructor that accepts `name` and `age` as arguments. When objects are created using this constructor, the `name` and `age` attributes of each object are initialized based on the values provided during object creation.

**Key Differences:**

- A default constructor doesn't take any parameters, while a parameterized constructor does.
- A default constructor is provided by the language if you don't define any constructor, while a parameterized constructor must be defined explicitly in the class.
- A default constructor initializes attributes with default values, while a parameterized constructor initializes attributes with values provided during object creation.

In both cases, the goal is to set up the initial state of the object, but a parameterized constructor allows more flexibility in specifying the initial values.

## 13. Constructor Overloading

Constructor overloading happens where a class can have multiple constructors with different parameter lists. Each constructor provides a different way to initialize the object's attributes. When you create an object of the class and pass specific arguments to the constructor, the appropriate constructor is selected based on the arguments' data types and number.

In Python, constructor overloading is not directly supported like it is in some other languages (such as Java or C++), where you can define multiple constructors with different signatures. In Python, there's a single constructor, the `__init__` method, per class. However, you can achieve constructor overloading by using default values for the constructor parameters and handling different cases within the constructor.

Let's illustrate this with an example:

```python
class Person:
    def __init__(self, name=None, age=None):
        if name is not None and age is not None:
            self.name = name
            self.age = age
        elif name is not None:
            self.name = name
            self.age = 0
        else:
            self.name = "Unknown"
            self.age = 0

# Using the constructor with different arguments
person1 = Person("Alice", 30)
person2 = Person("Bob")
person3 = Person()

print(person1.name, person1.age)  # Output: Sam 30
print(person2.name, person2.age)  # Output: Ben 0
print(person3.name, person3.age)  # Output: Unknown 0
```

In this example, the `Person` class has a single constructor (`__init__` method) with two parameters: `name` and `age`. By using default values for these parameters, we create a form of constructor overloading. Depending on the arguments provided during object creation, the constructor initializes the attributes of the object accordingly.

Keep in mind that this approach allows you to provide different ways to initialize objects based on the provided arguments, simulating constructor overloading in Python.

## 14. new vs init

`__new__` and `__init__` are both special methods in Python that play distinct roles in the process of object creation and initialization. They serve different purposes and are part of the object life cycle. Let's delve into the differences between these two methods:

1. **`__new__` Method:**

   - The `__new__` method is responsible for creating a new instance of a class. It is called before the `__init__` method.
   - It receives the class as its first argument (`cls`) and any additional arguments that are passed during object creation.
   - The primary use case for overriding `__new__` is when you want to customize the object creation process or create objects of a different type (metaclass usage).
   - The `__new__` method returns a new instance of the class, and it is not responsible for initializing the object's attributes.

Example of `__new__`:

```python
class CustomString(str):
    def __new__(cls, value):
        # Modify the object creation process
        value = value.upper()
        instance = super(CustomString, cls).__new__(cls, value)
        return instance

# Using the __new__ method
custom_str = CustomString("hello")
print(custom_str)  # Output: "HELLO"
```

2. **`__init__` Method:**

   - The `__init__` method is responsible for initializing the attributes of an object after it has been created by the `__new__` method.
   - It receives the newly created instance as its first argument (`self`) and any additional arguments that were passed during object creation.
   - The primary use case for overriding `__init__` is to set up the initial state of the object by initializing instance variables.

Example of `__init__`:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Using the __init__ method
person = Person("Sam", 30)
print(person.name, person.age)  # Output: "Sam", 30
```

In summary, `__new__` is responsible for creating the object, while `__init__` is responsible for initializing its attributes. You rarely need to override `__new__` unless you have specific requirements related to object creation. On the other hand, `__init__` is a common method used to set up the initial state of objects.

## 15. Explain below concepts in detail with examples
a. Encapsulation
b. Abstraction
c. Inheritance
d. Polymorphism

Sure, I'll explain each of these fundamental concepts in object-oriented programming (OOP) in detail and provide examples for better understanding.

**a. Encapsulation:**

Encapsulation is one of the core principles of object-oriented programming. It refers to the practice of bundling the data (attributes) and methods (functions) that operate on the data into a single unit, known as a class. Encapsulation helps in controlling the access to the data and ensures that the implementation details are hidden from the outside world. The internal state of an object is protected, and interactions with the object are carried out through well-defined interfaces.

**Example of Encapsulation:**

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

# Creating an instance of BankAccount
account = BankAccount("123456", 1000)

# Accessing and modifying the balance through methods
account.deposit(500)
account.withdraw(300)
print(account.balance)  # Output: 1200
```

In this example, the `BankAccount` class encapsulates the account number and balance attributes. The `deposit` and `withdraw` methods provide controlled access to modify the balance. The implementation details of how the balance is modified are hidden from the outside, ensuring proper encapsulation.

**b. Abstraction:**

- Abstraction is the process of simplifying complex reality by modeling classes based on the essential properties and behaviors relevant to the application.
- Abstraction in OOP is a process of hiding the real implementation of the method by only showing a method signature.In Python, we can achieve abstraction using ABC (abstraction class) or abstract method.
- It involves hiding the unnecessary details and showing only the necessary parts of an object.
- Abstraction allows you to focus on what an object does rather than how it does it.
- ABC is a class from the abc module in Python
- In a normal class, we have all concrete method and abstraction is 0%.
- In an abstraction class, abstraction can be between 0-100%. We can have either all concrete methods, or all abstract methods, or a combination of both abstract
  and concrete methods.
- In a interface, we have all abstract methods

**Example of Abstraction:**

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

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Using the abstracted Shape class
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape.area())


The output is:
78.5
24
```

In this example, the `Shape` class represents an abstraction of a geometric shape with an `area` method. The `Circle` and `Rectangle` classes implement the `Shape` interface by providing their specific implementations of the `area` method. The `Shape` class abstracts the concept of calculating the area, allowing us to work with different shapes without worrying about the details of their implementations.

**c. Inheritance:**

Inheritance is a mechanism in which a new class (subclass or derived class) inherits properties and behaviors (attributes and methods) from an existing class (superclass or base class). Inheritance promotes code reuse and allows the creation of more specialized classes based on existing ones.

**Example of Inheritance:**

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating instances of derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Using the inherited methods
print(dog.name, dog.speak())  # Output: Buddy Woof!
print(cat.name, cat.speak())  # Output: Whiskers Meow!
```

In this example, the `Animal` class serves as the base class with a common `name` attribute and an abstract `speak` method. The `Dog` and `Cat` classes inherit from the `Animal` class and provide their specific implementations of the `speak` method. Inheritance allows the derived classes to reuse the attributes and methods of the base class while adding or overriding functionality.

**d. Polymorphism:**

Polymorphism allows objects of different classes to be treated as objects of a common base class. It enables you to use the same interface (methods or attributes) to represent different data types. Polymorphism simplifies code, enhances flexibility, and supports dynamic behavior.

**Example of Polymorphism:**

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Using polymorphism with a common interface
def animal_sound(animal):
    return animal.speak()

# Creating instances of derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Using the common interface
print(animal_sound(dog))  # Output: Woof!
print(animal_sound(cat))  # Output: Meow!
```

In this example, the `animal_sound` function accepts an `Animal` object as a parameter, and the `speak` method of the appropriate derived class is called based on the object type. The common interface (`speak` method) allows us to use polymorphism to handle different types of animals without knowing their specific implementations at compile time.

These four concepts—encapsulation, abstraction, inheritance, and polymorphism—are fundamental pillars of object-oriented programming, helping developers build modular, organized, and extensible software systems.

## 16. Method overloading (Static Polymorphism) vs Method overriding (Dynamic Polymorphism)

- Methods in python can be called with zero, one or more parameters.
- The process of calling the same method in different ways by passing different number of arguments is called method overloading.
- Two methods will have the same name, but the latest method will hide previous method.
- In Python, Method Overloading can't be achived directly but if a method with parameters has default arguments then that method can be called in 2 or more ways.
- Because the latest method will hide the previous method, we can't achieve method overloading directly and hence we should use default arguments inside method signature.
- Method overloading is achieved indirectly with default values for parameter or with *args or **kwargs.
- With *args, we pass a tuple of arguments and with **kwargs, we pass value in key value pair mechanism. 

**Method Overloading:**

Method overloading occurs when a class defines multiple methods with the same name but different parameter lists. The methods must have different numbers or types of parameters. The overloaded methods provide different ways to perform similar operations based on the input arguments. In some programming languages (e.g., Java), method overloading is supported explicitly by the language, allowing you to define multiple methods with the same name within the same class.

**Example of Method Overloading (Python does not support method overloading directly):**

```python
class Calculator:

    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z

# Creating an instance of the Calculator class
calc = Calculator()

# Calling the overloaded add methods
print(calc.add(2, 3))         # Output: Error (Python does not support overloading)
print(calc.add(2, 3, 4))      # Output: 9
```

In this example, we define two methods named `add` in the `Calculator` class, each with a different number of parameters. However, in Python, only the second `add` method will be recognized because Python does not directly support method overloading. The earlier definition of `add` is overwritten.

**Method Overriding:**

    Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass (base class). The overridden method in the subclass has the same name, parameters, and return type as the method in the superclass. The goal of method overriding is to customize the behavior of the inherited method in the subclass.

**Example of Method Overriding:**

```python
class Animal:
    def make_sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Creating instances of derived classes
dog = Dog()
cat = Cat()

# Calling the overridden method
print(dog.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow!
```

In this example, the `Animal` class defines a generic `make_sound` method. The `Dog` and `Cat` classes inherit from `Animal` and provide their specific implementations of the `make_sound` method, overriding the behavior defined in the base class. This allows each subclass to customize the sound it makes.

In summary, method overloading is about defining multiple methods with the same name but different parameter lists, which is not directly supported in Python. Method overriding, on the other hand, is about providing a specialized implementation of a method in a subclass, allowing customization of behavior inherited from the superclass.

## 17. Inheritance types

- Inheritance is a fundamental concept in object-oriented programming that allows a new class to inherit properties (attributes and methods) from an existing class.
- This concept promotes code reuse and allows the creation of more specialized classes based on existing ones.
- There are several types of inheritance that define the relationship between the base (parent) class and the derived (child) class. Let's explore the common types of inheritance:

1. **Single Inheritance:**
   
   In single inheritance, a derived class inherits from only one base class. This is the simplest form of inheritance and is commonly used to create a hierarchical relationship between classes.
   
   ```python
   class Parent:
       def parent_method(self):
           print("Parent method")

   class Child(Parent):
       def child_method(self):
           print("Child method")

   # Creating an instance of the Child class
   child = Child()
   child.parent_method()  # Output: Parent method
   child.child_method()   # Output: Child method
   ```

2. **Multiple Inheritance:**

- In multiple inheritance, a derived class inherits from more than one base class. This allows the derived class to inherit properties from multiple parent classes.
- The derived class inherits all the features of the base case.
- Care should be taken when using multiple inheritance to avoid the "diamond problem" where ambiguity may arise if multiple parent classes have methods with the same name.

   ```python
   class Parent1:
       def parent1_method(self):
           print("Parent1 method")

   class Parent2:
       def parent2_method(self):
           print("Parent2 method")

   class Child(Parent1, Parent2):
       def child_method(self):
           print("Child method")

   # Creating an instance of the Child class
   child = Child()
   child.parent1_method()  # Output: Parent1 method
   child.parent2_method()  # Output: Parent2 method
   child.child_method()    # Output: Child method
   ```

3. **Multilevel Inheritance:**

- The multi-level inheritance includes the involvement of at least two or more than two classes. One class inherits the features from a parent class and the newly created sub-class becomes the base class for another new class.
   
   ```python
   class Grandparent:
       def grandparent_method(self):
           print("Grandparent method")

   class Parent(Grandparent):
       def parent_method(self):
           print("Parent method")

   class Child(Parent):
       def child_method(self):
           print("Child method")

   # Creating an instance of the Child class
   child = Child()
   child.grandparent_method()  # Output: Grandparent method
   child.parent_method()       # Output: Parent method
   child.child_method()        # Output: Child method
   ```

4. **Hierarchical Inheritance:**

- In hierarchical inheritance, multiple derived classes inherit from a single base (parent) class.
- Each derived class can have its own additional properties and methods while sharing the properties of the base class.

   ```python
   class Animal:
       def make_sound(self):
           print("Generic animal sound")

   class Dog(Animal):
       def make_sound(self):
           print("Woof!")

   class Cat(Animal):
       def make_sound(self):
           print("Meow!")

   # Creating instances of derived classes
   dog = Dog()
   cat = Cat()
   dog.make_sound()  # Output: Woof!
   cat.make_sound()  # Output: Meow!
   ```

5. **Hybrid Inheritance**:
   Hybrid inheritance is a combination of different types of inheritance (usually multiple and multilevel inheritance) within a single program. It's a more complex form of inheritance where classes are derived from multiple base classes and may create a complex inheritance hierarchy.

Here's an example of hybrid inheritance in Python:

```python
# Base class
class Person:
    def __init__(self, name):
        self.name = name

# Derived classes
class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

# Derived class with multiple base classes
class Manager(Employee, Student):
    def __init__(self, name, emp_id, student_id, department):
        # Call the constructors of both Employee and Student classes
        Employee.__init__(self, name, emp_id)
        Student.__init__(self, name, student_id)
        self.department = department

# Create an object of the Manager class
manager = Manager("John Doe", "E123", "S456", "IT")

# Access attributes from both base classes
print("Name:", manager.name)
print("Employee ID:", manager.emp_id)
print("Student ID:", manager.student_id)
print("Department:", manager.department)
```

In this example, we have three classes: `Person` as the base class, `Employee` and `Student` as derived classes from `Person`, and `Manager` as a class derived from both `Employee` and `Student`. This demonstrates hybrid inheritance, where `Manager` inherits attributes and methods from both `Employee` and `Student`.

Note that hybrid inheritance can lead to complex relationships, and careful design is essential to avoid confusion and maintain the integrity of the program's structure.

These are the main types of inheritance in object-oriented programming. Each type has its own use cases and considerations, and understanding the relationship between base and derived classes is crucial for designing effective class hierarchies.

## 18. Explain settr, gettr, hasattr and delattr

The four different Python functions or concepts: `setattr`, `getattr`, `attr`, and `delattr` are used to manipulate attributes of objects.

1. **`setattr`**:
The `setattr` function is used to set the value of an attribute of an object. It takes three arguments: the object, the attribute name as a string, and the value to be assigned to that attribute. Here's the syntax:

```python
setattr(object, attribute_name, value)
```

Example:
```python
class Person:
    pass

person = Person()
setattr(person, 'name', 'John')
print(person.name)  # Output: John
```

2. **`getattr`**:
The `getattr` function is used to retrieve the value of an attribute of an object. It takes two arguments: the object and the attribute name as a string. Optionally, you can provide a default value as a second argument, which will be returned if the attribute doesn't exist on the object. Here's the syntax:

```python
getattr(object, attribute_name, default_value)
```

Example:
```python
class Person:
    name = 'John'

person = Person()
print(getattr(person, 'name'))  # Output: John
print(getattr(person, 'age', 30))  # Output: 30 (default value since 'age' doesn't exist)
```

3. **`delattr`**:
The `delattr` function is used to delete an attribute from an object. It takes two arguments: the object and the attribute name as a string. Here's the syntax:

```python
delattr(object, attribute_name)
```

Example:
```python
class Person:
    name = 'John'

person = Person()
print(person.name)  # Output: John
delattr(person, 'name')
# After deleting the attribute 'name', trying to access it will raise an AttributeError
```

Please note that `setattr`, `getattr`, and `delattr` work with regular attributes of an object. If you're working with properties, methods, or other more complex attributes, their behavior might differ. Also, Python encourages the use of dot notation for attribute access and assignment whenever possible, as it's more readable and conventional. These functions are usually used in scenarios where attribute names are determined dynamically or when dealing with more complex attribute manipulation.

## 19. MRO principle.Explain in detail

MRO (Method Resolution Order) is a principle in object-oriented programming that defines the order in which classes are searched when invoking a method on an object. The MRO principle is crucial for languages that support multiple inheritance, where a class can inherit attributes and methods from more than one parent class. Python is one such language that uses the C3 Linearization algorithm to determine the MRO.

The MRO principle ensures that the correct method is called when a method is invoked on an object, considering the inheritance hierarchy and the order of method definitions in the classes involved. The goal is to provide a consistent and predictable way to resolve method calls in cases of multiple inheritance.

**MRO Algorithm in Python (C3 Linearization):**

Python uses the C3 Linearization algorithm, also known as C3 superclass linearization, to determine the MRO. This algorithm ensures a consistent and deterministic MRO for classes with multiple inheritance. The C3 Linearization algorithm follows these rules:

1. The base classes are ordered according to their definition in the subclass's inheritance declaration.
2. The base classes are visited in a left-to-right order, and their base classes (excluding duplicates) are recursively traversed.
3. If a base class has multiple parent classes, the algorithm considers a merge of the MROs of those parent classes.

**Example of MRO in Python:**

```python
class A:
    def method(self):
        print("Method in class A")

class B(A):
    def method(self):
        print("Method in class B")

class C(A):
    def method(self):
        print("Method in class C")

class D(B, C):
    pass

# Creating an instance of class D
d = D()

# Calling the method
d.method()
```

In this example, we have a class hierarchy with multiple inheritance: `D` inherits from both `B` and `C`, which in turn inherit from `A`. When we create an instance of `D` and call the `method`, the MRO determines that the method from class `B` is invoked. The MRO follows the C3 Linearization algorithm, and the output of this code will be:

```
Method in class B
```

This demonstrates how the MRO ensures that the method is resolved in a predictable and consistent manner in the presence of multiple inheritance. Understanding the MRO is essential for designing class hierarchies and resolving method calls correctly in Python.

## 20. Access modifiers in Python

- The access modifiers in Python are used to modify the default scope of variables. Access modifiers in Python are keywords used to define the visibility and accessibility of class members (attributes and methods) in object-oriented programming.
- Access modifiers help control the level of encapsulation and protect the internal state of objects. In Python, access modifiers are not enforced as strictly as in some other languages like Java, but they provide a way to indicate the intended level of visibility.

Python has three main access modifiers:

1. **Public (No Modifier):**
   A class member with no access modifier is considered public, which means it can be accessed from anywhere, both within and outside the class.

- The members of a class that are declared public are easily accessible from any part of the program.
- All data members and member functions of a class are public by default.

   ```python
   class MyClass:
       def __init__(self):
           self.public_variable = 10

   obj = MyClass()
   print(obj.public_variable)  # Output: 10
   ```

2. **Protected (_ prefix):**
   A class member with a single underscore prefix (e.g., `_variable`) is considered protected. While Python does not enforce strict protection, this naming convention indicates that the variable or method should not be accessed directly from outside the class. It's a common convention among Python programmers.

- The members of a class that are declared protected are only accessible to a class derived from it.
- Data members of a class are declared protected by adding a single underscore `_` symbol before the data member of that class.

   ```python
   class MyClass:
       def __init__(self):
           self._protected_variable = 20

   obj = MyClass()
   print(obj._protected_variable)  # Output: 20 (although it's a protected variable, it's accessible)
   ```

4. **Private (__ double underscore prefix):**
   A class member with a double underscore prefix (e.g., `__variable`) is considered private. This naming convention indicates that the variable or method is intended to be used only within the class and should not be accessed from outside the class.

- The members of a class that are declared private are accessible within the class only.
- Private access modifier is the most secure access modifier.
- Data members of a class are declared private by adding a double underscore `__` symbol before the data member of that class. 

   ```python
   class MyClass:
       def __init__(self):
           self.__private_variable = 30

   obj = MyClass()
   # print(obj.__private_variable)  # Error: AttributeError (private variable is not directly accessible)
   ```

   Note that Python performs name mangling on private attributes, making them harder to access directly from outside the class. However, it's still possible to access them using the `_ClassName__private_variable` syntax, but this is discouraged.

Remember that Python's access modifiers are more of a convention than a strict rule. It's a good practice to use public, protected, and private naming conventions to indicate the intended visibility and prevent accidental misuse. Encapsulation and data hiding are essential principles in object-oriented programming, and access modifiers play a role in achieving these goals.

## 21. Multiple Inheritance. Explain in detail

Multiple inheritance is a feature in object-oriented programming that allows a class to inherit attributes and methods from more than one base class. In other words, a class can have multiple parent classes, and it can inherit the properties of all those parent classes. This concept facilitates code reuse by allowing a single class to combine the features of multiple classes.

In multiple inheritance, a derived (child) class can inherit from two or more base (parent) classes. This allows the derived class to gain access to the attributes and methods defined in each of its parent classes. However, multiple inheritance can introduce some complexities, such as the "diamond problem" and the need for a clear method resolution order (MRO) to resolve method conflicts.

Let's explain multiple inheritance in detail:

**Advantages of Multiple Inheritance:**

1. **Code Reusability:** Multiple inheritance allows a class to reuse the features of multiple classes. This promotes a more modular and efficient design, as common functionalities can be defined in base classes and reused across different classes.

2. **Flexibility:** Multiple inheritance provides flexibility in designing class hierarchies. It allows developers to create complex class relationships and build classes that represent more specific and specialized concepts.

**Example of Multiple Inheritance:**

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Mammal(Animal):
    def speak(self):
        return "Mammal sound"

class Bird(Animal):
    def speak(self):
        return "Bird sound"

class Bat(Mammal, Bird):
    pass

# Creating an instance of the Bat class
bat = Bat("Batty")

# Accessing methods from parent classes
print(bat.name)         # Output: Batty
print(bat.speak())      # Output: Mammal sound (MRO favors the first parent class in the declaration, Mammal)
```

In this example, we have an `Animal` base class with a `name` attribute and a `speak` method. There are two derived classes, `Mammal` and `Bird`, each of which inherits from `Animal` and provides its own implementation of the `speak` method.

The `Bat` class is derived from both `Mammal` and `Bird` using multiple inheritance. Despite the potential for a "diamond problem" (if both `Mammal` and `Bird` inherited from another common class), Python's C3 Linearization algorithm (MRO) resolves the method call, favoring the method from the first parent class declared in the `Bat` class.

**Complexities and Considerations:**

1. **Diamond Problem:** In some cases, multiple inheritance can lead to the "diamond problem" where a class inherits from two classes that have a common base class. This can result in ambiguity when resolving method calls. Python's MRO helps resolve this issue.

2. **Method Resolution Order (MRO):** MRO is essential in multiple inheritance to determine the order in which the parent classes are searched when resolving method calls. Python uses the C3 Linearization algorithm to establish a consistent and predictable MRO.

3. **Avoid Overuse:** While multiple inheritance is a powerful feature, it should be used judiciously to avoid creating overly complex class hierarchies.

4. **Maintainability:** It's important to ensure that the design using multiple inheritance remains understandable and maintainable. Clearly documenting the class hierarchy and understanding the MRO is crucial.

In summary, multiple inheritance allows a class to inherit properties from more than one base class, enhancing code reusability and flexibility. While it brings advantages, it should be used thoughtfully, and developers need to be aware of the complexities it can introduce, such as the diamond problem and the importance of a clear MRO.

## 22. super keyword importance

- The `super()` function is used to give access to methods and properties of a parent or sibling class. 
- The `super()` function returns an object that represents the parent class.
- The `super()` keyword in Python is essential when working with inheritance, especially in cases of method overriding and cooperative multiple inheritance. It allows a subclass to call a method from its parent class.
- The `super()` keyword is crucial for maintaining the correct method resolution order (MRO) and ensuring that method calls are properly delegated to the appropriate parent class.

Here are some important use cases and benefits of the `super()` keyword:

1. **Method Overriding:** When a subclass provides its own implementation of a method that is also defined in the parent class, using `super()` allows the subclass to invoke the parent class's method while extending or modifying its behavior.

   ```python
   class Parent:
       def say_hello(self):
           print("Hello from Parent")

   class Child(Parent):
       def say_hello(self):
           super().say_hello()  # Calling the parent class's method
           print("Hello from Child")

   child = Child()
   child.say_hello()
   ```

   In this example, the `Child` class overrides the `say_hello()` method from the `Parent` class. By using `super()`, the child class can invoke the parent class's method before adding its own behavior.

2. **Cooperative Multiple Inheritance:** When working with multiple inheritance, the `super()` keyword is crucial to ensure that the method resolution order is consistent and follows the C3 Linearization algorithm (MRO). It allows subclasses to cooperate and call parent class methods in a well-defined order.

   ```python
   class A:
       def say_hello(self):
           print("Hello from A")

   class B(A):
       def say_hello(self):
           print("Hello from B")
           super().say_hello()  # Calling the parent class's method

   class C(A):
       def say_hello(self):
           print("Hello from C")
           super().say_hello()  # Calling the parent class's method

   class D(B, C):
       pass

   d = D()
   d.say_hello()
   ```

   In this example, we have classes `A`, `B`, `C`, and `D`. The `D` class inherits from both `B` and `C`. By using `super()`, we ensure that the MRO is respected, and the `say_hello()` method from class `A` is called once despite the multiple inheritance.

3. **Flexibility and Code Maintenance:** The `super()` keyword enhances code flexibility, as it allows changes in parent classes to propagate to subclasses without needing to modify the subclasses' code. This reduces the risk of code duplication and makes the codebase easier to maintain.

   ```python
   class Parent:
       def configure(self):
           # Configuration logic

   class Child(Parent):
       def configure(self):
           super().configure()  # Use the parent's configuration logic
           # Additional configuration logic specific to the Child class
   ```

   In this example, if the configuration logic in the `Parent` class changes, the `Child` class can still benefit from the updated logic by using `super()` to invoke the parent's `configure()` method.

Overall, the `super()` keyword is an essential tool for maintaining a clear and consistent hierarchy in class inheritance, enabling method reuse, and ensuring proper cooperation in multiple inheritance scenarios.

## 23. Calling super class method from sub class

Calling a superclass method from a subclass can be done using the `super()` keyword. The `super()` function allows you to call a method in the parent class from the context of the subclass. This is useful when you want to extend or modify the behavior of the parent class's method in the subclass while still utilizing the functionality of the parent class's method.

Here's an example that demonstrates how to call a superclass method from a subclass:

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        # Call the greet() method of the Parent class
        super().greet()
        print("Hello from Child")

# Create an instance of the Child class
child = Child()

# Call the greet() method of the Child class
child.greet()
```

In this example, we have a `Parent` class with a `greet()` method, and a `Child` class that inherits from the `Parent` class. The `Child` class overrides the `greet()` method to add its own behavior, but it also wants to call the `greet()` method of the parent class.

When we create an instance of the `Child` class and call its `greet()` method, the `super().greet()` line inside the `Child` class's `greet()` method invokes the `greet()` method of the `Parent` class, and then the additional "Hello from Child" message is printed.

The output of this code will be:

```
Hello from Parent
Hello from Child
```

By using `super()`, you ensure that the parent class's method is invoked, allowing you to extend or modify the behavior in the subclass while still benefiting from the functionality provided by the parent class. This promotes code reuse and maintains a clear hierarchy in the class structure.

## 24. Difference between public protected private methods Ex: x() _x() __x()

In Python, methods and attributes have different levels of visibility and accessibility, denoted by naming conventions. The naming conventions for methods and attributes indicate their visibility to other parts of the code. Here's the difference between public, protected, and private methods:

1. **Public Methods:**
   - Public methods have no special naming convention. They are typically named in lowercase with words separated by underscores (snake_case).
   - Public methods are accessible from outside the class, meaning they can be called directly on an instance of the class.

Example:
```python
class MyClass:
    def public_method(self):
        print("This is a public method")

obj = MyClass()
obj.public_method()  # Calling the public method
```

2. **Protected Methods:**
   - Protected methods are denoted by a single leading underscore before the method name. For example, `_protected_method`.
   - Protected methods are a convention in Python, indicating that the method should not be accessed from outside the class, but they are still accessible.
   - The idea behind protected methods is to indicate to other developers that the method is intended for internal use within the class or its subclasses, but it's not enforced by the language.

Example:
```python
class MyClass:
    def _protected_method(self):
        print("This is a protected method")

obj = MyClass()
obj._protected_method()  # Accessing the protected method
```

3. **Private Methods:**
   - Private methods are denoted by a double leading underscore before the method name. For example, `__private_method`.
   - Private methods are meant to be used within the class only. They are name-mangled to make them less accessible from outside the class.
   - Private methods are not inherited by subclasses.

Example:
```python
class MyClass:
    def __private_method(self):
        print("This is a private method")

obj = MyClass()
# Accessing a private method directly will result in an AttributeError
# obj.__private_method()  # Uncommenting this line will raise an AttributeError
```

It's important to note that these naming conventions are by convention only, and Python does not enforce access control like some other languages. Developers can still access "protected" and "private" methods, but it's a best practice to respect the intended visibility as indicated by the naming conventions.

In summary:
- **Public methods** have no special notation and are accessible from outside the class.
- **Protected methods** have a single leading underscore and are intended for internal use but are still accessible.
- **Private methods** have a double leading underscore and are intended for use within the class only, and they have name mangling to make them less accessible from outside.

## 25. Importance of dunder functions

Dunder (double underscore) methods, also known as magic methods or special methods, are a crucial feature in Python. These methods are invoked by specific language constructs and are used to define how objects of a class behave in certain situations. Understanding and implementing dunder methods is important for creating custom classes that work seamlessly with Python's built-in functionalities and for defining the behavior of objects in various contexts. Here's why dunder methods are important:

1. **Operator Overloading:** Dunder methods enable operator overloading, allowing you to define custom behavior for standard operators when applied to objects of your class. For example, you can define the `__add__()` method to specify how instances of your class should behave with the `+` operator.

2. **Custom Representation:** The `__repr__()` and `__str__()` methods allow you to define custom string representations for your objects. This is particularly useful for debugging and improving the readability of your objects when printed.

3. **Context Management:** Dunder methods like `__enter__()` and `__exit__()` are essential for context management using the `with` statement. They allow you to define the setup and cleanup actions for your objects when used in a `with` block.

4. **Iteration:** Dunder methods such as `__iter__()` and `__next__()` enable you to define custom iteration behavior for your objects. This is essential for making instances of your class iterable.

5. **Comparison:** Dunder methods like `__eq__()`, `__lt__()`, and others allow you to define custom comparison behavior for instances of your class. This is crucial for making your objects comparable with the standard comparison operators (`<`, `>`, `==`, etc.).

6. **Attribute Access:** Dunder methods like `__getattr__()`, `__setattr__()`, and `__delattr__()` enable you to define custom behavior for attribute access, assignment, and deletion, respectively.

7. **Dynamic Behavior:** Dunder methods allow you to control the dynamic behavior of your objects. For example, the `__call__()` method lets you define instances of your class as callable, allowing them to be invoked like functions.

8. **Custom Numeric Operations:** Dunder methods such as `__add__()`, `__sub__()`, and others enable you to define custom numeric operations for your objects, allowing them to work seamlessly with numeric operations.

By implementing appropriate dunder methods, you make your custom classes more intuitive, Pythonic, and compatible with existing language constructs and built-in functions. This promotes code readability, reusability, and enhances the overall user experience when working with instances of your classes.

## 26. __str__ vs __repr__

Both `__str__` and `__repr__` are special methods in Python that deal with providing string representations of objects, but they have distinct purposes and use cases. Let's explore the differences between `__str__` and `__repr__`:

1. **`__str__` Method:**
   - The `__str__` method is used to define a human-readable string representation of an object.
   - It's intended to provide a user-friendly, informative string that represents the object in a way that is easy to understand.
   - The primary use of `__str__` is for end-users and for displaying objects in a readable format.
   - This method is called by the built-in `str()` function and the `print()` function when an object is passed to it.
   - If `__str__` is not defined, the default implementation from the base `object` class is used, which provides a basic representation.

Example:
```python
class MyClass:
    def __str__(self):
        return "This is an instance of MyClass"

obj = MyClass()
print(obj)  # Output: This is an instance of MyClass
```

2. **`__repr__` Method:**
   - The `__repr__` method is used to define an unambiguous, developer-focused string representation of an object.
   - It's intended to provide a string that, when passed to the Python interpreter (`eval()` or in the interactive console), would create an equivalent object.
   - The primary use of `__repr__` is for developers, debugging, and inspecting objects.
   - This method is called by the built-in `repr()` function and is used when displaying objects in the interactive console.
   - If `__repr__` is not defined, the default implementation from the base `object` class is used, which provides a basic representation.

Example:
```python
class MyClass:
    def __repr__(self):
        return "MyClass()"

obj = MyClass()
print(repr(obj))  # Output: MyClass()
```

In summary:
- Use `__str__` to define a user-friendly string representation of an object, suitable for end-users and for display.
- Use `__repr__` to define an unambiguous string representation of an object, suitable for developers, debugging, and creating equivalent objects.

It's common to implement both `__str__` and `__repr__` methods in your classes to provide meaningful representations for both end-users and developers. If only one of them is implemented, the other may use the default implementation provided by the base `object` class.

## 27. Abstraction, Abstract class. When to use. Explain in detail

**Abstraction** is a fundamental concept in object-oriented programming that focuses on hiding the complex implementation details while exposing a simplified and high-level interface for users. It allows you to represent real-world objects in a more understandable and manageable way.

Abstraction is achieved through the creation of **abstract classes** and **interfaces**. These abstract constructs define a blueprint for derived classes, providing a set of methods (including abstract methods) that must be implemented in the derived classes. Here's a detailed explanation of abstraction and abstract classes:

1. **Abstraction:**
   - Abstraction helps manage complexity by focusing on what an object does (its behavior) rather than how it does it (its implementation).
   - It provides a way to create generalized, reusable, and easily maintainable code by defining a clear contract between classes.
   - Abstraction allows you to build a high-level model of a system, hiding the low-level implementation details, which simplifies the interaction with the system.
   - It promotes code modularity, making it easier to change or extend the system without affecting other parts of the code.
   - Abstraction is a crucial principle in object-oriented design, enabling you to create more flexible, adaptable, and understandable software.

2. **Abstract Class:**
   - An abstract class is a class that cannot be instantiated on its own; it serves as a base for other classes that derive from it.
   - Abstract classes may contain both regular (non-abstract) methods and abstract methods.
   - Abstract methods are declared in the abstract class but have no implementation. They are meant to be implemented by derived classes.
   - Abstract classes provide a common interface that derived classes must follow, ensuring a consistent structure and behavior across multiple subclasses.
   - Abstract classes define a contract that derived classes must adhere to, promoting code consistency and ensuring that essential methods are implemented.

**When to use abstraction and abstract classes:**
1. **When designing a hierarchy:** Use abstraction when you have a group of related classes that share common behavior but need to vary in some specific aspects. Create an abstract base class with the shared behavior and define abstract methods that must be implemented by the subclasses.

2. **To enforce a contract:** Use abstraction to define a contract that derived classes must follow. This ensures that certain methods are implemented in all subclasses, providing a consistent interface.

3. **To hide implementation details:** Use abstraction to hide the complex implementation details of a class, exposing only the essential methods and properties that users need to interact with.

4. **When you want to create a blueprint:** Use abstraction to create a blueprint for classes, ensuring that they follow a specific structure and behavior.

Example of an abstract class:
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

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Example usage
circle = Circle(5)
print(circle.area())  # Output: 78.5

rectangle = Rectangle(4, 6)
print(rectangle.area())  # Output: 24
```

In this example, the `Shape` class is an abstract class with an abstract method `area()`. The `Circle` and `Rectangle` classes are derived from the `Shape` class and provide implementations for the `area()` method. The abstract class `Shape` defines a contract that both `Circle` and `Rectangle` classes must adhere to, ensuring that they both have an `area()` method. This abstraction simplifies the interaction with different shapes by providing a consistent interface.

## 28. Abstract class vs Interface

Both abstract classes and interfaces are used to achieve abstraction and define a contract that derived classes must follow, but they have some key differences in terms of implementation, usage, and their role in object-oriented design.

**Abstract Class:** 

An abstract contains one or more abstract methods. An abstract method is a method that is declared, but contains no implementation. Abstract classes may be instantiated and its abstract classes must be implemented by its subclass.

1. An abstract class is a class that cannot be instantiated on its own. It serves as a base for other classes (concrete subclasses) that derive from it.
2. Abstract classes can have both regular (non-abstract) methods with implementations and abstract methods (declared without implementation).
3. Abstract methods in an abstract class are meant to be overridden by concrete subclasses, which ensures that derived classes implement essential behavior.
4. Abstract classes may contain member variables (attributes) that can be shared among subclasses.
5. A class can inherit from only one abstract class, meaning that there is a restriction on single inheritance when using abstract classes.
6. Abstract classes are a way to provide a common base and shared behavior for related classes.

**Interface:**

An interface is a collection of method signatures that should be provided by the implementing class. Implementing an interface is a way of writing an organized 
code and achieving abstraction. 

1. An interface is a completely abstract class in Python. It cannot be instantiated, and all its methods are abstract, meaning they have no implementation.
2. Interfaces define a contract that classes must adhere to by implementing all the methods declared in the interface.
3. A class can implement multiple interfaces, which allows for achieving multiple inheritance of interface contracts.
4. Interfaces are used to specify a set of methods that must be present in implementing classes, but they do not provide any implementation details themselves.
5. Interfaces are useful for achieving loose coupling and promoting code modularity. They allow different classes to share common behavior without forcing them to be part of a common hierarchy.

**When to Use Abstract Classes and Interfaces:**
1. **Abstract Class:** Use an abstract class when you want to provide a common base with shared behavior for a group of related classes. If you have methods with default implementations that you want to be available in some derived classes, use an abstract class.
2. **Interface:** Use an interface when you want to define a contract that multiple classes can adhere to. If you want to ensure that classes provide specific methods but you don't want to impose a common base, use an interface.

Example illustrating the use of an interface:
```python
from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Drawable):
    def draw(self):
        print("Drawing a circle")

class Square(Drawable):
    def draw(self):
        print("Drawing a square")

# Example usage
shapes = [Circle(), Square()]
for shape in shapes:
    shape.draw()
```

In this example, the `Drawable` interface defines the contract that classes must implement the `draw()` method. Both the `Circle` and `Square` classes implement the `Drawable` interface by providing their own implementation of the `draw()` method. This allows them to be used interchangeably in a more abstract and unified way.

## 29. Special functions

- `__init__`: The `__init__` function is called every time an object is created from a class. The `__init__` method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes

- `__str__`: The `__str__` method in Python represents the class objects as a string – it can be used for classes. The `__str__` method should be defined in a way that is easy to read and outputs all the members of the class.
           This method is also used as a debugging tool when the members of a class need to be checked.
  
- `__repr__`: In Python, `__repr__` is a special method used to represent a class's objects as a string. `__repr__` is called by the `repr()` built-in function. You can define your own string representation of your class objects using the `__repr__` method. Special methods are a set of predefined methods used to enrich your classes.

- `__iter__`: The Python `iter()` function returns an iterator for the given object. The `iter()` function creates an object which can be iterated one element at a time. These objects are useful when coupled with loops like for loop, while loop.
   
- `__next__`: The `__next__()` method must return the next item in the sequence. On reaching the end, and in subsequent calls, it must raise `StopIteration`.

## 30. What is the purpose of __init__ constructor?

- `__init__` is short for initialization.
- It is a constructor which gets called when you make an instance of the class.
- Although not necessary, it is a usual practice to write `__init` for setting the default state of the object.

The `__init__` method in Python is a special method, also known as a constructor, that is automatically called when an object of a class is created. It is used to initialize the attributes (or properties) of the object. In other words, it sets up the initial state of the object and allows you to provide values for its attributes.

The main purposes of the `__init__` method are:

1. **Initializing Attributes:** You can use the `__init__` method to set the initial values of the attributes of an object. This ensures that each object created from the class starts with the specified attributes.

2. **Passing Parameters:** The `__init__` method can accept parameters that you pass when creating an object. These parameters can be used to provide values for the attributes of the object.

3. **Object Setup:** If there are any setup steps or computations that need to be performed when an object is created, you can include them in the `__init__` method.

4. **Customization:** By providing parameters to the `__init__` method, you can customize the behavior of each object. Different objects can be created with different initial attribute values.

5. **Default Values:** You can define default values for attributes in the `__init__` method. If a value is not provided during object creation, the default value will be used.

6. **Validation and Error Handling:** The `__init__` method can include logic to validate the input values and raise exceptions if they are not valid.

Here's an example of how the `__init__` method is used:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating objects of the Person class
person1 = Person("Sam", 30)
person2 = Person("Ben", 25)

print(person1.name, person1.age)  # Output: Sam 30
print(person2.name, person2.age)  # Output: Ben 25
```

In this example, the `__init__` method initializes the `name` and `age` attributes of each `Person` object with the values provided during object creation.

# Extras

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


## Example of builtin decorators in pyton

Certainly! Here are some examples of built-in Python decorators:

1. `@staticmethod`:
This decorator is used to define static methods within a class. Static methods belong to the class and do not have access to instance-specific data.

```python
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

result = MathOperations.add(5, 10)
print(result)  # Output: 15
```

2. `@classmethod`:
This decorator is used to define class methods. Class methods take the class as their first argument (conventionally named `cls`) instead of the instance (`self`).

```python
class MyClass:
    class_variable = 10

    @classmethod
    def get_class_variable(cls):
        return cls.class_variable

result = MyClass.get_class_variable()
print(result)  # Output: 10
```

3. `@property`:
This decorator is used to create getter methods for class properties. It allows you to access a method like an attribute without using parentheses.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

circle = Circle(5)
print(circle.radius)  # Output: 5
```

4. `@abstractmethod` (from the `abc` module):
This decorator is used to define abstract methods within abstract classes. Abstract methods must be implemented by subclasses.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(4, 5)
print(rectangle.area())  # Output: 20
```

These are just a few examples of built-in Python decorators. They provide useful functionalities and help in structuring code and maintaining proper object-oriented design principles.

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


## Give example of using classes with parameterized functions

Sure, let's use a common class, such as the `Person` class, to demonstrate default arguments, keyword arguments, variable-length arguments, and pass by reference concepts. We'll create a `Person` class with methods that showcase each of these concepts.

```python
class Person:
    @staticmethod
    def greet(self, name, designation, age):
        return f"Hello, {name}, you are a/an {designation} who is {age} years old."

    @staticmethod
    def


positional_arguments = Person.greet("Sam", "Engineer", 26)
print(positional_arguments)

```

In this example, the `Person` class has methods for introducing the person, updating age, updating information using keyword arguments, and displaying information. We demonstrate:

1. Default Arguments: The `introduce` method has a default argument for the greeting, which is used if no greeting is provided.
2. Keyword Arguments: We create a `Person` instance using keyword arguments (`age` and `name`) and provide a greeting using a keyword argument in the `introduce` method.
3. Variable Length Arguments: The `update_info` method accepts keyword arguments (`**kwargs`) to update attributes dynamically.
4. Pass by Reference: We demonstrate pass by reference by assigning `person3` to the same object as `person1`, and any changes made to `person3` affect `person1`.

This example showcases the use of these concepts within a common `Person` class.

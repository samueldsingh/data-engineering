## 1. What is an object?
In programming, an object is a fundamental concept in object-oriented programming (OOP) that represents a real-world entity, concept, or thing. 
Objects are self-contained units that encapsulate data (attributes) and behaviors (methods) related to the entity they represent.

## Key characteristics of objects:
**1. State:** An object's state is determined by its attributes or properties. Attributes of an object represent its current condition or characteristics. 
For example, an object representing a car may have attributes such as color, model, and speed.

**2. Behavior:** Objects exhibit behavior through methods, which are functions or procedures associated with the object. Methods define the actions or operations that an object can perform. 
For example, an object representing a car may have methods such as ```accelerate()```, ```brake()```, and ```turn()```.

**3. Identity:** Each object has a unique identity that distinguishes it from other objects. This identity allows the program to differentiate between multiple objects of the same class. 

**4. Encapsulation:** Objects encapsulate data and behavior, which means that the internal details and implementation are hidden from external entities. 

**5. Interaction:** Objects can interact with each other by invoking methods, exchanging data, or passing messages. 

The concept of objects allows for modular and organized code design, as it promotes the encapsulation of data and behavior into reusable and self-contained units. Objects facilitate code reusability, maintainability, and scalability, making them a powerful tool in software development.


## 2. How are objects stored in Python
A Python object is stored in memory with **names and references**. 
A **name** is just a label for an object, so one object can have many names. 
A reference is a name(pointer) that refers to an object.

A python object has 3 things -  Type, value, and reference count. As python is a dynamic language, the type is automatically detected. Value is 
declared while defining the object. Reference count is the number of names pointing that object. 

## 3. What is a reference count
In Python, a reference count is automatic memory management system that helps determine when an object is no longer in use and can be safely deallocated from memory. It is a count that keeps track of the number of references pointing to an object.

Here's how the reference count works:

**Reference Count Increment:** When a reference to an object is created, either by assigning the object to a variable or passing it as an argument to a function, the reference count of the object is incremented by one. This indicates that there is now one reference to the object.

**Reference Count Decrement:** When a reference to an object is removed, either by reassigning the variable to another object or when a variable goes out of scope, the reference count of the object is decremented by one. This indicates that there is now one less reference to the object.

**Zero Reference Count:** When the reference count of an object reaches zero, it means that there are no more references to that object in the program. At this point, the object is considered no longer in use.

**Deallocation:** Once an object's reference count reaches zero, Python's memory manager deallocates the memory occupied by the object. The memory is then returned to the system and made available for reuse.

The reference count mechanism is a fundamental part of Python's memory management system because it allows the interpreter to determine when an object is no longer needed. By keeping track of the number of references to an object, Python can ensure that memory is deallocated only when it is no longer being used by the program.

However, it's important to note that the reference count mechanism is not the sole memory management technique used in Python. Python also employs a garbage collector to handle situations where objects have cyclic references or when memory deallocation cannot be determined solely based on reference counting. The garbage collector identifies and collects objects that are no longer accessible even if their reference count is not zero.

Overall, the reference count mechanism, combined with the garbage collector, allows Python to efficiently manage memory allocation and deallocation, ensuring that memory is properly used and reclaimed when objects are no longer needed. This automatic memory management helps relieve the programmer from manual memory management tasks and reduces the likelihood of memory leaks and dangling pointers.

## 4. Explain Garbage Collection in detail
Garbage collection releases memory when no object is in use. It is like a recycling system in computers where the system deletes the unused object and 
reuses its memory slot for new objects.

- Python has an automated garbage collection system.
- Python has algorithms to deallocate objects and it has two ways to delete the unused objects from the memory.

1. Reference Counting - Suppose we assign c to 50. Next, when we assign a new variable to the object c, the reference count increases by 1.
For now we print the ID's of each object to see if they are the same or different.

![object](https://github.com/samueldsingh/python-dev-90-days-bootcamp/assets/62851341/12f8cb3e-3933-43e2-b987-ba00e9be0474)

Next we change the value of ```a``` to ```60```, and then to ```None```. The integer 60 has no reference and it is deleted by the garbage collection.

Now we assign a boolean, ```False``` to ```b```. The previous integer object, ```60``` is not deleted because it still has a reference by ```c```.

![reference](https://github.com/samueldsingh/python-dev-90-days-bootcamp/assets/62851341/ba8519dc-d611-4339-b26b-abebabc7762d)

When we delete **c**, we decrease the reference count to **c** by one.

![reference1](https://github.com/samueldsingh/python-dev-90-days-bootcamp/assets/62851341/10d08de5-dcdc-4476-af1f-c8bf7d2a6569)

The ```del()``` statement doesn’t delete objects, it removes the name (and reference) to the object. When the reference count is zero, the object is deleted from the system by the garbage collection.

**Pros:** Reference counting are easy to implement because programmers don’t have to worry about deleting objects when they are no longer used. 

**Cons:** The most important issue in reference counting garbage collection is that it doesn’t work in cyclical references.

Cyclical reference is a situation in which an object refers to itself. The simplest cyclical reference is appending a list to itself.

Reference counting alone can not destroy objects with cyclic references. If the reference count is not zero, the object cannot be deleted. The solution 
to this problem is the second garbage collection method.

2. Generational Garbage Collection:
It is a type of **trace-based garbage collection**. It can break cyclic references and delete the unused objects even if they are referred by themselves.

**How does generational Garbage Collection work?**
Python keeps track of every object in memory. 3 lists are created when a program is run. Generation 0, 1, and 2 lists.

Newly created objects are put in the Generation 0 list. A list is created for objects to discard. Reference cycles are detected. If an object has no outside references it is discarded. The objects who survived after this process are put in the Generation 1 list. The same steps are applied to the Generation 1 list. Survivals from the Generation 1 list are put in the Generation 2 list. The objects in the Generation 2 list stay there until the end of the program execution.

![generation](https://github.com/samueldsingh/python-dev-90-days-bootcamp/assets/62851341/d0b300cb-ea82-4de3-9875-cbfd8d8bbdae)

**Conclusion:**
Python is a high-level language and we don’t have to do the memory management manually. Python garbage collection algorithm is very useful to open up space in the memory. Garbage collection is implemented in Python in two ways: reference counting and generational. When the reference count of an object reaches 0, reference counting garbage collection algorithm cleans up the object immediately. If you have a cycle, reference count doesn’t reach zero, you wait for the generational garbage collection algorithm to run and clean the object. While a programmer doesn’t have to think about garbage collection in Python, it can be useful to understand what is happening under the hood.

## 5. Variables in Python
-	In Python, variables are used to store and manipulate data. Variable is a name which is used to refer **memory location of value**. 
-	Variable also known as identifier and used to hold value.
-	A variable, as the name indicates is something whose value is changeable over time.  X = 10

**Rule:** Variable names can be a group of both letters and digits, but they have to begin with a letter or an underscore. It is recommended to use lowercase letters for variable name. Rahul and rahul both are two different variables.

Based on the data type of a variable, the interpreter allocates memory and decides what can be stored in the reserved memory. Therefore, by assigning different data types to variables, you can store integers, decimals or characters in these variables.

**Variable References:** In Python, variables are references to objects rather than direct storage locations. Multiple variables can reference the same object, and changes made through one variable will be reflected in others.

**Variable Use and Manipulation:** Variables are used to store data, perform calculations, pass values between functions, and store intermediate results in a program. They can be used in expressions, combined with operators, and passed as arguments to functions.

## Using Python in Command Prompt
https://codeberryschool.com/blog/en/python-in-command-prompt/

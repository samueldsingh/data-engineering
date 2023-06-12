## How are objects stored in Python
In C, C++, and Java we have variables and objects. A Python object is stored in memory with **names and references**. 
A name is just a label for an object, so one object can have many names. 
A reference is a name(pointer) that refers to an object.

A python object has 3 things -  Type, value, and reference count. As python is a dynamic language, the type is automatically detected. Value is 
declared while defining the object. Reference count is the number of names pointing that object. 

## Explain Garbage Collection in detail
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

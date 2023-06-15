## 1. What is an object?
In programming, an object is a fundamental concept in object-oriented programming (OOP) that represents a real-world entity, concept, or thing. 
Objects are self-contained units that encapsulate data (attributes) and behaviors (methods) related to the entity they represent.
Every item of data in a Python program can be described by the abstract term **object**, and we can manipulate objects using symbolic names called variables.

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

## 4. Variables in Python
-	In Python, variables are used to store and manipulate data. Variable is a name which is used to refer **memory location of value**. 
-	Variable also known as identifier and used to hold value.
-	A variable, as the name indicates is something whose value is changeable over time.  X = 10

**Rule:** Variable names can be a group of both letters and digits, but they have to begin with a letter or an underscore. It is recommended to use lowercase letters for variable name. Rahul and rahul both are two different variables.

Based on the data type of a variable, the interpreter allocates memory and decides what can be stored in the reserved memory. Therefore, by assigning different data types to variables, you can store integers, decimals or characters in these variables.

**Variable References:** In Python, variables are references to objects rather than direct storage locations. Multiple variables can reference the same object, and changes made through one variable will be reflected in others.

**Variable Use and Manipulation:** Variables are used to store data, perform calculations, pass values between functions, and store intermediate results in a program. They can be used in expressions, combined with operators, and passed as arguments to functions.

Every item of data in a Python program can be described by the abstract term **object**, and objects can be manipulated using symbolic names called **variables**.

## Object References
What is actually happening when you make a variable assignment? 
Python is a highly object-oriented programming language. Every item of data in a Python program is an object of a specific type or class. 

Consider the code below that prints the number 300:
```
print(300)
300
```

When you print the statement, the interpreter does three things: Creates an integer object, Gives it the value 300, Displays it to the console. 

Print the type of the object using the built-in ```type``` function:
```
>>> type(300)
<class 'int'>
```

A Python variable is a symbolic name that is a reference or pointer to an object. Once an object is assigned to a variable, you can refer to the object by that name. But the data itself is still contained within the object.

For example, assign an object integer, ```n=300```, to the variable ```n``` using the assignment operator ```=```. The assignment operator assigns the variable n to point to that object.

```
n = 300
```

Now consider the following statement:
```
>>> m = n
```

What happens when it is executed? Python does not create another object. It simply creates a new symbolic name or reference, m, which points to the same object that n points to.

Next, suppose assign a new variable to the object ```m```:
```
>>> m = 400
```
Python creates a new integer object with the value 400, and m becomes a reference to it.

Lastly, execute the statement:
```
>>> n = "hello"
```
Python creates a string object with the value "foo" and makes n reference that.
 
There is no longer any reference to the integer object 300. It is orphaned, and there is no way to access it. The number of references to an object drops to zero, it is no longer accessible. At that point, its lifetime is over. Python will eventually notice that it is inaccessible and reclaim the allocated memory so it can be used for something else. This process is referred to as garbage collection.

## Object Identity
In Python, every object that is created has a unique identifier. Once an object’s reference count drops to zero and it is garbage collected, as happened to the 300 object above, then its identifying number becomes available and may be used again.

The built-in Python function ```id()``` returns an object’s integer identifier.

After the assignment ```m = n```, ```m``` and ```n``` both point to the same object, confirmed by the fact that ```id(m)``` and ```id(n)``` return the same number. Once ```m``` is reassigned to ```400```, ```m``` and ```n``` point to different objects with different identities.

> ## Deep Dive: Caching Small Integer Values
> From what you now know about variable assignment and object references in Python, the following probably won’t surprise you:
>
```
>>> m = 300
>>> n = 300
>>> id(m)
60062304
>>> id(n)
60062896
```
> With the statement m = 300, Python creates an integer object with the value 300 and sets m as a reference to it. n is then similarly assigned to an integer object with value 300—but not the same object. Thus, they have different identities, which you can verify from the values returned by id().
But consider this:
>
```
>>> m = 30
>>> n = 30
>>> id(m)
1405569120
>>> id(n)
1405569120
```
> Here, m and n are separately assigned to integer objects having value 30. But in this case, id(m) and id(n) are identical!
> For purposes of optimization, the interpreter creates objects for the integers in the range [-5, 256] at startup, and then reuses them during program execution. > Thus, when you assign separate variables to an integer value in this range, they will actually reference the same object.

## Global and local variables
**Local variables** in Python are the ones that are defined and declared inside a function. We can not call this variable outside the function.

```
# This function uses global variable s
def f():
	s = "Welcome geeks"
	print(s)


f()
```

The output is:
```
Welcome geeks
```

**Global variables** in Python are the ones that are defined and declared outside a function, and we need to use them inside a function.

```
# This function has a variable with
# name same as s.
def f():
    print(s)
 
 
# Global scope
s = "I love Geeksforgeeks"
f()
```

The output is:
```
I love Geeksforgeeks
```

## Variable Type Conversion
Sometimes when performing operations or assignments that involve different types of data, you need to perform conversion or type casting to 
change the variable from one type to another.

Type conversion can be done explicitly by using type-casting functions or operators. Here are some common examples:

1. Implicit conversion - if you assign an integer value to a floating-point variable, the language will perform an implicit conversion to make the assignment.
2. Explicit conversion - When you want to explicitly convert a variable to a different type, you can use type-casting functions or operators. 

It's essential to understand the rules and limitations of type conversions in the specific programming language you're working with as some conversions may result
in data loss or unexpected behavior.

### Converting between strings to list
```str_list = "[1, 2, 3, 4, 5]"
num_list = eval(str_list)
print(num_list)  # Output: [1, 2, 3, 4, 5]
```

The ```eval()``` function can be used to evaluate a string as a Python expression. However, we have to be cautious when using eval() with untrusted inputs, as it can execute arbitrary code.

### Converting list of strings to integers
```
str_list = ["1", "2", "3", "4", "5"]
num_list = [int(num_str) for num_str in str_list]
print(num_list)  # Output: [1, 2, 3, 4, 5]
```

### Converting List of Numbers to String:
```
num_list = [1, 2, 3, 4, 5]
str_list = [str(num) for num in num_list]
print(str_list)  # Output: ['1', '2', '3', '4', '5']
```

Remember to handle potential errors when converting between incompatible types, as Python may raise exceptions if the conversion is not possible.

## Summary of memory management in variables
In short the memory management in variables follow the given path:
```
Variable Allocation --> Memory Address --> Garbage Collection --> Reference Counting --> Automatic Memory Management --> Memory Optimization
```

**Variable allocation:** On creating a variable, memory is allocated to store its value. The size of the memory depends on the data type of the variable. Integers require a fixed amount of memory whereas string may require memory size proportional to its size.

**Memory Address:** Each allocated memory block has a unique address, which is used to identify and access the data stored in that block.

**Garbage Collection:** Automatically reclaims memory that is no longer in use. It reduces the likelihood of memory leaks and manual memory management errors.

**Reference Counting:** Keeps track of the number of references pointing to that allocated object.

**Automatic memory management:** In cases where cyclic references exist, a garbage collector runs periodically to identify and deallocate unreachable objects.

**Memory Optimization:** In cases where you may need to optimize memory usage in your program, techniques like object pooling (limited set of objects are reused instead of creating new ones) or using generators instead of lists for large datasets, can help reduce memory consumption.

## Example of memory management:
1. Variable Allocation: Execute the below assignment to store the value ```100```. On execution, memory is allocated to store the value ```1000```.
```
x=100
```

2. Reference Counting: Let's create a list ```[1,2,3]``` and assign the variables ```x``` and ```y``` to reference it. As long as there are references to the object, its reference count remains non-zero, indicating that the memory is still in use. When all references to the object are removed (set to ```None``` or go out of scope), the reference count becomes zero, and the memory occupied by the list object is deallocated.

```
x = [1, 2, 3]  # Reference count of the list object becomes 1
y = x  # Reference count of the list object becomes 2
x = None  # Reference count of the list object becomes 1 again
y = None  # Reference count of the list object becomes 0, and memory is deallocated
```

3. Garbage Collection: Create a large object using the ```create_large_object()``` function. Perform some operations with the object, and when it is no longer needed, deallocate its memory by setting it to ```None```. Use the ```gc.collect()``` function to explicitly trigger the garbage collector and reclaim the memory occupied by the large object.

```
import gc

def create_large_object():
    # Creates a large object
    return [0] * 10**6

def do_something():
    # Performs some operations
    pass

def main():
    large_object = create_large_object()  # Allocates memory for the large object
    do_something()  # Some operations that may or may not use the large object
    large_object = None  # Deallocates memory for the large object

    # Trigger garbage collection explicitly
    gc.collect()

if __name__ == '__main__':
    main()
```

These examples demonstrate the automatic memory management in Python, where memory is allocated for variables when needed and deallocated when they are no longer in use. The specifics of memory management, such as reference counting and garbage collection, are handled by the Python runtime environment.

## List Operations:
Operations are fundamental building blocks for performing calculations, manipulating data, and controlling program flow in many programming languages.

Some examples of common operations that can be performed on variables: arithmetic operations, comparison operations, assignment operations, string concatenation and list operations.

### 1. Arithmetic Operation:
```
a = 5
b = 3

sum = a + b
difference = a - b
product = a * b
quotient = a / b
remainder = a % b
exponentiation = a ** b

print(sum)  # Output: 8
print(difference)  # Output: 2
print(product)  # Output: 15
print(quotient)  # Output: 1.6666666666666667
print(remainder)  # Output: 2
print(exponentiation)  # Output: 125
```

### 2. Comparison Operation:
```
a = 5
b = 3

greater_than = a > b
less_than = a < b
equal_to = a == b
not_equal_to = a != b
greater_than_equal_to = a >= b
less_than_equal_to = a <= b

print(greater_than)  # Output: True
print(less_than)  # Output: False
print(equal_to)  # Output: False
print(not_equal_to)  # Output: True
print(greater_than_equal_to)  # Output: True
print(less_than_equal_to)  # Output: False
```

### 3. Assignment Operation
```
a = 5
b = 3

a += b  # Equivalent to a = a + b
print(a)  # Output: 8

a -= b  # Equivalent to a = a - b
print(a)  # Output: 5

a *= b  # Equivalent to a = a * b
print(a)  # Output: 15

a /= b  # Equivalent to a = a / b
print(a)  # Output: 5.0

a %= b  # Equivalent to a = a % b
print(a)  # Output: 2.0

a **= b  # Equivalent to a = a ** b
print(a)  # Output: 125.0
```

### 4. String concatenation:
```
first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name
print(full_name)  # Output: "John Doe"

```

### 5. List Operations:
```
numbers = [1, 2, 3, 4, 5]

length = len(numbers)
maximum = max(numbers)
minimum = min(numbers)
total = sum(numbers)
sorted_numbers = sorted(numbers)

print(length)  # Output: 5
print(maximum)  # Output: 5
print(minimum)  # Output: 1
print(total)  # Output: 15
print(sorted_numbers)  # Output: [1, 2, 3, 4, 5]
```

### Complex operations on variables
Complex operations involving conditional statements, loops, string formatting, list comprehension, function calls, and file operations. Such operations allow you to perform conditional branching, repeat tasks, format and manipulate strings, transform lists, call functions, and interact with files, providing powerful capabilities to solve complex problems in your programs.

1. Conditional Statements
```
a = 5
b = 3

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a and b are equal")

# Output: a is greater than b
```

2. Loops
```
# While Loop
i = 1
while i <= 5:
    print(i)
    i += 1

# Output: 1 2 3 4 5

# For Loop
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# Output: 1 2 3 4 5
```

3. String Formatting:
```
name = "Sam"
age = 25

message = f"My name is {name} and I am {age} years old."
print(message)

# Output: My name is Sam and I am 25 years old.

```

4. List Comprehensions:
```
numbers = [1, 2, 3, 4, 5]

squared_numbers = [num ** 2 for num in numbers if num % 2 == 0]
print(squared_numbers)

# Output: [4, 16]
```

5. Function Calls:
```
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

result = multiply(add(2, 3), 4)
print(result)

# Output: 20
```

6. File Operations:
```
# Reading from a File
with open("data.txt", "r") as file:
    data = file.read()
    print(data)

# Writing to a File
with open("output.txt", "w") as file:
    file.write("Hello, world!")

# Appending to a File
with open("log.txt", "a") as file:
    file.write("Log entry: Something happened")
```

## References
- [Using Python in Command Prompt](https://codeberryschool.com/blog/en/python-in-command-prompt/)
- [Python Variables - by realpython.org](https://realpython.com/python-variables/)
- [Python Variables - gfg](https://www.geeksforgeeks.org/python-variables/)
- [Python Variables - javatpoint](https://www.javatpoint.com/python-variables)

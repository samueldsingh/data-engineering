# List:
          
## 1. What is use of list. Explain different use cases of List.
- In Python, a list is a versatile data structure that is used to store a collection of items.
- It is a mutable, ordered sequence of elements enclosed in square brackets `([])`.
- Lists offer various functionalities and are commonly used in many programming scenarios. A few of the common use cases are:

1. Storing a collection of related data (homogeneous and heterogenous data in a sequence): Lists can be used to store multiple elements of different types. For example, you can use a list to store a collection of numbers, strings, objects, or any other data type.
2. Iteration and looping: Lists are iterable, which means you can iterate over each element in the list using loops like `for` or `while`. This makes lists useful for performing repetitive operations or calculations on a collection of items.
3. Maintaining order: Lists preserve the order of elements as they are added. This allows you to access elements by their index and perform operations based on their relative positions.
4. Modifying and updating data: Lists are mutable, meaning you can modify their elements. You can add or remove items, update existing values, or rearrange the order of elements as needed.
5. Storing and processing data in sequences: Lists can be used to store and process sequences of data, such as time series data, sensor readings, or any other data that requires sequential processing.
6. Implementing stacks and queues: Lists can be used to implement data structures like stacks (Last-In-First-Out) and queues (First-In-First-Out) by utilizing the `append()` and `pop()` methods.
7. Grouping related data: Lists provide a convenient way to group related data together. You can have nested lists within a list to create a hierarchical structure.
8. Passing and returning multiple values: Lists allow you to pass multiple values as arguments to functions or return multiple values from a function by encapsulating them in a list.

The flexibility and functionality provided by lists make them an essential tool for many programming tasks.

## 2. Sequence operations on List
Lists are a type of sequence, which means they support various sequence operations. Here are some common sequence operations that can be performed on lists:

Accessing elements by index `(my_list[0])`, Slicing `(my_list[1:4])`, Concatenation `(list1 + list2)`, Repetition `(*)`, Length `(len)`, Membership `(in)`, Iteration `(for)`, `max`, `min`, Sorting (`sort` method rearranges the elements of the list in ascending order and `sorted` function creates a new sorted list without modifying the original list), searching (`index` method returns the index of the first occurrence of the element).

## 3. Characteristics(Properties) of List

Lists are mutable, **ordered** (maintain the order of elements as they are inserted and allow indexing), allows duplicates, can store heterogeneous data types, Variable Length (items can be added or removed as needed), iterable, supports sequence operations, inbuilt methods and functions.

## 4. CRUD operations on List
CRUD stands for Create, Read, Update, and Delete, which are the basic operations performed on data. Here's how you can perform CRUD operations on a list in Python:

1. Create:
Create an empty list: `my_list = []`
Create a list with initial values: `my_list = [1, 2, 3]`

2. Read:
Access an element by index: `element = my_list[index]`
Iterate over the list:
```
for element in my_list:
    print(element)
```

3. Update
Update an element at a specific index: `my_list[index] = new_value`
Extend the list by appending another list: `my_list.extend(another_list)`

4. Delete
- Delete an element by index: `del my_list[index]`
- Remove the first occurrence of a value: `my_list.remove(value)`
Clear the entire list: `my_list.clear()`

These are the basic operations you can perform on a list. You can combine these operations to manipulate and modify the list according to your requirements.

## 5. Memory allocation of List
In Python, the memory allocation of a list is dynamic and managed by the Python interpreter. Here are some key points about memory allocation for lists:

1. List Size: The size of a list is not fixed and can vary based on the number of elements it contains. It can grow or shrink dynamically as elements are added or removed.

2. Memory Efficiency: Lists in Python are implemented as dynamic arrays, which means they provide efficient memory usage. The underlying array is automatically resized as needed to accommodate more elements.

3. Memory Overhead: Lists have some memory overhead due to additional information stored for each element, such as references to objects, size information, and internal bookkeeping. This overhead is relatively small compared to the actual data stored in the list.

4. Memory Reallocation: When a list grows beyond its current capacity, the Python interpreter automatically reallocates a larger block of memory to accommodate more elements. This process is transparent to the user and ensures efficient memory usage.

5. Garbage Collection: Python employs automatic garbage collection to reclaim memory occupied by unused objects, including lists. When a list becomes unreachable or is explicitly deleted, the memory occupied by the list and its elements is eventually freed by the garbage collector.
  
It's important to note that memory allocation and management in Python are abstracted away from the programmer, allowing you to focus on working with the list data structure without worrying about low-level memory details.

**Example:**
```
list1 = [1,2,3,4,5]
print(list1,id(list1))
list1[2] = 7
print(list1,id(list1))
```

The output is:
```
[1, 2, 3, 4, 5] 1640370354752
[1, 2, 7, 4, 5] 1640370354752
```

## 6. Write all possible combinations of list structure(homo,hetero with all data types, data structures)
 Here are examples of possible combinations of list structures in Python:

1. Homogeneous List of Integers:
```
string_list = ["apple", "banana", "cherry", "date"]
```

2. Homogeneous List of Strings:
```
string_list = ["apple", "banana", "cherry", "date"]
```

3. Homogeneous List of Floating-Point Numbers:
```
float_list = [1.2, 3.4, 5.6, 7.8, 9.0]
```

4. Heterogeneous List:
```
mixed_list = [1, "apple", 3.14, [1, 2, 3], {"name": "John", "age": 30}]
```

5. List of Lists:
```
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

6. List of Tuples:
```
list_of_tuples = [("apple", 1), ("banana", 2), ("cherry", 3)]
```

7. List of Dictionaries:
```
list_of_dicts = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}, {"name": "Bob", "age": 35}]
```

8. List of Sets:
```
list_of_sets = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
```

9. Nested List Structures:
```
nested_list = [[1, 2, 3], ["apple", "banana", "cherry"], [True, False, True]]
```

   These examples demonstrate various combinations of list structures using different data types and data structures. Remember, lists in Python can hold any type of object and can be nested to create complex data structures.

## 7. Explain about each method of List
- **append:** The `append()` method is used to add an element to the end of a list. It takes a single argument, which is the element to be added, and modifies the list in place by appending the element to the end.
```
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
```
In the above example, the append() method adds the element 4 to the end of the list my_list.

- **pop:** The `pop()` method is used to remove and return the last element from a list. It can also optionally take an index argument to remove and return an element at a specific index. If no index is provided, it removes and returns the last element by default.

```
my_list = [1, 2, 3, 4]
last_element = my_list.pop()
print(last_element)  # Output: 4
print(my_list)  # Output: [1, 2, 3]
```

In the above example, the `pop()` method removes and returns the last element `4` from the list `my_list`. The list is modified in place, and the resulting list contains the remaining elements `[1, 2, 3]`.

Example:
```
my_list = [1, 2, 3, 4]
second_element = my_list.pop(1)
print(second_element)  # Output: 2
print(my_list)  # Output: [1, 3, 4]
```

In this example, the `pop()` method with index `1` removes and returns the element at index `1` (which is `2`) from the list `my_list`.

Both `append()` and `pop()` are useful methods for manipulating lists. `append()` allows you to add elements to the end of a list, while `pop()` allows you to remove and retrieve elements, either from the end of the list or at a specific index.

## 8. shallow copy vs deep copy 
Generally, we use the ```=``` (assignment operator) to create a copy of the Python object.

**Copy in Python**
As we all know, the assignment operator is used to create the copy of the Python object, but this is not true; it only creates the binding between a target and object. When we use the assignment operator, instead of creating a new object, it creates a new variable that shares the old object's reference.

The copies are helpful when a user wants to make changes without modifying the original object at the same time. A user also prefers to create a copy to work with mutable objects.

Example:
```
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]  
list2 = list1  
  
list2[1][2] = 4  
  
print('Old List:', list1)  
print('ID of Old List:', id(list1))  
  
print('New List:', list2)  
print('ID of New List:', id(list2)) 
```

Output is:
```
Old List: [[1, 2, 3], [4, 5, 4], [7, 8, 'a']]
ID of Old List: 1909447368968
New List: [[1, 2, 3], [4, 5, 4], [7, 8, 'a']]
ID of New List: 1909447368968
```

**Explanation:**
- In the above output, we can see that both variable list1 and list2 share the same id 1909447368968.
- If we make any changes in any value in list1 or list2, the change will reflect in both.

**Types of Copies in Python**
The main motive is to create a copy of Python object that we can modify the copy without changing the original data. In Python, there are two methods to create copies.
- Shallow Copy
- Deep Copy

We can use the copy module to create the above copies.

**The copy Module**
The copy module is used to create the shallow copy and deep copy. 

**Shallow Copy**
A shallow copy is a copy of an object that stores the reference of the original elements. It creates the new collection object and then occupies it with reference to the child objects found in the original.

It makes copies of the nested objects' reference and doesn't create a copy of the nested objects. So if we make any changes to the copy of the object will reflect in the original object. We will use the copy() function to implement it.

Example:
```
import copy  
  
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]  
list2 = copy.copy(list1)  
  
list1.append([13, 14,15])  
  
print("Old list:", list1)  
print("New list:", list2) 
```

Output:
```
Old list: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
New list: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
```

Explanation -
In the above code, we have created a shallow copy of list1. The newly created list2 contains the reference of the original nested object stored in list1. We have then appended the `[13, 14, 15]` into the old list and sublist not copied in the new list.

**Deep Copy**
A deep copy is a process where we create a new object and add copy elements recursively. We will use the `deecopy()` method which is present in `copy` module. The independent copy is created of original object and its entire object. Let's understand the following example.

```
import copy  
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  
z = copy.deepcopy(xs)  
print(x)  
prin(z) 
```

The output is:
```
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

**Explanation**
In the above output, we can see that `z` is a clone of `x` that we have created using the `deecopy()` method. If we make change to one of child won't affect the original object.

## 10. append vs extend
`append()` and `extend()` are both methods used to add elements to a list in Python, but they differ in how they add the elements:

1. `append()`: The `append()` method is used to add a single element to the end of a list. It modifies the original list by adding the element as a single item.

Example:
```
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
```

In this example, the `append()` method is used to add the integer `4` as a single element to the end of the list.

2. `extend()`: The `extend()` method is used to add multiple elements to the end of a list. It takes an iterable (such as another list or tuple) and adds each element from the iterable to the end of the original list.

Example:
```
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
```

In this example, the `extend()` method is used to add the elements `[4, 5, 6]` to the end of the list individually, resulting in a list with six elements.

To summarize:

Use `append()` when you want to add a single element to the end of a list.
Use `extend()` when you want to add multiple elements from an iterable to the end of a list.

It's important to note that `append()` and `extend()` modify the original list in place, meaning they directly modify the list object and do not create a new list.

## 11. pop vs remove

`pop()` and `remove()` are both methods used to remove elements from a list in Python, but they differ in how they remove the elements:

1. `pop()`: The `pop()` method is used to remove and return an element from a **specific index** in a list. It modifies the original list by removing the element at the specified index and returning its value.

Example:
```
my_list = [1, 2, 3, 4, 5]
removed_element = my_list.pop(2)
print(my_list)  # Output: [1, 2, 4, 5]
print(removed_element)  # Output: 3
```

In this example, the `pop()` method is used to remove and return the element at index 2 (which is `3`) from the list.

2. `remove()`: The `remove()` method is used to **remove the first occurrence of a specific value** from a list. It modifies the original list by removing the first occurrence of the specified value.

Example:
```
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list)  # Output: [1, 2, 4, 5]
```

In this example, the `remove()` method is used to remove the first occurrence of the value `3` from the list.

## 12. Pass by value vs Pass by reference

"Pass by value" and "pass by reference" are two different approaches to passing arguments to functions or methods. The distinction between them relates to how the values of the arguments are handled and whether modifications made to the arguments within the function affect the original values.

**Pass by value:**
- In pass by value, a copy of the value of the argument is passed to the function.
- Any modifications made to the argument within the function do not affect the original value.
- Changes made to the copied value inside the function are local to the function and do not impact the original value.
- This approach is typically used with immutable data types, such as numbers, strings, and tuples.
- Examples of pass by value languages are C, C++, and Java.

Example:
```
def modify_value(x):
    x = 10

value = 5
modify_value(value)
print(value)  # Output: 5
```

In this example, the function `modify_value` takes an argument `x` and assigns it a new value of `10`. However, since integers are immutable in Python, the assignment `x = 10` creates a new integer object and the original value of `value` is not modified. Therefore, the output is still `5`.

The integer value is passed by value, meaning that the function receives a copy of the value, and modifications made inside the function do not affect the original variable. 

**Pass by reference:**
- In pass by reference, a reference to the memory address of the argument is passed to the function.
- Any modifications made to the argument within the function directly affect the original value.
- Changes made to the referenced value inside the function are reflected outside the function as well.
- This approach is typically used with mutable data types, such as lists and dictionaries.
- Examples of pass by reference languages are Python, Ruby, and JavaScript.

Example:
```
def modify_list(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]
```

In this example, the function `modify_list` takes a list `lst` and appends the value 4 to it. Since lists are mutable in Python, any modifications made to the list `lst` within the function will be reflected in the original list `my_list`. Therefore, the output is `[1, 2, 3, 4]`.

The list is passed by reference, so the function receives a reference to the original list, and modifications made inside the function are reflected in the original variable.

In summary, "pass by value" involves copying the value of the argument, while "pass by reference" involves passing a reference to the memory address of the argument. The choice between them depends on the programming language and the type of data being passed.

# Tuple:
## 1. What is use of Tuple. Explain different use cases of Tuple
Tuples in Python are used to store an ordered collection of items. Unlike lists, tuples are immutable, meaning their elements cannot be modified once defined. Tuples have several use cases due to their unique properties:

1. Data Integrity: Tuples are used when you want to ensure that the data in the collection remains unchanged. Since tuples are immutable, they provide data integrity, preventing accidental modifications.

2. Data Protection: Tuples can be used to protect sensitive data. For example, if you have a collection of values that should not be modified, you can store them in a tuple to prevent accidental changes.

3. Function Return Values: Tuples are often used to return multiple values from a function. By packing the values into a tuple, you can easily return and unpack them in the calling code.

4. Dictionary Keys: Tuples can be used as keys in dictionaries since they are immutable. This is useful when you want to use a collection of values as a dictionary key.

5. Iteration: Tuples are useful when you want to iterate over a collection of items in a specific order. Since tuples are immutable, they can be safely used in scenarios where the items should not be modified during iteration.

6. Grouping of Data: Tuples can be used to group related data together. For example, you can store the name and age of a person as a tuple, making it easy to pass around as a single entity.

7. Multiple Assignments: Tuples can be used for multiple assignments, where you assign multiple values to multiple variables in a single statement.

Overall, tuples provide a way to store and manage collections of data in a way that guarantees immutability, data integrity, and specific ordering. They are suitable for scenarios where you need to represent fixed or unchangeable data.

## 2. Sequence operations on Tuple
Tuples in Python support various sequence operations that can be performed on them. Here are some common sequence operations you can perform on tuples: indexing, slicing, concatenation, multiplication, length, iteration, membership, max, min.

## 3. Characteristics (Properties) of Tuple
Tuples in Python have the following characteristics or properties:
1. Immutable: Tuples are immutable, meaning their elements cannot be changed after they are created. Once a tuple is defined, you cannot add, remove, or modify its elements. However, you can create new tuples by concatenating or slicing existing tuples.

2. Ordered: Tuples maintain the order of elements as they are defined. The elements in a tuple are accessed by their index values, starting from 0 for the first element.

3. Heterogeneous: Tuples can store elements of different data types, such as integers, floats, strings, and even other tuples. You can mix and match different data types within a single tuple.

4. Indexed: Elements in a tuple can be accessed using their index positions. You can retrieve a specific element from a tuple by specifying its index value.

5. Iterable: Tuples are iterable, which means you can iterate over their elements using loops, such as `for` loops. This allows you to process each element of a tuple individually.

6. Size and Length: Tuples have a fixed size, meaning the number of elements in a tuple is fixed when it is created. The size of a tuple cannot be changed. You can determine the length of a tuple using the `len()` function.

7. Storage Efficiency: Tuples are more memory-efficient compared to lists because they are immutable. This can be beneficial when dealing with large amounts of data or when you need to ensure the integrity of data.

8. Used for Grouping: Tuples are often used to group related data together. For example, you can use a tuple to represent a point in 2D or 3D space with its x, y, and z coordinates.

Overall, tuples provide a way to store and organize data in an ordered and immutable manner. They are suitable for situations where you need to store a fixed collection of elements that should not be modified.
          
## 4. CRUD operations on Tuple
In Python, tuples are immutable, which means their elements cannot be modified once the tuple is created. Therefore, the CRUD (Create, Read, Update, Delete) operations that involve modifying the elements of a data structure are not applicable to tuples. However, let's explore the available operations on tuples:

1. Create: Tuples can be created using parentheses `()` or the `tuple()` constructor. Elements are separated by commas.
```
my_tuple = (1, 2, 3)  # Creating a tuple using parentheses
another_tuple = tuple([4, 5, 6])  # Creating a tuple using the tuple() constructor
```

2. Read: Elements of a tuple can be accessed using their index positions. Indexing starts from 0 for the first element.
```
my_tuple = (1, 2, 3)
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3
```

3. Update: Since tuples are immutable, you cannot directly update or modify their elements. However, you can create a new tuple by concatenating or slicing existing tuples.
```
my_tuple = (1, 2, 3)
new_tuple = my_tuple + (4, 5)  # Concatenating tuples
print(new_tuple)  # Output: (1, 2, 3, 4, 5)
```

4. Delete: Elements of a tuple cannot be individually deleted or removed. However, you can delete the entire tuple itself using the `del` statement.
```
my_tuple = (1, 2, 3)
del my_tuple  # Deleting the entire tuple
```

It's important to note that while you cannot modify a tuple directly, you can assign a new tuple to the same variable, effectively replacing the old tuple with a new one.

```
my_tuple = (1, 2, 3)
my_tuple = (4, 5, 6)  # Reassigning a new tuple to the same variable
```

Overall, tuples are primarily used for storing and accessing immutable data. While they do not support the same level of flexibility for modification as lists, they provide benefits such as immutability, storage efficiency, and ensuring data integrity.

## 5. Memory allocation of Tuple
In Python, tuples are stored in memory in a contiguous block of memory, similar to lists. However, there are some differences in memory allocation between tuples and lists:

1. Memory Size: Tuples generally require less memory compared to lists. This is because tuples are immutable, meaning their size and elements cannot be changed after creation. As a result, the memory for tuples can be allocated more efficiently.

2. Fixed Size: Once a tuple is created, its size remains fixed. This allows the Python interpreter to allocate a fixed amount of memory for the tuple. The memory allocation is based on the number of elements in the tuple and the memory required to store each element.

3. Element References: Tuples store references to objects rather than the actual objects themselves. When a tuple contains objects, such as other tuples, lists, or objects of custom classes, the memory for those objects is allocated separately. The tuple stores references to these objects, which are pointers to their memory locations.

4. Immutable Nature: The immutability of tuples ensures that the memory allocated for a tuple remains unchanged. It eliminates the need for dynamic memory allocation or resizing, as is the case with lists. This can lead to more efficient memory usage and faster access times.

5. Memory Deallocation: When a tuple is no longer referenced by any variable, it becomes eligible for garbage collection. The Python interpreter automatically frees the memory occupied by the tuple during the garbage collection process.

Overall, the memory allocation for tuples in Python is optimized for efficient storage and access of immutable data. Tuples are well-suited for situations where data integrity and immutability are important, and memory efficiency is a concern.
          
## 6. Write all possible combinations of Tuple structure(homo,hetero with all data types, data structures)
Some examples of possible combinations of tuple structures:

**1. Homogeneous Tuple:**
- Integer Tuple: (1, 2, 3)
- String Tuple: ("apple", "banana", "cherry")
- Boolean Tuple: (True, False, True)

**2. Heterogeneous Tuple:**
- Mixed Data Types: ("John", 25, True)
- Tuple of Lists: ([1, 2, 3], ["a", "b", "c"], [True, False])
- Tuple of Tuples: ((1, 2), ("a", "b"), (True, False))
- Tuple of Dictionaries: ({"name": "John", "age": 25}, {"fruit": "apple", "color": "red"})

**3. Nested Tuple:**
- Tuple of Tuples and Lists: ((1, 2), [3, 4, 5], (6, 7, 8))
- Tuple of Tuples and Dictionaries: ((1, 2), {"name": "John", "age": 25}, (True, False))

**4.Tuple with Different Data Structures:**
- Tuple of Sets: ({1, 2, 3}, {"apple", "banana", "cherry"})
- Tuple of Strings and Lists: ("Hello", ["world", "python", "programming"])
- Tuple of Lists and Dictionaries: (["a", "b", "c"], {"name": "John", "age": 25})

These are just a few examples, and you can create various combinations of tuples based on your specific requirements. Tuples provide flexibility in storing different data types and structures together, allowing you to represent complex and structured data in a single object.
          
## 7. Explain about each function of Tuple
Some commonly used functions with tuple are:
1. Indexing: Allows you to access individual elements of a tuple by their position. It uses square brackets `[]` along with the index of the element you want to access. Example: `my_tuple[0]` returns the first element of the tuple.

2. Slicing: Enables you to extract a subset of elements from a tuple by specifying a range of indices. It uses the colon `:` operator. Example: `my_tuple[1:4]` returns a new tuple with elements from index 1 to 3.

3. Concatenation: Allows you to combine two tuples into a single tuple. It uses the `+` operator. Example: `tuple1 + tuple2` returns a new tuple with elements from both `tuple1` and `tuple2`.

4. Length: Returns the number of elements in a tuple. It uses the `len()` function. Example: `len(my_tuple)` returns the length of the tuple.
 
5. Membership: Checks if a specific element exists in a tuple. It uses the `in` keyword. Example: `element in my_tuple` returns `True` if the element is present in the tuple, otherwise `False`.

6. Count: Returns the number of occurrences of a specific element in a tuple. It uses the `count()` method. Example: `my_tuple.count(element)` returns the count of occurrences of `element` in the tuple.

7. Index: Returns the index of the first occurrence of a specific element in a tuple. It uses the `index()` method. Example: `my_tuple.index(element)` returns the index of the first occurrence of `element` in the tuple.

8. Iteration: Allows you to iterate over the elements of a tuple using a loop or other iterable constructs. Example: for `item in my_tuple`: allows you to iterate over each element of the tuple.

These functions provide various operations to work with tuples, enabling you to access, manipulate, and iterate over the elements effectively.
          
## 8. shallow copy vs deep copy in tuple.
In Python, a shallow copy and a deep copy are two different ways to create copies of objects, including tuples. Let's understand the differences between shallow copy and deep copy in the context of tuples:

1. Shallow Copy:
- Shallow copy creates a new tuple object, but it references the same elements as the original tuple.
- If the elements of the original tuple are immutable (e.g., numbers, strings), modifying the elements in the shallow copy does not affect the original tuple.
- However, if the elements of the original tuple are mutable objects (e.g., lists, dictionaries), modifying the elements in the shallow copy will affect the original tuple.
- Shallow copy can be created using the `tuple()` constructor or the slice operator `[:]`.
- Example: `tuple2 = tuple(tuple1)` or `tuple2 = tuple1[:]`

2. Deep Copy:
- Deep copy creates a completely independent copy of the original tuple, including all its elements.
- Regardless of whether the elements are mutable or immutable, modifying the elements in the deep copy does not affect the original tuple.
- Deep copy can be created using the copy.deepcopy() function from the copy module.
- Example: import copy and tuple2 = copy.deepcopy(tuple1)

Here's an example to demonstrate the difference between shallow copy and deep copy:
```
import copy

# Original tuple
tuple1 = ([1, 2, 3], 'abc')

# Shallow copy
tuple2 = tuple(tuple1)
tuple2[0].append(4)

# Deep copy
tuple3 = copy.deepcopy(tuple1)
tuple3[0].append(5)

print(tuple1)  # ([1, 2, 3, 4], 'abc')
print(tuple2)  # ([1, 2, 3, 4], 'abc')
print(tuple3)  # ([1, 2, 3, 5], 'abc')
```

In the above example, the shallow copy tuple2 and the original tuple tuple1 share the same list object, so modifying the list in tuple2 also affects tuple1. However, the deep copy tuple3 is completely independent, so modifying its list doesn't affect the original tuple.
          
## 9. list vs tuple ( Min. 4 differences in detail)

**List:** 
In other programming languages, list objects are declared similarly to arrays. Lists don't have to be homogeneous all the time, so they can simultaneously store items of different data types. This makes lists the most useful tool. The list is a kind of container data Structure of Python that is used to hold numerous pieces of data simultaneously. Lists are helpful when we need to iterate over some elements and keep hold of the items.

**Tuple:** 
A tuple is another data structure to store the collection of items of many data types, but unlike mutable lists, tuples are immutable. A tuple, in other words, is a collection of items separated by commas. Because of its static structure, the tuple is more efficient than the list.


*1. Time Complexity:*

Because lists are mutable, the flexibility comes with a slight overhead in terms of time complexity. Because Tuples are immutable, the performance is optimized.

| Lists      | Tuples |
| ----------- | ----------- |
| Accessing an element by index `O(1)`: Accessing an element by index takes constant time because the index allows direct access to the desired element.      | Accessing an element by index `O(1)`. Since tuples are indexed collections, accessing an element by its index takes constant time.       |
| Appending an element to the end `O(1)`: Appending an element to the end of a list takes amortized constant time `(O(1))`.   | Concatenating two tuples: `O(n)` The time complexity in concatenating two tuples is proportional to the sum of the sizes of the two tuples.        |
| Inserting or deleting an element at a specific index: Inserting or deleting an element at a specific index in a list takes linear time `(O(n))` because it may require shifting elements. Tuples are immutable, so you cannot perform these operations on them.   |    |
| Searching for an element: In both cases, searching for an element in a list or tuple takes linear time `(O(n))` in the worst case because the entire collection needs to be traversed.      |  Searching for an element: `O(n)` (similar to lists)   |

*2. Space Complexity:*

The space complexity of lists and tuples in Python differs based on their characteristics.
| Lists      | Tuples |
| ----------- | ----------- |
|  Lists are mutable, meaning they can be modified by adding, removing, or changing elements.  |  Tuples are immutable, meaning they cannot be modified once created.  |
|  The space complexity of a list is O(n), where n is the number of elements in the list.  |  The space complexity of a tuple is also O(n), where n is the number of elements in the tuple.  |
| Lists require additional space to store the elements as well as the underlying data structure that allows dynamic resizing.   |  Tuples require space to store the elements, but they do not require additional memory for dynamic resizing.  |
|  In lists, each element is stored as a separate object, and additional memory is needed to store references to these objects.  |  In tuples, elements are stored consecutively in memory without the need for extra references.  |

In general, tuples tend to have slightly lower space complexity than lists due to their immutability and lack of dynamic resizing overhead. However, the difference in space complexity between lists and tuples is typically negligible unless dealing with a very large number of elements.


*3. Mutability:*
The main difference between a list and a tuple is mutability. A list is mutable, which means its elements can be modified after creation. On the other hand, a tuple is immutable, which means its elements cannot be modified once the tuple is created. In other words, you can add, remove, or change elements in a list, but you cannot do so in a tuple.

*4. Syntax:*
Lists are defined using square brackets `[ ]`, while tuples are defined using parentheses `( )`. For example, `my_list = [1, 2, 3]` is a list, and `my_tuple = (1, 2, 3)` is a tuple.

*5. Usage and Intended Purpose:*
- Lists are commonly used when you need a collection of elements that can be modified. They are suitable for situations where you want to add, remove, or change elements dynamically.
- Tuples, on the other hand, are used when you want to create a collection of elements that should remain constant and unchanged. They are suitable for situations where you want to store related pieces of information together, such as coordinates, settings, or database records.

*6. Performance:*
Tuples are generally more lightweight and faster than lists in terms of performance. Since tuples are immutable, the interpreter can optimize memory allocation for tuples, resulting in faster access and execution. Lists, being mutable, require additional memory allocation and management, which can impact performance, especially when dealing with large lists.

*7. Use as Dictionary Keys:*
Tuples can be used as keys in dictionaries, whereas lists cannot. Since tuples are immutable, they provide a reliable and hashable representation for dictionary keys. This allows tuples to be used in scenarios where you need an unchangeable, unique identifier for dictionary entries.

It's important to note that the choice between using a list or a tuple depends on the specific requirements of your program. If you need mutability and dynamic modifications, a list is the appropriate choice. If you need immutability and a collection of constant elements, a tuple is a better fit.

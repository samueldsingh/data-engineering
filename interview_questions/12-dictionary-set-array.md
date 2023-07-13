# 1. Dictionary

A dictionary is an unordered collection of key-value pairs, where each key is unique within the dictionary. It is also known as an associative array or a hash table in other programming languages. Sequences follow indexing mechanism but dictionaries use the `item` function to access the key-value pair in a dictionary.`item` function works by converting the dictionary into a list of tuples.

They provide fast access to values based on their associated keys, making them suitable for situations where you need to retrieve values by a unique identifier.

Key features of dictionaries in Python include:

1. Uniqueness of keys: Each key in a dictionary must be unique. If you try to add a key that already exists, it will update the corresponding value.

2. Mutable: Dictionaries can be modified by adding, updating, or deleting key-value pairs.

3. Flexible data types: Dictionaries can store values of any data type, allowing you to associate different types of data together.

4. Efficient lookup: Retrieving a value from a dictionary based on a key is efficient, even for large dictionaries, as the lookup time is close to constant time.

Unordered: The order of elements in a dictionary is not fixed or preserved. If you need to maintain the order, you can use the `collections.OrderedDict` class.

Dictionaries provide a powerful and versatile way to store and retrieve data using key-value associations. They are commonly used for tasks such as data mapping, caching, configuration settings, and organizing data in a structured manner.

Example:
We have the given dictionary:
```
order_details = {'order_no': 123213,
                 'ref_no': 3432,
                 'cust_name': 'Madhu Nettem',
                 'del_loc': 'Bangalore',
                 'total_bill': 543.56,
                 'discount': 23,
                 'disc_percnt': 5,
                 'pin_code': '560037',
                 'no_of_items': 4,
                 }
```

```
for key, val in order_details.items():  #  [('eid', 45000), ('name','Madhu Nettem')]
    print(key, "-----", val)
```

The output is:
```
order_no ----- 123213
ref_no ----- 3432
cust_name ----- Madhu Nettem
del_loc ----- Bangalore
total_bill ----- 543.56
discount ----- 23
disc_percnt ----- 5
pin_code ----- 560037
no_of_items ----- 4
```

Properties of a dictionary:
1. Keys should be immutable and values can be anything
Example:
```
dict1 = {100: 10,
         200: {1: 1, 2: 2},
         102.3: 29,
         True: 'Madhu',
         'Message': [1, 2, 3, 4, 5],
         (1, 2, 3): (1, 2, 3),      # Tuples are immutables and can be used as key value pairs
         [1, 2, 3]: {1: 1, 2: 2},  # Wrong, List is mutable
         {1: 1, 2: 2}: "Hello",   # Wrong, dict is mutable
         {1, 2, 3}: "Hello"     # Wrong, set is mutable
         }
```

2. Keys should be unique

## 2. CRUD operations in Dictionaries

### CREATE
```
data = {1: 'One', 2: 'Two', 3: 'Two', 'id': '100'}
```

### RETRIEVE
```
print("Dictionary : ", data, type(data))
print("Dict item  :", data[2])
print("Dict item  :", data['id'])
```

Output:
```
Dictionary :  {1: 'One', 2: 'Two', 3: 'Two', 'id': '100'} <class 'dict'>
Dict item  : Two
Dict item  : 100
```

### UPDATE
```
data[2] = 'Twenty'
data['id'] = 200
print("Dictionary update: ", data)
```

Output:
```
Dictionary update:  {1: 'One', 2: 'Twenty', 3: 'Two', 'id': 200}
```

### DELETE

1. Delete entire  dict   --> `del dict1`
2. Delete any one item   --> `del dict1['id']`
3. Delete entire items   --> `dict1.clear()`

```
data = {1: 'One', 2: 'Two', 3: 'Two', 'id': '100'}
```

```
del data[3]
del data['id']
print("Dictionary delete1: ", data)

data.clear()
print("Dictionary delete2: ", data)

data['sal'] = 1000
print("Dictionary delete3: ", data)
```

Output is:
```
Dictionary delete1:  {1: 'One', 2: 'Two'}
Dictionary delete2:  {}
Dictionary delete3:  {'sal': 1000}
```

## 3. Memory allocation of dictionary
Generally, dictionaries in Python use more memory compared to other data structures like lists or tuples due to their flexible and dynamic nature. 

Dictionaries are implemented as hash table. The hash table consists of an array of buckets, and each bucket stores multiple key-value pairs:
1. When key-values are added, calculate hash value (integer representing the object) of dict key.
2. Check if bucket exists or not based on hashkey.
3. If bukcet exists, value is stored in the same or else new bucket is created.
4. If multiple key values have the same hash value, chaining which involves creating a linked list of key-value pairs is done in the same bucket.


## 4. Shallow copy vs deep copy
In shallow copy, changes made to the recursive list will be affected. In deep copy, changes made to the recursive list will not be affected.

When creating copies of dictionaries, you have to option to perform shallow copies or deep copies.

A shallow copy creates a new dictionary object, but the keys and values of the new dictionary still refer to the same objects as the original dictionary. Any modifications made to the shared elements will be reflected in both the original and the copy.

Example of a shallow copy of a dictionary:
```
original = {'a': [1, 2, 3], 'b': [4, 5, 6]}
copy = original.copy()

# Modifying the value of 'a' in the copy affects the original
copy['a'].append(4)

print(original)  # Output: {'a': [1, 2, 3, 4], 'b': [4, 5, 6]}
print(copy)  # Output: {'a': [1, 2, 3, 4], 'b': [4, 5, 6]}
```

A deep copy, on the other hand, creates a completely independent copy of the original dictionary, including all the nested objects. Any modifications made to the elements in the deep copy will not affect the original dictionary, and vice versa.

Example of a deep copy of a dictionary:
```
import copy

original = {'a': [1, 2, 3], 'b': [4, 5, 6]}
deep_copy = copy.deepcopy(original)

# Modifying the value of 'a' in the deep copy does not affect the original
deep_copy['a'].append(4)

print(original)  # Output: {'a': [1, 2, 3], 'b': [4, 5, 6]}
print(deep_copy)  # Output: {'a': [1, 2, 3, 4], 'b': [4, 5, 6]}
```

## 5. Dictionary Functions

The commonly used dictionary functions are: `len()`, `type()`, `str()`, `dict()`.
The built-in functions are:
`keys()`, `values()`, `items()`, `update()`, `clear()`, `fromkeys()`, `copy()`, `has_key()`, `pop()`, `popitem()`, `setdefault()`

Certainly! Here are examples of various dictionary functions and methods in Python:

1. `len()`:
   - The `len()` function returns the number of key-value pairs in a dictionary.
   - Example:
     ```python
     my_dict = {"name": "John", "age": 30, "city": "New York"}
     print(len(my_dict))  # Output: 3
     ```

2. `type()`:
   - The `type()` function returns the type of an object, which in this case would be "dict" for a dictionary.
   - Example:
     ```python
     my_dict = {"name": "John", "age": 30, "city": "New York"}
     print(type(my_dict))  # Output: <class 'dict'>
     ```

3. `str()`:
   - The `str()` function converts a dictionary into a string representation.
   - Example:
     ```python
     my_dict = {"name": "John", "age": 30, "city": "New York"}
     dict_str = str(my_dict)
     print(dict_str)  # Output: "{'name': 'John', 'age': 30, 'city': 'New York'}"
     ```

4. `dict()`:
   - The `dict()` function creates a new dictionary object.
   - Example:
     ```python
     my_dict = dict(name="John", age=30, city="New York")
     print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
     ```

5. `keys()`:
   - The `keys()` method returns a list containing all the keys in the dictionary.
   - Example:
     ```python
     my_dict = {"name": "John", "age": 30, "city": "New York"}
     key_list = my_dict.keys()
     print(key_list)  # Output: ['name', 'age', 'city']
     ```

6. `values()`:
   - The `values()` method returns a list containing all the values in the dictionary.
   - Example:
     ```python
     my_dict = {"name": "John", "age": 30, "city": "New York"}
     value_list = my_dict.values()
     print(value_list)  # Output: ['John', 30, 'New York']
     ```

7. `items()`:
   - The `items()` method returns a list of tuples containing key-value pairs in the dictionary.
   - Example:
     ```python
     my_dict = {"name": "John", "age": 30, "city": "New York"}
     item_list = my_dict.items()
     print(item_list)  # Output: [('name', 'John'), ('age', 30), ('city', 'New York')]
     ```

8. `update()`:
   - The `update()` method updates the dictionary with key-value pairs from another dictionary or iterable.
   - Example:
     ```python
     my_dict = {"name": "John", "age": 30}
     new_data = {"city": "New York", "country": "USA"}
     my_dict.update(new_data)
     print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}
     ```

9. `clear()`:
   - The `clear()` method removes all key-value pairs from the dictionary, making it empty.
   - Example:
     ```python
     my_dict = {"name": "John", "age": 30}
     my_dict.clear()
     print(my_dict)  # Output: {}
     ```

10. `fromkeys()`:
    - The `fromkeys()` method creates a new dictionary with specified keys and a default value.
    - Example:
      ```python
      keys = ["name", "age", "city"]
      default_value = "Unknown"
      my_dict = dict.fromkeys(keys, default_value)
      print(my_dict)  # Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}
      ```

Certainly! Here are examples of some additional dictionary functions and methods:

11. `copy()`:
   - The `copy()` method creates a shallow copy of a dictionary.
   - Example:
     ```python
     my_dict = {"name": "John", "age": 30, "city": "New York"}
     new_dict = my_dict.copy()
     print(new_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
     ```

12. `has_key()` (Deprecated):
   - The `has_key()` method checks if a specified key exists in the dictionary.
   - Note: In Python 3.x, `has_key()` has been removed. Instead, you can use the `in` operator.
   - Example:
     ```python
     my_dict = {"name": "John", "age": 30, "city": "New York"}
     print("age" in my_dict)  # Output: True
     ```

13. `pop()`:
   - The `pop()` method removes and returns the value associated with the specified key from the dictionary.
   - Example:
     ```python
     my_dict = {"name": "John", "age": 30, "city": "New York"}
     age = my_dict.pop("age")
     print(age)  # Output: 30
     print(my_dict)  # Output: {'name': 'John', 'city': 'New York'}
     ```

14. `popitem()`:
   - The `popitem()` method removes and returns the last inserted key-value pair as a tuple from the dictionary.
   - Note: In Python 3.7 and later versions, `popitem()` removes an arbitrary key-value pair instead of the last inserted one.
   - Example:
     ```python
     my_dict = {"name": "John", "age": 30, "city": "New York"}
     item = my_dict.popitem()
     print(item)  # Output: ('city', 'New York')
     print(my_dict)  # Output: {'name': 'John', 'age': 30}
     ```

15. `setdefault()`:
   - The `setdefault()` method returns the value of a specified key in the dictionary. If the key does not exist, it inserts the key with a default value and returns the default value.
   - Example:
     ```python
     my_dict = {"name": "John", "age": 30}
     city = my_dict.setdefault("city", "New York")
     print(city)  # Output: 'New York'
     print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
     ```

These are some examples of functions and methods available for working with dictionaries in Python. Dictionaries provide a flexible and efficient way to store and manipulate data using key-value pairs.

These are just a few examples of functions and methods that can be used with dictionaries in Python. Dictionaries offer a wide range of functionality for storing, accessing, and manipulating data in a key-value format.

## 6. get() method

- `get()` method is used in dictionaries when you don't know if a key exists
- The `get()` method in Python dictionaries is used to retrieve the value associated with a given key.
- It takes two parameters: the key whose value needs to be retrieved, and an optional default value that is returned if the key is not found in the dictionary.

```
my_dict = {'name': 'John', 'age': 30, 'country': 'USA'}
```

```
name = my_dict.get('name')
print(name)  # Output: John
```

``` 
city = my_dict.get('city', 'Unknown')
print(city)  # Output: Unknown (since 'city' key does not exist) 
```

```
country = my_dict.get('country', 'Unknown')
print(country)  # Output: USA
```

## 7. List vs array
|  List |  Array  |
|---|---|
|Flexibility: Lists in Python are dynamic and can store elements of different types.   | Arrays, on the other hand, are more rigid and have a fixed size.   |
| Element Types: Lists can store elements of any type, including integers, strings, floats, booleans, and even other lists or complex objects.  | Arrays, however, are designed to store elements of a single type.   |
| Memory Efficiency: Lists in Python are implemented as dynamic arrays that can resize themselves as needed, which can result in memory overhead and slower performance for large lists.   | Arrays can be more memory-efficient than lists in certain scenarios because they store elements as contiguous blocks in memory. This allows for efficient indexing and element access. |
| Functionality: Lists have built-in functions and methods that provide a wide range of operations, such as appending, inserting, removing, sorting, and searching elements.   |  Arrays, particularly the `array` module in Python, offer a more limited set of operations and methods, mainly focused on efficient element access, slicing, and basic mathematical operations  |


In summary, lists are versatile and flexible data structures that can store elements of different types 
and have extensive built-in functionality. Arrays, specifically the array module in Python, are more 
specialized data structures that offer efficiency and performance benefits for working with homogeneous 
data of a single type. Additionally, Python provides powerful external libraries like NumPy and Pandas 
that further enhance the capabilities of arrays for numerical computations and data analysis tasks.

## 8. Set
- In Python, a set is an unordered collection of unique elements. 
- It is a built-in data type that is used to 
store a collection of items where each item is unique. 
- It is a collection of distinct objects of the same type or class of objects. An object can be numbers, alphabets, names, etc.
- Sets are utilized when an object only needs to exist within a collection of objects.

Examples of sets are:
- A set of rivers of India.
- A set of vowels.

Some common set operations are:
Union, Intersection, Difference, Symmetric Difference, Update

Key features of set are:
- Uniqueness: duplicate element will be ignored.
- Unordered: the order of elements in a set is arbitrary and can change
- Mutable: you can add or remove elements from them
- Mathematical set operations: Union, Intersection, difference, symmetric difference
- It doesn't follow indexing.
- It follows hashing algorithm
- Both homo/heterogeneous data allowed (But Immutable)

Example: Set Operations
```
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union of sets
union = set1.union(set2)
print(union)  # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection of sets
intersection = set1.intersection(set2)
print(intersection)  # {4, 5}

# Difference of sets
difference = set1.difference(set2)
print(difference)  # {1, 2, 3}

# Symmetric difference of sets
symmetric_difference = set1.symmetric_difference(set2)
print(symmetric_difference)  # {1, 2, 3, 6, 7, 8}
```

Example: Creating a Set from a List
```
# Creating a set from a list
numbers = set([1, 2, 3, 4, 5])
print(numbers)
```

Example: Symmetric Difference
```
set1 = {1, 2, 3}
set2 = {3, 4, 5}

symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}
```

## When to use sets:
Sets are useful in situations where you need to work with a collection of unique elements
and perform operations like intersection, union, difference, and symmetric difference.

A few of the other scenarios where set is used are:
- Removing duplicates, Membership testing, Set operations (operations like union, intersection, difference, 
and symmetric difference can be used to combine or compare sets, find common elements, 
or determine the unique elements between sets),
- Mathematical modeling (they represent mathematical concepts 
such as sets, subsets, and universal sets, making it easier to perform calculations and analyze relationships between elements),
removing unwanted elements.
- Sets cannot contain mutable objects like lists or dictionaries since they need to be hashable. If you need 
to maintain the order of elements or store mutable objects, you may need to consider other data structures like lists or dictionaries.

## Mutability and immutability of elements within a set
The mutability or immutability of elements within a set is independent of the mutability or immutability of the 
set itself. In other words, a set can contain both mutable and immutable objects.

1. Mutability of elements:
If an object within a set is mutable, it means that its state can be modified after it is added to the set.
Modifying a mutable object within a set will not affect the membership or position of the object within the set.

```
my_set = {1, [2, 3], 'hello'}
print(my_set)  # Output: {1, [2, 3], 'hello'}

# Modifying the list object within the set
my_set[1].append(4)
print(my_set)  # Output: {1, [2, 3, 4], 'hello'}
```

In the above example, we have a set containing an integer, a list, and a string. Since lists are mutable, 
we can modify the list object within the set without affecting its membership within the set.

2. Immutability of elements:
If an object within a set is immutable, it means that its state cannot be modified after it is added to the set.
Immutable objects are usually hashable, allowing them to be used as elements within a set.

```
my_set = {1, (2, 3), 'hello'}
print(my_set)  # Output: {1, (2, 3), 'hello'}

# Trying to modify the tuple object within the set (will raise an error)
my_set[1][0] = 4  # Raises a TypeError
```

In the above example, we have a set containing an integer, a tuple, and a string. Since tuples are immutable, 
we cannot modify the tuple object within the set. Attempting to modify an immutable object within the set will result in a TypeError.

It's important to note that the mutability or immutability of the elements within a set affects how they can 
be modified or used, but it does not affect the set itself. The set can still be modified by adding or 
removing elements, regardless of the mutability or immutability of the elements it contains.


## Array

- Arrays are commonly used in programming to store and manipulate collections of data. Arrays are used to store multiple values of the same type in single variable.
- It provides random access to its elements based on an index.
- The elements in an array are typically stored in contiguous memory locations.
- Arrays can be one-dimensional (a list of elements) or multi-dimensional (e.g., a matrix or a table).
- The `array` module, which provides a more efficient storage and operations for arrays of homogeneous data types can be used to create arrays.

- Arrays are useful for various tasks, including:
1. Storing and manipulating collections of data.
2. Accessing elements by their index for efficient retrieval and modification.
3. Performing mathematical and statistical operations on numerical data.
4. Representing matrices, tables, or other multi-dimensional data structures.
5. Implementing algorithms and data structures that rely on sequential or random access to data.

Example 1: Storing integers in an array
```
import array

# Create an array of integers
my_array = array.array('i', [1, 2, 3, 4, 5])

# Accessing elements
print(my_array[0])  # Output: 1
print(my_array[2])  # Output: 3

# Modifying an element
my_array[1] = 10

# Printing the modified array
print(my_array)  # Output: array('i', [1, 10, 3, 4, 5])
```

Example 2: Storing characters in an array

```
import array

# Create an array of characters
my_array = array.array('c', ['a', 'b', 'c', 'd'])

# Accessing elements
print(my_array[0])  # Output: b
print(my_array[2])  # Output: c

# Modifying an element
my_array[1] = 'x'

# Printing the modified array
print(my_array)  # Output: array('c', ['a', 'x', 'c', 'd'])
```

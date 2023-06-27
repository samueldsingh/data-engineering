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

Accessing elements by index `(my_list[0])`, Slicing `(my_list[1:4])`, Concatenation `(list1 + list2)`, Repetition `(*)`, Length `(len)`, Membership `(in)`, Iteration (for), `max`, `min`, Sorting (`sort` method rearranges the elements of the list in ascending order and `sorted` function creates a new sorted list without modifying the original list), searching (`index` method returns the index of the first occurrence of the element).

## 3. Characteristics(Properties) of List

Lists are mutable, **ordered** (maintain the order of elements as they are inserted and allow indexing), allows duplicates, can store heterogeneous data types, Variable Length (items can be added or removed as needed), iterable, supports sequence operations, inbuilt methods and functions.

4. CRUD operations on List


5. Memory allocation of List


6. Write all possible combinations of list structure(homo,hetero with all data types, data structures)


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
1. **Shallow Copy:** A shallow copy of a list creates a new list object, but the elements of the new list still refer to the same objects as the original list. Any modifications made to the original list or its elements will be reflected in the shallow copy.

Example:
```
original_list = [1, 2, [3, 4]]
shallow_copy = original_list.copy()

# Modify the original list
original_list[0] = 10
original_list[2][0] = 30

print(original_list)  # Output: [10, 2, [30, 4]]
print(shallow_copy)  # Output: [1, 2, [30, 4]]
```

In this example, the `copy()` method creates a shallow copy of the `original_list`. When we modify the element at index `0` in the original list, the change is not reflected in the shallow copy. However, when we modify the nested element at index `0` `(original_list[2][0])`, the change is reflected in both the original list and the shallow copy.

2. **Deep Copy:** A deep copy of a list creates a new list object and recursively creates new copies of all the objects within the original list. The new list and its elements are completely independent of the original list. Modifications made to the original list or its elements will not affect the deep copy.

Example:
```
import copy

original_list = [1, 2, [3, 4]]
deep_copy = copy.deepcopy(original_list)

# Modify the original list
original_list[0] = 10
original_list[2][0] = 30

print(original_list)  # Output: [10, 2, [30, 4]]
print(deep_copy)  # Output: [1, 2, [3, 4]]
```

In this example, the `deepcopy()` function from the `copy` module is used to create a deep copy of the `original_list`. Modifying the elements of the original list does not affect the deep copy. The nested element modification at index `0` is only reflected in the original list, while the deep copy remains unchanged.

In summary, a shallow copy creates a new list with references to the same objects as the original list, while a deep copy creates a new list with completely independent copies of all the objects within the original list. The choice between shallow copy and deep copy depends on your specific requirements and the level of independence needed between the original list and the copied list.

10. append vs extend
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

12. pop vs remove

`pop()` and `remove()` are both methods used to remove elements from a list in Python, but they differ in how they remove the elements:

1. `pop()`: The `pop()` method is used to remove and return an element from a specific index in a list. It modifies the original list by removing the element at the specified index and returning its value.

Example:
```
my_list = [1, 2, 3, 4, 5]
removed_element = my_list.pop(2)
print(my_list)  # Output: [1, 2, 4, 5]
print(removed_element)  # Output: 3
```

In this example, the `pop()` method is used to remove and return the element at index 2 (which is `3`) from the list.

2. `remove()`: The `remove()` method is used to remove the first occurrence of a specific value from a list. It modifies the original list by removing the first occurrence of the specified value.

Example:
```
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list)  # Output: [1, 2, 4, 5]
```

In this example, the `remove()` method is used to remove the first occurrence of the value `3` from the list.

13. Pass by value vs Pass by reference



    iv. Tuple:
          1. What is use of Tuple. Explain different use cases of Tuple
          2. Sequence operations on Tuple
          3. Characteristics(Properties) of Tuple
          4. CRUD operations on Tuple
          5. Memory allocation of Tuple
          6. Write all possible combinations of Tuple structure(homo,hetero with all data types, data structures)
          7. Explain about each function of Tuple
          8. shallow copy vs deep copy in tuple.
          9. list vs tuple ( Min. 4 differences in detail)

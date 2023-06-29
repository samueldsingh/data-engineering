# 1. Dictionary

Sequences follow indexing mechanism but dictionaries use the `item` function to access the key-value pair in a dictionary.`item` function works by converting the 
dictionary into a list of tuples.

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
data[2] = 'Twenty'
data['id'] = 200
print("Dictionary update: ", data)

Output:
```
Dictionary update:  {1: 'One', 2: 'Twenty', 3: 'Two', 'id': 200}
```

### DELETE

1. Delete entire  dict   --> `del dict1`
2. Delete any one item   --> `del dict1['id']`
3. Delete entire items   --> `dict1.clear()`

data = {1: 'One', 2: 'Two', 3: 'Two', 'id': '100'}

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

Dictionaries follow the hashing algorithm. The steps involved in hashing algorithm are:
1. Calculate hashcode of dict key
2. Check if bucket exists or not based on hashkey
3. If bukcet exists, value is stored in the same or else new bucket is created.

## 4. Shallow copy vs deep copy
In shallow copy, changes made to the recursive list will be affected. In deep copy, changes made to the recursive list will not be affected.

In list dictionaries, changes made to the list will not affect original content. Let's compare the memory address after appending an item to the lists, `list1` and `list2`. We can see they have the same memeory address.

```
list1 = [1, 2, 3]
list2 = list1
print("Before :", list1, list2)
print("Address:", id(list1), id(list2))
list2.append(10)
print("After :", list1, list2)
print("Address:", id(list1), id(list2))
```

The output is:
```
Before : [1, 2, 3] [1, 2, 3]
Address: 2022319995328 2022319995328
After : [1, 2, 3, 10] [1, 2, 3, 10]
Address: 2022319995328 2022319995328
```

Let's compare the memory address of two lists, after `list2` is shallow copied from `list1`. 

```
list1 = [1, 2, 3]
list2 = list1.copy()
print("Shallow copy before at Index: ", list1, list2)
print("Shallow copy before at Index: ", id(list1), id(list2))
```

The output is:
```
Shallow copy before at Index:  [1, 2, 3] [1, 2, 3]
Shallow copy before at Index:  2098796181888 2098804765632
```

After `list2` is shallow copied from `list1`, the memory address changes.

Let's append an item to recursive list:

```
list1 = [1, 2, [10, 20]]
list2 = list1.copy()
print("Shallow copy before at recursive: ", list1, list2)
list2[2].append(100)
print("Shallow copy after at recursive : ", list1, list2)
```

The output is:
```
Shallow copy before at recursive:  [1, 2, [10, 20]] [1, 2, [10, 20]]
Shallow copy after at recursive :  [1, 2, [10, 20, 100]] [1, 2, [10, 20, 100]]
```

**Deep copy:**
Let's perform a deep copy before and after at index:
```
import copy
list1 = [1, 2, 3]
list2 = copy.deepcopy(list1)
print("Deep copy before at Index   : ", list1, list2)
list2.append(100)
print("Deep copy after at Index    : ", list1, list2)
print("ID of list1: ", id(list1))
print("ID of list2: ", id(list1))

```

Output:
```
Deep copy before at Index   :  [1, 2, 3] [1, 2, 3]
Deep copy after at Index    :  [1, 2, 3] [1, 2, 3, 100]
ID of list1:  2508988898496
ID of list2:  2508988898496
```

Changes do not affect the original list.

Let's try performing deep copy on a recursive list:
```
import copy
list1 = [1, 2, [10, 20]]
list2 = copy.deepcopy(list1)
print("Deep copy before at recursive: ", list1, list2)
list2[2].append(100)
print("Deep copy after at recursive : ", list1, list2)
```

The output is:
```
Deep copy before at recursive:  [1, 2, [10, 20]] [1, 2, [10, 20]]
Deep copy after at recursive :  [1, 2, [10, 20]] [1, 2, [10, 20, 100]]
```

Let's perform deep copy in dictionaries:
```
di1 = {1: 1, 2: 2}
di2 = di1.copy()
print("-----Before modification-----------")
print("Dict1 copy : ", di1)
print("Dict2 copy : ", di2)
print("-----After modification-----------")
di2['name'] = 'Madhu'
print("Dict1 copy : ", di1)
print("Dict2 copy : ", di2)
```

The output is:
```
-----Before modification-----------
Dict1 copy :  {1: 1, 2: 2}
Dict2 copy :  {1: 1, 2: 2}
-----After modification-----------
Dict1 copy :  {1: 1, 2: 2}
Dict2 copy :  {1: 1, 2: 2, 'name': 'Madhu'}
```

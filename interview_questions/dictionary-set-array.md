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





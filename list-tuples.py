
# I. List properties:
# ==================
# 1. Follows indexing mechanism while storing elements(Sequence)
# 2. List is Mutable ***
# 3. List allows Duplicate elements
# 4. Maintains Insertion order wrt Memory
# 5. List will allow both Homogeneous and Heterogenous data

# When to use list data structure:
# ---------------------------------
# - Handle group of elements
# - Homogeneous/Heterogeneous,
# - Mutable structures **
# - With Duplicate values

# List Properties
# 1. List indexing mechanism

# list1 = [12, 22, 13, 54, 35]
#
# print("List : ", list1)                     #Output: List :  [12, 22, 13, 54, 35]
# print("List : ", list1[1])  # Indexing      #Output: List :  22
# print("List : ", list1[1:2])  # Slicing     #Output: List :  [22]

# 2. List is mutable
# print("----List is MUTABLE-----")  # Insert, Update, Delete ops
#         # 0   1   2   3   4   5
# list1 = [12,  22, 13, 54, 35]
# print("Before list : ", list1)      # Output: Before list :  [12, 22, 13, 54, 35]
# list1[2] = 300   # Update
# print("After list1  : ", list1)     # Output: After list1  :  [12, 22, 300, 54, 35]
# list1.insert(1, 100)
# print("After list2  : ", list1)     # Output: After list2  :  [12, 100, 22, 300, 54, 35]
# del list1[3]
# print("After list3  : ", list1)     # Output: After list3  :  [12, 100, 22, 54, 35]
# del list1

# 3. List will allow both homogeneous and heterogenous data
    # Homogeneous data
# print("----------Homogeneous---------")
# list1 = [1, 2, 3, 4, 5, 6]
# print('Integers is list : ', list1)     # Output: Integers is list :  [1, 2, 3, 4, 5, 6]
#
# list1 = [1.5, 3.2, 5.6, 4.8]
# print('Float is list   : ', list1)      # Output: Float is list   :  [1.5, 3.2, 5.6, 4.8]
#
# list1 = [True, False, True, False]
# print('Boolean is list : ', list1)      # Output: Boolean is list :  [True, False, True, False]

# list1 = ['hello', 'world', 'welcome', 'python']
# print('Strings is list : ', list1)        # Output: Strings is list : ['hello', 'world', 'welcome', 'python']
#
# print("Index value : ", list1[1])         # Output: Index value :  world
# print("Index value : ", list1[1][2])      # Output: Index value :  r
#
# list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print('Lists   in list : ', list1)          # Output: Lists   in list :  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print('Lists   in list : ', list1[0])       # Output: Lists   in list :  [1, 2, 3]
# print('Lists   in list : ', list1[2][0])    # Output: Lists   in list :  7
#
# list1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# print('Tuples  in list : ', list1)          # Output: Tuples  in list :  [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# print('Tuples  in list : ', list1[1])       # Output: Tuples  in list :  (4, 5, 6)
# print('Tuples  in list : ', list1[2][1])    # Output: Tuples  in list :  8
#
# list1 = [{1: 1, 2: 2}, {'id': 100, 'name': 'Sam'}]
# print('Dict is list: ', list1)              # Output: Dict is list:  [{1: 1, 2: 2}, {'id': 100, 'name': 'Sam'}]
#
# list1 = [{1, 2, 3}, {4, 5, 6}]
# print('Set is list: ', list1)              # Output: Set is list:  [{1, 2, 3}, {4, 5, 6}]

    # Heterogeneous data
# list1 = [100, 14.5, False, 'Hello', [1, 2, 3], (1, 2, 3), {1: 1, 2: 2}, {1, 2, 3}]
# print("---Hetero-------", list1)
# list2 = [1, 2, 3]
# list3 = [True, 1, 1.5]

# 4. List allows duplicate elements
# list1 = [10, 10, 20]
# print("Duplicates in list: ", list1)        # Output: Duplicates in list:  [10, 10, 20]

# 5. Maintains Insertion order
# list1 = [1, 2, 3, 4, 5, 6]
# print("Insertion order: ", list1)             # Output: Insertion order:  [1, 2, 3, 4, 5, 6]

# II. Sequence Operations on lists
# 8 important operations: Indexing, Slicing, Adding, Multiplying, Membership, Length, Max, Min
#
# list1 = [12, 22, 13, 54, 35, 76, 14]
# print("List1: ", list1)
#
# # 1. Indexing
# print("List1 1: ", list1[1])                                # Output: List1 1:  22
# print("List1 5,-1: ", list1[5], list1[6], list1[-1])        # Output: List1 5,-1:  76 14 14

# 2. Slicing
# list1 = [12, 22, 13, 54, 35, 76, 14]
# print("Slicing operation: ", list1[2:])             # Output: Slicing operation:  [13, 54, 35, 76, 14]
# print("Slicing operation: ", list1[2:5])            # Output: Slicing operation:  [13, 54, 35]
# print("Slicing operation: ", list1[:5])             # Output: Slicing operation:  [12, 22, 13, 54, 35]
# print("Slicing operation: ", list1[::1])            # Output: Slicing operation:  [12, 22, 13, 54, 35, 76, 14]
# print("Slicing operation: ", list1[::2])            # Output: Slicing operation:  [12, 13, 35, 14]

# 3. Adding
# list1 = [10, 20, 30]
# list2 = [11, 12, 13]
# print("Adding 2 lists:", list1+list2)   # x=10 y= 20   print(x+y)

# 4. Multiplying
# print("Multiply 2 lists :", [1, 2, 3] * 5)      # Output: Multiply 2 lists : [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

# 5. Membership
# print("Check value: ", 1 in [1, 2, 3])          # Output: Check value :  True

# # 6. Length
# list1 = [12, 22, 13, 54, 35, 76, 14]
# print("Length of list1: ", len(list1))            # Output: Length of list1:  7

# 7. Max
# list1 = [12, 22, 13, 54, 35, 76, 14]
# print("Length of list1 : ", max(list1))

# 8. Min
# list1 = [12, 22, 13, 54, 35, 76, 14]
# print("Length of list1 : ", min(list1))

# III. Conversions

# x = 10
# li = list(x)  # string tuple range()  # Hello World
# print("List : ", li) # Not possible

# x = 10
# print("To float: ", float(x), type(x))         # Output: To float:  10.0 <class 'int'>
# x = 10.5
# print("To int: ", int(x), type(x))             # Output: To int:  10 <class 'float'>
# x = 0
# print("To bool: ", bool(x), type(x))           # Output: To bool:  False <class 'int'>
# x = -5
# print("To bool: ", bool(x), type(x))           # Output: To bool:  True <class 'int'>

# x = 12345
# print("To str: ", x, type(x))           # Output: To str:  12345 <class 'int'>
# x = str(x)
# print("To str: ", x, type(x))           # Output: To str:  12345 <class 'str'>

# str1 = 'Hello World'
# print("Convert to list: ", list(str1))    # Output: Convert to list:  ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

# list1 = [1, 2, 3, 4, 5, 6]
# print("List to string : ", list1, type(list1))      # Output: List to string :  [1, 2, 3, 4, 5, 6] <class 'list'>
# st = str(list1)
# print("List to string : ", st, type(st))  # "[1, 2, 3, 4, 5, 6]"        # Output: List to string :  [1, 2, 3, 4, 5, 6] <class 'str'>
#
# list1 = ['1', '2', '3', '4', '5', '6']  # "123456"    "123456"
# num_str = ''.join(list1)   # ''+'1'  '1'+'2' ==>  '123456'
# print(num_str, type(num_str))           # Output: 123456 <class 'str'>
# num_str = ' '.join(list1)
# print(num_str, type(num_str))           # Output: 1 2 3 4 5 6 <class 'str'>
# num_str = '*'.join(list1)
# print(num_str, type(num_str))           # Output: 1*2*3*4*5*6 <class 'str'>

# IV. LIST MUTABILITY
# list1 = [32, 12, 35, 76, 43, 52, 15]
# print("Before list: ", list1, id(list1), id(list1[0]), id(list1[1]), id(list1[2]))           # Output: Before list: [32, 12, 35, 76, 43, 52, 15] 2301454858240 2301452446992 2301452446352 2301452447088
# list1[1] = 1000
# print("After list: ", list1, id(list1), id(list1[0]), id(list1[1]), id(list1[2]))            # Output: After list: [32, 1000, 35, 76, 43, 52, 15] 2301454858240 2301452446992 2301454940624 2301452447088
# list1.insert(1, 22)
# print("After list: ", list1, id(list1), id(list1[0]), id(list1[1]), id(list1[2]))            # Output: After list: [32, 22, 1000, 35, 76, 43, 52, 15] 2301454858240 2301452446992 2301452446672 2301454940624

# V. CRUD OPERATIONS

# 1. CREATE
# list1 = [1, 2, 3, 4, 5, 6]
#
# list1 = [1, 2, [30, 40, 50], (11, 22, 33), {1, 2, 3}, {1: 100, 2: 200}]

# # 2. RETRIEVE
# print('List values1: ', list1)              # Output: List values1:  [1, 2, [30, 40, 50], (11, 22, 33), {1, 2, 3}, {1: 100, 2: 200}]
# print('List values2: ', list1[2])           # Output: List values2:  [30, 40, 50]
# print('List values21: ', list1[2][1])       # Output: List values21:  40

# 3. UPDATE
# list1[1] = 200
# print('List values2 : ', list1)               # Output: List values2 :  [1, 200, [30, 40, 50], (11, 22, 33), {1, 2, 3}, {1: 100, 2: 200}]

# 4. DELETE
# del list1[2]
# print('List values3 : ', list1)
# del list1
# # print('List values4 : ', list1)

# a = list(input("Enter list : "))   # [1,2,3]
# print(a)                                                # Output: ['1', '2', '3', '4']
# print([int(x) for x in list("1234")])                   # Output: [1, 2, 3, 4]
# st = '[1,2,3,4]'
# li2 = []
# for val in st:  # '1' '2' '3' '4'
#     if val.isnumeric():
#         val = int(val)
#         li2.append(val)
# print(li2)                                              # Output: [1, 2, 3, 4]
# print([x for x in list()])                              # Output: []

# li = list("1234")
# print(li)                   # Output: ['1','2','3','4']
# li[0] = li[1] = 5           # Output: [5,5,'3','4']
# print(li)

# VI. LIST FUNCTIONS

# # Builtin functions:
# ---------------------
# append insert extend   : UPDATE
# pop  remove            : DELETE
# count                  : RETRIEVE
# index                  : RETRIEVE
# reverse                : UPDATE
# sort                   : UPDATE
# copy                   : CREATE

# list1 = [1, 2, 3, 4, 5, 6, 5, 5, 6]
#
# list1 = [1, 2, 3, 4, 5, 6]
# print("Before append : ", list1)            # Output: Before append :  [1, 2, 3, 4, 5, 6]
# list1.append(10)
# print("After append  : ", list1)            # Output: After append  :  [1, 2, 3, 4, 5, 6, 10]
# list1.append([10, 20, 30])
# print("After append  : ", list1)            # Output: After append  :  [1, 2, 3, 4, 5, 6, 10, [10, 20, 30]]

# for ind, val in enumerate(list1):
#     print(ind, "----", val)
#
# print("After append  :", list1)
#
# Output:
# 0 ---- 1
# 1 ---- 2
# 2 ---- 3
# 3 ---- 4
# 4 ---- 5
# 5 ---- 6
# 6 ---- 5
# 7 ---- 5
# 8 ---- 6
# After append  : [1, 2, 3, 4, 5, 6, 5, 5, 6]

# list1 = [1, 2, 3]
# list1.append(5)
# list1.append({1: 1, 2: 2})
# list1.extend([])
# print(list1)

# list1 = [1, 2, 3]
# print("Before list : ", list1)
# list1.extend([4, 5, 6])
# print("After list : ", list1)           # After list :  [1, 2, 3, 4, 5, 6]

# ======================================================================================

## TUPLE

# I. MEMORY ALLOCATION

# x = 10              # write operation  CREATE
# print(x)            # read operation  RETRIEVAL/READ
# print(20)
# print(10+20)
# li = [1]
# li1 = [1, 2, 3, 4]     # Mutable  :  Modifications
# tup1 = (1, 2, 3, 4)    # Immutable:  No Modifications
# print(tup1, type(tup1))         # Output: (1, 2, 3, 4) <class 'tuple'>

# tup1 = ()
# print("Empty tuple1 :", tup1, type(tup1))           # Output: Empty tuple1 : () <class 'tuple'>
#
# tup1 = (1)
# print("Empty tuple2 :", tup1, type(tup1))           # Output: Empty tuple2 : 1 <class 'int'>
#
# tup1 = (1,)
# print("Empty tuple :", tup1, type(tup1))            # Output: Empty tuple : (1,) <class 'tuple'>

# II. SEQUENCE OPERATION ON TUPLES
#
# Sequence operations on tuple involve:
# Indexing, Slicing, Adding, Multiplying, Membership, length, max, min

# tup1 = (1, 2, 3, 4, 5, 6, 7)
#
# # 1. Indexing # RETRIEVAL
# print("Indexing : ", tup1[2])       # Output: Indexing :  3
#
# # 2. Slicing
# print("Slicing : ", tup1[0:2])      # Output: Slicing :  (1, 2)

# # 3. Adding
# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
# print("Tuple1 : ", t1)              # Output: Tuple1 :  (1, 2, 3)
# print("Adding : ", t1 + t2)  # One time usage  (1,2,3,4,5,6)            # Output: Adding :  (1, 2, 3, 4, 5, 6)
# t1 = t1 + t2
# print("Tuple1 : ", t1)   # 2 or more times                              # Output: Tuple1 :  (1, 2, 3, 4, 5, 6)

# # 4. Multiplying
# t1 = (1, 2, 3)
# print("Mulitiply : ", t1*3)         # Output: Mulitiply :  (1, 2, 3, 1, 2, 3, 1, 2, 3)

# # 5. Membership
# t1 = (1, 2, 3, 4)
# print("Membership : ", 1 in t1)         # Output: Membership :  True
# print("Length : ", len(t1))             # Output: Length :  4
# print("Max : ", max(t1))                # Output: Max :  4
# print("Min : ", min(t1))                # Output: Min: 1
#
# original_list = [1, 2, [3, 4]]
# shallow_copy = original_list.copy()
#
# # Modify the original list
# original_list[0] = 10
# original_list[2][1] = 40
#
# print(original_list)  # Output: [10, 2, [30, 4]]
# print(shallow_copy)  # Output: [1, 2, [30, 4]]

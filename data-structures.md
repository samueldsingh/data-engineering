### Tasks:
-------------
1. Store 5 students information like sid,name, age, marks, school_name, gender using Data Structure
2. Store 10 states of country India 
3. Store 10 employee ids of a company 
4. Store marks of 10 students with their name and employee id.
5. Take any 3 random invoices(like current bill) and store all attributes using data structure



### 1. Store 5 students information like sid,name, age, marks, school_name, gender using Data Structure

   You can utilize data structures like lists or dictionaries and iterate over the data input using loops. To
store data use a loop such as:

```
students = []  # Empty list to store student information

num_students = int(input("Enter the number of students: "))

for i in range(num_students):
    student = {}  # Empty dictionary to store information for each student
    
    print(f"\nEnter information for Student #{i+1}:")
    student['sid'] = input("Enter Student ID: ")
    student['name'] = input("Enter Name: ")
    student['age'] = int(input("Enter Age: "))
    student['marks'] = float(input("Enter Marks: "))
    student['school_name'] = input("Enter School Name: ")
    student['gender'] = input("Enter Gender: ")
    
    students.append(student)  # Add the student information dictionary to the list

# Printing the stored student information
print("\nStudent Information:")
for i, student in enumerate(students):
    print(f"\nStudent #{i+1}:")
    print("Student ID:", student['sid'])
    print("Name:", student['name'])
    print("Age:", student['age'])
    print("Marks:", student['marks'])
    print("School Name:", student['school_name'])
    print("Gender:", student['gender'])

for i in students:
    print(i)
```

The output is:
```
{'sid': '1', 'name': 'Samuel', 'age': 21, 'marks': 80.0, 'school_name': 'SHUATS', 'gender': 'M'}
{'sid': '2', 'name': 'Benjamin', 'age': 21, 'marks': 90.0, 'school_name': 'SHUATS', 'gender': 'M'}
```

### 2. Store 10 states of country India

   You can utilize data structures like lists or dictionaries and iterate over the data input using loops. To
store data use a loop such as:

```
states = []  # Empty list to store student information

num_states = int(input("Enter the number of states: "))

for i in range(num_states):
    state = {}

    print(f"\nEnter information for State #{i + 1}:")
    state['name'] = input("Enter State Name: ")
    state['capital'] = input("Enter Capital Name: ")

    states.append(state)  # Add the student information dictionary to the list

# Printing the stored state information
print("\nState Information:")
for i, state in enumerate(states):
    print("The Capital of ", state['name'], "is", state['capital'])
```

The output is:
```
State Information:
The Capital of  Karnataka is Bangalore
The Capital of  Tamil Nadu is Chennai
```

### Another Approach:
### Create a dictionary to store the states and their capitals
```
states = {
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun",
    "West Bengal": "Kolkata"
}
```

### Print the states and their capitals
```
for state, capital in states.items():
    print(f"The capital of {state} is {capital}")
```

The output is:
```
The capital of Sikkim is Gangtok
The capital of Tamil Nadu is Chennai
The capital of Telangana is Hyderabad
The capital of Tripura is Agartala
The capital of Uttar Pradesh is Lucknow
The capital of Uttarakhand is Dehradun
The capital of West Bengal is Kolkata
```
This program uses a dictionary called states to store the names of Indian states as keys and their respective capital cities as values. It then iterates over the dictionary using a for loop and prints the state-capital pairs. You can add or remove states as needed to customize the dictionary.

### 3. Store marks of 10 students with their name and student_id.
```
students = []  # Empty list to store student information

num_students = int(input("Enter the number of students: "))

for i in range(num_students):
    student = {}  # Empty dictionary to store information for each student
    
    print(f"\nEnter information for Student #{i+1}:")
    student['sid'] = input("Enter Student ID: ")
    student['name'] = input("Enter Name: ")
    
    students.append(student)  # Add the student information dictionary to the list

# Printing the stored student information
print("\nStudent Information:")
for i, student in enumerate(students):
    print(f"\nStudent #{i+1}:")
    print("Student ID:", student['sid'])
    print("Name:", student['name'])

for i in students:
    print(i)
```

The output is:
```
Student Information:

Student #1:
Student ID: 1
Name: Samuel

Student #2:
Student ID: 2
Name: Ashwin
```

#### Write a python program to print list, tuples, sets
```
list = []  # Empty list to store a number

number = int(input("Enter how many values you want in the list: "))

for i in range(number):
    numbers = input("Enter a value to append: ")
    list.append(numbers)


print("The list:", list)
print("The tuple:", tuple(list))
print("The set:", set(list))
```

The output is:
```
Enter how many values you want in the list: 5
Enter a value to append: 1
Enter a value to append: 2
Enter a value to append: 3
Enter a value to append: 4
Enter a value to append: 5

The list: ['1', '2', '3', '4', '5']
The tuple: ('1', '2', '3', '4', '5')
The set: {'2', '5', '1', '4', '3'}
```

```
dict = {}
number=int(input("Enter how many values you want: "))
for i in range(number):
    dict[i] = i*2

print("The Dictionary:", dict)
```

The output is:
```
Enter how many values you want: 5
The Dictionary: {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
```

Questions:
--------------
1. Variables. Explain in detail 
2. Tokens in python 
3. Implicit casting vs Explicit casting 
4. Type promotion 
5. Explain about each function 
	print type id int float bool str list tuple dict set 
6. == vs is 
7. Difference between and or operators. Any two realtime examples 
8. Keywords in python


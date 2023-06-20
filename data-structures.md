Tasks:
-------------
1. Store 5 students information like sid,name, age, marks, school_name, gender using Data Structure
2. Store 10 states of country India 
3. Store 10 employee ids of a company 
4. Store marks of 10 students with their name and employee id.
5. Take any 3 random invoices(like current bill) and store all attributes using data structure



1. Store 5 students information like sid,name, age, marks, school_name, gender using Data Structure

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

print(students)
```

The output is:
```
[{'sid': '1', 'name': 'Samuel', 'age': 21, 'marks': 90.0, 'school_name': 'SHUATS', 'gender': 'M'}, {'sid': '2', 'name': 'Benjamin', 'age': 21, 'marks': 95.0, 'school_name': 'SHUATS', 'gender': 'M'}, {'sid': '3', 'name': 'Ashwin', 'age': 21, 'marks': 85.0, 'school_name': 'SHUATS', 'gender': 'M'}, {'sid': '4', 'name': 'Kamlesh', 'age': 21, 'marks': 75.0, 'school_name': 'SHUATS', 'gender': 'M'}, {'sid': '5', 'name': 'Aslam', 'age': 21, 'marks': 80.0, 'school_name': 'SHUATS', 'gender': 'M'}]
```

2. Store 10 states of country India

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


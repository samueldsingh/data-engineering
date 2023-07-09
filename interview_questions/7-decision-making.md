# VII. Decision Making:
=====================
## 1. What is Decision Making. Explain different scenarios when to go for Decision Making
Decision making in Python refers to the process of selecting different paths of execution based on certain conditions or criteria. It allows your program to make choices and perform specific actions based on the evaluation of one or more conditions. Decision-making constructs in Python include if-else statements, elif statements, and switch-case statements (implemented using if-elif-else). Here are different scenarios when decision-making constructs are commonly used:

1. Conditional Execution:
   - Decision-making constructs are used when you want to execute a block of code only if a certain condition is satisfied.
   - Example:
     ```python
     x = 5
     if x > 0:
         print("Positive number")
     ```

2. Multiple Conditional Branches:
   - Decision-making constructs with multiple conditions allow you to choose from several possible execution paths based on different conditions.
   - Example:
     ```python
     x = 5
     if x > 0:
         print("Positive number")
     elif x < 0:
         print("Negative number")
     else:
         print("Zero")
     ```

3. Nested Decision Making:
   - Decision-making constructs can be nested to handle more complex scenarios with multiple levels of conditions and sub-conditions.
   - Example:
     ```python
     x = 10
     if x > 0:
         if x < 100:
             print("x is a positive number less than 100")
         else:
             print("x is a positive number greater than or equal to 100")
     else:
         print("x is either zero or a negative number")
     ```

4. Boolean Conditions:
   - Decision-making constructs can evaluate boolean expressions, allowing you to perform actions based on the logical result of the condition.
   - Example:
     ```python
     x = 5
     y = 10
     if x > 0 and y > 0:
         print("Both x and y are positive")
     ```

5. User Input Validation:
   - Decision-making constructs are commonly used to validate user input and provide appropriate feedback or error handling.
   - Example:
     ```python
     age = int(input("Enter your age: "))
     if age >= 18:
         print("You are eligible to vote")
     else:
         print("You are not eligible to vote")
     ```

6. Program Flow Control:
   - Decision-making constructs are essential for controlling the flow of a program based on different conditions, enabling more dynamic and responsive behavior.
   - Example:
     ```python
     is_logged_in = False
     if is_logged_in:
         # Perform actions for logged-in users
     else:
         # Perform actions for non-logged-in users
     ```

In summary, decision-making constructs allow you to make choices and perform specific actions based on conditions. They are used in various scenarios where the execution of code needs to be determined dynamically based on different criteria. Decision-making constructs provide flexibility and control over program flow, enabling you to handle different scenarios and make your code more responsive and intelligent.

## 2. Give examples for below conditions

Sure! Here are examples for each of the conditions you mentioned:

1. Single if:
   ```python
   age = 20
   if age >= 18:
       print("You are eligible to vote")
   ```

2. if-else:
   ```python
   age = 15
   if age >= 18:
       print("You are eligible to vote")
   else:
       print("You are not eligible to vote")
   ```

3. if-elif-else:
   ```python
   grade = 75
   if grade >= 90:
       print("You achieved an A grade")
   elif grade >= 80:
       print("You achieved a B grade")
   elif grade >= 70:
       print("You achieved a C grade")
   else:
       print("You need to improve your grade")
   ```

4. if-elif-elif-else:
   ```python
   month = 6
   if month == 12:
       print("It's December")
   elif month == 1:
       print("It's January")
   elif month == 2:
       print("It's February")
   else:
       print("It's some other month")
   ```

5. Nested if:
   ```python
   age = 25
   if age >= 18:
       print("You are eligible to vote")
       if age >= 65:
           print("You are also eligible for senior citizen benefits")
   else:
       print("You are not eligible to vote")
   ```

These examples demonstrate different scenarios of using conditional statements in Python. The single if statement is used when there is a single condition to be evaluated. The if-else construct allows for different actions to be taken based on whether a condition is true or false. The if-elif-else construct is used when there are multiple conditions to be evaluated in a sequential manner. The if-elif-elif-else construct expands on this by including additional elif (else if) conditions. Finally, nested if statements are used when conditions need to be evaluated within the scope of another if statement.

## 3. Prepare Programs for below questions
	1. Prepare state and assign North South West East 
	    north = []
		south = ['Andhra Prades', 'Telangana', 'Karnataka','Tamil Nadu', 'Kerala']
		west = []
		east = []
	2. Prepare dictionary with key as state name and value as "list of districts"

Sure! Here are the programs for the given questions:

1. Program to Assign States:
```python
north = []
south = ['Andhra Pradesh', 'Telangana', 'Karnataka', 'Tamil Nadu', 'Kerala']
west = []
east = []

print("North States:", north)
print("South States:", south)
print("West States:", west)
print("East States:", east)
```

2. Program to Create Dictionary of States and Districts:
```python
state_districts = {
    'Andhra Pradesh': ['Visakhapatnam', 'Vijayawada', 'Guntur'],
    'Telangana': ['Hyderabad', 'Warangal', 'Karimnagar'],
    'Karnataka': ['Bangalore', 'Mysore', 'Hubli'],
    'Tamil Nadu': ['Chennai', 'Coimbatore', 'Madurai'],
    'Kerala': ['Thiruvananthapuram', 'Kochi', 'Kozhikode']
}

# Accessing the dictionary
for state, districts in state_districts.items():
    print("State:", state)
    print("Districts:", districts)
    print()
```

These programs address the given questions. The first program assigns the states to their respective regions (North, South, West, and East) by initializing empty lists and populating the 'south' list with some sample states. The program then prints the states assigned to each region.

The second program creates a dictionary called 'state_districts', where the state names are used as keys, and the corresponding district names are stored as values in a list. The program then accesses the dictionary and prints the state along with its associated districts.


## 4. Get employee details(in dict format, empid,name,sal, exp) and update hike for employee with below 
		If exp is 0 to 2 years - 10% Hike
				  2 to 5 years - 20% Hike
				  5 to 8 years - 30% Hike
				  8+           - No hike


Here's a program that takes employee details in dictionary format, calculates the hike based on their experience, and updates the salary accordingly:

```python
employee_details = {
    'empid': 'E001',
    'name': 'John Doe',
    'sal': 50000,
    'exp': 4
}

exp = employee_details['exp']
sal = employee_details['sal']

if exp >= 0 and exp <= 2:
    hike = 0.1  # 10% hike
elif exp > 2 and exp <= 5:
    hike = 0.2  # 20% hike
elif exp > 5 and exp <= 8:
    hike = 0.3  # 30% hike
else:
    hike = 0  # No hike

new_salary = sal + (sal * hike)
employee_details['sal'] = new_salary

print("Employee Details:")
print("Employee ID:", employee_details['empid'])
print("Name:", employee_details['name'])
print("Experience:", employee_details['exp'], "years")
print("Old Salary:", sal)
print("Hike:", str(int(hike * 100)) + "%")
print("New Salary:", new_salary)
```

In this program, we take the employee details (empid, name, sal, exp) in a dictionary called `employee_details`. The `exp` represents the experience in years, and `sal` represents the current salary.

Based on the value of `exp`, we calculate the hike percentage (`hike`) according to the given conditions. Then, we calculate the new salary (`new_salary`) by adding the hike amount to the current salary.

Finally, we print the updated employee details, including the old salary, hike percentage, and the new salary.

You can modify the employee details in the `employee_details` dictionary to test different scenarios and see how the program calculates the hike based on experience.

## 5. Explain below terms in detail 
	- Requirement
	- User Criteria
	- Validations(Client vs Server)

1. Requirement:
   A requirement is a specific statement or description of a capability, feature, or functionality that a software system or product should possess. Requirements define what the system should do or how it should behave to meet the needs of its users or stakeholders. They serve as the foundation for software development, providing guidance for design, implementation, and testing.

   Requirements can be categorized into various types, including functional requirements (what the system should do), non-functional requirements (quality attributes like performance, security, usability), and constraints (limitations or conditions imposed on the system).

   Requirements are typically gathered through requirements elicitation techniques such as interviews, workshops, surveys, and analysis of existing systems or documents. They are documented in requirement specifications or user stories, and they form the basis for system design, development, and validation.

2. User Criteria:
   User criteria, also known as user requirements or user needs, are specific expectations or conditions that users have for a software system or product. They represent the desired functionalities, features, or qualities that users want to see in the system to fulfill their needs or address their problems.

   User criteria are captured by understanding and analyzing the perspectives, preferences, and goals of the users or stakeholders. They are essential for designing user-centric systems that meet user expectations and provide a positive user experience. User criteria can include both functional and non-functional aspects, such as desired features, user interface preferences, performance expectations, ease of use, and compatibility with existing systems.

   User criteria are often expressed through user stories, use cases, or personas, which help to communicate and prioritize user needs during the software development process. They provide a user-centered focus and drive the design and implementation decisions of the system.

3. Validations (Client vs Server):
   Validations refer to the process of checking the correctness, integrity, and consistency of data or inputs provided to a software system. Validations ensure that the entered data meets certain criteria, rules, or constraints to maintain data quality and prevent errors or unexpected behavior.

   Validations can be performed at different levels, including client-side and server-side:

   - Client-side validations: These validations are performed on the client-side (usually in the user's web browser) before sending data to the server. They help improve the user experience by providing immediate feedback and reducing unnecessary server requests. Client-side validations often involve validating input formats, checking field lengths, and enforcing data constraints in real-time.

   - Server-side validations: These validations are performed on the server-side after receiving data from the client. They provide an additional layer of security and integrity by validating the data independently on the server. Server-side validations are crucial because client-side validations can be bypassed or manipulated by malicious users. They involve more comprehensive checks, such as business rule validations, database integrity validations, and cross-field or cross-entity validations.

   It is important to note that while client-side validations enhance user experience and provide immediate feedback, server-side validations are essential for data integrity and security. A well-designed system includes both client-side and server-side validations to ensure data correctness and protect against malicious or erroneous inputs.

Validations play a critical role in maintaining the reliability, usability, and security of software systems by ensuring that data meets the specified criteria and constraints. They help prevent data inconsistencies, improve user experience, and safeguard the system against potential vulnerabilities.

6. State vs Behavior . Examples

State and behavior are fundamental concepts in object-oriented programming that help describe the characteristics and actions of objects. Let's explore each concept and provide examples:

1. State:
   State refers to the data or attributes that describe the current condition or characteristics of an object. It represents the values held by an object's variables at a given point in time. State is associated with the object's properties, which can be accessed and modified as needed. In other words, state defines the "what" of an object.

   Example:
   Consider a class named "Car." The state of a car object may include attributes such as "color," "make," "model," and "currentSpeed." These attributes hold specific values that describe the car's characteristics. For instance:
   ```python
   class Car:
       def __init__(self, color, make, model):
           self.color = color
           self.make = make
           self.model = model
           self.currentSpeed = 0

   myCar = Car("Blue", "Toyota", "Camry")
   print(myCar.color)  # Output: Blue
   ```

   In this example, the attributes "color," "make," "model," and "currentSpeed" represent the state of the car object. The values assigned to these attributes provide information about the car's color, make, model, and its current speed.

2. Behavior:
   Behavior refers to the actions or operations that an object can perform. It describes how an object can interact with its environment or other objects. Behavior is associated with the object's methods or functions, which define the actions that can be performed on the object. In other words, behavior defines the "what it can do" of an object.

   Example:
   Continuing with the "Car" class example, the behavior of a car object may include methods such as "accelerate," "brake," and "turn." These methods define the actions that a car object can perform. For instance:
   ```python
   class Car:
       def __init__(self, color, make, model):
           self.color = color
           self.make = make
           self.model = model
           self.currentSpeed = 0

       def accelerate(self, speed):
           self.currentSpeed += speed

       def brake(self):
           self.currentSpeed = 0

   myCar = Car("Blue", "Toyota", "Camry")
   myCar.accelerate(50)
   print(myCar.currentSpeed)  # Output: 50
   myCar.brake()
   print(myCar.currentSpeed)  # Output: 0
   ```

   In this example, the methods "accelerate" and "brake" define the behavior of the car object. The "accelerate" method increases the current speed of the car by a given value, while the "brake" method sets the current speed to zero.

By separating state and behavior, object-oriented programming enables the creation of reusable and modular code. Objects can maintain their individual state while exhibiting consistent behavior across different instances. This distinction between state and behavior helps in designing and modeling complex systems, allowing objects to interact and collaborate effectively.

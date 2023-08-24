
## Why OOPs?

Everthing is an object in Python. It focuses on the design and manipulation of objects to solve complex problems in a more modular and organized way.
- Classes: Classes are blueprints or templates for creating objects. They define the attributes (data) and methods (functions) that the objects will have.
- Objects: Objects are instances of classes. They represent real-world entities and encapsulate both data and behavior
- OOPs enable:
  - Encapsulation: Bundling the attributes and methods into a common unit
  - Inheritance: child class inherits properties and methods of a parent class
  - Polymorphism: allows objects of different classes to be treated as objects of a common base class.
  - Abstraction: enforce specific structure and behavior in the subclasses using abstract methods (methods without implementation). Ensure certain methods are
    available in all derived classes.
- OOPs is mainly used for modularity, reusability, collaboration, modelling real world systems and extensibility.

## 1. Using OOPs

The three steps used while working with OOPs is:
- Step 1: Defining Class
- Step 2: Create object: Initialization of State
- Step 3: Method Call

```
\\Step1: Defining Class
class Employee:
    # State
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal
    # Behavior
    def get_einfo(self):
        print(self.name, "with employee ID,", self.eid, "has salary", self.sal, ".")

\\Step2: Create object: Initialization of State**
samuel = Employee(100, "Samuel David", 50000)

\\Step3: Method Call**
samuel.get_einfo()

The output is:
Samuel David with employee ID 100 has salary 50000
```

```
# Updating marks using OOPs
# Step1: Create Class
class Student:
    # State
    def __init__(self, sid, name, marks):
        self.sid = sid
        self.name = name
        self.marks = marks
    # Behavior
    def get_sinfo(self):
        print("Student Information: ", self.sid, self.name, self.marks)

    def update_marks(self, val):
        self.marks = val

    def del_marks(self):
        self.marks = None

# Step2: Create Object
samuel = Student(100, "Samuel DS", 65)

# Step3: Method Call
samuel.get_sinfo()
samuel.update_marks(90)
samuel.get_sinfo()
samuel.del_marks()

The output is:
Student Information:  100 Samuel DS 65
Student Information:  100 Samuel DS 90
Student Information:  100 Samuel DS None
```

Update Example:
```
class Student:
    # State
    def __init__(self, sid, name, marks):
        self.sid = sid
        self.name = name
        self.marks = marks
    # Behavior
    def get_sinfo(self):
        print("Student info : ", self.sid, self.name, self.marks)

    def get_result(self):
        if self.marks >= 35:
            print("Result : PASS : ", self.name)
        else:
            print("Result :FAIL  : ", self.name)

    def update_name(self):
        self.name = "Samuel David Singh"

The output is:
Student info :  100 Samuel DS 56
Before update :  None
Student info :  100 Samuel David Singh 56
After update :  None
```

## Object creation:

During object creation,

- Python will load class Employee
- It will call init method and passes arguments (wrapper_addr, other args)
- Inside init, data will be initialized using self variable 
- self address will be given to object 

## Method call:

During method call, python follows the following sequence:

- Python will find type of object (`samuel.get_einfo()`: samuel is of type employee class)
- It will go to the class and will check whether method exists or not.
- It will call method by passing samuel object to self parameter(samuel obj addr to self)
- Method execution will happen

## Print employee salary hike with OOPs and without OOPs

```
# Without OOPs
emp_id = 100
emp_name = 'Samuel DS'
e_sal = 10000

# BEHAVIOR
def get_edata(eid, name, sal):
    sal = sal + sal*10/100
    print("Employee after Hike :", eid, " - ", name, " - ", sal)

get_edata(emp_id, emp_name, e_sal)

## Output is:
Employee after Hike : 100  -  Samuel DS  -  11000.0
```


```
# With OOPs

class Employee:
    # STATE  can be achieved by defining Fields
    def __init__(self, eid, ename, sal, address):  # parameters
        self.eid = eid      # RHS --> Local variables eid,name,sal
        self.ename = ename  # LHS --> Instance variables*  self.eid, self.ename,self.sal
        self.sal = sal      # self -> Instance/Object/Reference
        self.address = address

    def update_address(self, new_addr):
        self.address = new_addr

    # BEHAVIOR  # Methods
    def update_sal(self, rating):
        print("Employee info during joining :", self.eid, " - ", self.ename, " - ", self.sal)
        if rating >= 3:
            self.sal += self.sal*30/100  # self.sal = self.sal + self.sal*30/100
        elif rating >= 2:
            self.sal += self.sal * 20/100
        else:
            self.sal += self.sal * 10/100
        print("Employee info after 1 year   :", self.eid, " - ", self.ename, " - ", self.sal)

# object creation
samuel = Employee(100, 'Samuel DS', 10000, '')  # samuel - object*/reference/instance  RHS - Object creation
samuel.update_address("ITPL, Whitefield")
samuel.update_sal(3)

The output is:
Employee info during joining : 100  -  Samuel DS  -  10000
Employee info after 1 year   : 100  -  Samuel DS  -  13000.0
```

## 2. SELF- Object Creation

The `init` method helps to construct object by initializing the data.

Step 1: 

Object creation : 2 parts : 
1. Employee  
2. (100, 'Samuel DS', 10000)

Step 2: 

Python will check and find the address of Employee

Step 3: 
- First python creates empty object(wrapper) of Employee class
- Employee class `__init__` method will be called, 
        passes 
                1. Address of empty object to self parameter         ==> self
                2. the tuple of arguments will be passed to remaining parameters  ==> (eid, name, sal) 

Step 4: Data passes to local variables (eid, name, sal)               

Step 5:         
```
self.eid = 100             LHS eid = instance variable, RHS eid = local variable
self.name = 'Samuel DS'
self.sal = '10000'
                                                 
==> Local variable eid data,we are setting to instance variable 
```

Step 6: 

Once object construction is done, address will be given to variable `(samuel)`        

Note:
-  Inside object data will be initialized.
- `__init__` method helps to initialize the STATE of object(instance)


## 3. Fields & Methods

- The state of a class is represented by the fields (Instance variables, Class variables)
- The behavior of a class is represented by the Methods (Instance Method, Class Method, Static Method)

## 4. Constructors

## 5. OOPs features

- Encapsulation (Binding Data Members and Member Methods into Single entity).
- Inheritance (super class, sub class mechanism).
- Polymorphism (Method Overloading using Static Polymorphism and Method Overriding using Dynamic Polymorphism).
- Abstraction (Hiding the implementation details in the methods of  a class). 
- In normal class, abstraction is 0%. In abstract class, it's between 0-100%. In interface, abstraction is 100%.

`setter`, `getter`, `hasattar`, `delattar` on class and objects

## 5.1 Encapsulation

## 5.2 Inheritance



## 5.3 Polymorphism

## 5.4 Abstraction


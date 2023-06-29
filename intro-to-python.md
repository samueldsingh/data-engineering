# What is Python? What are the advantages and disadvantages of Python? Where is it used?

- It is a high level (user-friendly), object-oriented, interpreted and general purpose programming language known for its simplicity, readability, versatility and reuseability. 
- It is often classified as a "scripting language" (used to manipulate, customize, and automate the facilities of an existing system) and is considered similar to languages such as Perl, Tcl, or Ruby. The syntax of Python is loosely inspired by elements of C programming.
- It is popular due to its clean and easy-to-understand syntax, which emphasizes code readability.
- It offers a wide range of built-in functions and libraries that make it efficient for various programming tasks.
- Python can be used for a wide range of applications, including web development, data analysis, scientific computing, artificial intelligence, machine learning, automation, and more. 
- Python programs consist of statements and expressions that define the logic and behavior of the program. 
- These programs can include control structures like loops and conditionals, data structures like lists and dictionaries, functions and classes for code organization and reusability, as well as modules and packages for code modularization and sharing.
- Its extensive standard library and third-party packages make it capable of handling a wide variety of programming tasks efficiently and effectively.

## Why Python is an Interpreted Language?
Python is often referred to as an interpreted language because it uses an interpreter to execute code directly, without the need for prior compilation into machine code. Here are a few reasons why Python is considered an interpreted language:

- Readability and Simplicity: Python emphasizes code readability and simplicity, and being an interpreted language aligns with these principles. Python code is written in a more human-readable format, which makes it easier for developers to write, understand, and modify.

- Dynamic Typing: Python is dynamically typed, meaning you **don't need to explicitly declare variable types**. The interpreter determines the type of a variable at runtime based on the assigned value. This flexibility is possible because the interpreter can evaluate and handle type information dynamically.

- Rapid Development: Interpreted languages like Python are known for their faster development cycle. Since there is no separate compilation step, developers can write code and immediately execute it. This facilitates faster iteration and prototyping, making Python suitable for rapid application development.

- Interactive Shell: Python provides an interactive shell, also known as a REPL (Read-Evaluate-Print Loop). The Python interpreter allows users to **interactively experiment with code, enter statements, and immediately see the results. This interactive nature is particularly useful for testing and exploring code snippets**.

Portability: Python's interpreted nature contributes to its portability. Python programs can run on any platform or operating system that has a compatible Python interpreter installed, without the need for recompilation. This enables code portability and simplifies the process of sharing and distributing Python applications.

While Python is primarily interpreted, it does have an optional compilation step. Python code can be compiled into bytecode, which is then executed by the interpreter. This bytecode compilation improves performance and enables distribution of compiled Python programs. However, this compilation step is transparent to the developer and handled automatically by the interpreter or tools like Just-In-Time (JIT) compilers.

## Entity, Attributes, Values, Datatypes

**Entity**: Represents real world object or concept that you want to model in your program. 
- It can be a person, a place, a thing, or an abstract concept. In programming, entities are typically represented as **objects or instances of classes**.

**Attributes**: Attributes are characteristics or properties associated with an entity. 
- They describe the state or features of an entity. 
- For example, if you have an entity representing a person, attributes could include name, age, height, and so on. 
- In Python, attributes can be represented as **variables or fields within a class or as properties associated with an object**.

**Values**: Values are the actual data assigned to attributes. They represent specific instances or data points for a given attribute. 
- For example, the attribute "name" of a person entity can have a value like "John," while the attribute "age" can have a value like 25. 
- Values can be of various types, such as numbers, strings, booleans, or more complex types like lists or dictionaries.

**Data Types**: Data types define the nature and behavior of values in a programming language. 
- In Python, data types specify the kind of data that a variable or attribute can hold. 
- Some commonly used data types in Python include:
```Numeric: int, float, string, boolean, 
Text Type: string (sequence of characters),
Boolean Types: bools (logical operations like True or False),
Sequence Types: List (ordered collection in square brackets), Tuple ( ordered collection in parenthesis), Range (sequence of numbers used in loops)
Mapping Type: Dictionary (collection of key-value pairs enclosed in curly braces)
Set Types: set (unordered collection of unique elements, enclosed in curly braces), frozenset (immutable sets)
Binary Types: bytes (sequence of bytes), bytearray (mutable sequence of bytes)
Other Types: NoneType (null value), complex (numbers with real and imaginary parts)
```

## 50 examples of an entity along with their attribute, value and data type
**States** represent the attribute and property of an entity. It describes the current condition or characteristics of the entity. 

The **behavior** of an entity represents the actions or operations that the entity can perform. Behavior is typically implemented as methods or functions associated with the object. Examples of behavior for a "Car" entity could include starting the engine, accelerating, braking, changing gears, turning, and stopping.

**CRUD Operations:** CRUD stands for Create, Read, Update, and Delete, which are the basic operations performed on data in most applications. These operations allow you to interact with a database or any other data storage system. 

**Create:** In Python, you typically need to connect to a database using a database driver or an ORM (Object-Relational Mapping) library like SQLAlchemy. Using appropriate functions and methods, you can create or insert records into the database.

```
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define a database engine and session
engine = create_engine('sqlite:///mydatabase.db')
Session = sessionmaker(bind=engine)
session = Session()

# Define a model or table
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

# Create a new user record
new_user = User(name='John')
session.add(new_user)
session.commit()
```

**Read:** SQLAlchemy ORM uses functions and methods to query and retrieve data from the database.

```
# Query and retrieve user records
users = session.query(User).all()  # Retrieve all users
for user in users:
    print(user.name)
```

**Update:** SQLAlchemy ORM can be used to modify existing records or objects in the data storage system.

```
# Update a user's name
user = session.query(User).filter_by(name='John').first()
user.name = 'John Doe'
session.commit()
```

**Delete:** SQLAlchemy ORM can be used to remove existing records or objects from the data storage system.

```
# Delete a user record
user = session.query(User).filter_by(name='John Doe').first()
session.delete(user)
session.commit()
```


### 1. Car:

**State:**
- Attributes: Model (string), year_of_make (int), Price (float)
- Values: Hyundai i10, 2017, 700000.50

**Behavior:** 
- Create: Add a new car to a car dealership inventory.
- Read: Retrieve car details by car ID, make, or model.
- Update: Update car information such as price, mileage, or color.
- Delete: Remove a car from the inventory.

### 2. Weather:

**State:**
- Attributes: date (string or datetime), temperature (float), humidity (float), is_rainy (boolean)
- Values: date = "30-03-2022", temperature = 28.5, humidity = 0.75, is_rainy = False

**Behavior:**
- Create: Add a new date to the weather database
- Read: Retrieve weather details like temperature, humidity
- Update: Update weather information such as is_rainy
- Delete: Remove old data

### 3. Restaurant:

**State:**
- Attributes: name (string), cuisine_type (string), rating (float), is_open (boolean)
- Values: name = "Barbeque Nation", cuisine_type = "Italian", rating = 4.5, is_open = True

**Behavior:**
- Create: Add a new restaurant to the database
- Read: Retrieve cuisines details like chinese, italian, different restaurants
- Update: Update restaurant information like rating, is_open
- Delete: Remove restaurants that no longer exists

### 4. Computer:

**State:**
- Attributes: brand (string), processor_speed (float), memory_capacity (integer), is_laptop (boolean), price (float)
- Values: brand = "HP Pavilion", processor_speed = 1.19, memory_capacity = 4, is_laptop = True, price = 5000.75

**Behavior:**
- Create: Add a new computer to the inventory
- Read: Retireve computer details like processor_speed, memory capacity
- Update: Update information like price, specifications
- Delete: Remove details of sold out computers

### 5. Event:

**State:**
- Attributes: name (string), date (string or datetime), location (string), is_free (boolean)
- Values: name = "Music Concert", date = "2023-07-15", location = "Phoenix Mall", is_free = False

**Behavior:**
- Create: Create a new event in the database
- Read: Retrieve information like genre, date
- Update: Update price depending on the time
- Delete: Remove events that no longer exists
### 6. Product:

**State:**
- Attributes: name (string), price (float), quantity (integer), is_available (boolean)
- Values: name = "iPhone 12", price = 70,000, quantity = 10, is_available = True

**Behavior:**
- Create: Add a new product to the product catalog.
- Read: Fetch product information by ID or name.
- Update: Update product details such as price, description, or quantity.
- Delete: Remove a product from the product catalog.

### 7. Student:

**State:**
- Attributes: id(int), name (string), age (integer), grade (integer), is_enrolled (boolean)
- Values: name = "Samuel David Singh", age = 15, grade = 9, is_enrolled = True4

**Behavior:**
- Create: Enroll a new student in a school or educational institution.
- Read: Retrieve student information by student ID or name.
- Update: Update student details such as contact information or grade level.
- Delete: Remove a student's record from the system.

### 8. Country:

**State:**
- Attributes: name (string), population (integer), capital (string), is_developed (boolean)
- Values: name = "United States", population = 331000000, capital = "Washington, D.C.", is_developed = True

**Behavior:**
- Create: Add a new country to the database
- Read: Retrieve information like population, capital
- Update: information like population (changes over time)
- Delete: countries (no longer exists)

### 9. Employee:

**State:**
- Attributes: eid(int), name (string), age (integer), position (string), salary (float)
- Values: name = "Samuel", age = 30, position = "Manager", salary = 50000.0

**Behavior:**
- Create: a new employee id for a new hire
- Read: information like position, age
- Update: salary
- Delete: eid (no longer an employee)

### 10. Movie:

**State:**
- Attributes: title (string), director (string), release_year (integer), rating (float)
- Values: title = "The Shawshank Redemption", director = "Frank Darabont", release_year = 1994, rating = 9.3

**Behavior:**
- Create: Add newly released movie to the database
- Read: Retrieve information like director name, movie name, release_year
- Update: Information like rating
- Delete: title (movie deleted)

### 11. Animal:

**State:**
- Attributes: name (string), age (int), diet (str), is_carnivore (boolean)
- Values: name = "Lion", avg_age = 5, diet = "Meat", is_carnivore = True

**Behavior:**
- Create: Add new animal to the zoo database
- Read: Update information on the behavior and diet of the animal
- Update: age information
- Delete: animals that no longer exist in the zoo

### 12. Customer:

**State:**
- Attributes: cid(int), name (string), age (integer), email (string), is_premium (boolean)
- Values: name = "Samuel", age = 35, email = "samuel@example.com", is_premium = True

**Behavior:**
- Create: Create a new customer profile in the customer database.
- Read: Retrieve customer information by ID, email, or phone number.
- Update: Update customer details such as address, contact information, or preferences.
- Delete: Remove a customer profile from the customer database.

### 13. Product:

**State:**
- Attributes: pid (int), name (string), price (float), quantity_available (int), is_discounted (boolean)
- Values: name = "Smartphone", price = 20000.50, quantity_available = 50, is_discounted = False

**Behavior:**

- Create: Add a new product to the product catalog.
- Read: Fetch product information by ID or name.
- Update: Update product details such as price, description, or quantity.
- Delete: Remove a product from the product catalog.

### 14. Song:

**State:**
- Attributes: id(int), title (string), artist (string), duration_seconds (integer), is_favorite (boolean)
- Values: title = "Tera yaar", artist = "Arijit Singh", duration_seconds = 355, is_favorite = True

**Behavior:**
- Create: Add a new song to the database
- Read: Retrieve information like song title, artist
- Update: whether song is_favorite or not
- Delete: songs from database

### 15. Bank:

**State:**
- Attributes: ifsc_code (int), name (string), location (string), total_assets (float), is_international (boolean)
- Values: ifsc_code = 98567, name = "HDFC", location = "Bangalore", total_assets = 5000000.0, is_international = True

**Behavior:**
- Create: Open a new bank account for a customer.
- Read: Retrieve account details by account number or customer ID.
- Update: Update account information such as balance or account type.
- Delete: Close an existing bank account.

### 16. Customer Feedback Entry:

**State:**
- Attributes: entry_id (int), c_name (string), date (string), feedback (str), rating (float)
- Values: entry_id = 0137, c_name = "Sam", date = "14-06-2023", feedback = "Good", rating = 4.5

**Behavior:**
- Create: Submit a new customer feedback entry.
- Read: Fetch customer feedback by ID, customer name, or date.
- Update: Update customer feedback comments or ratings.
- Delete: Remove a customer feedback entry from the system.


### 17. Blog Post Entry:

**State:**
- Attributes: post_id (int), author (string), title (str), metadata (str), tag (str), 
- Values: post_id = 012, author = "Sam", title = "Python Programming", metadata = "Blog on Python Variables", tag="python"

**Behavior:**
- Create: Create a new blog post on the blogging platform.
- Read: Retrieve blog post content and metadata by post ID, title, or author.
- Update: Update blog post content, title, or tags.
- Delete: Delete a blog post from the blogging platform.

### 18. Project

**State:**
- Attributes: project_id (int), name (str), owner(str), deadlines (str), team_members (list), Objectives (str), 
- Values: project_id = 02, name = "Sam", owner = "Sam", deadline = "14-07-2023", team_members = [x,y,z], Objectives = "Deployment"

**Behavior:**
- Create: Create a new project in the project management system.
- Read: Fetch project details by project ID, name, or owner.
- Update: Update project information such as deadlines, team members, or objectives.
- Delete: Delete an existing project from the project management system.

### 19. Event 

**State:**
- Attributes: event_id (int), name (str), date (str), venue (str), time (datatime), description (str)
- Values: event_id = 01, name = "musical_evening", venue = "bangalore", date = "14-07-2023", time = 18:00, description = "Rock Concert"

**Behavior:**
- Create: Create a new event in the event management system.
- Read: Retrieve event details by event ID, name, or date.
- Update: Update event information such as venue, time, or description.
- Delete: Cancel an existing event and remove it from the system.

### 20. Book:

**State:**
- Attributes: book_id (int), author (str), isbn_no (int), pub_year (int), genre (str), availability (boolean)
- Values: book_id = 567, author = "Salman Rushdie", isbn_no = "0084635", pub_year = "2023", genre = "fiction", availability = "True"

**Behavior:**
- Create: Add a new book to the library catalog.
- Read: Retrieve book details by ISBN, title, or author.
- Update: Update book information such as publication year, genre, or availability.
- Delete: Remove a book from the library catalog.

### 21. Order

**State:**
- Attributes: c_name (str), order_name (str), qty (int), order_id (int), c_id (int), order_status (str), address (str), payment (str)
- Values: c_name = "Sam", order_name = "mobile", qty = 1, order_id = 4968, c_id = 938, order_status = "active", address = "101, Bangalore", payment = "COD"

**Behavior:**
- Create: Place a new order for a customer, including the ordered items and quantities.
- Read: Fetch order details by order ID or customer ID.
- Update: Update order status, shipping address, or payment information.
- Delete: Cancel an existing order.

### 22. User

**State:**
- Attributes: u_id (int), u_name (str), email (str), password (str)
- Values: u_id = 638, u_name = "Sam", email = "samuel@gmail.com", password = "653286"
- 
**Behavior:**
- Create: Create a new user account in the system.
- Read: Retrieve user information by username or ID.
- Update: Update user details such as name, email, or password.
- Delete: Delete a user account from the system.

### 23. Appointment

**State:**
- Attributes: app_id (int), date (str), name (str), time (str), ph_no (str)
- Values: app_id = 038, date = "14-07-2023", name = "Sam", time = "17:00", ph_no = "123456789"

**Behaviour:**
- Create: Schedule a new appointment with a client or service provider.
- Read: Fetch appointment details by appointment ID, date, or participant.
- Update: Update appointment information such as time, location, or description.
- Delete: Cancel an appointment and remove it from the system.

### 24. Task

**State:**
- Attributes: task_id (int), assignee (str), date (str), status (str)
- Values: task_id = 938, assignee = "Sam", date = "14-06-2023", status = "High"

**Behaviour:**
- Create: Create a new task in a task management system.
- Read: Fetch task details by task ID or assignee.
- Update: Update task information such as due date, status, or priority.
- Delete: Delete a task from the task management system.

### 25. Product Review

**State:**
- Attributes: product_id (int), reviewer (str), comments (str), rating (float)
- Values: product_id = 34, reviewer = "Sam", comments = "Good", rating = 4.0

**Behavior:**
- Create: Submit a new review for a product.
- Read: Retrieve product reviews by product ID or reviewer.
- Update: Update review comments or ratings.
- Delete: Remove a product review from the system.

### 26. Employee Timesheet Entity:

**State:**
- Attributes: emp_id (int), project (str), start_date (datetime), end_date (datetime)
- Values: emp_id = 924, project = "Python", start_date = "14-06-2023", end_date = 14-07-2023

**Behavior:**
- Create: Record a new timesheet entry for an employee.
- Read: Fetch timesheet details by employee ID, date, or project.
- Update: Update timesheet information such as hours worked or project allocation.
- Delete: Remove a timesheet entry from the system.

### 27. Recipe Entity:

**State:**
- Attributes: recipe_id (int), recipe (str), ingredients (list), end_date (datetime)
- Values: recipe_id = 123, recipe = "biryani", ingredients = ["rice", "biryani", "masala"], end_date = 14-07-2023

**Behavior:**
- Create: Add a new recipe to a recipe management system.
- Read: Retrieve recipe details by recipe ID or name.
- Update: Update recipe information such as ingredients, instructions, or cooking time.
- Delete: Delete a recipe from the recipe management system.

### 28. Social Media Post:

**State:**
- Attributes: post_id (int), author(str), date (str), comments = "str"
- Values: product_id = 34, reviewer = "Sam", comments = "Good", rating = 4.0

**Behavior:**
Create: Publish a new post on a social media platform.
Read: Retrieve post content and metadata by post ID, author, or date.
Update: Update post content, add comments, or modify privacy settings.
Delete: Delete a post from the social media platform.

### 29. Hotel:

**State:**
- Attributes: hotel_id (int), hotel_name (str), location (str), room_avail (boolean), pricing (float)
- Values: hotel_id = 28, hotel_name = "Meridian", location = "bangalore", room_avail = "yes", pricing = 2000.50

**Behavior:**
- Create: Add a new hotel to a booking system.
- Read: Retrieve hotel details by hotel ID or location.
- Update: Update hotel information such as room availability or pricing.
- Delete: Remove a hotel from the booking system.

### 30. Customer Support Ticket:

**State:**
- Attributes: ticket_id (int), agent_name (str), status (str), task_name (str)
- Values: ticket_id = 828, agent_name = "Samuel", status = "Completed", task_name = "Software Demo"

**Behavior:**
- Create: Create a new support ticket for a customer query or issue.
- Read: Fetch support ticket details by ticket ID or customer.
- Update: Update ticket information such as status, priority, or assigned agent.
- Delete: Close or remove a support ticket from the system.

### 31. Sales Order:

**State:**
- Attributes: order_id (int), c_name (str), qty (int), address (str), payment (str)
- Values: order_id = 476, c_name = "Sam", qty = 1, address = "101, Bangalore", payment ="COD"

**Behavior:**
- Create: Place a new sales order for a customer.
- Read: Fetch sales order details by order ID or customer.
- Update: Update order information such as quantities, shipping address, or payment method.
- Delete: Cancel a sales order and remove it from the system.

### 32. Inventory Item:

**State:**
- Attributes: item_id (int), name (str), category (str), qty (int), price (float), description (str)
- Values: item_id = 24, name = mobile, category = electronics, qty = 500, price = 300000.50, description = "Apple Iphones"

**Behavior:**
- Create: Add a new item to the inventory system.
- Read: Retrieve item details by item ID, name, or category.
- Update: Update item information such as quantity, price, or description.
- Delete: Remove an item from the inventory system.

### 33. Movie:

**State:**
- Attributes: movie_id (int), title (str), genre (str), release_date (str), director (str)
- Values: movie_id = 389, title = "Avatar", genre = "fiction", release_date = "2022", direction = "James Cameroon"

**Behavior:**
- Create: Add a new movie to a movie database.
- Read: Retrieve movie details by movie ID, title, or genre.
- Update: Update movie information such as release date, director, or cast.
- Delete: Delete a movie from the movie database.

### 34. Supplier:

**State:**
- Attributes: supplier_id (int), supplier_name (str), contact (str), payment (str)
- Values: supplier_id = 839, supplier_name = "Amazon", contact = "123456789", payment = "NEFT"

**Behavior:**
- Create: Add a new supplier to the supplier list.
- Read: Retrieve supplier details by supplier ID or name.
- Update: Update supplier information such as contact information or payment terms.
- Delete: Remove a supplier from the supplier list.

### 35. Forum Thread:

**State:**
- Attributes: thread_id (int), topic (str), tags (str)
- Values: thread_id = 48, topic = "Programming", tags = "Python"

**Behavior:**
- Create: Start a new forum thread with a topic and initial post.
- Read: Retrieve forum thread details by thread ID or topic.
- Update: Update thread information such as title or category.
- Delete: Delete a forum thread and remove it from the forum.

### 36. Course:

**State:**
- Attributes: course_id (int), title (str), instructor (str), description (str)
- Values: course_id = 395, title = "Python", instructor = "Samuel", description = "Top Rated"

**Behavior:**
- Create: Create a new course in an e-learning platform.
- Read: Retrieve course details by course ID or title.
- Update: Update course information such as description or instructor.
- Delete: Delete a course from the e-learning platform.

### 37. Warehouse:

**State:**
- Attributes: warehouse_id (int), location (str), capacity_in_tonnes (int)
- Values: warehouse_id = 938, location = "Whitefield, Bangalore", capacity_in_tonnes = 1500

**Behavior:**
- Create: Create a new warehouse in the warehouse management system.
- Read: Retrieve warehouse details by warehouse ID or location.
- Update: Update warehouse information such as capacity or address.
- Delete: Remove a warehouse from the system.

### 38. Flight:

**State:**
- Attributes: flight_no (int), departure (str), arrival (str), dep_time (str), arr_time (str)
- Values: flight_no = 12345, departure = "Chennai", arrival = "Bangalore", dep_time = "12:00", arr_time = "13:00"

**Behavior:**
- Create: Schedule a new flight in an airline reservation system.
- Read: Retrieve flight details by flight number, departure/arrival airports, or date.
- Update: Update flight information such as departure/arrival times or gate.
- Delete: Cancel a flight and remove it from the system.

### 39. Music Album:

**State:**
- Attributes: album_id (int), artist (str), title (str), release_date (str), genre (str)
- Values: album_id = 937, artist = "Sam", title = "Good Day", release_date = "13-06-2023", genre = "rock"

**Behavior:**
- Create: Add a new music album to a music library.
- Read: Retrieve album details by album ID, artist, or title.
- Update: Update album information such as tracklist, release date, or genre.
- Delete: Remove an album from the music library.

### 40. Rental Property:

**State:** 
- Attributes: property_id (int), location (str), owner (str), price (float), availability (bool)
- Values: property_id = 397563, location = "Bangalore", owner = "Sam", price = 395000.50, availability = Yes

**Behavior:**
- Create: Add a new rental property to a property management system.
- Read: Retrieve property details by property ID, location, or owner.
- Update: Update property information such as rent price, availability, or amenities.
- Delete: Remove a rental property from the system.

### 41. Donation:

**State:** 
- Attributes: donation_id (int), donor (str), date (str), amount (float), donor_details (str)
- Values: donation_id = 98765, donor = "Sam", date = "15-07-2023", amount = 50000.50, donor_details = "Business owner, Bangalore"

**Behavior:**
- Create: Record a new donation in a fundraising system.
- Read: Fetch donation details by donation ID, donor, or date.
- Update: Update donation information such as amount, donor details, or allocation.
- Delete: Remove a donation from the system.

### 42. Social Media Profile:

**State:** 
- Attributes: profile_id (int), profile_name (str), bio (str), privacy (str)
- Values: profile_id = 9283, profile_name = "sam7", bio = "python_dev", privacy = "open"

**Behavior:**
- Create: Create a new social media profile for a user.
- Read: Retrieve profile details by profile ID or user.
- Update: Update profile information such as bio, profile picture, or privacy settings.
- Delete: Delete a social media profile.

### 43. Library Membership:

**State:** 
- Attributes: user_id (int), borrowing_limit (int), membership_status (str), joining_date (str)
- Values: user_id = 123, borrowing_limit = 2, membership_status = "Permanent", joining_date = "23-11-2019"

**Behavior:**
- Create: Create a new library membership for a user.
- Read: Retrieve membership details by membership ID or user.
- Update: Update membership information such as borrowing limits or membership status.
- Delete: Cancel a library membership.

### 44. Supplier Product:

**State:** 
- Attributes: prod_id (int), supplier (str), price (float), qty (int), supplier_address (str)
- Values: prod_id = 123, supplier = "b2c", price = 5000.75, qty =5, supplier_address = "Whitefield, Bangalore"

**Behavior:**
- Create: Add a new product supplied by a supplier.
- Read: Retrieve product details by product ID, name, or supplier.
- Update: Update product information such as price, quantity, or supplier details.
- Delete: Remove a product from the system.

### 45. Expense Report Entity:

**State:** 
- Attributes: report_id (int), submitter (str), date (str), items (list), amount (float)
- Values: report_id = 9876, submitter = "sam", date = "14-07-2023", items = ["food", "utilities", "education"], amount = 25000.75

**Behavior:**
- Create: Create a new expense report with itemized expenses.
- Read: Retrieve expense report details by report ID, submitter, or date.
- Update: Update expense report information such as expense items, amounts, or categories.
- Delete: Delete an expense report from the system.

### 46. Sports Team Entity:

**State:** 
- Attributes: team_id (int), name (str), league (str), coach (str), home_stadium (str)
- Values: team_id = 456, name = "Chelsea", league = "EPL", coach = "maradona", home_stadium = "london"

**Behavior:**
- Create: Create a new sports team in a sports management system.
- Read: Retrieve team details by team ID, name, or league.
- Update: Update team information such as roster, coach, or home stadium.
- Delete: Remove a sports team from the system.

### 47. Job Application Entity:

**State:** 
- Attributes: app_id (int), app_name (str), position (str), status (str)
- Values: app_id = 234, app_name = "sam", position = "python dev", status = "waitlist"

**Behavior:**
- Create: Submit a new job application for a job opening.
- Read: Retrieve application details by application ID, applicant, or position.
- Update: Update application information such as resume, cover letter, or status.
- Delete: Remove a job application from the system.

### 48. Document Entity:

**State:** 
- Attributes: doc_id (int), title (str), author (str), tags (list)
- Values: doc_id = 345, title = "python", author = "sam", tags = ["AI", "ML", "SQL"]

**Behavior:**
Create: Create a new document in a document management system.
Read: Retrieve document details by document ID, title, or author.
Update: Update document information such as content, tags, or access permissions.
Delete: Delete a document from the system.

### 49. Healthcare Appointment Entity:

**State:** 
- Attributes: app_id (int), patient (str), date (datetime), time (datetime)
- Values: app_id = 345, patient = "sam", date = "str", time = 

**Behavior:**
- Create: Schedule a new healthcare appointment for a patient.
- Read: Fetch appointment details by appointment ID, patient, or date.
- Update: Update appointment information such as time, doctor, or reason for visit.
- Delete: Cancel a healthcare appointment and remove it from the system.

### 50. Invoice Entity:

**State:** 
- Attributes: invoice_id (int), billing_items (list), amount (float), due_date (datetime)
- Values: invoice_id = 987), billing_items = ["mobile", "laptop"], amount = 5000.50, due_date = 14-07-2023

**Behavior:**
- Create: Generate a new invoice for a customer.
- Read: Retrieve invoice details by invoice ID or customer.
- Update: Update invoice information such as billing items, amounts, or due date.
- Delete: Delete an invoice from the system.

## Decision making in Python
Decision making in Python is typically implemented using **conditional statements**. Python provides several types of conditional statements to control the flow of a program based on certain conditions. The most commonly used conditional statements are:
```if, for, while, try-except```

## Control statements in python
In Python, control statements are used to **control the flow of execution in a program**. 
They allow you to make decisions, repeat blocks of code, and handle exceptions. Here are some commonly used control statements in Python:
```if, for, while, break, continue, try-except-else-finally```

## States and behaviors in Python
In Python, states and behaviors are fundamental concepts in object-oriented programming (OOP). 
- Objects have states that represent their data or properties, and they have behaviors that define their actions or methods. 

Let's explore how states and behaviors are implemented in Python:

## States
States in Python refer to the data or properties associated with an object. 
- These states are represented by instance variables, which are unique to each object of a class. 
- Instance variables hold the state of an object and can have different values for different instances. 
- They define the characteristics or attributes of an object.

Example:
```
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

# Creating objects
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

# Accessing object states
print(car1.brand)  # Output: Toyota
print(car2.color)  # Output: Blue
```

- In the above example, the `Car` class has two instance variables, `brand` and `color`, which represent the state of a car object. 
- Each car object (`car1` and `car2`) has its own values for these instance variables, representing their specific states.

## Behaviors:
Behaviors in Python are defined by methods or functions associated with an object. Methods represent the actions or operations that an object can perform. They can modify the object's state, access its data, or perform specific tasks.

Example:
```
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print(f"The {self.brand} car's engine is starting.")

    def stop_engine(self):
        print(f"The {self.brand} car's engine is stopping.")

# Creating objects
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

# Invoking object behaviors
car1.start_engine()  # Output: The Toyota car's engine is starting.
car2.stop_engine()  # Output: The Honda car's engine is stopping.
```

In the above example, the Car class has two methods, `start_engine()` and `stop_engine()`, which represent the behaviors of a car object. The methods are defined within the class and can be invoked on the objects (`car1` and `car2`) to perform the specified actions.

By combining states (instance variables) and behaviors (methods) within a class, you can create objects that have their own unique states and can perform specific actions. This encapsulation of data and behavior is a fundamental principle of object-oriented programming in Python.


# VII. Decision Making:
=====================
1. What is Decision Making. Explain different scenarios when to go for Decision Making
2. Give examples for below conditions
	1. single if : 
	2. if else:
	3. if elif else:
	4. if elif elif else:
	5. Nested if: 
3. Prepare Programs for below questions
	1. Prepare state and assign North South West East 
	    north = []
		south = ['Andhra Prades', 'Telangana', 'Karnataka','Tamil Nadu', 'Kerala']
		west = []
		east = []
	2. Prepare dictionary with key as state name and value as "list of districts"
4. Get employee details(in dict format, empid,name,sal, exp) and update hike for employee with below 
		If exp is 0 to 2 years - 10% Hike
				  2 to 5 years - 20% Hike
				  5 to 8 years - 30% Hike
				  8+           - No hike
5. Explain below terms in detail 
	- Requirement
	- User Criteria
	- Validations(Client vs Server)

Requirements and user criteria are essential components that guide the development process and ensure that the software meets the desired objectives and user expectations. 

**Requirement:**
Requirements represent a clear and concise description of what the software system should accomplish. They define the features, functionalities, and constraints that the software must adhere to. 

Gathering requirements is typically one of the initial stages in the software development life cycle. It involves interacting with stakeholders (such as clients, users, and business analysts) to identify and document their needs and expectations.

Requirements can be classified into different types, including:

a. Functional Requirements: These specify the specific actions the software should perform, describing what the system needs to do. For example, "The system should allow users to create new accounts" or "The system should calculate the total purchase amount."

b. Non-Functional Requirements: These define the qualities or characteristics that the software should possess, such as performance, security, usability, scalability, and reliability. Non-functional requirements often address aspects like response time, system availability, data encryption, user interface design, and so on.

c. Business Requirements: These requirements focus on the broader goals and objectives of the software from a business perspective. They capture the high-level needs and benefits the software is expected to provide to the organization. For example, "The software should streamline the inventory management process and reduce costs."

d. Technical Requirements: These specify the technological aspects and constraints that the software must consider. They may include hardware and software compatibility, programming languages or frameworks to be used, database requirements, and any specific integration needs.


Requirements should be well-documented, unambiguous, and testable, allowing developers to clearly understand what needs to be built and enabling testers to verify if the software meets the specified criteria.

1. User Criteria:
User criteria, also known as user requirements or user stories, represent the specific needs and expectations of the end-users or stakeholders who will interact with the software. They provide a user-centric perspective and help developers understand how the software should behave from the user's point of view. User criteria are typically expressed in a narrative format or as user stories and capture the functionalities and behaviors that users desire.

User criteria often follow a specific template known as "As a [type of user], I want [some goal] so that [some reason]." For example:

"As a customer, I want to be able to add items to my shopping cart so that I can purchase them later."
"As an administrator, I want to be able to generate reports on user activities for auditing purposes."

User criteria are often collected through user interviews, surveys, or direct observations. They help prioritize development efforts and ensure that the software aligns with the user's needs, resulting in a more user-friendly and satisfying experience.

It's important to note that requirements and user criteria are interconnected and influence each other. User criteria provide the user's perspective, while requirements encompass a broader scope, including technical, business, and non-functional aspects. Both play a crucial role in defining the scope of the software and driving the development process to meet the desired objectives.


**User Criteria:**


 
 **Client Validation:**
 - Client-side validation refers to the validation performed on the client-side, typically using JavaScript, before the data is sent to the server. It is performed within the user's web browser and provides instant feedback to the user. 
 - Client-side validation is commonly used to validate input formats, required fields, length limits, and other basic validations. It helps in enhancing the user experience by preventing unnecessary server round trips and providing immediate feedback to the user.


**Server Validation:**
 - refers to the validation performed on the server-side, typically using server-side programming languages like Python, PHP, or Java.
 -  - it ensures that the data sent by the client is valid, regardless of any client-side validation that may have been performed. It provides an additional layer of security and integrity to the application.
 - Server-side validation is used to validate complex business rules, perform database queries, and enforce security constraints that cannot be reliably implemented on the client-side.

Client-side validation improves the user experience by providing instant feedback, while server-side validation ensures the integrity and security of the application. It is recommended to perform both client-side and server-side validation to have a robust and secure validation mechanism in web applications.

6. State vs Behavior . Examples

## Preparation for group discussion

### Tell me about yourself?


### Data Engineering
"Hello, my name is Samuel David Singh. I am a Data Engineer with expertise in designing and implementing data infrastructure solutions. I have a strong background in managing and processing large-scale data sets, building data pipelines, and ensuring the smooth flow of data between various systems. I am experienced in working with tools and technologies such as AWS, PySpark, Hadoop, Databases and Azure. My goal as a Data Engineer is to optimize data systems, improve data quality, and enable efficient data analysis and processing. I enjoy collaborating with cross-functional teams and leveraging my technical skills to drive data-driven solutions and insights. I am passionate about leveraging data to solve complex business problems and contribute to the success of organizations. I am excited about the ever-evolving field of data engineering and look forward to applying my expertise to tackle challenging data-related projects."

### Python Developer
"Hello, my name is Samuel, and I am a Python developer. With 2 years of experience in Python programming, I have developed a strong foundation in building robust and scalable applications using this versatile language.

Throughout my career, I have successfully delivered various projects, ranging from web development to data analysis and automation. I am proficient in leveraging Python frameworks such as Django and Flask for web development, as well as libraries like NumPy, Pandas, and Matplotlib for data manipulation and visualization.

What truly drives me as a developer is the problem-solving aspect of programming. I enjoy tackling complex challenges and finding innovative solutions using Python's extensive ecosystem. I am constantly staying up to date with the latest trends and advancements in the Python community, allowing me to incorporate best practices and optimize code efficiency.

Apart from my technical skills, I also possess strong collaboration and communication abilities. I have experience working in agile teams, collaborating with designers, product managers, and other developers to deliver high-quality software solutions.

I am genuinely passionate about Python and its vast capabilities. I am excited to contribute my skills and expertise to a team where I can continue to learn, grow, and create impactful solutions using Python.

Thank you for considering my profile as a Python developer. I am eager to discuss potential opportunities and how my skills align with your organization's goals."

Some of the challenges that I face as a Python Developer on a daily basis is

**1. Performance:** overcome performance challenges like optimizing critical code sections, utilizing efficient algorithms and data structures, and leveraging compiled extensions or libraries written in languages like C or Cython for computationally intensive tasks.

**2. Scalability:** Python's Global Interpreter Lock (GIL) limits multi-threading performance, making it challenging to scale applications on multiple CPU cores. To address this, explore alternative concurrency models such as multiprocessing, asynchronous programming with libraries like asyncio, or using task queues and message brokers to distribute workloads across multiple processes or machines.

**3. Dependency Management:** Managing dependencies and their versions can be challenging, especially in large projects or when collaborating with other developers. Utilize virtual environments, tools like pipenv or Poetry for dependency management, and consider using tools like Docker for containerization to ensure consistent environments across development, testing, and production.

**4. Compatibility:** Python has multiple versions in use, and compatibility issues may arise when working with different versions or when interacting with libraries that may have specific requirements. Use tools like pip to specify and manage library versions, adopt continuous integration (CI) systems for automated testing across multiple Python versions, and document compatibility requirements for your projects.

**5. Debugging and Troubleshooting:** Identifying and resolving bugs or unexpected behavior in Python code can be challenging. Familiarize yourself with debugging tools like pdb or integrated development environments (IDEs) with built-in debuggers. Logging and unit tests can also be valuable tools for troubleshooting issues and maintaining code quality.

**6. Security:** Python applications are not immune to security vulnerabilities. Stay updated with security best practices, such as properly validating and sanitizing user input, protecting against common attack vectors (e.g., SQL injection, cross-site scripting), and using secure authentication and authorization mechanisms.

**7. Documentation and Code Maintenance:** Poorly documented code or lack of documentation can lead to confusion and difficulty maintaining the project. Document code consistently using docstrings and consider using tools like Sphinx to generate documentation. Adhering to coding standards, employing good naming conventions, and refactoring code regularly can help improve code maintainability.

**8. Continuous Learning:** The Python ecosystem is vast and continuously evolving. Staying updated with new libraries, frameworks, and best practices can be challenging. Engage with the Python community through forums, conferences, and online resources. Participate in open-source projects, collaborate with other developers, and allocate time for self-study and exploration of new tools and technologies.


I. Introduction:
=================
0. Introduce yourself.
1. Tell me about Python?
2. Why Python is so popular now a days?
3. Features of Python
4. Advantages and Disadvantages of Python
5. Interpreted vs Compiled time programming languages. Explain in detail
6. .py vs .pyc files
7. How compilation will happen internally. Explain in detail
8. Why Python is Dynamically typed programming Language. Explain
9. Python is Platform independent.Explain
10. Different ways to write python program.
   Interactive, IDLE, CommandPrompt, IDE
   Advantages, Disadvantages
11. sourcecode vs bytecode
12. Register instruction set
13. High Level vs Low level programming Language
14. Python architecture
15. Explain Garbage Collection mechanism in detail.

## 1. About Python
Python is a general purpose, dynamic, scripting, high-level and interpreted programming language.
- **General purpose** means that it can create all kinds of programs
- **Dynamic** refers to the fact that you don't need to assign keywords suchs as int.
- **Dynamic** also means that you can use a variable that was previously assigned an integer can be assigned a string
- **Scripting** 
- **High Level** language is one that is user-oriented in that it has been designed to make it  straightforward for a programmer to convert an algorithm into program code
- **Interpreted language** is where the source code is executed directly without the need for a separate compilation step. In an interpreted language, the code is read, interpreted, and executed line by line by an interpreter.

## 2. Why is python popular nowadays?
- Python has emerged as a leading language for data science and machine learning. 
- Its rich ecosystem of libraries, including NumPy, Pandas, and scikit-learn, coupled with frameworks like TensorFlow and PyTorch, make Python a go-to choice for data scientists and machine learning practitioners. 
- Python's simplicity and readability also make it a preferred language for prototyping and experimentation in these fields.

## 3. Features of Python

1. Interpreted Language:
There are no separate compilation and execution steps like C, C++, Java. Directly run the program from the source code. Internally, Python converts the source code into an intermediate form called bytecodes then translated into native language of specific computer to run it. No need to worry about linking and loading with libraries, etc.

2. Platform independent:
Python programs can be developed and executed on multiple operating system platforms. Python can be used on Linux, Windows, Macintosh, Solaris and many more.

3. Free and Open Source: Redistributable
4. High-level Language:
In Python, no need to take care about low-level details such as managing the memory used by the program.
5. Simple:
Closer to learning Mathematics basics in English medium. Easy to Learn. More emphasis on the solution to the problem rather than the syntax
6. Embeddable:
Python can be used within C/C++ program to give scripting capabilities for the program’s users.
7. Robust:
Exceptional handling features. Memory management techniques in built
8. Rich Library Support:
The Python Standard Library is very vast. Known as the “batteries included” philosophy of Python. It can help do various things involving regular expressions, documentation generation, unit testing, threading, databases, web browsers, CGI, email, XML, HTML, WAV files, cryptography, GUI and many more.
9. Easy-to-learn: Python has few keywords, simple structure, and a clearly defined syntax. This allows the student to pick up the language quickly.
10. Easy-to-read: Python code is more clearly defined and visible to the eyes.
11. Easy-to-maintain: Python's source code is fairly easy-to-maintained
12. Databases: Python provides interfaces to all major commercial databases.

## 4. Advantages and disadvantages of python
| Advantages      | Disadvantages |
| ----------- | ----------- |
| Readability & Simplicity: code readability, reduces the cost of program maintenance and development.      | Performance: Interpreted language perform slowly on computationally intensive tasks      |
| Large standard library: pre-built modules and functions for various tasks such as file I/O, networking, web developement   | Global Interpreter Lock allows only one thread to execute Python bytecode at a time, hence the performance to achieve true parallelism in multi-threaded applications is impacted|
| Cross Platform Compatibility: Can run on different operating systems which makes it convenient for developing applications that need to run on multiple platforms.      | Mobile and Game Development: Although frameworks like Kivy and Pygame exist, they may have limitations compared to platform-specific languages like Java, Kotlin, Swift, or C++ .      |
| Rich Ecosystem and Community Support: supportive community that actively contributes to the development of tools, libraries, and resources. This availability of resources simplifies development tasks and promotes collaboration.  | Memory Consumption: due to its dynamic type system and high-level abstractions, building memory-intensive applications can be a concern|
| Integration Capabilities: seamless integration with other languages like C, C++, and Java. It provides interfaces to popular databases, allowing easy data manipulation and management.     | Design Restrictions: the use of whitespace indentation for code blocks can be a challenge for developers accustomed to other programming languages.      |

## 5. Interpreted vs compiled programming languages
Interpreted and compiled languages are two different approaches to executing computer programs.
| Compiled      | Interpreted |
| ----------- | ----------- |
| **Compilation**: the source code is first passed through a compiler, which translates the entire code into machine-readable instructions called object code or bytecode. The output of the compilation process is usually an executable file or a binary file that can be directly executed by the target machine's processor. | **Interpretation**: In an interpreted language, the source code is directly executed by an interpreter without a separate compilation step. The interpreter reads the code line by line and translates each line into machine instructions or bytecode at runtime. |
| **Execution Process:** the compiled program is loaded directly into memory and executed by the computer's processor. The machine understands and directly executes the compiled instructions without the need for further translation or interpretation. | **Execution Process**: The interpreter processes and executes each line of code sequentially, translating and executing it on the fly. The interpreter may perform additional tasks like memory management, garbage collection, and error handling during the execution process. |
| **Advantages:** **Efficiency**: provide faster execution speed because the entire code is translated into machine code upfront. **Portability**: The compiled executable can be run on any machine with a compatible architecture without requiring the presence of the compiler. | **Advantages:** The interpreter processes and executes each line of code sequentially, translating and executing it on the fly. The interpreter may perform additional tasks like memory management, garbage collection, and error handling during the execution process. |
| **Examples**: C, C++, Java, Rust, Go | **Examples**: Python, JavaScript, Ruby, Perl, PHP |

### Key Differences and Considerations:

**Compilation Time**: Compiled languages require an additional compilation step before execution, which can increase the overall development time compared to interpreted languages.

**Portability**: Interpreted languages are generally more portable because the interpreter can run on different platforms without the need for recompilation.

**Performance**: Compiled languages often offer better performance due to their direct translation into machine code, whereas interpreted languages may have slightly slower execution due to the interpretation process.

**Development and Debugging**: Interpreted languages can provide more interactive and dynamic development and debugging experiences since they can execute code directly without the need for recompilation.

Some languages, like Java and C#, combine elements of interpreted and compiled approaches, using a bytecode compilation step followed by interpretation or just-in-time (JIT) compilation at runtime.

The choice between compiled and interpreted languages depends on various factors, including performance requirements, development speed, platform compatibility, and the specific goals and constraints of the project.

## 6. .py vs .pyc files
In Python, .py and .pyc files serve different purposes:

**.py Files**:
 .py files are the source code files that developers can write and edit using Python programming language. These files are plain text files that can be opened and modified using any text editor. When you run a .py file, the Python interpreter reads and executes the code directly from the .py file.

**.pyc Files**:
.pyc files are compiled bytecode files generated by the Python interpreter. They are created for performance optimization purposes.
- When a .py file is first imported or executed, the Python interpreter compiles the source code into bytecode, which is a lower-level representation of the code that is easier and faster for the interpreter to execute.
- The compiled bytecode is then stored in a .pyc file, which can be used for subsequent executions to skip the compilation step and improve the startup time of the program.
- .pyc files are platform-specific and not meant to be human-readable or editable.
- If a .pyc file is present and its corresponding .py file has not been modified since the .pyc file was created, the interpreter will use the .pyc file for execution.
- If the .py file is modified, the interpreter will recompile the source code and generate a new .pyc file.

The use of .pyc files provides performance benefits as the compilation step is avoided during subsequent executions, resulting in faster program startup. However, the presence of .pyc files does not change the behavior or functionality of the Python code itself.

It's important to note that .pyc files are automatically generated by the Python interpreter and are usually stored in a pycache directory alongside the .py files. The .pyc files can be safely deleted, and they will be regenerated when the corresponding .py files are executed again.

In summary, .py files contain the human-readable source code written by developers, while .pyc files store the compiled bytecode generated by the Python interpreter for performance optimization purposes.

## 7. How compilation happens internally in Python:
Internally, in CPython (the reference implementation of Python), the compilation process involves several stages and components. Here's a brief overview of how compilation happens internally in Python:
1. **Lexical Analysis (Tokenization):** The interpreter performs lexical analysis, also known as tokenization or scanning, to break down the source code into individual tokens such as keywords, identifiers, operators, and literals.
2. **Parsing (Syntax Analysis) and Abstract Syntax Tree (AST) Generation:** The token stream is then parsed according to the Python grammar rules to create an Abstract Syntax Tree (AST) which represents the syntactic structure of the code and guides the subsequent execution steps.
3. **Compilation to bytecode:** The AST is then compiled into a lower-level representation known as bytecode. The bytecode is a platform-independent set of instructions that can be executed by the Python Virtual Machine (PVM).
4. **Bytecode execution:** The bytecode is executed by the Python interpreter or the Python Virtual Machine (PVM). The interpreter reads the bytecode instructions one by one, interpreting and executing them to produce the desired output.

It's important to note that Python's compilation process happens dynamically at runtime. When a Python module or script is imported or executed, the compilation steps are performed automatically by the interpreter. The compiled bytecode can be cached in .pyc files to speed up subsequent executions.

## 8. Why Python is a dynamically typed language?
Python is considered a dynamically typed language because the type of a variable is determined and checked at runtime, rather than being explicitly declared or enforced during compile-time. 

Some key reasons why python is dynamically typed:
1. Implicit Type Declaration: Python will automatically infer the type based on the assigned value.
2. Flexible Variable Assignment: Python allows you to reassign variables to different types.
3. Dynamic Type Checking: the type of a variable is checked during the actual execution of the program. 
4. Dynamic Dispatch and Polymorphism: Dynamic typing enables dynamic dispatch and polymorphism, allowing different objects to respond differently to the same method or function call based on their actual types. This flexibility enables powerful abstraction and code reuse.

Advantages of Dynamic Typing:
1. Enhanced Flexibility: allows variables to hold different types of values, facilitating rapid prototyping and quick iterations during development.
2. Expressiveness: reduces the need for explicit type declarations, resulting in cleaner and more readable code.
3. Quick and Easy Development: eliminates the need for lengthy type annotations, which can speed up the development process and reduce boilerplate code.

Disadvantages of Dynamic Typing:
1. **Runtime Errors**: The lack of compile-time type checking in dynamic typing can lead to runtime errors
2. **Reduced Performance**: can introduce some overhead compared to statically typed languages, as type checks and conversions are performed at runtime.

## 9. Python is platform independent. Explain?
Python is often regarded as a platform-independent language due to its ability to run on various operating systems and hardware platforms without requiring extensive modifications to the code. Here's an explanation of how Python achieves platform independence:
1. Interpreted language: the source code is executed by an interpreter.  The interpreter reads the source code, converts it into bytecode (a low-level representation), and executes it using a virtual machine.
2. Abstraction from Low-Level Details: It allows developers to write code that is independent of the underlying hardware or operating system by abstracting many
low-level details and system-specific intricacies.
3. Cross-Platform Libraries and Modules: a rich ecosystem of cross-platform libraries and modules that provide functionality for a wide range of tasks allowing developers to write code that can be executed on multiple operating systems without modification.
4. Bytecode and Virtual Machine: When Python source code is executed, it is compiled into bytecode, which is a platform-independent representation of the code. 
5. Portability of Python Interpreter: The Python interpreter itself is implemented in a platform-independent manner. For example, CPython, the reference implementation of Python, is written in C and can be compiled and run on various operating systems, including Windows, macOS, Linux, and more. 
6. Standardized Language Specification: Python has a well-defined language specification (e.g., Python Language Reference) that serves as a standard for implementing Python interpreters across different platforms. 

## 10. Different ways to write python programs and their advantages and disadvantages:
|      | Advantages | Disadvantages      | Examples |
| ----------- | ----------- | ----------- | ----------- |
|  IDE's    | Flexible and customizable. Support for syntax highlighting, code completion, and debugging. Suitable for both small scripts and large projects. | Requires manual saving and execution. Lack some advanced features of specialized environments. Setup and configuration may be required.      |  Sublime Text, Visual Studio Code, PyCharm, Atom, IDLE |
|  CLI    | Lightweight and readily available. Convenient for running short scripts and one-liners. Useful for automation and scripting tasks. | No integrated editor or advanced features. Limited in terms of code editing and debugging capabilities. Execution parameters need to be specified explicitly.      | Command Prompt (Windows), Terminal (macOS and Linux) |
|  Jupyter Notebooks    | Interactive and supports a mix of code, text, and visualizations. Great for data exploration, prototyping, and sharing analyses. Allows executing code cells individually. | Less suitable for large-scale projects. Limited support for refactoring and code organization. Not designed for traditional software development workflows.     | Jupyter Notebook, JupyterLab |
|    Integrated Development Environment (IDE) with Notebook-like capabilities:  | Combines features of traditional IDEs and Jupyter notebooks. Provides an integrated environment for coding, debugging, and data analysis. Offers the flexibility of notebooks within a larger development ecosystem. | Requires additional setup and configuration. Can be resource-intensive, especially for large notebooks. Might have a steeper learning curve compared to simpler options.      | Spyder, PyCharm, VS Code with Jupyter extensions |

## 11. Source code vs Bytecode
Source code and bytecode are different representations of a program that serve different purposes in the execution process. 
| Source Code     | Bytecode |
| ----------- | ----------- | 
| Source code is the human-readable form of a program written in a programming language like Python.     | Bytecode is an intermediate representation of the source code that is generated during the compilation or interpretation process. |
| It is composed of text-based instructions and high-level language constructs that are easily understood by developers.    | It is a lower-level form of code that is closer to machine language but is still platform-independent. |
| Source code is written by programmers and serves as the input for the compilation or interpretation process.    | Bytecode is designed to be executed by a virtual machine or interpreter rather than directly by the hardware. |
| It typically has a file extension of ".py" in Python.    | It is often stored in files with a ".pyc" extension (compiled bytecode) for caching and faster subsequent executions. |
|    | Bytecode can be executed more efficiently than source code because it has already undergone some level of translation and optimization. |

## 12. Register instruction set
A microprocessor is made up of 3 main units:
1. **Arithmetic and Logic Unit (ALU):** to perform arithmetic and logical instruction based on computer instructions
2. **Control Unit:** To control the overall operations of the computer through signals.
3. Registers 

Registers in internal memory are used to hold the instruction and data for the execution of the processor. A microprocessor's performance depends on the following characteristics:
1. Clock Speed: Each microprocessor has an **internal clock** that regulates the speed at which it executes instructions. The speed at which the microprocessor executes instruction is called the **clock speed**. Clock speed is measured in GHz (GigaHertz) or MHz (MegaHertz).
2. Instruction Set: A command which is given to a computer to perform an operation on data is called an **instruction**. Basic set of machine level instructions that a microprocessor is designed to execute is called an **instruction set**. This instruction set carries out the following types of operations:
- Data Transfer
- Arithmetic Operations
- Logical Operations
- Control Flow
- Input/Output   
3. Word Size: The number of bits that can be processed by a processor in a single instruction is called its word size. **Word size** determines the amount of RAM that can be accessed by a microprocessor. 

## 13. High level vs low level programming language
High-level and low-level programming languages are different categories of programming languages that offer varying levels of abstraction and control over hardware and system details.

| High Level Programming Languages      | Low Level Programming Languages |
| ----------- | ----------- | 
| designed to be human-readable and provide a high level of abstraction from the underlying hardware and system details. | provide a closer representation of the hardware and system architecture, allowing for direct control over hardware resources. |
| They offer built-in features and constructs that make programming easier and more efficient, focusing on problem-solving rather than low-level implementation. | They are less abstract and require a deep understanding of the system architecture and hardware details. | 
| High-level languages are closer to natural language and use common programming paradigms, such as object-oriented programming or functional programming. | Low-level languages are typically used for tasks that require fine-grained control, optimization, or interfacing with specific hardware devices. |
| Examples of high-level programming languages include Python, Java, C++, JavaScript, and Ruby.| Assembly language and machine code are examples of low-level languages. |
| Advantages: Easier to learn and use. Increased productivity and faster development. Platform independence, as they are typically designed to run on different operating systems. Extensive libraries and frameworks for various tasks | Advantage: Direct access to hardware resources and system-level operations. Highly optimized code for performance-critical applications. Ability to interact with hardware devices or write low-level system components. | 
| Disadvantage: They may sacrifice fine-grained control over hardware-specific operations. Some high-level languages may have slower performance compared to low-level languages. Limited access to low-level system features and hardware. | Disadvantage: Steeper learning curve and more complex syntax. Code written in low-level languages is usually less portable across different platforms. Requires detailed knowledge of the system architecture and hardware-specific instructions. Development can be time-consuming and error-prone. |

## 14. Python Architecture
The Python architecture refers to the overall structure and components involved in the execution of Python programs. Here's an overview of the Python architecture:

1. Source Code:
- The source code that contains the instructions and logic written by the developer are written in plain text files with a .py extension.

2. Python Interpreter:
- The Python interpreter reads and executes Python code line by line, transforming it into the desired output or behavior.
- The default interpreter for Python is CPython, but other implementations like Jython, IronPython, and PyPy are also available.

3. Lexical Analysis and Parsing:
- The interpreter performs lexical analysis, also known as tokenization or scanning, to break down the source code into individual tokens such as keywords, identifiers, operators, and literals.
- The token stream is then parsed according to the Python grammar rules to create an Abstract Syntax Tree (AST) which represents the syntactic structure of the code and guides the subsequent execution steps.

4. Compilation to Bytecode
- After parsing, the Python interpreter compiles the AST into bytecode which is a lower-level representation of the code that can be executed by the Python Virtual Machine (PVM).
- The bytecode is stored in .pyc files for caching and reuse in subsequent executions.

5. Python Virtual Machine (PVM)
- The reads and interprets the bytecode instructions, performing the necessary operations to produce the desired output.
- The PVM manages memory, executes instructions, handles exceptions, and provides the runtime environment for Python programs.

6. Standard Library and Built-in Modules:
- Python comes with a comprehensive standard library that provides a wide range of modules and functions for common programming tasks.
- The standard library includes modules for file I/O, networking, regular expressions, data manipulation, and much more.
- Additionally, Python has built-in modules that provide essential functionality, such as math, string manipulation, and system-level operations.

7. Third-Party Libraries and Modules:
- Third-party libraries and modules for various domains such as web development, scientific computing, machine learning, data analysis, and more are developed by the community.

8. Execution and Output:
- Once the bytecode is executed by the PVM, the Python program produces the desired output or performs the specified behavior.
- Output can be displayed in the console, written to files, or interacted with through GUI interfaces, depending on the program's design.

The Python architecture is designed to provide a high-level and versatile programming environment. It offers features such as dynamic typing, automatic memory management, extensive libraries, and cross-platform compatibility. The combination of the Python interpreter, bytecode compilation, the PVM, and the vast ecosystem of libraries contributes to the popularity and effectiveness of the Python programming language.

## Memory Management in Python
When we execute our Python script, there are so many logic that runs behind in Python memory to make the code efficient. Memory management is very important for software developers to work efficiently with any programming language. Memory management is related to writing memory-efficient code. Improper memory management leads to slowness on the application and the server-side components. If the memory is not handled well, it will take much time while preprocessing the data.

In Python, memory is managed by the Python manager which determines where to put the application data in the memory. 

Let's assume memory looks like an empty book and we want to write anything on the book's page. Then, we write data any data the manager find the free space in the book and provide it to the application. The procedure of providing memory to objects is called **allocation**.

Python Memory Allocation
Memory allocation is an essential part of the memory management for a developer. This process basically allots free space in the computer's virtual memory, and there are two types of virtual memory works while executing programs.

- Static Memory Allocation
- Dynamic Memory Allocation

Static memory allocation happens at the compile time. For example - In C/C++, we declare a static array with the fixed sizes. However, we cannot use the memory again in the further program.

```
static int a=10; 
```

**Stack Allocation:** The Stack data structure is used to store the static memory. It is only needed inside the particular function or method call. The function is added in program's call stack whenever we call it. 

**Dynamic memory allocation:**
Unlike static memory allocation, Dynamic memory allocates the memory at the runtime to the program. For example - In C/C++, there is a predefined size of the integer of float data type but there is no predefine size of the data types in dynamic memory allocation. Memory is allocated to the objects at the run time. We use the **Heap** to implement dynamic memory management. We can use the memory throughout the program.

Everything in Python is an object means dynamic memory allocation inspires the Python memory management. Python memory manager automatically vanishes when the object is no longer in use.

**Heap Memory Allocation**
Heap data structure is used for dynamic memory which is not related to naming counterparts. It is type of memory that uses outside the program at the global space. One of the best advantages of heap memory is to it freed up the memory space if the object is no longer in use or the node is deleted.

## 15. Explain Garbage Collection mechanism in detail.

Garbage collection releases memory when no object is in use. It is like a recycling system in computers where the system deletes the unused object and 
reuses its memory slot for new objects.

When we assign the new name or placed it in containers such as a dictionary or tuple, the reference count increases its value. If we reassign the reference to an object, the reference counts decreases its value if. It also decreases its value when the object's reference goes out of scope or an object is deleted. As we know, Python uses the dynamic memory allocation which is managed by the Heap data structure. Memory Heap holds the objects and other data structures that will be used in the program. Python memory manager manages the allocation or de-allocation of the heap memory space through the API functions.

**Reference Counting in Python**
Reference counting states that how many times other objects reference an object. When a reference of the object is assigned, the count of object is incremented one. When references of an object are removed or deleted, the count of object is decremented. The Python memory manager performs the de-allocation when the reference count becomes zero. Let's make it simple to understand.

**Example:** Suppose you have 5 objects referring to the same variable:

```
a=b=c=d=e=10
```

Now you assign a new variable to the object `a`:
```
a=5
```

The reference count for the variable `10` decreases to 4. Likewise, when all objects get assigned to different variables, the reference count for `10` becomes `0` and `10` becomes garbage collected.

The Python garbage collector initiates its execution with the program and is activated if the reference count falls to zero.

- Python has an automated garbage collection system.
- Python has algorithms to deallocate objects and it has two ways to delete the unused objects from the memory.

1. Reference Counting - In Python, a reference count is automatic memory management system that helps determine when an object is no longer in use and can be safely deallocated from memory. It is a count that keeps track of the number of references pointing to an object.

Here's how the reference count works:

**Reference Count Increment:** When a reference to an object is created, either by assigning the object to a variable or passing it as an argument to a function, the reference count of the object is incremented by one. This indicates that there is now one reference to the object.

**Reference Count Decrement:** When a reference to an object is removed, either by reassigning the variable to another object or when a variable goes out of scope, the reference count of the object is decremented by one. This indicates that there is now one less reference to the object.

**Zero Reference Count:** When the reference count of an object reaches zero, it means that there are no more references to that object in the program. At this point, the object is considered no longer in use.

**Deallocation:** Once an object's reference count reaches zero, Python's memory manager deallocates the memory occupied by the object. The memory is then returned to the system and made available for reuse.

The reference count mechanism is a fundamental part of Python's memory management system because it allows the interpreter to determine when an object is no longer needed. By keeping track of the number of references to an object, Python can ensure that memory is deallocated only when it is no longer being used by the program.

However, it's important to note that the reference count mechanism is not the sole memory management technique used in Python. Python also employs a garbage collector to handle situations where objects have cyclic references or when memory deallocation cannot be determined solely based on reference counting. The garbage collector identifies and collects objects that are no longer accessible even if their reference count is not zero.

Overall, the reference count mechanism, combined with the garbage collector, allows Python to efficiently manage memory allocation and deallocation, ensuring that memory is properly used and reclaimed when objects are no longer needed. This automatic memory management helps relieve the programmer from manual memory management tasks and reduces the likelihood of memory leaks and dangling pointers. 

2. Generational Garbage Collection:
It is a type of **trace-based garbage collection**. It can break cyclic references and delete the unused objects even if they are referred by themselves.

**How does generational Garbage Collection work?**
Python keeps track of every object in memory. 3 lists are created when a program is run. Generation 0, 1, and 2 lists.

Newly created objects are put in the Generation 0 list. A list is created for objects to discard. Reference cycles are detected. If an object has no outside references it is discarded. The objects who survived after this process are put in the Generation 1 list. The same steps are applied to the Generation 1 list. Survivals from the Generation 1 list are put in the Generation 2 list. The objects in the Generation 2 list stay there until the end of the program execution.

![generation](https://github.com/samueldsingh/python-dev-90-days-bootcamp/assets/62851341/d0b300cb-ea82-4de3-9875-cbfd8d8bbdae)

**Conclusion:**
Python is a high-level language and we don’t have to do the memory management manually. Python garbage collection algorithm is very useful to open up space in the memory. Garbage collection is implemented in Python in two ways: reference counting and generational. When the reference count of an object reaches 0, reference counting garbage collection algorithm cleans up the object immediately. If you have a cycle, reference count doesn’t reach zero, you wait for the generational garbage collection algorithm to run and clean the object. While a programmer doesn’t have to think about garbage collection in Python, it can be useful to understand what is happening under the hood.



## 18. Why is string immutable?

- In Python, strings are immutable, which means they cannot be changed once they are created. They have to be used as is or either be deleted. 

- When you perform any operation that appears to modify a string, such as concatenation or converting to capital, it actually creates a new string object with the modified value instead of modifying the original string.

- Integer are also immutable: When you create a new variable, `x=10`, memory is allocated to save the object 10. Next when you try to save a new object to the same variable, `x=20`, only the object value changes and not the variable. The memory for the object 10 is deallocated and new memory is allocated for the object 20.

- String immutablity: Same logic applies when you change a string from `msg = hello` to `msg = hello world`.


11. What is an entry control loop and an exit control loop

**Entry Control loops:**
In an entry control loop, the condition is checked before the loop body is executed. If the condition is not satisfied initially, the loop body will not be executed at all. In other words, the loop may not run even once if the condition is false from the beginning.

Example:
```
n = 5
for i in range(1, n+1):
    print(n)
    n -= 1
```

Here, the condition `n > 0` is checked before executing the loop body. If the initial value of `n` is not greater than `0`, the loop will not run.

**Exit control loops:**
In an exit control loop, the condition is checked after executing the loop body. The loop body will be executed at least once, and then the condition is checked to determine if the loop should continue or exit.

```
n = 1
while True:
    print(n)
    n += 1
    if n > 5:
        break
```

Here, the loop runs indefinitely `(while True)`, but the condition `n > 5` is checked within the loop. If the condition becomes true, the `break` statement is encountered, and the loop is exited.

12. 

## General caching
## What is caching?
- Caching is a technique used in computer systems to store and retrieve frequently accessed or computationally expensive data in a faster and more efficient manner. 
- In the context of software applications, caching involves storing a copy of data in a cache, which is typically a faster storage medium, such as memory or a dedicated cache server. When a request for the data is made, the system first checks the cache. If the requested data is found in the cache, it can be quickly retrieved, avoiding the need to perform the original, potentially time-consuming operation again. This can significantly speed up subsequent access to the data.
- The purpose of caching is to reduce latency, improve performance, and minimize the need for repeated computations or expensive data retrieval operations.
- Caching can occur at various levels within a computer system, including: Hardware Caches, Operating System Caches, Database Caches, Application-Level Caches.
- Caching provides several benefits, including: Improved Performance, Reduced Resource Usage, Scalability and Cost Savings.

## Data Structures

1. What are datatypes in Python.Explain in detail
2. What are datastructures in Python.Explain in detail
3. Generic functions in Python.
4. Realtime examples for usage of integer,float,boolean,string
5. When to use string 
6. Importance of String datatype in Python 
7. Why and how string is Immutable.Explain in detail
8. What is Sequence. Types
9. How to use sequence operations on String
10.How memory will be allocated for string 
11.Explain 10 very freqently used functions in String 
12. isdigit() vs isnumeric() vs isdecimal() 
13. find vs index in string 


II. Variables:
===============



III. IDE PyCharm:
===================
1. Different IDEs in market 
2. Advantages of IDE
3. Shortcuts in PyCharm (Explain min 10)

IV. Operators:
===============
1. Explain in detail about all operators 
## 2. == (equality) vs is (identity) operator

- "==" is used for equality comparison to compare two values and check if they are equal.
- "is" operator is used for identity comparison, checking whether two objects refer to the same memory location.

Example:
```
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True, because the values of a and b are the same
print(a is b)  # False, because a and b refer to different memory locations
```

In the example above, the "==" operator returns True because the values of the lists a and b are the same. However, the "is" operator returns False because a and b are separate list objects with different memory locations.

3. and or operators. Explain 2 examples 
4. Operator precedence.
5. Subtract 2 numbers and print result program.
	- Write down all scenarios with different input values 

V. DataTypes Intro:
====================
1. Importance of DataTypes.2
2. Different data types, data structures available in Python
3. int vs float
4. Boolean. give all scenarios
5. 0 vs null
6. Explain each data type, data structure with real life examples.
7. CRUD Operations.Give examples for each 
8. Sequences. Types of sequences. Sequence operations
9. Explain about below functions and give examples 
	print()
	id()
	type()
	int()
	float()
	complex()
	bool()	
	input()
	
VI. Keywords:
=====================
1. Explain all keywords with examples and areas of usage

VII. Decision Making:
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
6. State vs Behavior . Examples


VIII. Loops:
============
1. Importance of Loops
2. while loop. Explain in detail with different use cases 
3. for loop. Explain in detail with different use cases 
4. while vs for
5. Give examples while with if else combination 
6. Give examples for with if else combination
7. Control statements.Explain and give examples for each keyword 
    - break 
    - continue
    - pass
8. Implement 5 examples which covers all topics if elif else for while break/continue/pass

Programs:
----------
- Between 1 to 100
    1. Print all numbers  
    2. Print even numbers
    3. Print odd numbers 
    4. Print all prime numbers
    5. Print numbers with power of 2 (1 2 4 8 16 32 64)
    6. Print all numbers which are divisible by 5 and 7 
    7. Print all numbers which are divisible by 4 or 6
    8. Print first 14 odd numbers 
    9. Print first 23 even numbers
   10. Print first 6 numbers which are divisible by 4 and 6 
   11. Print all numbers except divisible by 9
   12. Write for loop to explain all data structures.
   
IX. Data Structures:
=====================
        1. What are CRUD operations.Explain in detail 
        2. Sequence.Types. Operations on each sequence
        3. HTTP Request methods for CRUD. Explain in detail 
     i. Numbers:
           1. Types of numbers. Explain each use case 
           2. type conversions
           3. Explain different operations of boolean type
    ii. String:
           1. Explain about string. 
           2. Multi line string 
           3. String is Immutable.Explain in detail 
           4. CRUD Operations on String
           5. Sequence operations on String
           6. Memory allocation of String 
           7. Explain 10 important functions of String


## Preparation for group discussion

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

## About Python
Python is a general purpose, dynamic, high-level and interpreted programming language.
- **General purpose** means that it can create all kinds of programs
- **Dynamic** refers to the fact that you don't need to assign keywords suchs as int.
- **Dynamic** also means that you can use a variable that was previously assigned an integer can be assigned a string
- **High Level** language is one that is user-oriented in that it has been designed to make it 
straightforward for a programmer to convert an algorithm into program code
- **Interpreted language** 

## 3. Features of Python

1. It is an interpreted language
- There are no separate compilation and execution steps like C, C++, Java
-	Directly run the program from the source code.
-	Internally, Python converts the source code into an intermediate form called bytecodes then translated into native language of specific computer to run it.
-	No need to worry about linking and loading with libraries, etc.

2. Platform independent
- 	Python programs can be developed and executed on multiple operating system platforms.
-	Python can be used on Linux, Windows, Macintosh, Solaris and many more.

3. Free and Open Source: Redistributable
4. High-level Language:
- In Python, no need to take care about low-level details such as managing the memory used by the program.
5. Simple:
- Closer to learning Mathematics basics in English medium. Easy to Learn
- More emphasis on the solution to the problem rather than the syntax
6. Embeddable
- Python can be used within C/C++ program to give scripting capabilities for the program’s users.
7. Robust:
- Exceptional handling features
- Memory management techniques in built
8. Rich Library Support
- The Python Standard Library is very vast.
- Known as the “batteries included” philosophy of Python. It can help do various things involving regular expressions, documentation generation, unit testing, threading, databases, web browsers, CGI, email, XML, HTML, WAV files, cryptography, GUI and many more.
9. Easy-to-learn − Python has few keywords, simple structure, and a clearly defined syntax. This allows the student to pick up the language quickly.
10. Easy-to-read − Python code is more clearly defined and visible to the eyes.
11. Easy-to-maintain − Python's source code is fairly easy-to-maintained
12. Databases − Python provides interfaces to all major commercial databases.

## 4. Advantages and disadvantages of python
| Advantages      | Disadvantages |
| ----------- | ----------- |
| Readability & Simplicity: code readability, reduces 
the cost of program maintenance and development.      | Performance: Interpreted language perform slowly on computationally intensive tasks      |
| Large standard library: pre-built modules and functions for various tasks such as file I/O, networking, web developement   | Global Interpreter Lock allows only one thread to execute Python bytecode at a time, hence the performance to achieve true parallelism in multi-threaded applications is impacted|
| Cross Platform Compatibility: Can run on different operating systems which makes it convenient for developing applications that need to run on multiple platforms.      | Mobile and Game Development: Although frameworks like Kivy and Pygame exist, they may have limitations compared to platform-specific languages like Java, Kotlin, Swift, or C++ .      |
| Rich Ecosystem and Community Support: supportive community that actively contributes to the development of tools, libraries, and resources. This availability of resources simplifies development tasks and promotes collaboration.  | Memory Consumption: due to its dynamic type system and high-level abstractions, building memory-intensive applications can be a concern|
| Integration Capabilities: seamless integration with other languages like C, C++, and Java. It provides interfaces to popular databases, allowing easy data manipulation and management.     | Design Restrictions: the use of whitespace indentation for code blocks can be a challenge for developers accustomed to other programming languages.      |

## 5. Interpreted vs compiled programming languages
Interpreted and compiled languages are two different approaches to executing computer programs.
| Compiled      | Interpreted |
| ----------- | ----------- |
| **Compilation**: the source code is first passed through a compiler, which translates the entire code into machine-readable instructions called object code or bytecode. The output of the compilation process is usually an executable file or a binary file that can be directly executed by the target machine's processor. | **Interpretation**: In an interpreted language, the source code is directly executed by an interpreter without a separate compilation step. The interpreter reads the code line by line and translates each line into machine instructions or bytecode at runtime. |
| **Execution Process:**: the compiled program is loaded directly into memory and executed by the computer's processor. The machine understands and directly executes the compiled instructions without the need for further translation or interpretation. | **Execution Process**: The interpreter processes and executes each line of code sequentially, translating and executing it on the fly. The interpreter may perform additional tasks like memory management, garbage collection, and error handling during the execution process. |

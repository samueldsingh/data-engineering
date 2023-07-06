# VIII. Loops:
============
## 1. Importance of Loops

## 2. while loop. Explain in detail with different use cases 

## 3. for loop. Explain in detail with different use cases 


## 4. while vs for


## 5. Give examples while with if else combination 


## 6. Give examples for with if else combination


## 7. Control statements.Explain and give examples for each keyword 
    - break 
    - continue
    - pass
  
- Control statements in Python are used to control the flow of execution in a program.
- They allow you to make decisions, repeat certain actions, and alter the normal sequence of execution.
- Python provides several control statements, including conditional statements (`if`, `elif`, `else`), loop statements (`for`, `while`), and control transfer statements (`break`, `continue`, `pass`, `return`).

**Conditional Statements:**
- `if`: The if statement is used to execute a block of code if a specified condition is true.
- `elif`: The elif statement is used to specify additional conditions to be checked if the previous if or elif conditions are false.
- `else`: The else statement is used to specify a block of code to be executed if all the previous if and elif conditions are false.

**Loop Statements:**
- `for`: The `for` loop iterates over a sequence (such as a list, tuple, string, or range) or any other iterable object, executing a block of code for each iteration.
- `while`: The `while` loop repeatedly executes a block of code as long as a specified condition is true.

**Control Transfer Statements:**
- `break`: The `break` statement is used to exit a loop prematurely. It terminates the loop and transfers control to the next statement following the loop.
- `continue`: The `continue` statement is used to skip the current iteration of a loop and move to the next iteration.
- `pass`: The `pass` statement is a placeholder statement that does nothing. It is used when a statement is syntactically required but you don't want any code to be executed.
- `return`: The `return` statement is used to exit a function and return a value to the caller.

## 8. Implement 5 examples which covers all topics if elif else for while break/continue/pass

## What is entry control loop and exit control loop?
What is an entry control loop and an exit control loop

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


Control statements allow you to make decisions, control the flow of execution based on conditions, and repeat certain actions. They provide flexibility and control in programming to handle different scenarios and conditions effectively.



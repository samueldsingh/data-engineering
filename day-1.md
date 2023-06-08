## Operators

Python Operators are used to perform operations on variables and values.

Python divides the operators in the following groups:
- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators

## Python Arithmetic Operators
Arithmetic operators are used with numeric values to perform common mathematical operations:
`+, -, *, /, %, **, //`

## Python Assignment Operators
Assignment operators are used to assign values to variables:
`=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=`

## Python Comparison Operators
Comparison operators are used to compare two values:
`==, !=, >, <, >=, <=`

## Python Logical Operators
Logical operators are used to combine conditional statements:
`and, or, not`

## Python Identity Operators
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
`is, is not`

## Python Membership Operators
Membership operators are used to test if a sequence is presented in an object:
`in, not in`

## Python Binary Operators
Bitwise operators are used to compare (binary) numbers:
`&, |, ^, ~, <<, >>`

Example:
```
if a = 7     
   b = 6       
then, binary (a) = 0111      
    binary (b) = 0110      
      
hence, a & b = 0011      
      a | b = 0111      
             a ^ b = 0100      
       ~ a = 1000
```

**AND** Operator: The bitwise **AND** operation, denoted as **&**, is a binary operation that operates on individual bits of two binary numbers. It compares the corresponding bits of the two numbers and **produces a new number where each bit is set to 1 only if both corresponding bits in the original numbers are also 1**. Otherwise, if either bit is 0, the result will have the corresponding bit set to 0.

**XOR (^)** Operator: Sets each bit to 1 if only one of two bits is 1

```print(6 ^ 3)```

The result is:
```5```

Explanation:
```
"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================
"""
```

## Operator Precedence
The precedence order is described in the table below, starting with the highest precedence at the top:
`(), **, +x  -x  ~x, *  /  //  %, +  -,  <<  >>, &, ^, |, ==  !=  >  >=  <  <= is  is not  in  not in, not, and, or`

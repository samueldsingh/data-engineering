
Programs:
----------
- Between 1 to 100
    
## 1. Print all numbers
```
for number in range(1, 101):
    print(number)
```

## 2. Print even numbers
```
for number in range(1, 101):
    if number % 2 == 0:
        print(number)
```
    
## 3. Print odd numbers 
```
for number in range(1, 101):
    if number % 2 != 0:
        print(number)
```
    
## 4. Print all prime numbers
```
# for number in range (lower_value, upper_value + 1):     # suppose lower range is 10 and upper range is 20
#     if number > 1:
#         for i in range (2, number):     # loop iterates from 2 to 9, excluding 10
#             if (number % i) == 0:       # 10 is divisible by 2 so loop breaks
#                 break
#         else:
#             print (number)
```
    
## 5. Print numbers with power of 2 (1 2 4 8 16 32 64)
```
n = int(input("Enter the number of terms: "))

for i in range(n):
    number = 2 ** i
    print(f"{i}: {number}")
```
    
## 6. Print all numbers which are divisible by 5 and 7 
```
print("Numbers divisible by 5 and 7:")
for number in range(1, 101):
    if number % 5 == 0 and number % 7 == 0:
        print(number)
```
    
## 7. Print all numbers which are divisible by 4 or 6
```
print("Numbers divisible by 4 or 6:")
for number in range(1, 101):
    if number % 4 == 0 or number % 6 == 0:
        print(number)
```
    
## 8. Print first 14 odd numbers 
```
print("First 14 odd numbers:")
count = 0
number = 1

while count < 14:
    if number % 2 != 0:
        print(number)
        count += 1
    number += 1
```

## 9. Print first 23 even numbers
```
print("First 23 even numbers:")
count = 0
number = 2

while count < 23:
    print(number)
    count += 1
    number += 2
```

## 10. Print first 6 numbers which are divisible by 4 and 6
```
print("First 6 numbers divisible by 4 and 6:")
count = 0
number = 1

while count < 6:
    if number % 4 == 0 and number % 6 == 0:
        print(number)
        count += 1
    number += 1
```
   
## 11. Print all numbers except divisible by 9
```
print("Numbers not divisible by 9:")
for number in range(1, 101):
    if number % 9 != 0:
        print(number)
```
   
## 12. Write for loop to explain all data structures.
```

```



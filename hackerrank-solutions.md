## Python Hackerrank

#### 1. Python If-else

Task

Given an integer, *n*, perform the following conditional actions:

- If n is odd, print Weird

* If n is even and in the inclusive range of 2 to 5, print ```Not Weird```
* If n is even and in the inclusive range of 6 to 20, print ```Weird```

* If n is even and greater than 20, print ```Not Weird```

**Input Format**
A single line containing a positive integer, *n*.

**Constraints**

$$ 1 \le n \le 100 $$

**Output Format**

Print ```Weird``` if the number is weird. Otherwise, print ```Not Weird```.

```
import sys                              #provides access to some variables used or maintained by the interpreter 
n = int(input().strip())                #remove leading and trailing whitespace characters from a string
if n % 2 == 1 or n in range(5, 21):
    print("Weird")
else:
    print("Not Weird")
```

The value of n is:
```
n=3
```

The output is:
```
Weird
```

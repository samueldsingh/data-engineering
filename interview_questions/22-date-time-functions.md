
## 1. What modules are available in Python for working with date and time?

In Python, date and time are not data types of their own, but a module named `DateTime` can be imported to work with the date as well as time. 
Python `Datetime` module comes built into Python, so there is no need to install it externally.

## Datetime module

Python `DateTime` module supplies classes to work with date and time. These classes provide a number of functions to deal with dates, times, and time 
intervals. `Date` and `DateTime` are an object in Python, so when you manipulate them, you are actually manipulating objects and not strings or timestamps. 

The `DateTime` module is categorized into 6 main classes:

1. `date`: The object of the Date class represents the naive date containing year, month, and date according to the current Gregorian calendar. 
The syntax is: `class datetime.date(year, month, day)`.

```
# initializing constructor and passing arguments in the format year, month, date

from datetime import date
my_date = date(2023, 9, 8)
print("Date passed as argument is", my_date)    # Output: Date passed as argument is 2023-09-08

# Example 2: Accessing the year, month, and date attribute from the date class

# creating the date object
Date = date(2023, 9, 8)

Accessing the attributes
print("Year -",Date.year)       # Output: Year - 2023
print("Month -",Date.month)     # Output: Month - 9
print("Day -",Date.day)         # Output: Day - 8


# Example 3: Getting the current date and casting the date to string

today = date.today()

print("Today's date is", today)         # Output: Today's date is 2023-09-08

# Converting the date to the string
Str = date.isoformat(today)
print("String Representation", Str)     # Output: String Representation 2023-09-08
print(type(Str))                        # Output: <class 'str'>
```

[DateTime - GFG](https://www.geeksforgeeks.org/python-datetime-date-class/)


2. `time`: Time class represents the local time of the day which is independent of any particular day. This class can have the tzinfo
   object which represents the timezone of the given time. If the tzinfo is None then the time object is the naive object otherwise it is the aware object.

```
from datetime import time

# calling the constructor
my_time = time(12, 14, 36)          

print("Entered time", my_time)          # Output: Entered time 12:14:36

# calling constructor with 1 argument
my_time = time(minute=12)
print("\nTime with one argument", my_time)      # Output: Time with one argument 00:12:00

# Calling constructor with 0 argument
my_time = time()
print("\nTime without argument", my_time)       # Output: Time without argument 00:00:00
```

[GFG - Time Class](https://www.geeksforgeeks.org/python-datetime-time-class/)

3. `DateTime`: Its a combination of date and time along with the attributes year, month, day, hour, minute, second, microsecond, and tzinfo.

```
from datetime import datetime

# Initializing constructor
a = datetime(2022, 10, 22)
print(a)

# Initializing constructor with time parameters as well
a = datetime(2022, 10, 22, 6, 2, 32, 5456)
print(a)
```

[GFG - DateTime](https://www.geeksforgeeks.org/python-datetime-datetime-class/)

4. `TimeDelta`: A duration expresses the difference between two date, time, or datetime instances to microsecond resolution. Timedelta class is used for calculating differences between dates and represents a duration.

```
# Timedelta function demonstration

from datetime import datetime, timedelta

# creating datetime objects
date1 = datetime(2023, 1, 3)
date2 = datetime(2023, 2, 3)

# difference between dates
diff = date2 - date1
print("Difference in dates:", diff)      # Output: Difference in dates: 31 days, 0:00:00

# Adding days to date1
date1 += timedelta(days = 4)
print("Date1 after 4 days:", date1)      # Output: Date1 after 4 days: 2023-01-07 00:00:00

# Subtracting days from date1
date1 -= timedelta(15)
print("Date1 before 15 days:", date1)    # Output: Date1 before 15 days: 2022-12-23 00:00:00

# Timedelta class provides only one function which is total_seconds(). This method returns the
# duration provided by the timedelta object in the number of seconds.

from datetime import timedelta

# Getting minimum value
obj = timedelta(hours=1)
print(obj.total_seconds())         # Output: 3600.0

obj = timedelta(minutes=1)
print(obj.total_seconds())         # Output: 60.0

obj = timedelta(days=1)
print(obj.total_seconds())         # Output: 86400.0
```

Operations supported by Timedelta Class are Addition (+), Subtraction (-), Multiplication (*), Division (/), Floor division (//), Modulo (%), +(timedelta),
-(timedelta), abs(timedelta), str(timedelta), repr(timedelta)

```

from datetime import timedelta

# creating the timedelta object
t1 = timedelta(days=1)
print("Original timedelta:", t1)        # Output: Original timedelta: 1 day, 0:00:00

# multiplication
t2 = t1*5.5
print("After Multiplication:", t2)      # Output: After Multiplication: 5 days, 12:00:00

# Subtraction
res = t2 - t1
print("After Subtraction:", res)        # Output: After Subtraction: 4 days, 12:00:00

# addition
res += t2
print("After Addition:", res)           # Output: After Addition: 10 days, 0:00:00

# division
res = t2/2.5
print("After division:", res)           # Output: After division: 2 days, 4:48:00

# floor division
res = t2 //2
print("After floor division:", res)     # Output: After floor division: 2 days, 18:00:00

# Modulo
res = t2%timedelta(days=3)
print("After Modulo:", res)             # Output: After Modulo: 2 days, 12:00:00
```



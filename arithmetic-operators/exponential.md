## Examples of exponential operations

## I. Based on count
### 1. 2 numbers  (Compound Interest Problem)

```
def calculate_compound_interest(principal, interest_rate, time):
    amount = principal * (1 + interest_rate) ** time
    return amount

principal = 1000
interest_rate = 0.05
time = 3

final_amount = calculate_compound_interest(principal, interest_rate, time)


print(f"The final amount after {time} years is: {final_amount}")
```

The output is:

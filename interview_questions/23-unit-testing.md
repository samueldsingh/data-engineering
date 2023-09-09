
## Addition Test Case

```
class Addition:
    def __init__(self):
        pass
    def add_nums(self, num1, num2):
        result = num1 + num2
        return result

obj = Addition()
print("Addition result:", obj.add_nums(10,20))

# Output is:
Addition result: 30
```

The test file is:

```
from unittest import TestCase
from _22_UnitTesting._2_testing_addition.adding import Addition


class TestAddition(TestCase):

    # the setUp method is a special method in unit testing that is run before each test method in a test class.
    # ensure that each test starts with a clean and consistent state, making the tests more reliable and isolated from each other.

    def setUp(self) -> None:        # This method is part of the test case setup. It specifies setUp methods doesn't return any value
        self.obj = Addition()       # instance of the Addition class is created and stored in self.obj.
                                    # This allows you to reuse this object in multiple test methods.

    def test_add_nums(self):
        n1 = 11
        n2 = 21
        exp_res = 32
        act_res = self.obj.add_nums(n1, n2)
        self.assertEqual(exp_res, act_res, "Both should be equal")

# Output:

============================= test session starts =============================
collecting ... collected 1 item

test_adding.py::TestAddition::test_add_nums PASSED                       [100%]

============================== 1 passed in 0.08s ==============================

Process finished with exit code 0
```

# import pytest
"""Write a function which calculates a given element of Fibonacci sequence.
Fibonacci sequence is defined as follows:
- F(0) = 0
- F(1) = 1
- F(x) = F(x-1) + F(x-2)
Hint: F(2) = F(1) + F(0) = 1 + 0 = 1,  F(3) = F(2) + F(1)...
"""


def fibonacci(x):
    if x == 0 or x == 1:
        return x
    return fibonacci(x - 1) + fibonacci(x - 2)


# @pytest.mark.parametrize(
#     "x,result",
#     ((0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (10, 55)),
# )
# def test_fibonacci(x, result):
#     assert fibonacci(x) == result

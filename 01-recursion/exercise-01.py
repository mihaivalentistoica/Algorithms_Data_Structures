import pytest

"""Write a function which returns a sum of integers in a given list recursively
Hint: sum(list) = list[0] + sum(list[1:])…"""


def recursive_sum(l):
    if len(l) == 0:
        return 0
    if len(l) == 1:
        return l[0]
    return l[0] + recursive_sum(l[1:])


@pytest.mark.parametrize("l", ([], [-1], [0], [1, 2, 3], list(range(15)), [798, 1, -17]))
def test_recursive_sum(l):
    assert recursive_sum(l) == sum(l)

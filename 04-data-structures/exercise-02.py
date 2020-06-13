"""
1. Implement a function which uses stack to check whether any sequence of parantheses (), braces {} or brackets [] is matching.
2. Each opening symbol must have a corresponding closing symbol.

Hint: opening symbol should be pushed to the stack; closing symbol pops a symbol from the stack and checks for match
"""
import pytest


class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, v):
        self.__stack.append(v)

    def pop(self):
        return self.__stack.pop()

    def __len__(self):
        return len(self.__stack)

    def is_empty(self):
        return self.__stack == []


def matching_brackets(sequence):
    s = Stack()
    matching_symbols = {"{": "}", "(": ")", "[": "]"}
    for symbol in sequence:
        if symbol in r"([{":
            s.push(symbol)
            continue
        if symbol != matching_symbols[s.pop()]:
            return False
    return s.is_empty()


@pytest.mark.parametrize(
    "sequence,expected",
    [
        (r"()", True),
        (r"[]", True),
        (r"{}", True),
        (r"{{({[]})}}", True),
        (r"{([])([])}", True),
        (r"(", False),
        (r"({[(]})", False),
    ],
)
def test_matching_brackets(sequence, expected):
    assert matching_brackets(sequence) is expected

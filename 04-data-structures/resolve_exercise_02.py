"""
1. Implement a function which uses stack to check whether any sequence of parantheses (), braces {} or brackets [] is matching.
2. Each opening symbol must have a corresponding closing symbol.

Hint: opening symbol should be pushed to the stack; closing symbol pops a symbol from the stack and checks for match
"""


class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, elem):
        self.__stack.append(elem)

    def pop(self):
        self.__stack.pop()



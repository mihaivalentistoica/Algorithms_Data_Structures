class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, element):
        self.__stack.append(element)

    def pop(self):
        return self.__stack.pop()

    def __len__(self):
        return len(self.__stack)

    def is_empty(self):
        return len(self.__stack) == 0

history = Stack()

history.push("Google")
history.push("Yahoo")


print(history.pop())
history.push("Amazon")

print(history.__stack)
print(history.__len__())

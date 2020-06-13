class Queue:
    def __init__(self):
        self.__queue = []

    def push(self, v):
        self.__queue.append(v)

    def pop(self):
        return self.__queue.pop(0)

    def __len__(self):
        return len(self.__queue)

    def is_empty(self):
        return self.__queue == []

    def __str__(self):
        return str(self.__queue)


q = Queue()
q.push(3)
q.push(7)
q.push(-1)
print(q.pop())
print(q.pop())
q.push(5)
print(q.pop())
print(q)

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


q = Queue()
print(f"The queue is empty - {q.is_empty()}")
q.push("first")
q.push("second")
print(f"Queue size - {len(q)}")
print(q.pop())
print(q.pop())

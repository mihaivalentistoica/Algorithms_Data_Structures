class LinkedElement:
    def __init__(self, value, prev=None, next_=None):
        self.value = value
        self.prev = prev
        self.next = next_

    def __str__(self):
        next_str = str(self.next) if self.next else ""
        return f"<-> {self.value} {next_str}"


class LinkedList:
    def __init__(self):
        self.__first = None

    def _get_last_element(self):
        if self.__first is None:
            return None
        current = self.__first
        while True:
            if current.next is None:
                return current
            current = current.next

    def append(self, value):
        elem = LinkedElement(value)
        if self.__first is None:
            self.__first = elem
            return
        last = self._get_last_element()
        last.next = elem
        elem.prev = last

    def __len__(self):
        if self.__first is None:
            return 0
        current = self.__first
        elements = 1
        while True:
            if current.next is None:
                return elements
            current = current.next
            elements += 1


l = LinkedList()
l.append(1)
l.append(2)
print(f"List length: {len(l)}")
l.append(3)
print(f"List length: {len(l)}")

# 1.Write a function which returns second-to-last (penultimate) element of a doubly linked list
# 2.Write a function which implements extension of a linked list by another list. Functionally it should be the same as list.extend()
# 3.*Write a function which iterates over the linked list and prints its contents.


class LinkedElement:
    def __init__(self, value, prev=None, next_=None):
        self.value = value
        self.prev = prev
        self.next = next_

    def __str__(self):
        prev_str = "<->" if self.prev else ""
        next_str = str(self.next) if self.next else ""
        return f"{prev_str} {self.value} {next_str}"


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

    def second_to_last(self):
        last = self._get_last_element()
        if last is None:
            return None
        return last.prev

    def append(self, value):
        elem = LinkedElement(value)
        if self.__first is None:
            self.__first = elem
            return
        last = self._get_last_element()
        last.next = elem
        elem.prev = last

    def get_first(self):
        return self.__first

    def extend(self, linked_list):
        ll_first = linked_list.get_first()
        if self.__first is None:
            self.__first = ll_first
            return
        last = self._get_last_element()
        last.next = ll_first
        if last.next is not None:
            ll_first.prev = last

    def print(self):
        print(str(self.__first))

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


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

ll2 = LinkedList()
ll.append(4)
ll.append(5)
ll.extend(ll2)

ll.print()

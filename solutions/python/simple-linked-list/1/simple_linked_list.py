"""linked list module"""
class EmptyListException(Exception):
    """Exception raised when the linked list is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class Node:
    """node for linked list"""
    def __init__(self, value, next=None):
        self._value = value
        self._next = next

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    """simple linked list class"""
    def __init__(self, values=None):
        self.values = None
        if values is not None:
            for v in values:
                self.push(v)

    def __iter__(self):
        current = self.values
        while current is not None:
            yield current.value()
            current = current.next()

    def __len__(self):
        result = 0
        item = self.values
        while item is not None:
            result += 1
            item = item.next()
        return result

    def head(self):
        if self.values is None:
            raise EmptyListException("The list is empty.")
        return self.values

    def push(self, value):
        hold = self.values
        self.values = Node(value, hold)

    def pop(self):
        if self.values is None:
            raise EmptyListException("The list is empty.")
        hold = self.values
        self.values = hold.next()
        return hold.value()
        
    def reversed(self):
        result = LinkedList()
        current = self.values
        while current is not None:
            result.push(current.value())
            current = current.next()
        return result

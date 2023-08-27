class linked_node:
    def __init__(self, data=None, next= None):
        self._data = data
        if next is None or isinstance(next, linked_node):
            self._next = next
        else:
            raise TypeError("Node type object expected")
        
        
        @property
        def data(self):
            return self._data

        @data.setter
        def data(self, value):
            self._data = value

        @property
        def tail(self):
            return self._next
        
        @tail.setter
        def tail(self, node):
            if node is None or isinstance(node, linked_node):
                self._next = node
            else:
                raise TypeError("Node type object expected")
            
class linked_list:
    def __init__(self):
        self._front = None
        self._tail = None
        self._size = 0
        
    def append(self, value):
        newNode = linked_node(value)
        if self._front is None:
            self._front = newNode
            self._front = newNode
        else:
            self._tail._next = newNode
            self._tail = newNode
            
        self._size += 1
        
    def pop(self):
        if self._size == 0:
            raise IndexError
        front_node = self._front
        self._front = self._front._next
        front_node._next = None
        self._size -= 1
        return front_node._data



class stack:
    def __init__(self):
        self._top = None
        self._size = 0
    
    def __str__(self):
        values = []
        current_node = self._top
        for x in range(0, self._size):
            next_node = current_node._next
            values.append(current_node._data)
            current_node = next_node
        return f"LinkedStack({values})"

    def __len__(self):
        return self._size
    
    def push(self, value):
        newNode = linked_node(value)
        if self._size == 0:
            self._top = newNode
        else:
            newNode._next = self._top
            self._top = newNode
        self._size += 1
        
    def pop(self):
        if self._size == 0:
            raise IndexError("list has no items")
        top_node = self._top
        self._top = self._top._next
        top_node._next = None
        self._size -= 1
        return top_node._data
    
    def peek(self):
        if self._size == 0:
            raise IndexError("list has no items")
        top_node = self._top
        return top_node._data
    
    def isempty(self):
        if self._size == 0:
            return True
        elif self._size > 0:
            return False
        else:
            raise IndexError("size of list is impossible value")
        
myStack = stack()
myStack.push(3)
myStack.push(6)
myStack.push(2)
myStack.push(5)
print(myStack)
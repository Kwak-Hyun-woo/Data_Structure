class EmptyException(Exception):
   """Raised when the input value is too large"""
   pass

class ArrayStack: # Space used: O(n)
    def __init__(self):
        self._data = []   # O(1)
    
    def __len__(self):
        return len(self._data) # O(1)


    def is_empty(self):
        return len(self._data) == 0  # O(1)
    
    def push(self, e):
        self._data.append(e)   # O(1)*

    def top(self):
        if self.is_empty():
            raise EmptyException('Stack is empty')
        return self._data[-1] # O(1)

    def pop(self):
        if self.is_empty():
            raise EmptyException('Stack is empty')
        return self._data.pop()  # O(1)*, same to self._data.pop(-1)

    def display(self):
        data_visaulized = ''.join(self._data)
        print(f'STACK: B|{data_visaulized}|T')

    def display_complex(self):
        data_visaulized = ','.join(list(map(lambda x: str(x), self._data)))
        print(f'STACK: B|{data_visaulized}|T')


class ArrayQueue: # Space used: O(n)
    DEFAULT_CAPACITY = 10

    def __init__(self, capacity=DEFAULT_CAPACITY):
        self._data = [None] * capacity
        self._size = 0
        self._front = 0

    def __len__(self): # O(1)
        return self._size
    
    def is_empty(self): # O(1)
        return self._size == 0

    def first(self): # O(1)
        if self.is_empty():
            raise EmptyException('Queue is empty')
        return self._data[self._front]

    def dequeue(self):   # O(1)*
        if self.is_empty():
            raise EmptyException('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None  # help garbage collection

        self._front = (self._front+1) % len(self._data)
        self._size -= 1
        
        return answer

    def enqueue(self, e): # O(1)*
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap): # O(n)
        old = self._data
        self._data = [None] * cap
        walk = self._front
        
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1+walk) % len(old)
        self._front = 0

    def display(self):
        array_for_display = ''.join(['.' if v is None else v for v in self._data])
        indicator = ''.join([' ']*self._front)

        print(f'QUEUE: |{array_for_display}|')
        print(f'        {indicator}^')
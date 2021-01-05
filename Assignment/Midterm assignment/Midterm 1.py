class LList:
    ## Start: Nested Node class, not visible from outside ----------------------
    class _Node:
        __slots__ = '_element', '_next'  # Optional: assign memory space for the member variables, faster!

        def __init__(self):
            self._element = None
            self._next = None

        def __init__(self, element, nxt):
            self._element = element
            self._next = nxt

    ## End: Nested Node class ----------------------

    __slots__ = '_head', '_tail', '_size'

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __str__(self):
        obj = self._head
        ret_str = f'{len(self)}: ['
        while obj != None:
            ret_str += str(obj._element)
            obj = obj._next
            if obj != None:
                ret_str += ','

        ret_str += ']'
        return ret_str

    def __repr__(self):
        return self.__str__()

    def is_empty(self):
        return len(self) == 0

    def add_first(self, obj):
        new_node = self._Node(obj, self._head)
        self._head = new_node
        self._size += 1

        if self._size == 1:
            self._tail = self._head

    # Add element at the tail of the list
    def add_last(self, obj):
        new_node = self._Node(obj, None)

        if len(self) == 0:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail._next = new_node
            self._tail = new_node

        self._size += 1

    # Add an element at the given position
    def add(self, pos, obj):
        # Three cases: insert at the head, or insert at the tail, or insert at the middle of the list.
        if pos == 0:
            self.add_first(obj)
        elif pos == len(self):
            self.add_last(obj)
        else:
            prev = None
            current = self._head
            for i in range(0, pos):
                prev = current
                current = current._next

                if current == None:
                    raise IndexError

            new_node = self._Node(obj, current)
            prev._next = new_node
            self._size += 1

    def get(self, pos):
        current = self._head
        for i in range(0, pos):
            current = current._next
            if current == None:
                raise IndexError
        return current._element

    def removeAt(self, pos):
        # Three cases: remove at the head, or remove at the tail, or insert at the middle of the list.
        if pos < 0 or pos >= len(self):
            raise IndexError

        prev = self._head
        current = self._head

        for i in range(0, pos):
            prev = current
            current = current._next

        if current == self._head:
            self._head = current._next
        if current == self._tail:
            self._tail = prev

        prev._next = current._next
        self._size -= 1

    def remove(self, obj):
        prev = None
        current = self._head

        while current != None:
            if current._element == obj:
                if current == self._head:
                    self._head = current._next
                if current == self._tail:
                    self._tail = prev
                if prev != None:
                    prev._next = current._next

                self._size -= 1
                return

            prev = current
            current = current._next

        raise LookupError

    def reverse(self):
        bool = True
        if len(self) <= 1:  # LList에 원소가 하나 또는 없을 때 reverse해도 같으므로 그대로 반환
            return self

        def switch(LList, bool, head=None):
            prev = None
            current = LList._head
            while current != LList._tail:  # 이전의 노드가 무엇인지 찾음
                prev = current
                current = current._next
            current._next = prev
            if bool:
                head = LList._tail
                bool = False
            prev._next = None
            LList._tail = prev
            if LList._head == LList._tail:  # 종료조건
                LList._head = head
            else:
                switch(LList, bool, head)  # 처음 head를 할당해준 값을 마지막 loop에서 활용하기 위해 argument에 head값을 새로 넣음
            return LList

        result = switch(self, bool)
        return result

#------------test code--------
a = LList()
a.add_last(1)
a.add_last(2)
a.add_last(4)
a.add_last(10)
a.add_last(7)
a.add_last(8)
print(a.reverse())
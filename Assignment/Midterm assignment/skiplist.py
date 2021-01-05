from collections import MutableMapping
import math, random, time
import matplotlib.pyplot as plt


class SkipList(MutableMapping):
    __slots__ = '_head', '_tail', '_n', '_height'

    # ------------------------------- nested _Node class -------------------------------
    class _Node:
        __slots__ = '_key', '_value', '_next'

        """Lightweight composite to store key-value pairs as map items."""

        def __init__(self, k, v, height):
            self._key = k
            self._value = v
            self._next = [None] * (height)

        def __eq__(self, other):
            if other == None:
                return False
            return self._key == other._key  # compare items based on their keys

        def __ne__(self, other):
            return not (self == other)  # opposite of __eq__

        def __lt__(self, other):
            return self._key < other._key  # compare items based on their keys

    def __init__(self):
        """Create an empty map."""
        self._head = self._Node(-math.inf, None, 1)  # Head: the first node in a skip list
        self._tail = self._Node(math.inf, None, 1)  # Tail: the last node in a skip list
        self._head._next[0] = self._tail  # Initially, there's no item -> head is directly linked to the tail
        self._n = 0  # Initially, there's no item, so _n = 0
        self._height = 1  # Initially, the height of a skip list is 1

    def __getitem__(self, k, update=None):
        """Return value associated with key k (raise KeyError if not found).--Search"""
        if k == -math.inf:
            return self._head._value
        find = self._head
        i = self._height
        while i != 0:
            if find._next[i - 1]._key == k:
                break
            while find._next[i - 1]._key < k:
                find = find._next[i - 1]
            i -= 1
        if i == 0:
            if find._next[i]._key != k:
                if update == None:
                    raise KeyError("There is no item with key k in this SkipList")
                else:
                    return update
            else:
                return find._next[i]._value
        return find._next[i - 1]._value

    def Prev_nodes(self, k):  # k값보다 작은값 중에 최대의 key값을 가지고 있는 node들을 list 형태로 반환
        result = [None] * self._height
        find = self._head
        i = self._height
        while i != 0:
            while find._next[i - 1]._key < k:
                find = find._next[i - 1]
            result[i - 1] = find
            i -= 1
        return result


    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present.--Insert"""
        tower_height = 1
        while random.randint(1, 2) != 2:
            tower_height += 1
        node = self._head
        while node != None:
            t = tower_height + 1
            while t > self._height:
                node._next.append(None)
                t -= 1
            node = node._next[0]

        h = max(self._height, tower_height + 1)
        new_node = self._Node(k, v, h)
        position = self.Prev_nodes(k)  # type: List
        if position[0]._next[0]._key == k:
            position[0]._next[0]._value = v
        else:
            if tower_height >= self._height:
                for i in range(self._height):
                    new_node._next[i] = position[i]._next[i]
                    position[i]._next[i] = new_node
                for i in range(self._height - 1, tower_height):
                    self._head._next[i] = new_node
                    new_node._next[i] = self._tail
                self._head._next[tower_height] = self._tail
                self._height = h
            else:
                for i in range(tower_height):
                    new_node._next[i] = position[i]._next[i]
                    position[i]._next[i] = new_node
            self._n += 1

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found).--Delete"""
        position = self.Prev_nodes(k)
        if position[0]._next[0]._key != k:  # raise Error
            raise KeyError("There is no item with key k in this SkipList")
        else:
            for i in range(len(position)):  # item을 del하는 과정
                if position[i]._next[i]._key == k:
                    del_node = position[i]._next[i]
                    position[i]._next[i] = del_node._next[i]
            while self._height != 1 and self._head._next[self._height - 2] == self._tail:  # 원소를 del하고 높이를 하나씩 줄여가는 과정
                node = self._head
                while node != None:
                    node._next.remove(node._next[self._height - 1])
                    node = node._next[0]
                self._height -= 1
            self._n -= 1

    def __len__(self):
        """Return number of items in the map."""
        return self._n

    def __iter__(self):
        """Generate iteration of the map's keys."""
        # iterate over the base height (=> height = 0)
        node = self._head._next[0]
        while not node is self._tail:
            yield node._key
            node = node._next[0]

    def print_tree(self):
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^')
        node = self._head
        while node != None:
            print('#', end='\t')
            for i in range(self._height):
                lnk = node._next[i]

                if node is self._tail:
                    print_val = '+'
                elif lnk == None:
                    print_val = '.'
                elif node._key == -math.inf:
                    print_val = '-'
                elif node._key == math.inf:
                    print_val = '+'
                else:
                    print_val = node._key

                print(print_val, end='\t')
            print()
            node = node._next[0]

        for h in reversed(range(self._height)):
            print(f"At height #{h}, ", end='')
            node = self._head
            while node != None:
                print(node._key, end=' -> ')
                node = node._next[h]
            print()
        print('vvvvvvvvvvvvvvvvvvvvvvvvvv')




#-----test code------
L = SkipList()
last_key = 0
for i in range(30):
    key = random.randrange(20)
    value = random.randrange(10000)
    print(f'Adding L[{key}] = {value}')
    L[key] = value
    last_key = key
L.print_tree()

print(L[last_key], "# This should be the same to the lastly inserted value")
L[last_key] = 123456789
print(L[last_key], "# This should be 123456789")

print('\nLet\'s iterate through the keys')
for key in L.keys():
    print(key)

print('\nLet\'s delete all the keys, one by one')

del_order = random.sample(list(L), int(len(L)/2))
for k in del_order:
    print(f"Deleting the key {k}")
    del L[k]

L.print_tree()

del_order = random.sample(list(L), len(L))
for k in del_order:
    print(f"Deleting the key {k}")
    del L[k]
L.print_tree()

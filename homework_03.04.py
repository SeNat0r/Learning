import copy


class Node(object):
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n


class LinkedLIst(object):
    def __init__(self, r=None):
        self.root = r
        self.size = 0
        self.i = 0

    def show(self):
        node = self.root
        while node:
            print(node.data)
            node = node.next_node

    def __getitem__(self, item):
        i = 0
        node = self.root
        if item <= self.size:
            while i != item:
                i += 1
                node = node.next_node
            return node.data
        else:
            raise IndexError('index out of range')

    def __setitem__(self, key, value):
        i = 0
        node = self.root
        if key <= self.size:
            while i != key:
                i += 1
                node = node.next_node
        else:
            raise IndexError('index out of range')
        node.data = value

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == self.size:
            raise StopIteration
        else:
            i = self.i
            self.i += 1
            return self[i]

    def __contains__(self, item):
        node = self.root
        while node:
            if node.data == item:
                return True
            node = node.next_node

    def __len__(self):
        return self.size

    def __add__(self, other):
        new_list = self
        for b in other:
            new_list.add(b)
        return new_list

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1


class DLNode(object):
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p


class DoubleLinkedLIst(object):
    def __init__(self, r=None):
        self.root = r
        self.size = 0
        self.i = 0

    def show(self):
        node = self.root
        while node:
            print(node.data)
            node = node.next_node

    def __getitem__(self, item):
        i = 0
        node = self.root
        if item <= self.size:
            while i != item:
                i += 1
                node = node.next_node
            return node.data
        else:
            raise IndexError('index out of range')

    def __setitem__(self, key, value):
        i = 0
        node = self.root
        if key <= self.size:
            while i != key:
                i += 1
                node = node.next_node
        else:
            raise IndexError('index out of range')
        node.data = value

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == self.size:
            raise StopIteration
        else:
            i = self.i
            self.i += 1
            return self[i]

    def __contains__(self, item):
        node = self.root
        while node:
            if node.data == item:
                return True
            node = node.next_node

    def __len__(self):
        return self.size

    def __add__(self, other):
        new_list = self
        for b in other:
            new_list.add(b)
        return new_list

    def add(self, d):
        new_node = DLNode(d, self.root)
        if self.root:
            self.root.prev_node = new_node
        self.root = new_node
        self.size += 1
        new_node.idx = self.i
        self.i += 1


l = LinkedLIst()
l.add(3)
l.add(10)
l.add('42')
l.add('ололо')
# print(len(l))
# print(l[0])

# print('ололо' in l)

t = LinkedLIst()
t.add('проверка1')
t.add('проверка2')

new = l + t
# new.show()
# for m in l:
#     print(m)

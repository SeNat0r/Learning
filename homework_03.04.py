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

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.size:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

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

    def __len__(self):
        return self.size

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1


l = LinkedLIst()
l.add(3)
l.add(10)
l.add('42')
l.add('ололо')
# print(len(l))
# a = iter(l)
# print(next(a))
# print(next(a))
# print(next(a))
print(l[0])


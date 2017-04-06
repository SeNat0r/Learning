import copy


class Node(object):
    """Создание ячейки с данными и ссылкой на следующую ячейку"""
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n


class LinkedLIst(object):
    """
    Односвязный список:
    Содержит:
        ссылку на последнюю ячейку
        ссылку на корневую ячейку
        размер списка
        вспомогательюную индексацию ячейки
    """
    def __init__(self, r=None):
        self.last = r
        self.root = None
        self.size = 0
        self.i = 0

    def show(self):
        """Вывод списка"""
        node = self.root
        while node:
            print(node.data)
            node = node.next_node

    def __getitem__(self, item):
        """
        Индексация списка:
            Итерация по списку с помощью корневой ячейки и ссылок на последующие
        """
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
        """Замена значений по индексу"""
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
        """Итератор"""
        if self.i == self.size:
            raise StopIteration
        else:
            i = self.i
            self.i += 1
            return self[i]

    def __contains__(self, item):
        """Проверка вхождения значения"""
        node = self.last
        while node:
            if node.data == item:
                return True
            node = node.next_node

    def __len__(self):
        return self.size

    def __add__(self, other):
        """Сложение списков, создающее новый список"""
        new_list = self
        for b in other:
            new_list.add(b)
        return new_list

    # def add(self, d):
    #     new_node = Node(d, self.root)
    #     self.root = new_node
    #     self.size += 1

    def add(self, d):
        """Добавление новой ячейки в конец списка"""
        node = self.last
        new_node = Node(d)
        if node:
            node.next_node = new_node
        self.last = new_node
        if self.size == 0:
            self.root = new_node
        self.size += 1

    def insert(self, d, i):
        """Вставка ячейки по индексу"""
        idx = 1
        node = self.root
        if i <= self.size and i != 0:
            while idx != i:
                idx += 1
                node = node.next_node
            new_node = Node(d, node.next_node)
            node.next_node = new_node
            self.size += 1
        elif i == 0:
            new_node = Node(d, self.root)
            self.root = new_node
            self.size += 1
        else:
            raise IndexError('index out of range')


class DLNode(object):
    """
    Создание ячейки с данными и ссылкой на следующую и предыдущую ячейку
    """
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p


class DoubleLinkedLIst(object):
    """
    Двусвязный список:
    Содержит:
        ссылку на последнюю ячейку
        ссылку на корневую ячейку
        размер списка
        вспомогательюную индексацию ячейки
    """
    def __init__(self, r=None):
        self.last = r
        self.root = None
        self.size = 0
        self.i = 0

    def show(self):
        """Вывод списка"""
        node = self.root
        while node:
            print(node.data)
            node = node.next_node

    def __getitem__(self, item):
        """
        Индексация списка:
            Итерация по списку с помощью корневой ячейки и ссылок на последующие
        """
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
        """Замена значений по индексу"""
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
        """Итератор"""
        if self.i == self.size:
            raise StopIteration
        else:
            i = self.i
            self.i += 1
            return self[i]

    def __contains__(self, item):
        """Проверка вхождения значения"""
        node = self.last
        while node:
            if node.data == item:
                return True
            node = node.next_node

    def __len__(self):
        return self.size

    def __add__(self, other):
        """Сложение списков, создающее новый список"""
        new_list = DoubleLinkedLIst()
        for a in self:
            new_list.add(a)
        for b in other:
            new_list.add(b)
        return new_list

    def add(self, d):
        """Добавление новой ячейки в конец списка"""
        node = self.last
        new_node = DLNode(d, p=node)
        if node:
            node.next_node = new_node
        self.last = new_node
        if self.size == 0:
            self.root = new_node
        self.size += 1

    def insert(self, d, i):
        """Вставка ячейки по индексу"""
        idx = 1
        node = self.root
        # print(node)
        if i <= self.size and i != 0:
            while idx != i:
                idx += 1
                node = node.next_node
                # print('node', node.prev_node)
            new_node = DLNode(d, n=node.next_node, p=node)
            # print(new_node)
            node.next_node = new_node
            # print(node.prev_node)
            self.size += 1
        elif i == 0:
            new_node = DLNode(d, n=self.root)
            node.prev_node = new_node
            self.root = new_node
            self.size += 1
        else:
            raise IndexError('index out of range')


l = LinkedLIst()
l.add(3)
l.add(10)
l.add('42')
l.add('ололо')
# print(len(l))
# l[1] = '1`31231231'
# print(l[1])

# print('ололо' in l)
#
t = DoubleLinkedLIst()
t.add('проверка1')
t.add('проверка2')
t.add(666)
t.add(11110)
t.add('4231231')
t.add('ололо123123')
# new = l + t
# l.show()
t.insert('добавление', 5)
#
# for m in t:
#     print(m)
t.show()

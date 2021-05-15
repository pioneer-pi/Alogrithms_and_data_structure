class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, a=None):
        self.head = Node(None)  # a dummy head node
        if a:
            for data in a:
                self.insert(data, pos=len(self))  # append nodes to the end

    def __len__(self):
        cur_node = self.head.next
        count = 0
        while cur_node:
            cur_node = cur_node.next
            count += 1
        return count

    def __repr__(self):
        rep = ''
        cur_node = self.head.next
        while cur_node:
            rep += str(cur_node) + ', '
            cur_node = cur_node.next
        if len(rep) > 0:
            rep = rep[:-2]
        return '[' + rep + ']'

    def insert(self, data, pos=0):  # insert data at position pos
        current = self.head.next
        pre = self.head
        count = 0
        while count < pos:
            pre = current
            current = current.next
            count += 1
        node = Node(data)
        node.next = current
        pre.next = node


    def delete(self, pos):  # delete the node at position pos
        if pos == 0:
            self.head.next = self.head.next.next
            return
        current = self.head.next
        pre = self.head
        count = 0
        while count < pos:
            pre = current
            current = current.next
            count += 1
        pre.next = current.next

def insert_sort_linkedlist(a):
    length = len(a)
    current = a.head.next
    for i in range(1,length):
        current = current.next
        node = a.head.next
        for j in range(0,i):
            if current.data <= node.data:
                a.delete(i)
                a.insert(current.data,j)
                break
            else:
                node = node.next
        print(a)
a = LinkedList([87, 61, 3, 89, 98, 65, 15, 60, 21, 36])
insert_sort_linkedlist(a)
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.data)

class BST:
    def __init__(self, root=None):
        self.root = root

    def insert(self, key):
        node = Node(key)
        if self.root == None:
            self.root = node
            return
        previous = None
        current = self.root
        while current != None:
            if current.data > key:
                previous = current
                current = current.left
            else:
                previous = current
                current = current.right
        if key < previous.data:
            previous.left = node
        else:
            previous.right = node

    def search(self, key):
        previous = None
        current = self.root
        while current != None and current.data != key:
            if key < current.data:
                previous = current
                current = current.left
            else:
                previous = current
                current = current.right
        if current == None:
            return None
        else:
            return previous

def range_search(bst,range):
    start = range[0]
    end = range[1]
    result = []
    queue = []
    queue.append(bst.root)
    if start<=bst.root.data <=end:
        result.append(bst.root.data)
    while queue:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
            if  start<=node.left.data <= end:
                result.append(node.left.data)
        if node.right:
            queue.append(node.right)
            if  start<=node.right.data <= end:
                result.append(node.right.data)
    return sorted(result)
keys = [4, 2, 6, 3, 7]

bst = BST()
for key in keys:
    bst.insert(key)

print(range_search(bst, [8, 9]))
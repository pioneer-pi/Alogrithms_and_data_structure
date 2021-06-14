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
            return current

def LCA(bst, x, y):
    if bst.search(x) and bst.search(y):
        x_ancestors = []
        y_ancestors = []
        current = bst.root
        while current.data != x:
            x_ancestors.append(current.data)
            if x < current.data:
                current = current.left
            else:
                current = current.right
        x_ancestors.append(x)
        current = bst.root
        while current.data != y:
            y_ancestors.append(current.data)
            if y < current.data:
                current = current.left
            else:
                current = current.right
        y_ancestors.append(y)
        for i in x_ancestors[::-1]:
            for j in y_ancestors[::-1]:
                if i == j:
                    return i
    else:
        return None

keys = [10, 8, 13, 7, 9, 11, 15]
bst = BST()
for key in keys:
    bst.insert(key)
print(LCA(bst,7,9))
keys = [72, 78, 90, 94, 81, 43, 49, 60, 50, 91]
bst = BST()
for key in keys:
    bst.insert(key)
print(LCA(bst, 91, 81))

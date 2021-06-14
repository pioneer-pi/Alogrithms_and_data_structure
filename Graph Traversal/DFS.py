from pythonds3.basic import stack
class Stack:
    """Stack implementation as a list"""

    def __init__(self):
        """Create new stack"""
        self._items = []

    def is_empty(self):
        """Check if the stack is empty"""
        return not bool(self._items)

    def push(self, item):
        """Add an item to the stack"""
        self._items.append(item)

    def pop(self):
        """Remove an item from the stack"""
        return self._items.pop()

    def peek(self):
        """Get the value of the top item in the stack"""
        return self._items[-1]

    def size(self):
        """Get the number of items in the stack"""
        return len(self._items)
graph = {
    "A":["B","C"],
    "B":["C","E"],
    "C":["D"],
    "D":[],
    "E":["D","A"]
}
def DFS(g,start):
    s = Stack()
    color = dict()
    for i in graph:
        if i not in color:
            color[i] = "White"
    s.push(start)
    color[start] = "Grey"
    # print(start)
    while not s.is_empty():
        pre = s.peek()
        has_child = False
        for i in graph[pre]:
            if color[i] == "White":
                color[i] = "Grey"
                s.push(i)
                has_child = True
                break
        if not has_child:
            color[s] = "Black"
            print(s.pop())
DFS(graph,"A")
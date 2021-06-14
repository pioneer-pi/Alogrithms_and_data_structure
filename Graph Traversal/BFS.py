class Queue:
    """Queue implementation as a list"""

    def __init__(self):
        """Create new queue"""
        self._items = []

    def is_empty(self):
        """Check if the queue is empty"""
        return not bool(self._items)

    def enqueue(self, item):
        """Add an item to the queue"""
        self._items.insert(0, item)

    def dequeue(self):
        """Remove an item from the queue"""
        return self._items.pop()

    def size(self):
        """Get the number of items in the queue"""
        return len(self._items)
graph = {
    "A":["B","C"],
    "B":["C","E"],
    "C":["D"],
    "D":[],
    "E":["D","A"]
}
def BFS(graph,start):
    q = Queue()
    color = dict()
    for i in graph:
        if i not in color:
            color[i] = "White"
    q.enqueue(start)
    color[start] = "Grey"
    while not q.is_empty():
        cur = q.dequeue()
        print(cur)
        for i in graph[cur]:
            if color[i] == "White":
                q.enqueue(i)
                color[i] = "Grey"
        color[cur] = "Black"
BFS(graph,"A")
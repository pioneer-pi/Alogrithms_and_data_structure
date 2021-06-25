"""
You can call this topological sort.
"""
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
    "0":["1","2"],
    "1":["3","4"],
    "2":[],
    "3":[],
    "4":[]
}
def TopSort(graph):
    indegree = dict()
    order = []
    count = 0
    for i in graph:
        if i not in indegree:
            indegree[i] = 0
    for i in graph:
        for j in graph[i]:
            indegree[j] += 1
    q = Queue()
    for i in graph:
        if indegree[i] == 0:
            q.enqueue(i)
    while not q.is_empty():
        u = q.dequeue()
        order.append(u)
        count += 1
        for i in graph[u]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.enqueue(i)

    print(order)
TopSort(graph)
from pythonds3.trees import priority_queue
from pythonds3.trees.binary_heap import BinaryHeap
class PriorityQueue(BinaryHeap):
    """
    This implementation of binary heap takes (key, value) pairs where key signifies priority
    We will assume that the keys are all comparable.
    """

    def change_priority(self, new_priority, value):
        """Change the priority"""
        key_to_move = 0
        for i in range(len(self._heap)):
            if self._heap[i][1] == value:
                key_to_move = i
                break
        if key_to_move > -1:
            self._heap[key_to_move] = (new_priority, self._heap[key_to_move][1])
            self._perc_up(key_to_move)
    def peek(self):
        return self._heap[0]

def PFS(graph,start):
    pq = PriorityQueue
    color = dict()
    for i in graph:
        if i not in color:
            color[i] = "White"
    pq.insert(start)
    color[start] = "Grey"
    while not pq.is_empty():
        cur = pq.peek()
        has_child = False
        for i in graph[cur]:
            if color[i] == "White":
                pq.insert(i)
                color[i] = "Grey"
                has_child = True
        if not has_child:
            pq.delete(cur)
            color[cur] = "Black"
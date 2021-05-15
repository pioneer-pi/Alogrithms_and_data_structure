#宽度优先搜索BFS 从一个点开始，辐射状的遍历其周围的区域
from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue
def bfs(g,start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while(vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == "while":
                nbr.setColor("gray")
                nbr.setDistance(currentVert.getDistance + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor("black")
def traverse(y):
    x = y
    while x.getPred():
        print(x.getId())
        x = x.getPred()
    print(x.getId())
graph = {
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","D","E"],
    "D":["B","C","E","F"],
    "E":["C","D"],
    "F":["D"]
}
def BFS(graph,start):
    queue = []
    queue.append(start)
    seen = set()
    seen.add(start)
    parent = {start:None}
    while len(queue)>0:
        vertex = queue.pop()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertex
        print(vertex)
    return parent
print(BFS(graph,"A"))

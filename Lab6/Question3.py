import heapq
def shortest_path(adj_list, s):
    length = [1 for _ in range(len(adj_list))]
    shortest_path = []
    for i in range(len(adj_list)):
        if i == s:
            shortest_path.append(0)
        else:
            shortest_path.append(float('inf'))
    pqueue = []
    heapq.heappush(pqueue,(0,s))
    seen = set()
    while len(pqueue) > 0:
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        seen.add(vertex)
        nodes = adj_list[vertex]
        for w in nodes:
            if w not in seen:
                if dist + 1 < shortest_path[w]:
                    heapq.heappush(pqueue,(dist + length[w],w))
                    shortest_path[w] = dist + length[w]
    return shortest_path

adj_list = [[], [2, 3], [1, 4], [1], [2]]
d = shortest_path(adj_list, 0)
print(d)
d = shortest_path(adj_list, 2)
print(d)

'''
Dijkstra 算法的一次小复习 假定每条边的距离为1
'''
def Dijkstra(adj_list,start):
    distance = []
    for i in range(len(adj_list)):
        if i == start:
            distance.append(0)
        else:
            distance.append(float('inf'))
    pqueue = []
    heapq.heappush(pqueue,(0,start))
    seen = []
    while len(pqueue) != 0:
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        seen.append(vertex)
        for i in adj_list[vertex]:
            if i not in seen:
                if dist + 1 < distance[i]:
                    heapq.heappush(pqueue,(dist + 1,i))
                    distance[i] = dist + 1
    return distance

'''
Teacher's code about this question
'''
from collections import deque

def shortest_path2(adj_list, s):
    color = []
    d = []
    for i in range(len(adj_list)):
        color.append(0)
        if i == s:
            d.append(0)
        else:
            d.append(float('inf'))
    bfs_visit(adj_list, s, color, d)
    return d

def bfs_visit(adj_list, s, color, d):
    q = deque()
    q.append(s)
    color[s] = 1
    while len(q) > 0:
        r = q[0]
        for j in adj_list[r]:
            if color[j] == 0:
                color[j] = 1
                q.append(j)
                d[j] = d[r] + 1
        q.popleft()
        color[r] = 2
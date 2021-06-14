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
"""
Find strong components by using DFS.
"""
def find_scc(adj_lists):
    # first find the reverse graph
    reverse_graph = [[] for _ in range(len(adj_lists))]
    for i in range(len(adj_lists)):
        for j in adj_lists[i]:
            reverse_graph[j].append(i)
    # Take DFS to find the done last
    done = dict()
    for i in range(len(reverse_graph)):
        stack = []
        seen = []
        count = 0
        stack.append(i)
        seen.append(i)
        last_vertex = i
        while len(stack) != 0:
            find = False
            vertex = stack[-1]
            for i in reverse_graph[vertex]:
                if i not in seen:
                    stack.append(i)
                    seen.append(i)
                    find = True
                    break
            if not find:
                stack.pop()
                count += 1
                last_vertex = vertex
        done[last_vertex] = count
    distance = dict()
    for i in done:
        if done[i] not in distance:
            distance[done[i]] = [i]
        else:
            distance[done[i]].append(i)
    print(distance)
    father = [0 for _ in range(len(adj_lists))]
    for i in distance:
        for j in distance[i]:
            father[j] = distance[i][0]
    # print(father)
    arc = []
    seen = []
    for i in distance:
        arc.append(dfs(adj_lists,distance[i][0],seen))
    print(arc)




def dfs(graph,start,seen):
    arc = []
    stack = []
    stack.append(start)
    seen.append(start)
    while len(stack)!= 0:
        find = False
        vertex = stack[-1]
        for i in graph[vertex]:
            if i not in seen:
                seen.append(i)
                stack.append(i)
                if (vertex,i) not in arc:
                    arc.append((vertex,i))
                find = True
                break
        if not find:
                stack.pop()
    return arc

find_scc([[3],[0],[0,3,4],[1],[2]])
# find_scc([[2, 3], [0], [1], [4], []])
# find_scc([[1], [2], [0]])
find_scc([[1],[2],[0],[4],[5],[0,6],[2,4],[5,3]])

# if i not in seen:
#     stack.append(i)
#     seen.append(i)
#     while len(stack) != 0:
#         vertex = stack[-1]
#         find = False
#         for j in adj_lists[vertex]:
#             if j not in seen:
#                 seen.append(j)
#                 stack.append(j)
#                 find = True
#                 break
#         if not find:
#             stack.pop()
#             father[vertex] = i
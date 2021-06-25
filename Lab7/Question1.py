'''
Implement the function for finding girth of undirected graphs: Given the adjacency lists of an undirected,
return the girth if there is any cycle in the graph. Otherwise, return 'inf'.
'''
def find_girth(adj_list):
    girth = float('inf')
    for v in range(len(adj_list)):
        tree = []
        # cross = []
        queue =[]
        seen = []
        time = dict()
        queue.append(v)
        time[v] = 0
        seen.append(v)
        while len(queue)!= 0:
            vertex = queue.pop(0)
            for i in adj_list[vertex]:
                if i not in seen:
                    seen.append(i)
                    queue.append(i)
                    time[i] = time[vertex] + 1
                    tree.append([vertex,i])
                elif i in seen and [vertex,i] not in tree and [i,vertex] not in tree:
                    if time[i] == time[vertex]:
                        circle_length = 2 * time[i] + 1
                        girth = circle_length if girth > circle_length else girth
                    else:
                        circle_length = time[i] + time[vertex] + 1
                        girth = circle_length if girth > circle_length else girth
    return girth

adj_list = [[2],[3],[0,3],[1,2,4,5],[3],[3]]
print(find_girth(adj_list))

adj_list = [[1, 2], [0, 4, 5], [0, 3], [2, 5, 6], [1, 6], [1, 3, 6], [3, 4, 5]]
print(find_girth(adj_list))

adj_list = [[1,5],[0,2],[1,3],[2,4],[3,5],[0,4]]
print(find_girth(adj_list))

adj_list = [[1, 2, 3], [0, 2], [0, 1, 4], [0, 4], [2, 3]]
print(find_girth(adj_list))
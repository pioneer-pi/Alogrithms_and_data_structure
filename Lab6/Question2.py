def is_reachable(adj_matrix, s, d):
    stack = []
    color = ["White" for _ in range(len(adj_matrix))]
    stack.append(s)
    color[s] = "Grey"
    while len(stack) != 0:
        cur = stack[len(stack)-1]
        find = False
        for i in range(len(adj_matrix)):
            if adj_matrix[cur][i] == 1:
                if i == d:
                    return True
                if color[i] == "White":
                    stack.append(i)
                    color[i] = "Grey"
                    find = True
                    break
        if not find:
            color[cur] = "Black"
            stack.pop()
    return False
"Test1"
adj_matrix = [[0,1,1,0],[0,0,1,0],[1,0,0,0],[0,1,0,0]]
print(is_reachable(adj_matrix, 0, 3))
print(is_reachable(adj_matrix, 3, 0))

# "Test2"
# adj_matrix = [
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 1],
#     [1, 0, 1, 1, 0]
# ]
# print(is_reachable(adj_matrix, 4, 4))
# print(is_reachable(adj_matrix, 0, 2))

"Test3"
adj_matrix = [
    [0, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0]
]
print(is_reachable(adj_matrix, 0, 3))
print(is_reachable(adj_matrix, 1, 2))
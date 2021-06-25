def dfs(adj_matrix):
    tree = []
    forward = []
    back = []
    cross = []
    number = len(adj_matrix)
    color = ["White" for _ in range(number)]
    for i in range(number):
        if color[i] == "White":
            dfs_compute(adj_matrix,tree,forward,back,cross,i,number,color)

    return sorted(tree), sorted(forward), sorted(back), sorted(cross)

def dfs_compute(adj_matrix,tree,forward,back,cross,vertex,number,color):
    stack = []
    pred = [None for _ in range(number)]
    stack.append(vertex)
    color[vertex] = "Grey"
    while len(stack) != 0:
        cur = stack[len(stack)-1]
        find = False
        for i in range(number):
            if adj_matrix[cur][i] == 1:
                if color[i] == "White":
                    stack.append(i)
                    pred[i] = cur
                    find = True
                    tree.append((cur,i))
                    color[i] = "Grey"
                    break
                elif color[i] == "Grey":
                    if (cur,i) not in back:
                        back.append((cur,i))
                elif color[i] == "Black":
                    if (cur,i) not in tree:
                        if is_cross(cur,i,pred):
                            if (cur,i) not in cross:
                             cross.append((cur,i))
                        else:
                            if (cur,i) not in forward:
                                forward.append((cur,i))
        if not find:
            color[cur] = "Black"
            stack.pop()
def is_cross(cur,des,pred):
    current = cur
    father = pred[current]
    while father != None:
        if father == des:
            return False
        current = father
        father = pred[current]
    current = des
    father = pred[current]
    while father != None:
        if father == cur:
            return False
        current = father
        father = pred[current]
    return True


adj_matrix = [[0, 1, 0], [0, 0, 0], [0, 0, 0]]
tree, forward, back, cross = dfs(adj_matrix)
print('Tree arcs: {}'.format(tree))
print('Forward arcs: {}'.format(forward))
print('Back arcs: {}'.format(back))
print('Cross arcs: {}'.format(cross))

# adj_matrix = [[0, 0, 0, 0, 1, 0],
#               [1, 0, 1, 1, 0, 0],
#               [0, 0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 0, 1],
#               [1, 0, 0, 0, 0, 0],
#               [0, 1, 1, 1, 0, 0]]
# tree, forward, back, cross = dfs(adj_matrix)
# print('Tree arcs: {}'.format(tree))
# print('Forward arcs: {}'.format(forward))
# print('Back arcs: {}'.format(back))
# print('Cross arcs: {}'.format(cross))

"Teacher's answer"
from collections import deque


def dfs(adj_matrix):
    color = []
    tree_arcs = []
    forward_arcs = []
    back_arcs = []
    cross_arcs = []
    seen = []
    done = []
    for i in range(len(adj_matrix)):
        color.append(0)
        seen.append(0)
        done.append(0)
    time = 0
    for i in range(len(adj_matrix)):
        if color[i] == 0:
            tree, forward, back, cross, time = dfs_visit(adj_matrix, i, color, seen, done, time)
            tree_arcs += tree
            forward_arcs += forward
            back_arcs += back
            cross_arcs += cross

    tree_arcs = list(tree_arcs)
    tree_arcs.sort(key=lambda x: str(x[0]) + str(x[1]))
    forward_arcs = list(forward_arcs)
    forward_arcs.sort(key=lambda x: str(x[0]) + str(x[1]))
    back_arcs = list(back_arcs)
    back_arcs.sort(key=lambda x: str(x[0]) + str(x[1]))
    cross_arcs = list(cross_arcs)
    cross_arcs.sort(key=lambda x: str(x[0]) + str(x[1]))
    return tree_arcs, forward_arcs, back_arcs, cross_arcs


def dfs_visit(adj_matrix, s, color, seen, done, time):
    tree = set()
    forward = set()
    back = set()
    cross = set()
    cur_time = time
    stack = deque()

    stack.append(s)
    color[s] = 1
    seen[s] = cur_time
    cur_time += 1

    while len(stack) > 0:
        r = stack[-1]  # pick the top
        done_flag = True
        for j in range(len(adj_matrix[r])):
            if adj_matrix[r][j] > 0:
                if color[j] == 0:
                    color[j] = 1
                    stack.append(j)
                    tree.add((r, j))
                    seen[j] = cur_time
                    cur_time += 1
                    done_flag = False
                    break
                elif color[j] == 1:
                    back.add((r, j))
                else:
                    if seen[r] < seen[j] and (r, j) not in tree:
                        forward.add((r, j))
                    elif seen[j] < seen[r] and (r, j) not in tree:
                        cross.add((r, j))

        if done_flag:
            stack.pop()
            done[r] = cur_time
            cur_time += 1
            color[r] = 2
    return tree, forward, back, cross, cur_time
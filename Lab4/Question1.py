# count = 0
# def inorder(index, lst, l):
#     global count
#
#     if index > len(lst):
#         return
#     inorder(index * 2, lst, l)
#     l[index] = lst[count]
#     count += 1
#     inorder(index * 2 + 1, lst, l)
#
#
# def to_bst(lst):
#     lst.sort()
#     ls = [0 for i in range(len(lst) + 1)]
#     inorder(1, lst, ls)
#     ls.pop(0)
#     for i in range(len(lst)):
#         lst[i] = ls[i]


# keys = [29, 72, 1, 34, 22]
# to_bst(keys)
# print(keys)

#teacher‘s way
def to_bst(lst):
    sorted_lst = sorted(lst)
    inorder(lst, 0, sorted_lst, 0)


def inorder(lst, root, sorted_data, cur_pos):
    if root >= len(lst):
        return cur_pos
    left = root * 2 + 1
    right = root * 2 + 2
    next_pos = cur_pos
    if left < len(lst):
        next_pos = inorder(lst, left, sorted_data, next_pos)
    lst[root] = sorted_data[next_pos]
    if right < len(lst):
        return inorder(lst, right, sorted_data, next_pos + 1)
    else:
        return next_pos + 1

keys = [29, 72, 1, 34, 22]
to_bst(keys)
print(keys)
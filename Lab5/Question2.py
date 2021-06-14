from typing import List


# find the maximum value of knapsack
# n is the number of items
# C is the maximum capacity of knapsack
# v lists values of the items, the ith item is worth vi
# w lists weight of the items, the ith item weighs wi
# m stores the optimal values of subproblems
# rec is used to record computing information
def find_optimal_value(n: int, C: int, v: List[int], w: List[int], m: List[List[int]], rec: List[List[int]]):
    # for i in range(n+1):
    #     for j in range(C+1):
    #         rec[i][j] = "0"*(n+1)
    for i in range(1,n+1):
        for j in range(1,C+1):
            if j >= w[i] and m[i-1][j-w[i]] + v[i] > m[i-1][j]:
                m[i][j] = m[i-1][j-w[i]] + v[i]
                rec[i][j] = 1
            else:
                m[i][j] = m[i-1][j]
                rec[i][j] = 0
    return m[n][C]

# construct the optimal solution
def find_optimal_solution(rec: List[List[int]], n: int, C: int, w: List[int]):
    x = [0 for i in range(n + 1)]
    items = n
    weight = C
    #0 1 2 3
    for i in range(n+1):
        if rec[items][weight] == 1:
            items -= 1
            weight -= w[n-i]
            x[n-i] = 1
        else:
            items -= 1
    return x



# print the optimal value and optimal solution
def knapsack(C: int, n: int, v: List[int], w: List[int]):
    m = [[0]*(C+1) for _ in range(n+1)]
    rec = [[0]*(C+1) for _ in range(n+1)]
    m = find_optimal_value(n,C,v,w,m,rec)
    l = find_optimal_solution(rec,n,C,w)
    print(m)
    print(l)


# C = 18
# n = 4
# v = [-1, 2, 5, 6, 9]
# w = [-1, 3, 5, 9, 7]
# knapsack(C, n, v, w)
# C = 16
# n = 3
# v = [-1, 5, 4, 1]
# w = [-1, 10, 8, 5]
# knapsack(C, n, v, w)

C = 10
n = 5
v = [-1, 6, 3, 5, 4, 6]
w = [-1, 2, 2, 6, 5, 4]
knapsack(C, n, v, w)
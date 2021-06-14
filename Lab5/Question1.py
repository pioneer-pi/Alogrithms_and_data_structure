from typing import List
# find length of the longest common subsequence of two sequences x and y
# m is the length of sequence x
# n is the length of sequence y
# c stores optimal values of subproblems
# rec is used to record computing information
def LCSLength(x: str, y: str, m: int, n: int, c: List[List[int]], rec: List[List[int]]):
    for i in range(m+1):
        c[i][0] = 0
    for i in range(n+1):
        c[0][i] = 0

    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1]+1
                rec[i][j] = "LU"
            elif c[i][j-1] > c[i-1][j]:
                c[i][j] = c[i][j-1]
                rec[i][j] = "L"
            else:
                c[i][j] = c[i-1][j]
                rec[i][j] = "U"

# construct optimal solution
def PrintLCS(rec: List[List[int]], x: str, i: int, j: int):
    if i == 0 or j == 0:
        return ""
    if rec[i][j] == "LU":
        return PrintLCS(rec,x,i-1,j-1) + x[i-1]
    elif rec[i][j] == "U":
        return PrintLCS(rec,x,i-1,j)
    else:
        return PrintLCS(rec,x,i,j-1)

# print length of the longest common subsequence
# print the longest common subsequence
def LCS(x: str, y: str):
    m = len(x)
    n = len(y)
    c = [[0] * (n+1) for _ in range(m+1)]
    rec = [[0] * (n+1) for _ in range(m+1)]
    LCSLength(x,y,m,n,c,rec)
    str = PrintLCS(rec,x,m,n)
    print(len(str))
    print(str)
x = 'ABCA'
y = 'BDCA'
LCS(x,y)
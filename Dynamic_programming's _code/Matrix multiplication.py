import math
class Matrix:
    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
def Matrix_multiplication(A,B):
    C = [[0] * B.columns for _ in range(A.rows)]
    if A.columns != B.rows:
        print("This two matrix can not multiplicate!")
    else:
        for i in range(A.columns):
            for j in range(B.rows):
                for k in range(A.columns):
                    C[i][j] += A[i][k]*B[k][j]
    return C

#p:List[int], n:int, m:List[List[int]], s:List[List[int]]
def MatrixChain(p,n,m,s):
    for i in range(1,n+1):
        m[i][i] = 0
    for r in range(2,n+1):
        for i in range(1,n-r+1+1):
            j = i+r-1
            m[i][j] = m[i][i] + m[i+1][j] + p[i-1]*p[i]*p[j]
            s[i][j] = i
            for k in range(i+1,j):
                t = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if t < m[i][j]:
                    m[i][j] = t
                    s[i][j] = k

def Traceback(s,i,j):
    if i == j:
        return
    Traceback(s,i,s[i][j])
    Traceback(s,s[i][j]+1,j)
    print(i,j,s[i][j])
def main():
    n = 6
    p = [30,35,15,5,10,20,25]
    s = [[0]*(n+1) for _ in range(n+1)]
    m = [[0]*(n+1) for _ in range(n+1)]
    MatrixChain(p,n,m,s)
    print(s)
    Traceback(s,1,n)

def recursive_matrix_chain(m,p,i,j):
    if i == j:
        return 0
    m[i][j] = math.inf
    for k in range(i,j):
        q = recursive_matrix_chain(m,p,i,k) + recursive_matrix_chain(m,p,k+1,j) + p[i-1]*p[k]*p[j]
        if q < m[i][j]:
            m[i][j] = q
    return m[i,j]

#Top-down memorized Dynamic programming
def MemoizedMatrixChain(n,m,s):
    for i in range(1,n+1):
        for j in range(i,n+1):
            m[i][j] = 0
            return LookupChain(1,n,m,s)
m = []
p = []
s = []
def LookupChain(i,j):
    if(m[i][j] > 0):
        return m[i][j]
    if i == j:
        return 0
    u = LookupChain(i,i) + LookupChain(i+1,j) + p[i-1]*p[i]*p[j]
    s[i][j] = i
    for k in range(i+1,j):
        t = LookupChain(i, k) + LookupChain(k + 1, j) + p[i - 1] * p[k] * p[j]
        if t < u:
            u = t
            s[i][j] = k
    m[i][j] = u
    return u
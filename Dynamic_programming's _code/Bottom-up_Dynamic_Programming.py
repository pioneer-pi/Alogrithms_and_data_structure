from typing import List


def MatrixChain(p:List[int],n:int,m:List[List[int]],s:List[List[int]]):
    for i in range(1,n+1):
        m[i][i] = 0
    for r in range(2,n+1):
        for i in range(1,n-r+1+1):
            j = i + r - 1
            m[i][j] = m[i][i] + m[i+1][j] + p[i-1]*p[i]*p[j]
            s[i][j] = i
            for k in range(i+1, j):
                t = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if t<m[i][j]:
                    m[i][j] = t
                    s[i][j] = k


def Traceback(i:int, j:int, s: List[List[int]]):
    if(i == j):
        return
    Traceback(i,s[i][j],s)
    Traceback(s[i][j]+1,j,s)
    print(i,j,s[i][j])

def main():
    n = 6
    p = []
    s = [[int]*100 for _ in range(100)]
    p[0] = 30
    p[1] = 35
    p[2] = 15
    p[3] = 5
    p[4] = 10
    p[5] = 20
    p[6] = 25
    sum = MatrixChain(p,1,n,s)
    print("zuiyoujie" + sum)
    print(s[1][6])
    Traceback(1,n,s)
main()
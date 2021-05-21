#x,y是
x = list()
y = list()
m = len(x)
n = len(y)
c = [[0]*(n+1) for _ in range(m+1)]
rec = [[0]*n for _ in range(m)]
def LCSLength(x,y,m,n,c,rec):
    for i in range(n+1):
        c[0][i] = 0
    for i in range(m+1):
        c[i][0] = 0

    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                rec[i][j] = "LU"
            elif c[i][j-1] > c[i-1][j]:
                c[i][j] = c[i][j-1]
                rec[i][j] = "L"
            else:
                c[i][j] = c[i-1][j]
                rec[i][j] = "U"
def PrintLCS(rec,x,i,j):
    if i == 0 or j == 0:
        return
    if rec[i][j] == "LU":
        PrintLCS(rec,x,i-1,j-1)
        print(x[i-1])
    elif rec[i][j] == "U":
        PrintLCS(rec,x,i-1,j)
    else:
        PrintLCS(rec,x,i,j-1)

def main():
    x = "ABCBDABPP"
    y = "BDCABAPQ"
    m = len(x)
    n = len(y)
    c = [[0] * (n+1) for _ in range(m+1)]
    rec = [[0] * (n+1) for _ in range(m+1)]
    LCSLength(x,y,m,n,c,rec)
    PrintLCS(rec,x,m,n)
    for i in range(m+1):
        for j in range(n+1):
            print(rec[i][j], end=" ")
        print("")
    return 0
main()
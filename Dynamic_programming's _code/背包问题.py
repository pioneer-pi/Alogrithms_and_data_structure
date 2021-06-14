v = [-1, 1, 4, 5]
w = [-1, 5, 8, 10]
def dppackage(n,w,v):
    row = len(w)
    column = n
    f = [[0]*(column+1) for _ in range(row+1)]
    for i in range(1,row):
        for j in range(1,column+1):
            if j < w[i]:
                f[i][j] = f[i-1][j]
            else:
                f[i][j] = max(f[i-1][j-w[i]] + v[i],f[i-1][j])
    return  f[row-1][column]
f = dppackage(10,w,v)
print(f)
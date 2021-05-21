weight = [2,2,6,4,5]
value =  [6,3,5,4,6]
def dppackage(n,w,v):
    row = len(w)
    column = n
    f = [[0]*(column+1) for _ in range(row)]
    for i in range(row):
        for j in range(column+1):
            if j < w[i]:
                f[i][j] = f[i-1][j]
            else:
                f[i][j] = max(f[i-1][j-w[i]] + v[i],f[i-1][j])
    return  f
f = dppackage(10,weight,value)
print(f)
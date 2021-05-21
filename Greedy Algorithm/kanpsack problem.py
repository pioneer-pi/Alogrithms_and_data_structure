def FractionalKnapsack(n,M,v,w,x):
    bi = []
    total = 0
    for i in range(n):
        bi.append(v[i]/w[i])
    for i in range(1,n+1):
        x[i] = 0
    c = M
    for i in range(n):
        if c <=0:
            break
        if(w[i] > c):
            x[i] = c/w[i]
            total += v[i]*x[i]
            break
        else:
            c -= w[i]
            x[i] = 1
            total += v[i]

n = int(input())
l = list(map(int,input().split()))
l = sorted(l)
sum_ = 0
for i in range(len(l)-1):
    sum_ += l[i] + sum(l[i+1:])
print(sum_)
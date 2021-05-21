#按照活动结束时间进行递增排序
def activity_selection(s,f):
    length  = len(s)
    A = [1]
    k = 1
    for m in range(1,length):
        if f[m] >= s[k]:
            A.append(m+1)
            k = m
    return A


def task(n,l):
    n = int(input())
    l = list(map(int,input().split()))
    length = len(l)
    count = 0
    while min(l) > 0:
        for i in range(len(l)):
            l[i] -= 1
        count += 1
    position = 0
    for i in range(length):
        if l[i] > 0:
            position = i
            while position < length and l[position] > 0:
                l[position] -= 1
                position += 1
            count += 1
    print(count)
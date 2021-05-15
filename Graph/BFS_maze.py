from pythonds import Queue
def getint():
    return [int(i) for i in input().split()]

#------------------------------------------------------------------------
class Point():#定义一个结构体，self.x与self.y表示一个点的横纵坐标
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

#------------------------------------------------------------------------
def bfs(begin,end):
    dist=[[1 for _ in range(m)] for _ in range(n)]
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    dist[begin.x][begin.y]=0
    q=Queue()
    q.enqueue(begin)
    while q:
        res=q.dequeue()
        flag=False
        for i in range(4):
            nx,ny=res.x+dx[i],res.y+dy[i]
            if 0<=nx<n and 0<=ny<m and a[nx][ny]!="#" and dist[nx][ny]==1:
                dist[nx][ny]=dist[res.x][res.y]+1
                q.enqueue(Point(nx,ny))
                if nx==end.x and ny==end.y:
                    flag=True
                    break
        if flag:
            break
    if flag:
        print("Yes")
        return
    print("No")
#------------------------------------------------------------------------
while True:
    try:
        n,m=getint()
        a=[]
        begin=Point()
        end=Point()
        for i in range(n):
            s=input()
            a.append(list(s))
            if "S" in s:
                begin.x=i
                begin.y=s.index("S")
            if "E" in s:
                end.x=i
                end.y=s.index("E")
        bfs(begin,end)
    except:
        break

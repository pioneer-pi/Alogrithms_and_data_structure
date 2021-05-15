from pythonds import Queue
# n = int(input("Please input the size of the maze: "))
# map_ = [[0]*n]*n
vis = [[0]*6 for _ in range(6)]
#右下左上
xi = [0,1,0,-1]
yi = [1,0,-1,0]
begin = [0,0]
map_ =[[0,1,0,0,0,0],
[0, 0, 0, 0, 1, 0],
[0, 1, 0, 0, 1, 1],
[0, 1, 0, 0, 0, 0],
[0, 1, 0, 1, 0, 0],
[0, 1, 0, 0, 0, 0]]
# for i in range (n):
#     for j in range(n):
#         m = input()
#         if m == "S":
#             begin = (i,j)
#             map_[i][j] = 0
#         elif m == "T":
#             end = (i,j)
#             map_[i][j] = 0
#         elif m == "1":
#             map_[i][j] = 1
#         elif m == "0":
#             map_[i][j] = 0
def bfs(begin): #x,y为初始点的坐标
    q = Queue()
    q.enqueue(begin)
    while q.size() > 0:
        now = q.dequeue()
        x = now[0]
        y = now[1]
        vis[x][y] = 2
        if now == [5,5]:
            print("Yes")
            return
        for i in range(4):
            x = now[0] + xi[i]
            y = now[1] + yi[i]
            if 0<=x<=5 and 0<=y<=5 and map_[x][y]==0 and vis[x][y] == 0:
                q.enqueue([x,y])
    print("No")
    return
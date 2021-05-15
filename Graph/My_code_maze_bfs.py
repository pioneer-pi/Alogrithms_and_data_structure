while True:
    try:
        n,m = map(int,input().split())
    except:
        break
    maze = [[0]*m for _ in range(n)]
    vis = [[0]*m for _ in range(n)]
    begin = []
    end = []
    xi = [0,1,0,-1]
    yi = [1,0,-1,0]
    for i in range(n):
        s = list(input())
        for j in range(m):
            if s[j] == "S":
                begin = [i,j]
                maze[i][j] = 0
            elif s[j] == "E":
                end = [i,j]
                maze[i][j] = 0
            elif s[j] == ".":
                maze[i][j] = 0
            elif s[j] == "#":
                maze[i][j] = 1
    def bfs(begin):
        q = []
        q.append(begin)
        while len(q) > 0:
            find = False
            now_position = q.pop(0)
            x = now_position[0]
            y = now_position[1]
            for i in range(4):
                xx = x + xi[i]
                yy = y + yi[i]
                if 0<=xx<=m-1 and 0<=yy<=n-1 and maze[xx][yy] == 0 and vis[xx][yy] == 0:
                    q.append([xx,yy])
                    vis[xx][yy] = 2
                    if [xx,yy] == end:
                        find = True
                        break
            if find:
                break
        if find:
            print("Yes")
            return
        print("No")
    bfs(begin)
    print(vis)
# 미로탈출
# 1초 128MB
# 13:58
 
from collections import deque

n,m = map(int,input().split())

maps =[] 

for i in range(n):
    maps.append(list(map(int,input().split())))

x,y = 0,0
queue = deque()
queue.append((x,y))

#이동할 방향 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]

while queue: #queue가 빌 때까지 반복
    x,y = queue.popleft()
    for i,j in zip(dx,dy):
        nx = x + i
        ny = y + j
        if(nx<0 or nx >=n or ny <0 or ny >= m):
            #맵 벗어남
            continue
        elif maps[nx][ny] == 0:
            #갈 수 없는 지역
            continue
        else :
            #정상적인 지역
            if maps[nx][ny] == 1 :
                #처음 가보면 기존보다 한 칸 늘어난거니까 + 1
                maps[nx][ny] = maps[x][y]+1
                queue.append((nx,ny))
print(maps[n-1][m-1])

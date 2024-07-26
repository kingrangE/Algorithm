#모범 답안
n,m = map(int,input().split())

graph = [] #좌표 값 받기 ( 전역변수처럼 이용 )
for i in range(n):
    graph.append(list(map(int,input().split())))

def dfs(x,y):
    if x <= -1 or y <= -1 or x >= n or y >= m :
        return False
    if graph[x][y] == 0 : # 탐색하는 지역이 가보지 않은 지역이라면
        graph[x][y] = 1 # 가봤다고 표시하기 
        #상하좌우로 재귀적 탐색
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)
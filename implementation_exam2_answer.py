"""
배워야 할 점
1. 이처럼 방향에 따라 움직이는 시뮬레이션 문제는 방향에 따른 움직임을 dx,dy로 리스트를 만들어서 푸는 것이 효율적
"""
#맵 크기
n,m = map(int,input().split())
#지나왔던 곳인지 확인용
d = [[0]*m for _ in range(n)]
#x,y,d 
x,y,d = map(int,input().split())
d[x][y] = 1 #시작 위치도 지나온 곳으로 처리
count = 1 # 지나온 곳의 개수

#전체 맵 정보
maps = [list(map(int,input().split())) for _ in range(n)]

#북,동,남,서 방향에 따른 이동 정의
#ex) 북쪽을 바라보면 -1 만큼 수직 이동, 0 만큼 수평 이동
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global d #방향 정보가 함수 밖에서 선언된 전역 변수이므로
    d -= 1
    if d == -1 : #음수는 없으므로
        d = 3

#종료 조건 
turn_time = 0
while True :
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    if(d[nx][ny] == 0 and maps[nx][ny]==0):
        #지나가보지도 않고 바다도 아니라면 이동 가능
        d[nx][ny]=1
        x = nx
        y = ny
        count+=1
        turn_time= 0
        continue
    else :
        turn_time +=1
    if turn_time == 4 :
        nx = x - dx[d]
        ny = y - dy[d]
        #현재 바라보는 방향에서 뒤로 가보기
        if d[nx][ny]==0 and maps[nx][ny]==0 :
            #갈 수 있다면 가기
            turn_time = 0
            x = nx
            y = ny
        else :
            #갈 수 없다면 종료
            break
print(count)
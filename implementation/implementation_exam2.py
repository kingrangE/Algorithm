# 게임 개발  (1초 128MB)
# 난이도 2
"""
2:03분 시작
1. 현재 위치 현재 방향 기준 왼쪽 방향부터 차례대로 갈 곳 정함
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다 -> 왼쪽 회전 후, 한 칸 전진
3. 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 회전 후, 1단계로
4. 네 방향 모두 가보았거나 갈 수 없다면, 바라보는 방향을 유지한채로 한 칸 뒤로 돌아가고 1단계 수행
5. 뒤 방향이 바다라면, 움직임을 멈춤
# 방문한 칸의 수를 출력하라
"""
# 0 :북,1 : 동, 2: 남, 3: 서

# 지도
N,M = map(int,input().split()) 

# x좌표,y좌표,방향 입력
x,y,d = map(int,input().split()) 

# 지도 정보 입력
maps = [ list(map(int,input().split())) for i in range(N) ]

result = 0
stack = 0

#방향별 Plan 설정 ((회전 후, 앞으로 갔을 때 좌표 변화 x,y),왼쪽 회전 했을 때의 방향 값)
plans = [[-1,0,3],[0,-1,0],[1,0,1],[0,1,2]]
while True:
 
    #지나간 자리이므로 1로 변경
    maps[x][y] = 1
    tmp_x,tmp_y,tmp_d = x+plans[d][0],y+plans[d][1],plans[d][2]
    if tmp_x > 0 and tmp_x < N and tmp_y >0 and tmp_y < M: # 맵을 벗어나지 않는 조건
        if maps[tmp_x][tmp_y] != 1 : #1이 아니면 0 
            stack = 0
            #자리 업데이트
            x,y,d = tmp_x,tmp_y,tmp_d
            result += 1
        else : 
            stack += 1
            d = plans[d][2]
            if stack == 4 :
                break
    else :
        d = plans[d][2]
print(result+1)
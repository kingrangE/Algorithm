# 상하좌우 (시간제한 1초, 메모리 제한 128MB)
# 시간 제한 1초 => 2000만 이하의 연산량 요구
# 메모리 제한 128MB => 3000만 개 이하의 list 이용
# 1,1에서 여행자가 계획서에 맞춰 움직이면 도착하는 좌표가 어딘지 출력하기

N = int(input()) # 지도의 크기 (NXN)
plan = input().split() # 이동 계획

x,y = 1,1 #현재 위치를 담는 x,y 
for p in plan :
    # 이동 계획을 하나씩 가져옴
    if p == 'R' and y < N:
        y += 1
    elif p == "U" and x < 1:
        x -= 1
    elif p == "L" and y > 1 :
        y -= 1
    elif p == "D" and x < N :
        x += 1

print(x,y)
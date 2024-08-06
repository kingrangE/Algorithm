# 개미전사
# 풀이시간 30분 시간제한 1초 메모리 제한 128MB
"""
식량 창고 개수 N
각 창고에 있는 식량의 수가 주어짐
붙어 있는 창고를 털게되면 들킴
따라서 붙어있지 않은 창고를 털면서 가장 많은 식량을 털 수 있게 해야하고 그때 터는 식량의 수를 출력하라.

풀이 시작 5:41
풀이 끝 : 5:49

"""

"""
떠오른 풀이
1. 현재 인덱스 기준으로 앞에서 -2 번째까지의 인덱스 중 최대값을 현재 인덱스에 더함 출력하며 ㄴ끝
"""

N = int(input())
foods = list(map(int,input().split()))

#최대값을 담을 list 생성
max_foods = [0]*N
#0,1은 앞에 더할게 없으므로 미리 값을 넣어줌
max_foods[0] = foods[0]
max_foods[1] = foods[1]
#반복하며 확인
for i in range(2,N) :
    max_foods[i] = max(max_foods[:i-1]) + foods[i]

print(max(max_foods))


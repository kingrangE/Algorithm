# 숫자 카드게임 ( 2019 국가 교육기관 코딩 테스트 )
N,M = map(int,input().split()) # 행, 열의 수
minimum = 0 #최소값을 담을 수
for i in range(N):
    #N개의 행만큼 숫자들을 입력받아 list에 저장
    tmp = list(map(int,input().split()))
    #tmp에서 가장 작은 수가 minimum보다 크다면, 교체
    if min(tmp)>minimum :
        minimum = min(tmp)

print(minimum)
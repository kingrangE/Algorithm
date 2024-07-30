#부품 찾기
# 풀이시간 30분, 시간제한 1초, 메모리 제한 128MB
# 매장의 부품 번호를 입력받고, 손님이 주문하는 부품 번호를 입력받음, 보유 중이면 yes 없으면 no


"""
처음 떠오른 풀이
1. 1~100만으로 부품 번호수가 정해져있음 -> count_sort로 리스트 생성 후, 계수정렬한 리스트 인덱스에 값이 0이 아니면 yes 0이면 no 출력

import sys

N = int(input())
markets = list(map(int,input().split()))
M = int(input())
customers = list(map(int,input().split()))

markets_sorted = [ 0 for _ in range(1000001)]
for i in markets :
    markets_sorted[i] += 1 #부품 번호에 해당하는 인덱스의 값을 1 증가시킴

for i in customers :
    if markets_sorted[i] != 0:
        print("yes",end=" ")
    else :
        print("no",end=" ")

"""

"""
2. 이진 탐색 파트에 있는 문제이므로 이진 탐색을 사용하는 풀이 -> 계수 정렬 이용한 풀이보다 시간 복잡도 자체는 높음

N = int(input())
markets = list(map(int,input().split()))
markets.sort()
M = int(input())
customers = list(map(int,input().split()))

def binary_search(arr,start,end,target):
    now = start + (end-start)//2
    #now 인덱스가 찾는 값과 같으면 return 
    if arr[now] == target :
        return True
    elif start >= end :
        # target이 아니고 더 이상 나눌 수 없다면
        return False
    else :
        #나눌 수 있고  arr[now]의 값이 target보다 크다면 왼쪽 반절 탐색 작다면 오른쪽
        if arr[now] > target:
            binary_search(arr,start,now-1,target)
        else :
            binary_search(arr,now+1,end,target)

for i in customers :
    if binary_search(markets,0,N,i) :
        print("yes",end=" ")
    else : 
        print("no", end=" ")

"""

"""
3. 수가 있는지 없는지만 검사를 하면 되는 것이므로 집합을 이용
"""
N = int(input())
markets = set(map(int,input().split()))
M = int(input())
customers = list(map(int,input().split()))

for i in customers :
    if i in markets :
        print("yes", end = " ")
    else : 
        print("no",end=" ")



    
    
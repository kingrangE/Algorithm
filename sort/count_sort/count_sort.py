import random
n = 100

arr = [i for i in range(n)]
random.shuffle(arr)

"""
계수정렬은 0 ~ 최대값 크기의 리스트를 제작한 후, 리스트 값에 맞게 해당 인덱스의 값을 추가해주어 정렬하는 방식입니다.
시간 복잡도는 O(N+K)입니다.
"""

num_list = [i for i in range(n)]

for i in range(n):
    
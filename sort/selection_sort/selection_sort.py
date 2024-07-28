
"""
Learning
1. Python can exchange same time
2. There should be no unnecessary variables in the code. (ex, min)
"""
import random
#Generate Random Array
arr = [i for i in range(10)]
random.shuffle(arr)
#selection sort
for i in range(len(arr)):
    min = 999999
    for j in range(i,len(arr)):
        # i-1번쨰까지는 이미 정렬된 상황이므로 i부터 끝까지 중 가장 작은 값을 찾고 맨 앞과 교환
        if arr[j] < min :
            min = arr[j]
    # for 반복 끝났으면, 최소값이 min에 들어있음 i번째 값과 교환
    tmp = arr[i]
    min_idx = arr.index(min)
    arr[i] = arr[min_idx]
    arr[min_idx] = tmp

print(arr)


arr = [i for i in range(10)]
random.shuffle(arr)

#other selection sort method
for i in range(len(arr)):
    min_idx = i
    for j in range(i,len(arr)):
        if arr[min_idx] > arr[j] :
            min_idx = j
    arr[i],arr[min_idx] = arr[min_idx],arr[i]

print(arr)


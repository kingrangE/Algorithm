import random
n = 10
arr = [i for i in range(n)]
random.shuffle(arr)

for i in range(1,n):
    #시작 지점 (0 인덱스)는 정렬이 되어 있다고 가정
    for j in range(i,0,-1):
        #뒤에서부터 확인하며 현재 숫자가 앞의 수보다 작으면 변경
        if (arr[j] < arr[j-1]) :
            arr[j-1],arr[j] = arr[j],arr[j-1]
print(arr)            
    
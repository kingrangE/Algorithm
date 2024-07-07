def sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            if arr[i] < arr[j] :
                arr[i],arr[j] = arr[j],arr[i]
    return arr

def compute_count(arr1,arr2):
    result = {}
    for i in arr2:
        result[i] = 0
        for j in arr1:
            if i == j :
                result[i] += 1
            if i != j and result[i]!= 0 :
                # 둘이 다르고 result i가 값이 안들어간 상태가 아니라면, 정렬을 했으므로 더이상 존재 X따라서 탈출
                break
    for key in result :
        print(result[key],end=" ")

n = int(input())
arr1 = []
arr1 = input().split(' ')
arr1 = list(map(int,arr1))
arr1 = sort(arr1)

n = int(input())
arr2 = []
arr2 = input().split(' ')
arr2 = list(map(int,arr2))

compute_count(arr1,arr2)
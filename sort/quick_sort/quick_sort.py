import random
n = 10
arr = [i for i in range(n)]
random.shuffle(arr)

def quick_sort(array,start,end):
    if start >= end :
        #시작지점이 끝지점과 같거나 크면 종료
        return
    pivot = start #기준(pivot)은 start지점
    left = start + 1 #pivot의 왼쪽부터 검사
    right = end
    while left <= right :
        while left <= end and array[left] <= array[pivot] :
            #left가 종료지점을 넘어가기 전까지 pivot보다 큰 값을 찾을 때까지 반복
            left += 1
        while right > start and array[right] >= array[pivot] :
            #right가 시작 지점보다 앞서나가기 전까지 pivot보다 작은 값을 찾을떄까지 반복
            right -= 1
        if left > right :
            #left와 right위치가 교차되었다면 pivot과 작은 값의 위치(right)를 바꿈
            array[right],array[pivot] = array[pivot],array[right]
        else:
            #교차되지 않았다면 작은 값과 큰 값의 위치를 변경
            array[right],array[left] = array[left],array[right]
    #이곳에 왔다면, left가 right를 벗어난 것이므로 분할하여 진행
    quick_sort(array,start,right-1)
    #right값은 pivot이므로 right-1까지 정렬 과 right+1~end까지 정렬
    quick_sort(array,right+1,end)

quick_sort(arr,0,n-1)
print(arr)

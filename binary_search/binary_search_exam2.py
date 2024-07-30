#떡볶이 떡 만들기 2초, 128MB 난이도 2
#시작 : 7:45
#떡의 개수와 손님이 요청한 길이
#각 떡의 개별 높이를 입력받으면
#손님이 요청한 길이를 맞추기 위해 절단기의 높이 설정을 몇으로 해야하는지 반환
#1 <= N <= 1,000,000
#1 <= M <= 2,000,000,000
N,M = list(map(int,(input().split())))

RC = list(map(int,input().split())) #떡의 개별 높이 입력 RiceCake
RC.sort()
"""
처음 생각한 풀이
1. 최대 높이부터 계속 잘라가며 맞추기 -> 시간 복잡도가 말 안된다. 최대 2억인데, 그럼 2억번을 해야하나...
2. 정렬 후, 중간값으로 자르고 높으면, 중간값과 최대값의 중간값으로 자르고 낮으면 또 반복 2번씩 나눠가며 반복하기 -> 좋은데? 천잰가 ㅋㅋ

풀이는 정확하게 찾았다. 내용도 같은데, 나는 저 말 자체를 제대로 구현하지 못함.
구현하기 위해서는 최대값만 고려하는게 아닌, 최솟값과 같이 고려하여 풀어야 하는데, 인덱스에 매몰되어 잘못된 풀이를 하고 있었다.
=> 풀다보면 정신없이 코드를 적으며 내가 무엇을 하려했는지 잊게되는데, 이것을 방지하기 위해 정확하게 내가 풀어나갈 방식을 적고 푸는 것이 좋을 것 같다.

1. binarysearch에는 전체 배열과 시작지점(0), 끝지점(최대길이), 목표 길이를 전달해주기
2. 끝지점 길이 - 시작지점 // 2 -> 우리가 설정한 절단기 높이
3. 절단기로 자른 길이가 목표와 맞으면 return 절단기 높이
    3-1. 맞지 않는데 모자라면
        a. 끝지점(최대길이)를 현재 길이-1로 당기고 2번부터 반복
    3-2. 맞지 않는데 넘치면
        a. 시작지점(최소길이)를 현재 길이+1로 당기고 2번부터 반복
"""
def binary_search(arr,start,end,target):
    if start>= end :
        return False
    
    slice_len = start + (end - start) // 2 #절단기 높이 

    result = 0 # 손님이 가져갈 높이
    for i in arr :
        if i> slice_len :
            result+= i-slice_len
    if result == target :
        return slice_len
    elif result < target:
        #목표에 미치지 못함 -> 더 잘라야댐
        return binary_search(arr,start,slice_len-1,target)
    else : 
        #덜 잘라야 함
        return binary_search(arr,slice_len+1,end,target)

num = binary_search(RC,0,max(RC),M)
print(num)
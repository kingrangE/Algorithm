# 큰 수의 법칙 ( 2019 국가 교육기관 코딩테스트 )
# 주석은 모범 답안
### 입력 예시 
"""
5 8 3
2 4 5 4 6
"""
if __name__ == "__main__" :
    # 입력 받고 정수형 변환 대신 map(int,input().split())
    N,M,K = input().split()  
    N,M,K = int(N),int(M),int(K)
    arr = input().split()
    arr = list(map(int,arr))
    
    """
    정렬하여 가장 큰 수와 두번쨰로 큰 수를 인덱스를 이용해서 찾고
    m 이 0이 될 때까지 가장 큰 수를 k번 더하고 두번쨰 큰 수를 더하는 방식으로 반복
    arr.sort()
    first = arr[n-1]
    second = arr[n-2]
    result = 0

    while m>0 :
        for i in range(k): #가장 큰 수 k번 더하기
            result+= first
            m-=1
            if m == 0:
                break
        result += second        
        m -= 1
        if m == 0 :
            break
    print(result)
    """
    max_num = max(arr)
    arr.remove(max_num)
    sub_max_num = max(arr)
    
    max_num_add = M - (M%K)
    sub_num_add = M%K
    print(max_num*max_num_add + sub_max_num * sub_num_add)

    """
    배운 점 
        입력 받는 방법 - 파이썬의 장점은 많은 기능이 구현되어 있다는 점. 이것을 잘 이용하는 것이 실력. map 함수의 사용법을 다시 한 번 배우게 되었다.
        코드의 가독성 - 내 코드는 어떻게 보면 간단하지만, 읽기에는 조금 까다롭다고 생각할 수 있다. 하지만, for문을 통해 푼 식은 한 눈에 구조를 이해할 수 있기에 가독성에 대해 배웠다.
    """
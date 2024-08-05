## 이진 탐색

- 범위를 반씩 줄여나가는 탐색 방법
- IDEA : '정렬한 후, 우리가 찾는 값이 중간점보다 큰지 작은지만 계속해서 판별하여 절반씩 줄여나가면, 빠르게 찾을 수 있다'

- 수행 과정
    1. 시작점, 중간점, 끝점을 설정
    2. 우리가 찾는 값이 중간점보다 큰지 작은지 판단
    3. 크다면, 중간점을 시작점으로 끝점을 끝점으로 하여 2번부터 다시 수행
    4. 작다면, 중간점을 끝점으로 시작점을 시작점으로 하여 2번부터 다시 수행
    5. 중간점과 찾는 값이 일치하면 종료한다.
    * 중간점이 소수일 땐, 정수부분만 취한다. 

- 시간 복잡도
    1. 한 번 사이클을 수행할 때마다 절반씩 줄어들기에 O(${logN}$)이라고 할 수 있다.
        - 정확하게는 O(${log_2N}$)이라고 할 수 있다.
        - 빅오표기법에 따라 O(${logN}$)으로 표기

```python
#재귀적 구현
import random
arr = [ i for i in range(10) ]
random.shuffle(arr)

def bin_search(arr,start,end,target):
    mid = start+ (end-start)//2
    if start >= end :
        return False

    if arr[mid] == target :
        return mid #인덱스 전달
    elif arr[mid] > target:
        return bin_search(arr,mid+1,end,target)
    else :
        return bin_search(arr,start,mid-1,target)

bin_search(arr,0,9,3)
```
```python
#반복문 구현
import random
arr = [i for i in range(10)]
random.shuffle(arr)

start = 0
end = 9
target = 4
while start < end :
    mid = (start+end)//2
    if arr[mid] == target:
        print(mid)
        break
    elif arr[mid] > target:
        end = mid - 1
    else :
        start = mid + 1

```
## 트리 자료구조
- 트리 자료구조란? 
    - 노드와 노드의 연결로 표현된 자료구조 ( 여기서 노드는 정보의 단위로 어떠한 정보를 갖는 개체 )
    - 몇 가지 주요한 특징을 가진다.
        1. 트리는 부모 노드와 자식 노드의 관계로 표현
        2. 트리의 최상단 노드를 루트 노드라고 부름
        3. 트리의 최하단 노드를 단말 노드라고 부름
        4. 트리에서 일부를 떼어내더라도 트리 구조, 여기서 떼어난 트리를 서브 트리라고 부름
        5. 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합하다.

- 이진 탐색의 전제 조건 : 데이터 정렬
    - 동작하고 있는 프로그램에서 데이터는 보통 정렬되어 있음 -> 효과적으로 사용할 수 있다.
    - 데이터 베이스는 내부적으로 대용량 데이터 처리에 적합한 **트리 자료구조**를 이용하여 데이터를 정렬
        - 따라서 데이터베이스에서의 탐색은 이진 탐색과는 약간 다르지만, 유사한 방법을 이용하여 항상 탐색을 빠르게 하도록 설계되어 있음

- 이진 탐색 트리
    - 트리 자료구조 중에서 **가장 간단한** 형태 : **이진 탐색 트리**
    - 이진 탐색 트리의 특징
        1. 부모 노드보다 왼쪽 자식 노드가 작다.
        2. 부모 노드보다 오른쪽 자식 노드가 크다.
        - 왼쪽 < 부모 < 오른쪽 

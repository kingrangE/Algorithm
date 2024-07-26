#실전문제 난이도 1.5
#시간제한 1초, 메모리 제한 128MB
#10:22


def DFS(arr,row,col):
    # 오른쪽에 값이 있으면 push 없으면 아래에 값을 검사하고 push 아래에도 없으면 pop 빈 리스트면 return  
    print(arr)
    arr[row][col] = 1
    row+=1
    if(row != len(arr)):
        if arr[row][col] == 0:
            DFS(arr,row,col)
    row -= 1
    col += 1
    if(col != len(arr[0])):
        if arr[row][col] == 0 : 
            DFS(arr,row,col)
    
    return arr

n,m = map(int,input().split())

arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

count = 0

for i in range(n):
    for j in range(m):
        # print(i,j,count)
        if arr[i][j] == 1 :
            continue
        print("-----------------")
        arr = DFS(arr,i,j)
        count += 1
        

print(count)
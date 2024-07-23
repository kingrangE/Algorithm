#1이 될 때까지 (2018 E 기업 알고리즘 대회 )
N,K = map(int,input().split())
cnt = 0

while True :
    if N%K == 0 : #나누어 떨어지면
        N //= K
        cnt += 1
    else : #나누어 떨어지지 않으면
        N -= 1
        cnt += 1
    print(f"N = {N} cnt = {cnt}")
    if(N == 1) : 
        break
print(cnt)

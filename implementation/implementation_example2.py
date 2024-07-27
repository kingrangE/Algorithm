# 시각 (시간제한 2초, 메모리 제한 128MB)
#3이 하나라도 포함되는 모든 경우의 수를 출력

N = int(input())
h,m,s = 0,0,0
total_time = (N+1)*60*60-1
result = 0
for i in range(total_time):
    h,m,s = int(h),int(m),int(s)

    s += 1

    if s==60 :
        m += 1
        s = 0
    if m==60 :
        h += 1
        m = 0
    h,m,s = str(h),str(m),str(s)

    if h.count('3') > 0 or m.count('3') > 0 or s.count('3') > 0 :
        #3이 하나라도 있으면
        result+=1

print(result)
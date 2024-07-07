import random
def sort(arr,ascend = True):

    n = len(arr)
    exchange = 0
    compare = 0
    k = 0
    while k < n-1 :
        last = n-1
        exchange_inter = 0
        for j in range(n-1,k,-1):
            compare +=1
            if(ascend) :
                if(arr[j-1]<arr[j]) :
                    exchange +=1
                    exchange_inter += 1
                    arr[j],arr[j-1] =arr[j-1],arr[j]
                    last = j
            else : 
                if(arr[j-1]>arr[j]):
                    exchange +=1
                    exchange_inter += 1
                    arr[j],arr[j-1] =arr[j-1],arr[j]
                    last = j
        k = last

        if(exchange_inter == 0):
            break

    print(f'교환횟수 : {exchange} 비교횟수 : {compare}')
    print(arr)
        

if __name__ == '__main__' :
    arr = list(range(1,11))

    random.shuffle(arr)
    #오름차순
    sort(arr)
    random.shuffle(arr)
    #내림차순
    sort(arr,ascend=False)
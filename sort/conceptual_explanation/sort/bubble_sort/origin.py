import random
def sort(arr,ascend = True):

    n = len(arr)
    exchange = 0
    compare = 0
    for i in range(n-1):
        for j in range(n-1,i,-1):
            compare +=1
            if(ascend) :
                if(arr[j-1]<arr[j]) :
                    exchange +=1
                    tmp = arr[j-1]
                    arr[j-1] = arr[j]
                    arr[j] = tmp
            else : 
                if(arr[j-1]>arr[j]):
                    exchange +=1
                    tmp = arr[j]
                    arr[j] = arr[j-1]
                    arr[j-1] = tmp


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
def merge(arr,low,mid,high):
    n = mid - low
    m = high - mid

    t1 = [arr[low+x] for x in range(n)]
    t2 = [arr[mid+x] for x in range(m)]

    i = 0
    j = 0
    k = low
    while i != n and j != m:
        if t1[i] >= t2[j]:
            arr[k] = t2[j]
            j += 1
            k += 1
        else:
            arr[k] = t1[i]
            i += 1
            k += 1

    while i != n:
        arr[k] = t1[i]
        i += 1
        k += 1

    while j != m:
        arr[k] = t2[j]
        j += 1
        k += 1

def mergeSort(arr,low,high):
    if low < high:
        mid = low + high
        mid //= 2
        mergeSort(arr,low,mid)
        mergeSort(arr,mid+1,high)
        merge(arr,low,mid,high)

n = int(input())
l = list(map(int,input().split()))
mergeSort(l,0,n)
for i in range(n):
    print(l[i], end = " ")
print()

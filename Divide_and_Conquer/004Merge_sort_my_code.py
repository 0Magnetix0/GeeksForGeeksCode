def merge(A,low,mid,high):
    n = mid - low + 1
    m = high - mid - 1
    
    t1 = [A[x+low] for x in range(n)]
    t2 = [A[x+mid+1] for x in range(m+1)]
    print(t1)
    print(t2)

    i = 0
    j = 0
    k = low

    while i < n and j < m:
        if t1[i] <= t2[j]:
            A[k] = t1[i]
            i += 1
            k += 1
        else:
            A[k] = t2[j]
            j += 1
            k += 1

    while i < n:
        A[k] = t1[i]
        i += 1
        k += 1

    while j < m:
        A[k] = t2[j]
        j += 1
        k += 1



def mergeSort(A,low,high):
    if low < high:
        mid = low + high
        mid //= 2
        mergeSort(A,low,mid)
        mergeSort(A,mid + 1, high)
        merge(A,low,mid,high)


l = list(map(int,input().split()))
mergeSort(l,0,len(l))
for i in range(len(l)):
    print(l[i], end = " ")
print()

def merge(A,low,mid,high):
    n = mid - low + 1
    m = high - mid

    t1 = [0]*n
    t2 = [0]*m

    for i in range(n):
        t1[i] = A[i+low]

    for j in range(m):
        t2[j] = A[j+mid+1]

    i = 0
    j = 0
    k = low

    while i < n and j < m:
        if t1[i] >= t2[j]:
            A[k] = t2[j]
            j += 1
            k += 1
        else:
            A[k] = t1[i]
            i += 1
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
        mergeSort(A,mid+1,high)
        merge(A,low,mid,high)


l = list(map(int,input().split()))
mergeSort(l,0,len(l)-1)

for x in l:
    print(x, end = " ")
print()

def partition(A,low,high):
    key = A[high]
    i = low - 1
    for j in range(low,high):
        if key >= A[j]:
            i += 1
            A[j] , A[i] = A[i] , A[j]

    A[i+1], A[high] = A[high], A[i+1]
    
    return i + 1


def quickSort(A,low,high):
    if low < high:
        mid = partition(A,low,high)
        quickSort(A,low,mid-1)
        quickSort(A,mid+1,high)
        

l = list(map(int,input().split()))
quickSort(l,0,len(l)-1)
for x in l:
    print(x, end = " ")
print()

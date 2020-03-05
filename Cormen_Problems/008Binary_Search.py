def binarysearch(A,low,high,key):
    mid = low + high
    mid //= 2
    if A[mid] == key:
        return mid
    elif A[mid] > key:
        return binarysearch(A,low,mid-1,key)
    else:
        return binarysearch(A,mid+1,high,key)


n = int(input())
l = list(map(int,input().split()))
print(binarysearch(l,0,n-1,4))


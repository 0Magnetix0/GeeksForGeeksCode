def binary_search(A,key,low,high):
    if low > high:
        return -1 
    mid = low + high
    mid //= 2
    if key == A[mid]:
        return mid + 1
    elif key > A[mid]:
        return binary_search(A,key,mid+1,high)
    else:
        return binary_search(A,key,low,mid-1)

l = list(map(int,input().split()))
k = int(input())
print(binary_search(l,k,0,len(l)-1))

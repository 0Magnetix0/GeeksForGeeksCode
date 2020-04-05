import random

def randomBinarySearch(A,low,high,key):
    if low > high:
        return -1
    n = random.randint(low,high)
    n = n%(high-low+1)
    n += low
    if A[n] == key:
        return n+1
    elif A[n] < key:
        return randomBinarySearch(A,n+1,high,key)
    else:
        return randomBinarySearch(A,low,n-1,key)





l = list(map(int,input().split()))
k = int(input())
print(randomBinarySearch(l,0,len(l)-1,k))

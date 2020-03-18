#https://practice.geeksforgeeks.org/problems/inversion-of-array/0
def merge(A,low,mid,high):
    n = mid - low + 1
    m = high - mid
    
    t1 = [0]*n
    t2 = [0]*m
    
    for i in range(n):
        t1[i] = A[i+low]
    
    for j in range(m):
        t2[j] = A[j+mid+1]
        
    count = 0
    
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
            count += (n-i)
            j += 1
            k += 1

    while j < m:
        A[k] = t2[j]
        k += 1
        j += 1
        
    while i < n:
        A[k] = t1[i]
        k += 1
        i += 1
        
    return count

def mergeSort(l,low,high):
    if low < high:
        mid = low + high
        mid //= 2
        left = mergeSort(l,low,mid)
        right = mergeSort(l,mid+1,high)
        inversions = merge(l,low,mid,high)
        #print("left = {0}, right = {1}, inversions = {2}".format(left,right,inversions))
        return inversions + left + right
    return 0

for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    print(mergeSort(l,0,len(l)-1))
    #print(l)

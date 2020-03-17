def check(a,b):
    p = str(a)
    q = str(b)
    r = p + q
    s = q + p
    r = int(r)
    s = int(s)
    if r >= s:
        return 0
    else:
        return 1
    
def partition(arr,low,high): 
    i = ( low-1 )        
    pivot = arr[high]     
  
    for j in range(low , high): 
        if  check(pivot,arr[j]): 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    quickSort(l,0,n-1)
    count = ""
    for i in range(n):
        count += str(l[i])
    print(count)
    
#https://practice.geeksforgeeks.org/problems/largest-number-formed-from-an-array/0

#Your task is to complete this function
#Function should return integer denoting the index
# indexing is done according to 0
# Left=0 and High=0
n = 0
def bin_search(arr, left, high, key):
    global n
    if left > high:
        return -1
    n = n % (high - left + 1)
    n += left
    if arr[n] == key:
        return n
    elif arr[n] > key:
        return bin_search(arr,left,n-1,key)
    else:
        return bin_search(arr,n+1,len(arr)-1,key)

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        x=int(input())
        print (bin_search(arr, 0, 0, x))
# } Driver Code Ends

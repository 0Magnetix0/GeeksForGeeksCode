#This program works by finding the largest element in the array.
def pivot(arr,low,high):

    #Corner case when the lenght of the array is 1.
    if len(arr) == 1:
        return 0

    #mid = -1 if no element is found.
    mid = -1

    #First to check whether the array is rotated or not.
    if arr[0] < arr[-1]:
        return 0

    #This is the size of the array.
    n = len(arr)

    #Binary Search termination condition.
    while low <= high:
        #computing mid.
        mid = (low+high)
        mid //= 2

        #Check whether the arr[mid] is max of the array or not.
        if arr[mid] > arr[(mid+1)%n] and arr[mid] > arr[(mid-1)]:
            return (mid+1)%n

        #Check wheter the arr[mid] is min of the array or not.
        elif arr[mid] < arr[(mid+1)%n] and arr[mid] < arr[(mid-1)]:
            return mid
        
        #If the arr[mid] is less than arr[low] then the largest number is on the right side of the mid element.
        elif arr[mid] < arr[low]:
            high = mid - 1

        #If the arr[mid] is greater than arr[low] then the largest number is on the left side of the mid element.
        else:
            low = mid + 1

def find_key(arr,key,p):
    n = len(arr)
    low = 0
    high = n - 1
    if p == 0:
        low = 0
        high = n - 1
    elif arr[p] > key or arr[p-1] < key:
        return -1
    elif arr[-1] >= key:
        low = p
        high = n - 1
    else:
        low = 0
        high = p - 1

    while low <= high:
        mid = low + high
        mid //= 2
        if arr[mid] == key:
            return mid
        elif arr[mid] >  key:
            high = mid - 1
        else:
            low = mid + 1
    return -1


#Enter the number of test cases.
print("Enter the number of test cases :: ", end = "")
t = int(input())

#Description of each test case.
for _ in range(t):

    #Enter the no of elements to be stored in the array.
    print("Enter the size of array :: ", end = "")
    n = int(input())

    #Enter the elements of the array.
    print("Enter the array elements :: ", end = "")
    l = list(map(int,input().split()))

    #Finding the pivot element.
    p = pivot(l,0,len(l)-1)

    #Enter the key to find.
    print("Enter the key to find :: ", end = "")
    key = int(input())
    
    #Printing the position of the key.
    print(find_key(l,key,p))

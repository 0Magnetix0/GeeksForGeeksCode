#Driven function defination.
def Selection_sort(A,n):
    for i in range(0,len(A)-1):
        #Selecting the minimum element for the following iteration.
        minimum = i

        #Checking for the minimum element in the following array.
        for j in range(i,len(A)):
            if A[minimum] > A[j]:
                minimum = j
               
        #Swap operation.
        temp = A[i]
        A[i] = A[minimum]
        A[minimum] = temp
        

#taking in the size of array.
n = int(input())

#taking in the array elements.
l = list(map(int,input().split()))

#Calling the selection sort function.
Selection_sort(l,n)

#Element's after the sorting process.
for x in l:
    print(x,sep = ",", end = " ")
print()

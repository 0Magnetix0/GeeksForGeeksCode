# Driven function called here.
def rotatebyk(l,n,k):
    #temp array creation.
    t = [x for x in l[:k]]

    #moving the equation from k, n to the starting position.
    for i in range(k,n):
        l[i-k] = l[i]

    #moving the elements saved in the t array back to prev array.
    for i in range(n-k,n):
        l[i] = t[i-n+k]

    #print the array.
    for i in range(n):
        print(l[i], end = " ")

    #next line
    print()

#no of test cases.
t = int(input())

#Details of every test cases.
for _ in range(t):

    #No of array elements.
    n = int(input())

    #Getting the array elements.
    l = list(map(int,input().split()))

    #No of position to move.
    k = int(input())

    #Calling the driven function.
    rotatebyk(l,n,k)

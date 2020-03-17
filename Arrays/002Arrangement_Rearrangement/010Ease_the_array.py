def ease_the_array(A,n):
    for i in range(len(A)-1):
        if A[i] == A[i+1]:
            A[i] *= 2
            A[i+1] = 0
    i = -1
    for j in range(len(A)):
        if A[j] > 0:
            i += 1
            A[j] , A[i] = A[i] , A[j]
            
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    ease_the_array(l,n)
    for i in range(n):
        print(l[i], end = " ")
    print()

# https://practice.geeksforgeeks.org/problems/ease-the-array/0

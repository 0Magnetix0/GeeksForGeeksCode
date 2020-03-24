def reverse(A,low,high):
    k = high - low
    k //= 2
    for i in range(k+1):
        A[i+low] , A[high-i] = A[high-i] , A[i+low]

def rearrangment(A, n):
    if n > 1:
        reverse(A, len(A) - n, len(A) - 1)
        n -= 1
        rearrangment(A, n)
        
for _ in range(int(input())):
    n = int(input())
    A = list(input().split())
    rearrangment(A, n)
    for x in A:
        print(x, end = " ")
    print()

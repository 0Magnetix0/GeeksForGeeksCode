def segregate(A):
    i = -1
    for j in range(len(A)):
        if A[j] % 2 == 0:
            i += 1
            A[i], A[j] = A[j] , A[i]

A = list(map(int,input().split()))
segregate(A)
for x in A:
    print(x, end = " ")
print()


def sort(A):
    l = []
    i = -1
    for k in range(len(A)):
        if A[k] < 0:
            l.append(A[k])
    for j in range(len(A)):
        if A[j] >= 0:
            i += 1
            A[j] , A[i] = A[i] , A[j]
    for k in range(len(l)):
        A[i+1+k] = l[k]

for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().split()))
    sort(A)
    for x in A:
        print(x, end = " ")
    print()

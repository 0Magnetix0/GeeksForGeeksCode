import random
def randomize_array(A):
    for i in range(len(A) - 1, -1, -1):
        idx = random.randint(24234124234,132121231231)
        idx = idx % (i + 1)
        A[i] , A[idx] = A[idx] , A[i]

A = list(map(int,input().split()))
randomize_array(A)
for x in A:
    print(x, end = " ")
print()


def display(n):
    count = 0
    for i in range(len(A)):
        if i % n == n - 1:
            print()
        print(A[i], end = " ")
    print()

def bubble_sort(A, idx):
    for i in range(len(A)//5):
        for j in range(i,len(A)//5):
            if A[i*5 + idx] < A[j*5 + idx]:
                A[i*5 + idx] , A[j*5 + idx] = A[j*5 + idx] , A[i*5 + idx]


def D_pivot(A, low, high):
    for i in range(len(A)//5):
        bubble_sort(A, i)
    return 0

n = int(input())
A = []
for i in range(n):
    l = list(map(int,input().split()))
    A.extend(l)
D_pivot(A, 0, len(A))
display(n)

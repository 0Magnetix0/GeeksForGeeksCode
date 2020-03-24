def display_A():
    print(A)

def rearrangment(A):
    low = 0
    high = len(A) - 1
    max_element = max(A)
    while low < len(A):
        key = A[high] % max_element
        if key == 0:
            key = A[high]
        A[low] = A[low] + max_element*key
        high -= 1
        low += 2
        #display_A()
    idx_i = 0
    idx_j = 1
    while idx_j < len(A):
        temp = A[idx_i] % max_element
        A[idx_j] = A[idx_j] + temp*max_element
        idx_i += 1
        idx_j += 2
        #display_A()
    for i in range(len(A)):
        A[i] = A[i]//max_element
        #display_A()
    A[-1] -= 1

for _ in range(int(input())):
    n = int(input())
    A = list(input().split())
    for i in range(len(A)):
        A[i] = int(A[i])
    rearrangment(A)
    for x in A:
        print(x, end = " ")
    print()

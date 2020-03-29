import random

def ranged_display(A):
    for x in A:
        print(x, end = " ")
    print()


def partition(A, low, high):
    i = low - 1
    idx = random.randint(0,high+1)
    idx %= (high - low + 1)
    key = A[idx]
    for j in range(low,high+1):
        if A[j] < key:
            i += 1
            A[i], A[j] = A[j], A[i]
    idx = i + 1
    for j in range(idx,high+1):
        if A[j] == key:
            i += 1
            A[j], A[i] = A[i], A[j]
    if i == low - 1:
        return i + 1
    return i

def kth_smallest(A, low, high, k):
    if low == high:
        return A[low]
    elif low < high:
        p = partition(A, low, high)
        ranged_display(A)
        if p >= k:
            return kth_smallest(A, low, p - 1, k)
        else:
            return kth_smallest(A, p + 1, high, k)



l = list(map(int,input().split()))
k = int(input())
print(kth_smallest(l, 0, len(l) - 1, k - 1))


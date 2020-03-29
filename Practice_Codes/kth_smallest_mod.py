import random

def ranged_display(A):
    for x in A:
        print(x, end = " ")
    print()


def partition(A, low, high):
    i = low - 1
    idx = random.randint(123412342141234,23423413412341232430)
    idx %= (high - low + 1)
    idx += low
    key = A[idx]
    print(key)
    for j in range(low,high+1):
        if A[j] <= key:
            i += 1
            A[i], A[j] = A[j], A[i]
            if j == idx:
                idx = i
    A[idx], A[i] = A[i], A[idx]
    return i

def kth_smallest(A, low, high, k):
    if low == high:
        return A[low]
    if low < high:
        p = partition(A, low, high)
        print(p)
        ranged_display(A)
        if p == k:
            return A[p]
        elif p > k:
            print("range- {0} to {1}".format(low,p-1))
            return kth_smallest(A, low, p-1, k)
        else:
            print("range- {0} to {1}".format(p+1,high))
            return kth_smallest(A, p+1, high, k)

'''
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    k = int(input())
    print(kth_smallest(l, 0, len(l) - 1, k - 1))
    print("#"*100)
'''
l = list(map(int,input().split()))
k = int(input())
print(kth_smallest(l, 0, len(l) - 1,k))

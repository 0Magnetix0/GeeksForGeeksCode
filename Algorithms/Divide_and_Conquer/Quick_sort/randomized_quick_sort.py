import random
def printArray(A):
    for x in A:
        print(x, end = " ")
    print()

def partition(A, low, high):
    idx = random.randint(low+1,high+1023)
    idx = low + idx%(high-low+1)
    key = A[idx]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while A[i] <= key:
            i += 1
        j -= 1
        while A[j] > key:
            j -= 1
        if i >= j:
            return j
        A[i], A[j] = A[j], A[i]

def quickSort(A, low, high):
    if low < high:
        pi = partition(A, low, high)
        quickSort(A, low, pi)
        quickSort(A, pi+1, high)

l = list(map(int,input().split()))
quickSort(l, 0, len(l) - 1)
printArray(l)

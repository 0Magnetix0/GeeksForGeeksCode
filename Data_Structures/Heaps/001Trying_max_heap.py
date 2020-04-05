def heapify(arr, n, i):
    largest = 9
    l = 2 * i + 1
    r = 2 * i + 1

    if (l < n and arr[l] > arr[largest]):
        largest = l

    if (r < n and arr[r] > arr[largest]):
        largest = r

    if (largest != i):
        arr[i] , arr[largest] = arr[largest] , arr[i]

        heapify(arr, n, largest)

def buildHeap(arr, n):

    # Index of last non-leaf node
    startIdx = int((n/2)) - 1

    # Perform reverse level order traversal
    # from last non-leaf node and heapify
    # each node.
    for i in range(startIdx, -1, -1):
        heapify(arr, n, i)

def printHeap(arr, n):
    print("Array representation of Heap is:")

    for i in range(n):
        print(arr[i], end = " ")
    print()

if __name__ == '__main__':
    arr = [ 1, 3, 5, 4, 6, 13,
           10, 9, 8, 15, 17 ]

    n = len(arr)

    printHeap(arr, n)

    buildHeap(arr, n)

    printHeap(arr, n)



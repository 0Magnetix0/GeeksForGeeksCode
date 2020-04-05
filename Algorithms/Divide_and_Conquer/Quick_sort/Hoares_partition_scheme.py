def partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        i = i + 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]
        printArray(arr, len(arr))

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi)
        quickSort(arr, pi + 1, high)

def printArray(arr, n):
    for x in arr:
        print(x, end = " ")
    print()

l = list(map(int,input().split()))
quickSort(l, 0, len(l) - 1)
printArray(l, len(l))


def array_reverse(array,n):
    for i in range(n//2):
        array[i] , array[n-1-i] = array[n-1-i], array[i]

    print("Array elements reversed are :: ")
    for x in array:
        print(x, end = " ");
    print()

print("Enter the size")
n = int(input())
print("Enter the array elements")
l = list(map(int,input().split()))
# The array reversal function called.
array_reverse(l,n)

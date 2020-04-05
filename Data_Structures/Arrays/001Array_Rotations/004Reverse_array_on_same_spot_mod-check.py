def array_reverse(array,k,n):
    for i in range(n//2):
        array[i+k] , array[n-1-i+k] = array[n-1-i+k], array[i+k]

print("Enter the size")
n = int(input())
print("Enter the array elements")
l = list(map(int,input().split()))
# The array reversal function called.
array_reverse(l,0,n)

print("Array rotated are :: ", end = "")
for x in l:
    print(x, end = " ")
print()

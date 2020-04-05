# mid gives the length of the sub array.
# Dividing the array in half to equating one half to other half.
# The index is incremented by i to get the current index.
def reverse(array, i, j):
    mid = j - i
    mid //= 2
    for k in range(mid):
        array[k+i], array[j-1-k] = array[j-1-k] , array[k+i]

#Rotate the first sub array A[:d].
#Rotate the second sub array A[d:].
#Rotate the final array formed.
def rotate(array, n, d):
    reverse(array, 0, d)
    reverse(array, d, n)
    reverse(array, 0, n)

#The size of the array.
print("Enter the size of the array", end = " ")
n = int(input())

#The elements are recoreded here.
print("Enter the array element :: ", end = "")
array = list(map(int,input().split()))

#The no of time's the array needs to be rotated.
print("Enter the time's to be rotated :: ", end = "")
d = int(input())

#performing mod of d with n.
d %= n

#rotate function called here.
rotate(array, n, d)

#printing the array elements after array rotation.
print("The array elements after performing the rotation operation is :: ", end = "")
for x in array:
    print(x, end = " ")
print()

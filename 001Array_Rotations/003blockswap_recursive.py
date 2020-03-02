def swap():
    print()

def block_swap(array, k):
    i = k
    j = len(array) - k
    while i != j:
        if i < j:
            swap(array[])

print("Block swap recursive version")
print("Enter the no of element's in the array :: ", end = "")
n = int(input())

#Enter the array elements here.
print("Enter the array elements :: ", end = "")
array = list(map(int,input().split()))

#The no of operation's to be performed.
print("The number of rotations to be performed")
k = int(input())

k %= n
#The rotation function is called here.
block_swap(array, k)


for x in array:
    print(x, end = " ")
print()


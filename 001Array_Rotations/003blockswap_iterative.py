def swap(array,

def block_swap(array, k):
    i = k
    j = len(array) - k
    while i != j:
        if i < j:
            swap(array[






print("Block Swap algorith iterative version")
n = int(input())
array = list(map(int,input().split()))
print("The number of rotaions to be peformed")
k = int(input())
k %= n
block_swap(array, k)


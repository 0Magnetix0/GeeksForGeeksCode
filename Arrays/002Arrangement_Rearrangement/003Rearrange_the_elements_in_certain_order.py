def rearrange(arr):
    arr.sort()
    l = [0 for i in range(len(arr))]
    i = len(arr)-1
    j = 0
    for k in range(len(arr)-1,-1,-1):
        if k % 2 == 0:
            l[k] = arr[i]
            i -= 1
        else:
            l[k] = arr[j]
            j += 1

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    rearrange(l)
    for i in range(len(l)):
        print(l[i], end = " ")
    print()

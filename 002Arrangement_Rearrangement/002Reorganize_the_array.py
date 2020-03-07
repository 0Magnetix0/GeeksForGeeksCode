def reorganize(l):
    for i in range(0,len(l),0):
        if l[i] >= 0 && i != -1:
            temp = arr[arr[i]]
            arr[arr[i]] = arr[i]
            arr[i] = temp
        else:
            i += 1

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    reorganize(l)
    for i in range(len(l)):
        print(l[i], end = " ")
    print()

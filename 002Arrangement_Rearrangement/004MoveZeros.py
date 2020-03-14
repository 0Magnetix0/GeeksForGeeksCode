def move_zeros(arr,n):
    j = -1
    for i in range(n):
        if arr[i] != 0:
            j += 1
            arr[j] , arr[i] = arr[i], arr[j]
    for i in range(j+1,n):
        arr[i] = 0
        
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    move_zeros(l,n)
    for i in range(n):
        print(l[i], end = " ")
    print()

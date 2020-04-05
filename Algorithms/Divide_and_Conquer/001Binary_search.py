for _ in range(int(input())):
    n, k = map(int,input().split())
    l = list(map(int,input().split()))
    flag = False
    low = 0
    high = n - 1
    while low <= high:
        mid = low + high
        mid //= 2
        if l[mid] == k:
            flag = True
            print("1")
            break
        elif l[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    if not flag:
        print("-1")

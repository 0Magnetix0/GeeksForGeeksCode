def min_steps(arr,n,k):
    l = []
    count_spots = 0
    for x in arr:
        if x <= k:
            l.append(1)
            count_spots += 1
        else:
            l.append(0)
    current_max = 0
    for i in range(0,count_spots):
        current_max += l[i]
    temp_max = current_max
    for i in range(1,n-count_spots+1):
        temp_max = temp_max - l[i-1] + l[count_spots+i-1]
        if temp_max > current_max:
            current_max = temp_max
    return count_spots-current_max

for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    k = int(input())
    print(min_steps(l,n,k))
    
    

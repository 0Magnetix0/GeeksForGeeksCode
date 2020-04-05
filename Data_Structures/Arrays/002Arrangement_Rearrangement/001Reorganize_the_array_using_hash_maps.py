t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    x = [0 for i in range(len(l))]
    for y in l:
        if y != -1:
            x[y] += 1
    
    for i in range(len(x)):
        if x[i] == 0:
            l[i] = -1
        else:
            l[i] = i
    
    for i in range(len(l)):
        if l[i] != i:
            l[i] = -1
    
    for i in range(len(l)):
        print(l[i], end = ' ')
    print()

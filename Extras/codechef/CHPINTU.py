t = int(input())
for _ in range(t):
    m, n = map(int,input().split())
    f = list(map(int,input().split()))
    p = list(map(int,input().split()))
    fq = [0 for i in range(m+1)]
    for i in range(len(f)):
        fruit = f[i]
        cost = p[i]
        print(fruit)
        print(cost)
        fq[fruit] += cost
    
    print(fq)

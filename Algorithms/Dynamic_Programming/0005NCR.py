for _ in range(int(input())):
    n, r = map(int,input().split())
    ncr = 1
    num = 0
    den = 0
    if n < r:
        print("0")
        continue
    for i in range(r+1,n+1):
        num = i
        den = i - r
        ncr *= num
        ncr //= den
    print(ncr%1000000007)

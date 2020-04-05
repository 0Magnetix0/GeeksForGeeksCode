def power(n,r):
    if r == 0:
        return 1
    elif r == 1:
        return n%1000000007
    elif r == 2:
        return n*n
    if r % 2 == 0:
        return (power((power(n,r/2)%1000000007),2))%1000000007
    else:
        return ((n%1000000007)*(power(n,r-1)%1000000007))%1000000007

for _ in range(int(input())):
    n = int(input())
    r = str(n)
    r = r[::-1]
    r = int(r)
    print(power(n,r))

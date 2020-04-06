#DIFFRENT METHOD COPIED

for i in range(1,1001):
    arr[i] = i * arr[i - 1]

for _ in range(int(input())):
    n, k = map(int, input().split())
    print((arr[n]//(arr[k] * arr[n - k])) % 1000000007)

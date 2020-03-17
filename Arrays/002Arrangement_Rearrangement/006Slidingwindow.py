def sliding_window_sum(A,n,k):
    window_sum = 0
    for i in range(0,k):
        window_sum += A[i]
    print("window sum {0}".format(window_sum))
    for j in range(1,n-k+1):
        window_sum = window_sum - A[i-1] + A[k+i-1]
        print("window sum {0}".format(window_sum))

n = int(input())
l = [x for x in range(1,n+1)]
print(l)
k = int(input())
sliding_window_sum(l,n,k)


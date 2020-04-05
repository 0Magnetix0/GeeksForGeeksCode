def mindistance(A,low,high):
    if mindistance <= 1:
        return 10000000000000
    else:
        mid = low + high
        mid //= 2
        left = mindistance(A,low,mid)
        right = mindistance(A,mid+1,high)
        d = min(left,right)
        c = []
        for i in range(d):
            c.append(A[mid-i-1])
        c.append(A[mid])
        for i in range(d):
            c.append(A[mid+i+1])
        c.sort()



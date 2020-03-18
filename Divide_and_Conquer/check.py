def mindistance(A,low,high):
    if mindistance <= 1:
        return 10000000000000
    else:
        mid = low + high
        mid //= 2
        left = mindistance(A,low,mid)
        right = mindistance(A,mid+1,high)
        c = [0]*(right-left)
        for i in range(
        

def merge(A,p,q,r):
    n = q - p + 1
    m = r - q

    s = [A[x] for x in range(p,q+1)]
    s.append(10000000)

    v = [A[x] for x in range(q+1,r)]
    v.append(10000000)

    j = 0
    k = 0
    for i in range(p,r):
        if s[j] >= v[k]:
            A[i] = v[k]
            k += 1
        else:
            A[i] = s[j]
            j += 1


n = int(input())
l = list(map(int,input().split()))
mid = 0+n
mid //= 2
merge(l,0,mid-1,len(l))
print(l)


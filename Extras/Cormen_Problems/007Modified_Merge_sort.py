def insertion_sort(A,p,q):
    for j in range(p+1,q):
        key = A[j]
        i = j - 1
        while i >= p and key > A[i]:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key


def merge(A,p,q,r):
    n = q - p + 1
    m = r - q

    l1 = [A[x+p] for x in range(n)]
    l1.append(1000000)
    l2 = [A[x+q] for x in range(m)]
    l2.append(1000000)
    
    b = 0
    c = 0

    for i in range(p,r):
        if l1[b] >= l2[c]:
            A[i] = l2[c]
            c += 1
        else:
            A[i] = l1[b]
            b += 1

def merge_sort(A,p,q,k):
    if p < q:
        r = p+q
        r //= 2
        if r - p >= k:
            merge_sort(A,p,r)
            merge_sort(A,r+1,q)
        else:
            insertion_sort(A,p,r)
            insertion_sort(A,r+1,q)
        merge(A,p,r,q)


n = int(input())
k = int(input())
l = list(map(int,input().split()))
merge_sort(l,0,n,k)
print(l)


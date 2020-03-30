def insertion_sort(l,n):
    for j in range(1,n):
        key = l[j]
        i = j - 1
        while i >= 0 and key < l[i]:
            l[i+1] = l[i]
            i -= 1
        l[i+1] = key

l = list(map(int,input().split()))
n = len(l)
insertion_sort(l,n)
for x in l:
    print(x, end = " ")
print()

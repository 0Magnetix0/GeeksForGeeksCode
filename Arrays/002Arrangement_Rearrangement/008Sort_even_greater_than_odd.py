#Sort the array in such a way that the element of the odd position is lower that its even counter parts.
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    cl = [x for x in l]
    cl.sort()
    j = 0
    k = len(cl) - 1
    for i in range(len(l)):
        if (i+1) % 2 == 0:
            l[i] = cl[k]
            k -= 1
        else:
            l[i] = cl[j]
            j += 1
    for i in range(len(l)):
        print(l[i], end = " ")
    print()

#https://practice.geeksforgeeks.org/problems/rearrange-array-such-that-even-positioned-are-greater-than-odd/0

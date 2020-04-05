max_count = 0

def reverse(l,low,high):
    n = high - low
    n //= 2
    n += 1
    for i in range(n):
        l[i+low] , l[high-i] = l[high-i] , l[i+low]


def rotate(c):
    reverse(l,0,1)
    reverse(l,2,len(c)-1)
    reverse(l,0,len(c)-1)

def max_humming_distance(l,c):
    global max_count
    current_count = 0
    for i in range(len(l)-1):
        for j in range(len(l)):
            if l[j] != c[j]:
                current_count += 1
        rotate(c)
        if current_count > max_count:
            max_count = current_count
    return max_count

l = list(map(int,input().split()))
c = l[:]
print(max_humming_distance(l,c))


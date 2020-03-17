def max_rotation(l):
    array_sum = 0
    current_sum = 0
    for i in range(len(l)):
        array_sum += l[i]
        current_sum += l[i]*i
    max_sum = current_sum
    for i in range(1,len(l)):
        current_sum = current_sum - (len(l))*l[n-i] + array_sum
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

n = int(input())
l = list(map(int,input().split()))
max_sum = max_rotation(l)
print(max_sum)

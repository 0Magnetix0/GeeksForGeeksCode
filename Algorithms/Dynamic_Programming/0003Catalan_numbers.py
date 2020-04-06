catalan_numbers = [1,1,2]
count = 2

for _ in range(int(input())):
    n = int(input())
    if n <= count:
        print(catalan_numbers[n])
    else:
        while count != n:
            sum = 0
            i = 0
            j = count
            while i != count + 1:
                temp = catalan_numbers[i]*catalan_numbers[j]
                sum += temp
                i += 1
                j -= 1
            count += 1
            catalan_numbers.append(sum)
        count = n
        print(catalan_numbers[n])

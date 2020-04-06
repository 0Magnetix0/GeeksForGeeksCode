# It was about saving previous test cases onto a array for future usage !!
ugly = [1]
count = 1
i2 = i3 = i5 = 0

for _ in range(int(input())):
    n = int(input())
    if n <= count:
        print(ugly[n-1])
    else:
        for i in range(n - len(ugly)):
            a = ugly[i2]*2
            b = ugly[i3]*3
            c = ugly[i5]*5
            temp = min(a,b,c)
            if temp == a:
                i2 += 1
            if temp == b:
                i3 += 1
            if temp == c:
                i5 += 1
            ugly.append(temp)
            count += 1
        print(ugly[-1])

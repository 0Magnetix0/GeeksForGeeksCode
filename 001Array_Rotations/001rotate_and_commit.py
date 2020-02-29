#Take no of test cases.
t = int(input())

#t test case follow.
for _ in range(t):
    #Each test case Descriptions.
    n = int(input())

    #taking in the array.
    a = list(map(int,input().split()))

    #According to the output pattern.
    if n <= 4:
        if n % 2 == 0:
            print(a[1])
        else:
            print(a[n-1])
    else:
        temp = n//4
        temp += 2
        if n % 4 == 3:
            print(a[temp])
        elif n % 4 == 0:
            print(a[temp-2])
        else:
            print(a[temp-1])

"""
1
2
3
2
3
3
4
3
4
4
5
4
5
5
6
5
6
6
7
6
"""

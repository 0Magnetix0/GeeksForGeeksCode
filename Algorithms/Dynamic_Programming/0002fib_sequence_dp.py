fib_numbers = [1,1]
count = 2

def fib(n):
    global count
    if n <= count:
        return (fib_numbers[n-1]%1000000007)
    else:
        for i in range(count,n):
            fib_numbers.append(fib_numbers[i-2] + fib_numbers[i-1])
        count = n
        return (fib_numbers[n-1]%1000000007)
    
    
for _ in range(int(input())):
    n = int(input())
    print(fib(n))

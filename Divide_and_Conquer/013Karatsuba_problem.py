def count_digits(a):
    count = 0
    while a != 0:
        count += 1
        a //= 10
    return count

def power(a,b):
    return pow(a,b)

def karatsubaMul(a, b):
    dig_a = count_digits(a)
    dig_b = count_digits(b)
    dig = min(dig_a,dig_b)
    ref = dig//2
    if dig <= 1:
        return a*b
    else:
        p = (a//power(10,ref))
        q = (b//power(10,ref))
        r = a - (p*power(10,ref))
        s = b - (q*power(10,ref))
        prod1 = karatsubaMul((p+r),(q+s))
        prod2 = karatsubaMul(p,q)
        prod3 = karatsubaMul(r,s)
        
        #look here you dumb idiot that ref is a integer division of dig
        #you spent a whole day because of this one dumb mistake 
        
        return prod2*power(10,2*ref) + (prod1-prod2-prod3)*power(10,ref) + prod3

def decConv(a, b):
    x = 0
    y = 0
    for i in a:
        x = x*2 + int(i)
    for j in b:
        y = y*2 + int(j)
    return x, y


for _ in range(int(input())):
    l, m = input().split(' ')
    p, q = decConv(l, m)
    print(karatsubaMul(p,q))
    
    

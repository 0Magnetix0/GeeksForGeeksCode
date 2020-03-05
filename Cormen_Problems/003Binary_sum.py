def binary_sum(A,B,C):
    carry = 0
    for i in range(0,len(A)):
        temp = A[i] + B[i]
        temp += carry
        if temp == 0:
            C[i] = 0
        elif temp == 1:
            C[i] = 1
        elif temp == 2:
            C[i] = 0
            carry = 1
        else:
            C[i] = 1
            carry = 2
    if carry <= 1:
        C[len(A)] = carry
    elif carry == 2:
        C[len(A)] = 0
        C.append(1)


n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = [0 for i in range(n+1)]
binary_sum(A,B,C)
for x in C:
    print(x, end = " ")
print()


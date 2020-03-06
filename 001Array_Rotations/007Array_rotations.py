n=int(input())
arr=list(map(int,input().split()))
mi=arr[0]
count=0
for i in range(1,n):
    if(arr[i]>=mi):
        count += 1
        mi=arr[i]
        continue
    if(arr[i]<mi):
        break
    if(count==n-1):
        count=0
        print(count)
    else:
        print(count+1)


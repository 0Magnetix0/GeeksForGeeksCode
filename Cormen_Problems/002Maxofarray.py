def max_ele(l,low,high):
    #print(high-low)

    #Condition for array with size 0.
    if low > high:
        return;

    #If there is only one element left.
    elif low == high:
        return l[low]

    #This is the recursive case in which the program is divided into two.
    else:
        mid = low + high
        mid //= 2
        max1 = max_ele(l,low,mid)
        max2 = max_ele(l,mid+1,high)

        #Comparing the max of the two sub arrays.
        if max1 > max2:
            return max1
        else:
            return max2

#Recursive program to find the minimum element.

#Enter the size of the array.
print("Enter the size of the array")
n = int(input())

#Enter the element's of the array.
print("Enter the element's of the array")
l = list(map(int,input().split()))

#Calling the driven function.
max_num = max_ele(l,0,n-1)

#Printing the maximum no in the array.
print(max_num)

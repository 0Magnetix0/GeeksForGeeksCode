def sorting_integers(arr):
    i = 1
    j = 2
    flag = True
    if arr[i] >= 0:
        flag = False

    while j != len(arr):
        if flag:
            if arr[i] < 0:
                flag = False
                i += 1
            else:
                if arr[j] < 0:
                    arr[i], arr[j] = arr[j] , arr[i]
                    flag = False
                    i += 1
                    j += 1
                else:
                    j += 1
        else:
            if arr[i] > 0:
                flag = True
                i += 1
            else:
                if arr[j] > 0:
                    arr[i], arr[j] = arr[j] , arr[i]
                    flag = True
                    i += 1
                    j += 1
                else:
                    j += 1

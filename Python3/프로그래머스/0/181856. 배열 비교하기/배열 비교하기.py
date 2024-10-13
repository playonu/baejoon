def solution(arr1, arr2):
    leng1 = len(arr1)
    leng2 = len(arr2)
    if leng1 > leng2 :
        return 1
    elif leng2 > leng1 :
        return -1
    sum1 = sum(arr1)
    sum2 = sum(arr2)
    
    if sum1 > sum2 :
        return 1
    elif sum2 > sum1 :
        return -1
    return 0
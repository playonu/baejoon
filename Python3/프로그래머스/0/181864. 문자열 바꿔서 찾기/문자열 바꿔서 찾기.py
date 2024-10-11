def solution(myString, pat):
    arr = list(myString)
    for i in range(0, len(arr)):
        if arr[i] == 'A':
            arr[i] = 'B'
        else:
            arr[i] = 'A'
    newStr = ''.join(arr)
    
    if pat in newStr :
        return 1
    else :
        return 0
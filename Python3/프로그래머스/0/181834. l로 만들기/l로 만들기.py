def solution(myString):
    arr = list(myString)
    for i in range (0, len(arr)):
        if ord("l")>= ord(arr[i]):
            arr[i] = "l"
            
    answer = ''.join(arr)
    return answer
def solution(n): 
    arr = []
    answer = 0
    for i in range(1, n+1):
        if n % i == 0: 
            arr.append(i)
    return sum(arr)

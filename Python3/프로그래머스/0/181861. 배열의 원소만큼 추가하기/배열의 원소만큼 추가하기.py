def solution(arr):
    answer = []
    for n in arr:
        for i in range(0, n):
            answer.append(n)
    return answer
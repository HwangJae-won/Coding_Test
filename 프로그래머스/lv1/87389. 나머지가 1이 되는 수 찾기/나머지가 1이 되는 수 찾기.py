def solution(n):
    x = n-1
    answer = 0
    for i in range(2, x+1):
        if x%i ==0:
            answer=i
            break
    return answer


def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    li = [score[i:i+m] for i in range(0, len(score), m)]
    
    for i in range(len(li)):
        if len(li[i]) == m:
            p= min(li[i])
            answer+= p*m
    return answer
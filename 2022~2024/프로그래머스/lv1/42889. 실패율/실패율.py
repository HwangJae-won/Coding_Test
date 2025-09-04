def solution(N, stages):
    rate= {}
    length = len(stages)
    for i in range(1, N+1):
        if length != 0:
            cnt = stages.count(i)
            rate[i] = cnt / length 
            length -= cnt
        else: 
            rate[i] = 0 
    answer = sorted(rate.keys(), key= lambda key: rate[key], reverse= True)
    return answer
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    #두개의 리스트를 비교해서 포함되지 않는 거 return
    for i in range(len(completion)):
        if (participant[i] !=completion[i]):
            return participant[i]
    return participant[len(participant)-1]

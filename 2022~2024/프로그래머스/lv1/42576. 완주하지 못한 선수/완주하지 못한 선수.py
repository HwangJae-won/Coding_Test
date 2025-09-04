def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    #두개의 리스트를 비교해서 포함되지 않는 거 return
    for i in range(len(completion)):
        if (participant[i] !=completion[i]):
            return participant[i]
    return participant[len(participant)-1]

##Counter 활용한 풀이
# import collections
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]
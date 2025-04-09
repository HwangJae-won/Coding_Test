from collections import Counter
def solution(participant, completion):
    answer =''
    c_p = Counter(participant)
    c_c = Counter(completion)
    no_complete_li = c_p-c_c
    answer = list(no_complete_li.keys())[0]
    return answer
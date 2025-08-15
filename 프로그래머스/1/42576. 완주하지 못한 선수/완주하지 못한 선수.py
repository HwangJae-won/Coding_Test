#Counter 없이 딕셔너리만 쓰기 
def solution(participant, completion):
    counts = {}
    for name in participant:
        if name in counts:
            counts[name] += 1
        else:
            counts[name] = 1

    for name in completion:
        counts[name] -= 1
        if counts[name] == 0:
            del counts[name]

    return list(counts.keys())[0]

#Counter 사용
from collections import Counter

def solution(participant, completion):
    diff = Counter(participant) - Counter(completion)
    return list(diff.keys())[0]

#조합 만들어서 합 구하기 
from itertools import combinations
def solution(numbers):
    answer = []
    li = list(combinations(numbers,2))
    for i in range(len(li)):
        answer.append(sum(li[i]))
    return sorted(list(set(answer)))

from itertools import combinations
def solution(number):
    answer = 0
    s_li = list(combinations(number, 3))
    for i in range(len(s_li)):
        if sum(s_li[i]) == 0:
            answer+=1
    return answer
#중복 가능, 순서 고려, 원소 개수 유한
import re
def solution(s):
    answer = []
    a = s.split(',{')
    a.sort(key = len)
    for j in a:
        numbers = re.findall("\d+", j)
        for k in numbers:
            if int(k) not in answer:
                answer.append(int(k))
    return answer
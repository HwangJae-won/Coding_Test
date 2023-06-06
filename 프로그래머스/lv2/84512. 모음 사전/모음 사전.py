#모음만을 사용하여 만들 수 있는 단어 : 순열 활용
from itertools import product

def solution(word):
    li = []
    for i in range(1,6):
        for c in product(['A',"E", "I","O","U"], repeat = i):
            li.append(''.join(list(c)))
    li.sort()
    return li.index(word)+1
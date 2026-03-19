#가장 많이 주문한 메뉴에 대해 코스 요리로 묶음
#2가지 이상 단품 메뉴, 2명 이상의 손님이 주문한 조합에 대해서만 후보에 포함
#길이별 조합 찾기+counter 활용?: 중복 이중문,,, 최선인가
from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer=[]
    for i in course:
        li=[]
        for j in orders:
            for k in combinations(j, i):
                res = ''.join(sorted(k))
                li.append(res)
        sorted_li = Counter(li).most_common()
        answer+= [menu for menu, cnt in sorted_li if cnt>1 and cnt == sorted_li[0][1] ]

    return sorted(answer)
#각 조각에 동일한 가짓수의 토핑이 올라가도록 하기 : 종류의 가지수가 동일하게 할 것 
#슬라이싱으로 리스트 나누고 유니크로 개수 확인하기: 2개로 나눌 수 있는 경우의 수 => X...
#Counter 활용
from collections import Counter
def solution(topping):
    dic = Counter(topping)
    set_dic = set()
    res = 0 
    for i in topping: 
        dic[i]-=1
        set_dic.add(i)
        if dic[i] ==0:
            dic.pop(i)
        if len(dic) == len(set_dic):
            res+=1
    return res
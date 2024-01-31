#자카드 유사도 : 집한 간의 유사도를 검사하는 방법 
#교집합의 크기/합집합 크기 | 모두 공집합일 경우 1로 정의 
#문자열 2개씩 끊어서 원소로 만들기 
import re
def clean(str, li):
    for i in range(len(str)-1):
        subset = str[i:i+2]
        if len(subset) == 2 and re.match('[a-zA-Z]{2}', subset):
            li.append(subset)
def solution(str1, str2):
    str1= str1.lower() ; str2= str2.lower()
    li1 = [] ; li2 = [] 
    clean(str1, li1) ; clean(str2, li2)
    print(li1) ; print(li2)
    if not set(li1) and not set(li2):
        print("empty")
        return 65536    # 두 다중집합이 공집합인 경우
    a = sum(min(li1.count(el), li2.count(el)) for el in set(li1))
    b = len(li1) + len(li2) - a

    return int((a / b) * 65536)
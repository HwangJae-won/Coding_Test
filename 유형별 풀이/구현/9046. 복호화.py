"""
9046. 복호화
- 알파벳 빈도수 체크 수 최빈 단어 출력
- 여러개일 경우 ?

---
Count 등 사용할 수 있지만 구현 연습 중이니까 최대한 내가 직접 알고리즘을 짠다는 느낌으로 짜보자 
- 반복문, 딕셔너리 활용하기 
구현처럼 생각해보자 
1. 빈도수 체크 알고리즘 
2. 단어수가 제일 큰 단어 출력

딕셔너리 자유자제로 다룰 수 있게 할 것 
"""
n = int(input())
for _ in range(n):
    s = input().replace(" ", "")
    dic ={}
    for temp in s:
        if temp in dic:
            dic[temp]+=1
        else: 
            dic[temp] = 1
    max_n = max(dic.values())
    max_li = [k for k,v in dic.items() if v ==max_n]
    
    if len(max_li)>1:
        print("?")
    else:
        print(max_li[0])
            

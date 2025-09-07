"""
9046. 복호화
https://www.acmicpc.net/problem/9046
---
문제
- 평문의 알파벳을 암호문의 알파벳으로 대치시켜 치환
- 암호문 알파벳의 빈도수를 체크하고, 가장 빈번하게 나타나는 문자를 출력하는 프로그램을 작성
- 만약 주어진 암호문에서 가장 빈번하게 나타나는 문자가 여러 개일 경우,'?'를 출력

입력
입력의 T(1 ≤ T ≤ 20)는 테스트 케이스로, 입력 제일 상단에 주어진다. 각각의 테스트 케이스는 한 줄마다 소문자와 공백으로 이루어진 영어 문장이 주어진다. 이 문장의 길이는 적어도 1이상이며 255이하다.

출력
각각의 테스트 케이스에 대해, 가장 빈번하게 나타나는 문자를 출력하거나 빈번하게 나타나는 문자가 여러 개일 경우 '?'를 출력한다.
"""

#빈도수 체크 - 가장 큰 value를 가지는 key 출력하기 
from collections import Counter

t = int(input())
for _ in range(t):
    word = input().replace(" ","")
    num_dic = Counter(word)
    max_val =[k for k,v in num_dic.items() if max(num_dic.values()) == v]

    if len(max_val) != 1 :
        print("?")
    else:
        print(max_val[0])
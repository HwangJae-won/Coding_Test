"""
[9012. 괄호]
- ( , ) 로만 구성된 괄호 문자열 
- () : 기본 문자열, VPS라 정의 
- x,y가 VPS면 (x), xy도 모두 VPS
- 주어진 문자열의 VPS 여부 판단하여 YES or NO 출력 
"""
n = int(input())
for i in range(n):
    
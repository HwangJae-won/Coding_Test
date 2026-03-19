#Greedy : 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자
#k: 제거할 수의 개수
from itertools import combinations
def solution(number, k):
    com= list(combinations(number, len(number) - k))
    s =[]
    for i in com:
        s.append(int(''.join(i)))
    return str(max(s))
#combination 활용 코드: 시간 초과..

#stack 활용
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
        
    return "".join(stack) if k == 0 else "".join(stack[:-k])
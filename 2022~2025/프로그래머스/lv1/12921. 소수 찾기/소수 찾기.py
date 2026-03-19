#소수 개수 반환하기: 에라토스테네스의 체 활용
import math 
def prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x% i ==0:
            return False
    return True
def solution(n):
    answer= 0
    for i in range(2, n+1):
        if prime(i):
            answer+=1
    return answer
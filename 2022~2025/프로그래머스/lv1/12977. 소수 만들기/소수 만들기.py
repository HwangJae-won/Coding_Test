from itertools import combinations
import math
#소수 체크 함수
def calculate(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    #리스트 내에서 숫자 3개 뽑는 조합
    temp =list(combinations(nums,3))
    sum_li =[]
    for i in range(len(temp)):
        sum_li.append(sum(temp[i]))
    answer= 0 
    for k in range(len(temp)):
        if calculate(sum(temp[k])) ==True:
            answer+=1
    return answer
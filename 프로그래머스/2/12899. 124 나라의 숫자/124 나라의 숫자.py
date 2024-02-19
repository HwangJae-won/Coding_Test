#규칙에 따라서 숫자 표시하기  (1,2,4로만 숫자 표현할 것)
#이진법같은거임 -> 규칙 찾기 
def solution(n):
    answer = ''
    num = [1,2,4]
    while n > 0:
        n -= 1
        answer = str(num[n%3]) + answer
        n = n // 3
             
    return answer
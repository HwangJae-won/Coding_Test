# 2병 미만이면 콜라 못 받음 -> 빈병의 개수가 콜라 받기 위해 필요한 수보다 크면 반복 
#while 사용
def solution(a, b, n):
    answer = 0
    while(n>=a):
        temp = n %a
        n = (n//a) *b
        answer +=n
        n+= temp
    return answer

#3진법: 3일 밑으로 하는 기수법: 3으로 나눠서 몫과 나머지 확인
#다시 10진법으로 바꿔서 return
def solution(n):
    answer = ''
    while (n>=1):
        r = n%3
        n=n//3
        answer += str(r)
    return int(answer, 3)
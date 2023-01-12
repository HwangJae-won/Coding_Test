# 대칭 만들기 문제
def solution(food):
    answer = '0' #가운데는 무조건 0
    for i in range(len(food)-1, 0, -1):
        answer = str(i) * (food[i]//2) +answer
        answer = answer+ str(i)*(food[i]//2)
    return answer
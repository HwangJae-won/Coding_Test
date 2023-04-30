#자연수 x를 자연수 y로 변환-> 조건에 맞게 변환할 수 있는 최소 연산횟수
#dynamic progrmnming 문제!
def solution(x, y, n):
    answer = 0
    s = set()
    s.add(x)
    while s:
        if y in s:
            return answer
        nxt = set()
        for i in s:
            if i+n <= y:
                nxt.add(i+n)
            if i*2 <= y:
                nxt.add(i*2)
            if i*3 <= y:
                nxt.add(i*3)
        s = nxt
        answer+=1

    return -1
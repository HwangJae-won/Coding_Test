#que 관련 문제: 하나의 큐에서 원소 추출해서 다른 큐에 집어넣기 (큐는 선입 선출)
#-> 결과적으로 두 큐의 원소 합이 같도록 만들기(전체 합을 파악한 후, 나눠서 담는다고 생각)
from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1=deque(queue1) ; queue2=deque(queue2) #큐로 변환해주기(popleft 함수 사용위해)
    q1= sum(queue1) ; q2= sum(queue2)
    que_sum = q1+q2
    l= len(queue1*4)

    if que_sum % 2 != 0: #반반 나눌 수 없으면(2로 나누어 떨어지지 않으면 -1 return)
        return -1

    while True:
        if q1>q2:
            v=queue1.popleft() 
            queue2.append(v)
            q1 -= v ; q2+=v #처리 해준 만큼 sum에서 빼주기 
            answer+=1
        elif q1< q2:
            v=queue2.popleft() 
            queue1.append(v)
            q2 -= v ; q1+=v #처리 해준 만큼 sum에서 빼주기 
            answer+=1
        else:
            break
        if answer == l:
            answer =-1
            break
    return answer
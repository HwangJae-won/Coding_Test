#큐 활용하기 : 큐는 선입선출!
#우선순위가 더 높은 프로세스가 있으면 방금 꺼낸 프로세스를 다시 큐에 넣기 
from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque(priorities) #실행 대기 큐
    #location에 해당되는 위치에 도달할 때까지 반복문 돌리기 
    while queue:
        m = max(queue)
        l = queue.popleft()
        location -= 1
        if l != m:
            queue.append(l)
            if location < 0:
                #여기를 추가해줘야하네 
                location = len(queue)-1
        else:
            answer +=1
            if location <0:
                break
    return answer
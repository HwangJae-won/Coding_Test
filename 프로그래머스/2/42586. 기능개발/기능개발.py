from collections import deque
def solution(progresses, speeds):
    answer = []
    #남은 작업 일수 계산해서 큐에 저장하는 방식이 더 적절함
    queue = deque()
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] ==0:
            queue.append((100 - progresses[i]) // speeds[i])
        else:
            queue.append(((100 - progresses[i]) // speeds[i])+1)

    while queue: #큐 안의 값이 다 없어질 때까지 반복함 
        # 하루 단위로 생각할 필요 없음 - 이미 남은 일수 계산함
        # 배포 단위라고 생각 
        current = queue.popleft() #맨 앞의 값(current) : 현재 몇일째인지
        cnt = 1
        
        #뒤에거도 함께 배포 가능한지 확인
        #큐가 존재하는지 확인+뒤에거 작업 종료 여부 확인
        #여기서의 큐는 맨 앞에거 빠진 상태, 뒤에거도 뺼지 말지 결정
        #왜 while을 써야하는가! : if만 쓰면 배포 날짜 남은지 여부를 뒤에 딱 하나만 확인함
        while queue and queue[0] <= current:            
            queue.popleft()
            cnt+=1
        answer.append(cnt)
    return answer

"""
잘못된 접근법
"""
# def solution(progresses, speeds):
#     answer = []
#     #작업 현황 담을 큐: 100이 넘으면 제외시키기
#     queue = deque()
    
#     for i in range(3):
#         queue.append(progresses[i]+speeds[i])

#     cnt = 0
#     while queue:
#         for _ in range(len(queue)):
#             if queue[0]==100:
#                 queue.popleft()
#                 cnt+=1
#                 if queue>=100:
#                     queue.popleft()
#                     cnt+=1
#                 else:
#                     pass

#     if cnt ==0: 
#         pass
#     if cnt != 0:
#         answer.append(cnt)
#     return answer
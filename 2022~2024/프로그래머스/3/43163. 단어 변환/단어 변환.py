from collections import deque  #BFS 구현 시에는 deque 활용 
#중복이 없다는 제한 사항이 없다면 set을 통해 중복 처리를 해줘야 함

def solution(begin, target, words):  
    #예외처리
    if target not in words : 
        return  0   
    return bfs(begin, target, words)

def bfs(begin, target, words):
    queue = deque()
    queue.append([begin, 0]) #시작 단어와 단계 0으로 초기화
    
    while queue: 
        now, step = queue.popleft() #큐의 가장 첫번째 요소 꺼내기
        
        if now == target:
            #시작 단어와 target이 같아지는 순간 지금까지 이동한 개수인 step 반환하기 
            return step
        
        #단어를 모두 체크하면서, 해당 단어가 변경될 수 있는지 체크
        for word in words:
            count = 0
            #단어의 길이만큼 반복하여 (모든 단어의 길이는 동일하다는 조건 있음)
            for i in range(len(now)):         
                if now[i] != word[i]: #단어에 알파벳 한개씩 체크하기
                    count += 1  #글자가 다를 경우 숫자 증가
            if count == 1: 
                queue.append([word, step+1])
    return answer
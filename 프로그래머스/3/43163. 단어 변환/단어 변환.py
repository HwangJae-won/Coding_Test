from collections import deque  #BFS 구현 시에는 deque 활용 

def solution(begin, target, words):  
    #예외처리
    if target not in words : 
        return  0   
    return bfs(begin, target, words)

def bfs(begin, target, words):
    #begin과 word ruddndml
    queue = deque()
    queue.append([begin, 0]) #시작 단어와 단계 0으로 초기화
    
    while queue: #
        now, step = queue.popleft() #큐의 가장 첫번째 요소 꺼내기
        
        if now == target:
            return step
        
        #단어를 모두 체크하면서, 해당 단어가 변경될 수 있는지 체크
        for word in words:
            count = 0
            for i in range(len(now)): #단어의 길이만큼 반복하여
                if now[i] != word[i]: #단어에 알파벳 한개씩 체크하기
                    count += 1
                    
            if count == 1: 
                queue.append([word, step+1])
    return answer
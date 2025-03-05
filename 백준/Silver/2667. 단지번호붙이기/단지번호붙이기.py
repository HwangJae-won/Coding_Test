"""
2667. 단지 번호 붙이기  
- 1은 집이 있는 곳 , 0은 집이 없는 곳 
- 좌우 상하 붙어있는 걸 연결되었다고 정의->단지 , 대각선은 안됨
- 단지수와 각각의 집의 개수 
====
시작점이 제시되어 있지 않다면 보편적인 x,y 좌표를 받는 bfs 함수를 만들고 활용하는게 더 좋음
"""
from collections import deque
def bfs(graph, x, y, n):
    dx = [-1,1,0,0] ; dy = [0,0,-1,1]
    queue = deque() #빈 큐 생성
    queue.append((x,y)) #시작점 추가
    graph[x][y] = 0 #방문 처리는 굳이 visited 안해주고 0으로 바꿔주면 방문 못함
    cnt = 1
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i] ; ny= y+dy[i]
            if (0 <= nx < n) and (0 <= ny < n) and graph[nx][ny]==1:
                cnt +=1
                queue.append((nx,ny))
                graph[nx][ny] = 0
    return cnt #단지내 집 개수
        
    
    
n = int(input())
graph = [list(map(int, input())) for _ in range(n)] #n*n의 입력값 받음 

li =[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            li.append(bfs(graph, i,j, n))
print(len(li))
li.sort()  #출력 조건: 오름차순 정렬하여 하나씩 출력            
for num in li:
    print(num) 
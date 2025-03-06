"""
백준 2465 안전영역
- 안전한 영역의 최대 개수
- 방문여부 체크해야함 ! 
- BFS 활용: 범위 내에서!
"""
from collections import deque
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
max_n = max(map(max, graph))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    global cnt
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    cnt +=1
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y+dy[i]
            if 0<=nx <n and 0<= ny <n:
                continue
            
            if visited[nx][ny] == 0:
                visited[nx][ny] =1
                queue.append((nx,ny))

answer = 0 
li = []
for R in range(max_n):
    cnt = 0 
    visited = [[0 for _ in range(n) for i in range(n)]]
    for i in range(n):
        for j in range(n):
            if graph[i][j]<=  R:
                visited[i][j] = 1 #물에 잠기는 영역 확인
    for i in range(n):
        for j in range(n):
            if graph[i][j]<=  R:
                visited[i][j] = 0
                bfs(i, j)
    li.append(cnt)
print(max(li))
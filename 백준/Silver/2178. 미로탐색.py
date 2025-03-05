"""
250305
2178.미로 탐색
- 1은 이동 가능 , 0은 이동 불가능
- (1,1) 출발 / (n,m) 도착
- 지나야하는 최소 칸의 수 
- 카운트 시에는 출발, 도착 칸도 포함
=============
배운 점
- 세로 길이 : 행의 개수  ; 가로 길이 :열의 개수임 헷갈리지 말 것 
"""
from collections import deque
#BFS 정의 
def bfs(graph, x,y ):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque()
    queue.append((0,0)) #초기 위치
    
    while queue:
        x,y= queue.popleft()
        
        #상하좌우 탐색
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 #이동했으므로 거리 누적시켜줌
                queue.append((nx,ny))
    return graph[n-1][m-1] #거리값 반환((0,0)에서 시작했으므로 -1해줘야 함)
                
#데이터 입력 받기 
n,m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
print(bfs(graph, n,m))


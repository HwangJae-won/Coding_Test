from collections import deque
def bfs(maps):
    #n,m 길이 재정의
    n = len(maps)
    m = len(maps[0])
    
    #초기화 시켜주기, 재방문 하면 안되므로 방문 여부 확인할 배열
    start_x, start_y = 0,0
    visited = [[False]*m for _ in range(n)]
    queue = deque()
    queue.append((start_x, start_y, 1))
    
    dx = [-1,1,0,0]
    dy = [0,0, -1, 1]
    
    #시작점 방문 처리 필요 
    visited[start_x][start_y] = True
    
    while queue:
        x, y , cnt = queue.popleft()
        if x== n-1 and y== m-1: #도달했을 경우 길이 반환
            return cnt
        
        for i in range(4):
            nx = x+ dx[i]
            ny = y + dy[i]
            if  0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, cnt+1))

    return -1 #도착 못했을 경우 -1

def solution(maps):
    answer= bfs(maps)
    return answer
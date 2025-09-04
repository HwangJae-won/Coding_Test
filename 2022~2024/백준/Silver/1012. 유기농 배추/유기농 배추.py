from collections import deque
import sys 
input = sys.stdin.readline

def bfs(maps, x,y):
    #이동시킬 방향 좌표 
    dx= [-1,1, 0, 0]
    dy = [0,0,-1,1]
    #큐 초기화 후 처음 좌표 넣기 
    queue = deque([(x,y)]) #좌표를 넣을 때는 꼭 리스트 사용해주기 , x,y, cnt를 넣는다면 그냥 괄호로 해도됨
    maps[x][y] = 0 #배추 심은 곳도 0으로 바꿔서 방문처리 
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x+ dx[i]
            ny = y+dy[i]
            
            if 0<=nx <m and 0<=ny<n and maps[nx][ny] ==1:
                maps[nx][ny] = 0
                queue.append((nx,ny))
t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    maps = [[0] * n for _ in range(m)]
    cnt = 0 
    # 0으로만 이루어진 배열 먼저 만들고 k개의 위치 정보 받아 1로 채워줌 
    for _ in range(k):
        x, y = map(int, input().split())
        maps[x][y] = 1

    for i in range(m):
        for j in range(n):  # m이 아니라 n 범위로 수정
            # 1일 경우에만 탐색하고 카운트 올려줌
            if maps[i][j] == 1:
                bfs(maps, i, j) 
                cnt += 1
    print(cnt)
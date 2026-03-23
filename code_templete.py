## 방향 벡터
#4방향 벡터: 상우하좌(시계 방향)로 고정 !
#회전 문제에 사용하기 좋음. 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#기본 4방향 탐색: BFS 활용 가능
for d in range(4):
    nx,ny = x+ dx[i], y+ dy[i]
    # if 0<=nx <N and 0<= ny <M: #경계 탐색
    #     #이동 가능 칸 처리

#8방향 탐색: 방향 번호를 0-7로 줄때
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for i in range(8):
    nx, ny = x+ dx[i], y+dy[i]
    # if 0<=nx<N and 0<=ny<M:
        

## 회전 문제: 현재 바라보는 방향을 기준으로 돌리기 
d= 0
d=(d+1)%4 #시계 90도
d= (d-1)%4 #반시계 90도
d= (d+2) %4 #180도 반대 

#회전 후 이동
d= (d+1)%4
x,y = x+dx[d], y+dy[d]

## 로봇 청소기 패턴: 왼쪽부터 탐색
d=0
x,y = sx,sy 
while True:
    for _ in range(4):
        d= (d-1)%4
        nx,ny = x+dx[d], y+dy[d]
        if 0<=nx<N and 0<= ny<M and board[nx][ny]==0:
            x,y = nx,ny 
            found= True
            break
    if not found:
        bx,by = x+dx[(d+2)%4], y+dy[(d+2)%4]
        if 0<=bx<N and 0<=by<M and board[bx][by] !=1:
            x,y = bx, by
        else:
            break

## 뱀 / 나선형 이동
d= 1 #시작 방향: 우
x,y = 0,0
for _ in range(total_moves):
    x,y = x+ dx[d], y+dy[d]
    
    if should_turn_right():
        d=(d+1)%4
    elif should_turn_left():
        d = (d-1)%4
        
##BFS/ 최단거리 
from collections import deque
def bfs(sx,sy):
    visited = [[-1]*M for _ in range(N)]
    visited[sx][sy]=0
    q = deque([(sx, sy)])
    
    while q:
        x,y  = q.popleft()
        for d in range(4):
            nx,ny = x+dx[d], y+dy[d]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==-1 and board[nx][ny]:
                visited[nx][ny]= visited[x][y] +1
                q.append((nx,ny))
                
    return visited 


##문자/숫자-> 방향변환-> 방식 동일하게 제외 
dir_map = {"U":0, "R":1, "D":2, "L":3}

##2D 배열 회전(90도)
def rotate_90(arr):
    N = len(arr)
    return [[arr[N-1-j][i] for j in range(N)] for i in range(N)]

##깊은 복사 
import copy
saved= copy.deepcopy(board) #시뮬레이션 전 상태 저장
board = copy.deepcopy(saved) #원상복구

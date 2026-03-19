"""
문제
어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

입력
첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

출력
첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.

1. 아이디어 
- 이중 for문 => 값 1&& 방문 X=> BFS
- BFS 돌면서 그림개수 + 1, 최대 그림수 출력
2. 시간복잡도 
- v=n*m = 500*500, e = v*4
o(v+e) = o(5*250000)
100만 < 2억 >> 가능 
3. 자료구조 
- 그래프 전체 지도 : int[][]: 이차원 배열 
- 방문: bool[][]
- Queue(BFS)
"""
#입출력 빠르게 해줌
import sys
#큐 사용 위함 
from collections import deque

input = sys.stdin.readline

#이동 시킬 수 있는 방향 벡터 만들기 
dx = [-1, 1, 0, 0] # 좌우
dy = [0,0,-1, 1] #상하

def bfs(x, y):
    queue = deque() #큐 생성
    queue.append((x,y)) #시작점 (x,y) 큐에 추가
    #방문 처리
    chk[x][y] = True
    area = 1 #현재 그림의 넓이 (최종 최대 넓이 구하기 위해 1씩 더해나갈 것)
    
    #방향 벡터로 이동시키면서 인접 노드 탐색하기
    while queue:
        x,y = queue.popleft() #탐색 위해서 꺼냈다고 생각 
        
        for i in range(4): #상하좌우 인접 노드 탐색 (4개!)
            nx = x+ dx[i]
            ny = y + dy[i] 
            
            if 0<= nx < n and 0 <= ny < m and not chk[nx][ny] and map[nx][ny]==1:
                #조건 만족할 경우 큐 추가 (탐색 완룐 노드!) 
                queue.append((nx, ny))
                chk[nx][ny] = True
                area +=1
    return area
        


n, m  = map(int, input().split())
#지도는 이중 리스트의 형태가 됨
map = [list(map(int, input().split())) for _ in range(n)] 
chk =[[False]*m for _ in range(n)]
cnt = 0 
maxv = 0
for i in range(n):
    for j in range(m):
        if map[i][j] == 1 and not chk[i][j]:
            
            # 전체 그림 개수 + 1
            cnt +=1
            #BFS를 통해서 그림크기 구하기 
            # 최대값 갱신
            maxv = max(maxv, bfs(i,j))

print(cnt)
print(maxv)
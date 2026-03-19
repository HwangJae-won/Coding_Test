
"""
백준 카드 2
N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.

이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.

N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.
"""

# from collections import deque
# n = int(input())
# queue = deque()

# for i in range(1, n+1):
#     queue.append(i)
# print(queue)
# while len(queue)>1:
#     queue.popleft()
#     queue.rotate(-1)
# print(queue[0])


"""
백준 1926
소수 구하기
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
"""
# #단순 소수 판별
# def is_prime(x):
#     if x == 1:
#         return False
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             return False
#     return True

# m, n = map(int, input().split())

# def solution(m, n):
#     for i in range(m, n + 1):
#         if is_prime(i):
#             print(i)

# # 예시 입력: m과 n 사이의 소수 출력
# solution(m, n)

# #에라토스테네스의 채 활용
# def eratosthenes_sieve(m, n):
#     sieve = [True] * (n + 1)  # 처음엔 모든 수를 소수라고 가정 (True)
#     sieve[0] = sieve[1] = False  # 0과 1은 소수가 아님

#     # 2부터 √n까지의 배수를 지움
#     for i in range(2, int(n ** 0.5) + 1):
#         if sieve[i]:  # i가 소수라면
#             for j in range(i * i, n + 1, i):  # i의 배수들은 소수가 아님
#                 sieve[j] = False

#     # m부터 n까지의 소수 출력
#     for i in range(m, n + 1):
#         if sieve[i]:  # True로 남은 수가 소수
#             print(i)

# # 입력 예시: m과 n 사이의 소수 출력
# m, n = map(int, input().split())
# eratosthenes_sieve(m, n)

"""
백준 1012 유기농 배추 
BFS 활용
"""
#격자, 좌표 문제 : BFS 고려
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
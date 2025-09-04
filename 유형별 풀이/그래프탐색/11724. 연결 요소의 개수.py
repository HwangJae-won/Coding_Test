"""
11724 연결 요소의 개수 
실버2
- 방향 없는 그래프가 주어졌을 때, 연결 요소의 개수
- 연결된 게 하나라도 있으면 연결된 걸로 간주 
"""
n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
print(graph)
from collections import deque
n = int(input()) #1부터 n까지의 수를 list에 넣고 
#넣었다 뺏다 하니까 ->큐로
from collections import deque
queue = deque(range(1, n+1)) #1부터 n까지의 큐 만들기 
while len(queue)> 1:
    queue.popleft() #첫번째거 버림
    queue.append(queue.popleft()) #버린거 추가
print(queue[0])

"""
시간 초과 코드 
n = int(input()) #1부터 n까지의 수를 list에 넣고 

from collections import deque
queue = deque(range(1, n+1)) #1부터 n까지의 큐 만들기 
while len(queue)> 1:
    queue.popleft() #첫번째거 버림
    queue.append(queue.popleft) #버린거 추가
print(queue[0])
"""

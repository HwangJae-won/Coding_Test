#런타임에러 발생코드 : Why ...
from collections import deque
import sys
input = sys.stdin.readline
#카드 개수 
n = int(input()) #이걸 int로 안받아서?
li = list(map(int, input().strip().split()))
li.reverse()

#바닥에 놓인 카드를 담을 큐
queue = deque()
#A_i가 1,2,3 중 하나임
for i in range(n):
    if li[i] ==1:
        queue.appendleft(i+1)
    elif li[i] ==2:
        queue.insert(1, i+1)
    elif li[i] ==3:
        queue.append(i+1)
for i in queue:
    print(i, end=' ')
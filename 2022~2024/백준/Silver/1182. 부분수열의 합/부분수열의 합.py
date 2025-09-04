import sys
from itertools import combinations
n,s  = map(int, input().split())
seq = list(map(int, input().split()))

cnt = 0
# 1~n-1 개의 원소를 가진 수열이 만들어질 것 
for i in range(1,n+1):
    #개수별 조합
    com_seq = combinations(seq, i)
    for j in com_seq:
        if sum(j)==s:
            cnt+=1 
print(cnt)
"""
부분 수열의 합 
N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.
"""
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
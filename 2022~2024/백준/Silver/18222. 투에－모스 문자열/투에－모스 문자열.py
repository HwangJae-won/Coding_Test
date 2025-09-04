import sys
input = sys.stdin.readline
k = int(input())


#무한 반복 : 재귀 함수 사용 
# 1. x, x', xx'의 형태로 숫자 만드는 코드 
# 2. 해당 과정 반복 , k번째 수가 나오면 stop (이게 탈출 조건)
# (k<10^18 니까.. 

#규칙을 찾아보자
#k가 크니까- 분할 정복?

def compute(index): #index: 확인하는 자리수! 
    if index==0: #0번째는 0으로 고정되어 있음
        return False
    if index % 2: #홀수 (나누기 2를 했을 때)
        return not compute(index //2)
    else: #짝수
        return compute(index //2)
    
if compute(k-1):
    print(1)
else: 
    print(0)
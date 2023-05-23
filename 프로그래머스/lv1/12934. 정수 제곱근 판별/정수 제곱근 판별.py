#n이 어떤 양의 정수 x의 제곱인지 아닌지 판단 
def solution(n):
    x = n** 0.5 #root :제곱근
    if x == int(x):
        return (x+1)**2
    else:
        return -1
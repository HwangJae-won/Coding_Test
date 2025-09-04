"""
1일 될 때까지 :Greedy 알고리즘
어떠한 수 N이 1이 될 때까지->N에서 1을 빼거나 k로 나눔
-> 두가지 방법 조합하여 1을 만들 수 있는 "최소" 횟수 구하기 
#뺄셈보다 나눗셈이 많을 때 횟수 최소 만들 수 있을 것 같다 -> k로 나눠떨어지는 수 만들 때까지 빼주고 -> 그 다음 K로 나누기 

"""
n, k = map(int,input().split())
answer= 0
while True:
    temp = (n//k) *k 
    answer += (n-temp)
    n = temp
    
    if n<k:
        break
    answer +=1
    n//=k
answer +=(n-1)
print(answer)
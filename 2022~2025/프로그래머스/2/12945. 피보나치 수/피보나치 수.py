#피보나치 수 : F(n) = F(n-1)+F(n-2)를 만족하는 수 
#n번째 피보나치 수를 1234567으로 나눈 나머지 return-> %

def solution(n):
    n_0 = 0 ; n_1= 1
    answer = [n_0, n_1] #피보나치수를 담을 list 생성: 
    for i in range(2, n+1): #0,1은 이미 정의했으므로 2부터 시작 
        answer.append(answer[i-1] + answer[i-2])
    x=answer[n] % 1234567 
    return x
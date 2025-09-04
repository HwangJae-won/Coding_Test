#n을 k진수로 변환하였을 떄, 변환된 수 안에 조건에 맞는 소수가 몇개 있는지 return 
def solution(n, k):
    #k진수로 변환 
    word= ""
    while n:
        word = str(n%k)+word
        n= n//k
    word = word.split("0") #0을 기준으로 나눠줌
    
    cnt = 0
    for w in word : 
        if len(w)==0: #0,1,빈공간이면 pass
            continue
        if int(w)<2:
            continue
        prime_n = True
        for i in range(2, int(int(w)**0.5)+1): #소수 개수 
            if int(w)%i ==0:
                prime_n = False
                break
        if prime_n:
            cnt+=1
    return cnt
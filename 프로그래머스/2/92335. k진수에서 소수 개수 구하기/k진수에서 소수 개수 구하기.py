#n을 k진수로 변환하였을 떄, 변환된 수 안에 조건에 맞는 소수가 몇개 있는지 return 
def solution(n, k):
    ##우선 k진수로 변환 
    number =""
    while n :
        number = str(n% k)+number #join으로 하면 나중에 뒤집어줘야함
        n = n // k  #몫
    number=number.split("0")  #0기준으로 나누기 
    print(number)
    ##조건에 맞는 소수 찾기: 중복되는 소수도 따로 count
    cnt = 0 
    for i in number:
        if len(i)==0:  
            continue
        if int(i)<2:
            continue
        prime=True
        for j in range(2, int(int(i)**0.5 + 1)):
            if int(i) % j ==0:
                prime=False
                break
        if prime:
            cnt+=1
    return cnt
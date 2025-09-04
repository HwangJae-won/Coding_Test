
def solution(price, money, count):
    temp =[]
    for i in range(1, count+1):
        temp.append(price*i)
    if sum(temp) <= money:
        answer = 0
    else:
        answer= sum(temp)- money
    return answer

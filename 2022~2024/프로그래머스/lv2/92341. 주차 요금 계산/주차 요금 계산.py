"""
1. 차량별로 딕셔너리 생성하는게 편할 것 같음:list, append쓰지 말아보자 
-> 빈 딕셔너리 만들어서 반복문 돌면서 하나씩 추가하는 방식?
-> 아 중복으로 들어온 차는 어쩌지 -> 딕셔너리에서 해당 차 삭제하면서
2. : 기준으로 시, 분 나누고 -> 요금 계산 (math 활용)
3. 입차는 있는데 출차가 없는 것에 대한 처리 필요
"""
import math
def get_fee(minutes, fees):
    return fees[1]+ math.ceil(max(0, (minutes-fees[0]))/ fees[2]) *fees[3]

def solution(fees, records):
    parking = dict() #주차 case 
    stack = dict() #출차 case
    
    for i in records:
        t, number, IO = i.split(' ')
        hour, minute = t.split(':') #시간은 또 분리해주기 
        t_to_minutes = int(hour) *60 +int(minute) #시간을 분으로 환산
        
        if IO == "IN":
            parking[number] = t_to_minutes
        elif IO == "OUT":
            try:
                stack[number] += t_to_minutes-parking[number]
            except:
                stack[number] = t_to_minutes-parking[number]
            del parking[number] #중복 방지 
    #입차는 있는데 출차는 없다면
    for number, minute in parking.items():
        try:
            stack[number] += 23*60+59 -minute
        except:
            stack[number] = 23*60+59 -minute
    #요금 계산: 함수로 
    return [get_fee(time, fees) for number, time in sorted(list(stack.items()), key = lambda x:x[0])]
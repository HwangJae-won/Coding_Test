#최소한의 객실만의 사용하여 예약 손님 받기: 한번 사용한 건 10분간 청소 
#시간으로 되어 있는 input 형태 변환 필요 : 분단위로 변환 -> list 내의 모든 요소에 적용해줘야하므로 함수로 만들어 주자 
def time_transformation(time):
    return int(time[:2])*60+ int(time[3:5])

def solution(book_time):
    dic ={}
    for book in book_time:
        start= time_transformation(book[0])
        end= time_transformation(book[1])
        for t in range(start, end+10): #10분은 청소 시간
            if dic.get(t) ==None:
                dic[t] =1
            else: 
                dic[t] +=1
    return max(dic.values())
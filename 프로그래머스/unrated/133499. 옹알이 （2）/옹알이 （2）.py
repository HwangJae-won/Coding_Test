###시간 초과 
# list 저장 후, 이중 반복문으로 포함되는지 확인하기 
# 발음이 연속되는 경우는 안됨(yeye, ayaaya는 발음 안됨): 중복되는 것에 대한 처리 필요
def solution(babbling):
    answer = 0 ; li = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in li: 
            if j*2 not in i: #두번 연속으로 올 경우는 count가 안되므로 하나로 바꿔줌  
                i = i.replace(j, ' ')
        if i.strip() =='':
            answer+=1
        # if len(i.strip()) ==0: #공백 제거 후의 길이가 0일 경우 : 공백 제거 안해주면 다르게 카운트가 된다 
        #     answer += 1
    return answer
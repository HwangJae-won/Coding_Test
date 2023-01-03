def solution(s):
    answer = []
    dict ={}
    li= list(s) #문자열 분리하여 리스트에 저장하기 
    for index, word in enumerate(li):
        if word not in dict:
            answer.append(-1)
            dict[word] = index
        else:
            answer.append(index- dict[word])
            dict[word] = index
    return answer
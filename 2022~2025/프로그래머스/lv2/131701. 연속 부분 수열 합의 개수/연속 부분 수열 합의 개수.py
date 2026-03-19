def solution(elements):
    answer = 0
    numberSet = set() #빈조합 만들기 
    
    elementLen = len(elements) #이어지는 수열: 두개의 수열 이어 붙이기
    elements = elements * 2
    
    for i in range(elementLen) : 
        for j in range(elementLen) : 
            numberSet.add(sum(elements[j:j+i+1]))
    answer = len(numberSet)
    return answer

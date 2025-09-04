def solution(ingredient):
    temp =[] 
    answer = 0
    for i in ingredient: #ingredient의 요소들을 하나씩 읽으며 확인
        temp.append(i) 
        if temp[-4:] == [1,2,3,1]: #-4로 슬라이싱을 해줘야 앞에서부터 4개만 뽑힘
            answer+=1
            del temp[-4:]
    return answer

"""
빵: 1
야채: 2
고기 : 3
- 1-2-3-1의 배열을 만들 수 있는 경우의 수를 구해야함. 
- 1-2-3-1의 배열이 등장하면 cnt 더하고 삭제 
"""

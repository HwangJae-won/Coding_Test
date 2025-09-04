def solution(clothes):
    #종류별 딕셔너리 생성 후 몇개있는지 만들기 
    cnt = {}
    for _, category in clothes:
        cnt[category] = cnt.get(category, 0) + 1 
    #이미 딕셔너리에 해당 카테고리가 있으면 그 값에 1을 더하고, 없으면 1로 설정
    answer = 1 #초기값 설정 
    for count in cnt.values():
        answer *= (count + 1)
    #각 종류의 의상을 선택하지 않는 경우도 고려하여 해당 종류의 의상을 선택하는 경우의 수
    result = answer - 1 #아무것도 선택하지 않은 경우 
    return result

def solution(numbers):
    # 숫자들을 문자열로 변환
    temp = list(map(str, numbers))
    
    # 정렬: 두 문자열을 이어 붙였을 때 더 큰 값이 되는 순서로 정렬
    # 숫자 하나 하나씩으로 보는게 아니라 붙여서 생각해야 하긴함
    temp.sort(key=lambda x: x*3, reverse=True)
    
    # 모든 숫자가 0일 경우 처리
    if temp[0] == '0':
        return '0'
    
    # 정렬된 문자열을 이어붙이기
    return ''.join(temp)
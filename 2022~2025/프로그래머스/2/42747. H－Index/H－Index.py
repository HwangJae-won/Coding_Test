def solution(citations):
    citations.sort(reverse=True) 
    #enemerate의 활용 : 리스트에서 인덱스와 요소를 반복문 돌릴 수 있음 
    for i, c in enumerate(citations):
        if c <= i:  # 인용 횟수가 인덱스보다 작거나 같을 때
            return i  
    return len(citations)  # 모든 논문이 h번 이상 인용된 경우
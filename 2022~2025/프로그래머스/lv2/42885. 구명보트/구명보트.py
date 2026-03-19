"""
- 최솟값 구하기: greedy 
- 아이디어: list내 요소들의 합이 limit 이하일지 검토
"""

def solution(people, limit):
    answer = 0
    people.sort()
    start, end = 0, len(people) - 1
    while start <= end:
        answer += 1
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
    
    return answer
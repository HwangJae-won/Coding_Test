def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    for i in range(n):
        hindex = n-i
        if citations[i] >= hindex:
            answer = hindex
            break
    return answer
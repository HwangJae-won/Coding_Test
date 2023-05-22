def solution(n):
    li=sorted(list(str(n)), reverse=True)
    answer=''.join(li)
    return int(answer)

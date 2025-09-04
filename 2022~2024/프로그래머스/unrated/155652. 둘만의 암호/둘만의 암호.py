def solution(s, skip, index):
    answer = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    for i in skip:
        if i in answer:
            answer = answer.replace(i, "") 
    for j in s:
        result.append(answer[(answer.index(j)+index) % len(answer)])
            
    return "".join(result)
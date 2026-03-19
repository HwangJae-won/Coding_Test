def solution(k, score):
    answer = [] ; temp = []
    for i in range(1, len(score)+1):
        temp.append(score[:i])

    for j in range(len(temp)):
        if len(temp[j])<k:
            answer.extend(sorted(temp[j])[:1])
        else:
            answer.extend(sorted(temp[j])[len(temp[j])-k:][:1])
    return answer
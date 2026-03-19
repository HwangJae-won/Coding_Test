def solution(name, yearning, photo):
    answer = []
    data = dict(zip(name, yearning))
    for i in photo: 
        result =0
        for key in i:
            if type(data.get(key)) == int:
                result += data.get(key)
        answer.append(result)
    return answer
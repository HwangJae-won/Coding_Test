def solution(order):
    answer = 0
    li =[]
    i = 1
    while i != len(order)+1:
        li.append(i)
        while li[-1] ==order[answer]:
            answer+=1
            li.pop()
            if len(li) ==0:
                break
        i+=1
    return answer
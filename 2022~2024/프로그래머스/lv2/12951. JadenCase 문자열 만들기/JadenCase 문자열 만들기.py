def solution(s):
    temp = s.split(' ')
    li = []
    for i in temp:
        i= i.capitalize()
        li.append(i)
    return ' '.join(li)
        
def solution(t, p):
    answer = 0
    letter= []
    for i in range(len(t)-len(p)+1):
        letter.append(t[i:len(p)+i])
    
    for j in letter:
        if int(p) > int(j) or int(p) == int(j):
            answer+=1
        else:
            pass
    return answer
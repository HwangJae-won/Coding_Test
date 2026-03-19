def solution(people, limit):
    answer = 0
    sort_p = sorted(people) 
    s= 0 #시작은 0
    e = len(sort_p)- 1 #전체 사람 수 -1
    while s < e:
        if sort_p[s]+sort_p[e] > limit:
            e -=1
        else:
            s+=1
            e-=1
        answer+=1
        if s==e:
            answer+=1
    return answer
    
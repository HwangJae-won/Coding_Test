
def solution(brown, yellow):
    answer = []
    full = brown + yellow
    for h in range(1, full+1):
        if (full/h) % 1 ==0:
            w= full/h
            if w>= h:
                if 2*w + 2*h == brown + 4: 
                    return [w,h]
    return answer
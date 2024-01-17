#캐릭터가 처음 걸어본 길의 길이 구하기 
def solution(dirs):
    visited_road=set() #방문하게 되는 길 
    x,y =0,0 #현 좌표 
    udrl = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L': (0, -1)} 
    for d in dirs:
        dy, dx = udrl[d] #딕셔너리에서 UDRL 중 하나 호출하여 어떻게 이동할지 바로 지정 가능
        new_y = y + dy
        new_x = x + dx
        #-5 범위 내에 있어야하는 조건 
        if -5 <= new_y <= 5 and -5 <= new_x <= 5: 
            visited_road.add(((y, x), (new_y, new_x)))
            visited_road.add(((new_y, new_x), (y, x)))
            y = new_y
            x = new_x
    return len(visited_road) // 2

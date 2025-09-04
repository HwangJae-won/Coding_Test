"""
10789 세로 읽기 
- 총 5줄의 입력 , 한줄에는 최소 1개 최대 15개 빈칸 없이 연속으로 주어짐 
- 가로로 주어진 문자열을 새로로 읽기

===

"""
li = [input() for _ in range(5) ]
answer =[]
for i in range(5):
    for j in range(len(li[i])):
        if i < len(li[j]):
            answer.append(li[j][i])
print(''.join(answer))

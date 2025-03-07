li = [input() for _ in range(5) ]
answer =[]
# 최대 길이를 찾기
max_length = max(len(row) for row in li)

# 세로 방향으로 읽기
for i in range(max_length):
    for j in range(5):
        if i < len(li[j]):  # 현재 문자열이 i 인덱스를 갖고 있다면 추가
            answer.append(li[j][i])

print(''.join(answer))
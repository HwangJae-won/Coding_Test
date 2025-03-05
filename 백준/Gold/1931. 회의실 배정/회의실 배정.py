n = int(input())
time_li = [list(map(int, input().split())) for _ in range(n)]

# 종료 시간이 같으면 시작 시간이 빠른 순서로 정렬
sorted_time_li = sorted(time_li, key=lambda x: (x[1], x[0]))

cnt = 0
last_end_time = 0  # 가장 마지막으로 선택한 종료 시간

for start, end in sorted_time_li:
    if start >= last_end_time:  # 종료 시간 이후에 시작하는 회의만 선택
        cnt += 1
        last_end_time = end  # 종료 시간 업데이트

# 결과 출력
print(cnt)
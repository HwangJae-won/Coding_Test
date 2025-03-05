"""
1931. 회의실 배정
- 한개의 회의실, n개의 회의 
- 시작시간, 끝나는 시간 주어져 있음
- 안겹치면서 사용할 수 있는 회의의 최대 개수 
- 중간에 중단 X, 한 회의가 끝나야 다음 회의 시작 가능, 종료 동시에 시작 가능 
===
왜 그리디인가? : 최적해가 보장되는 상황이다 !
1. 각각의 회의 진행 시간이 서로에게 영향을 주지 않음
2. 각각의 best 배치를 모아 최적 해를 구할 수 있음 
===

sorted_time_li = [x for x in sorted_time_li if x[0] >= earliest[1]]
이렇게 하면 매 반복마다 리스트를 생성하므로 시간초과/ 메모리 초과가 발생함
"""
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
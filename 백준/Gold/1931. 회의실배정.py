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
"""
n = int(input())
time_li = []
for _ in range(n):
    time_li.append(list(map(int, input().split())))
cnt =0
sorted_time_li = sorted(time_li, key=lambda x: x[1])
selected_li = []
while sorted_time_li:
    earliest = sorted_time_li[0]
    selected_li.append(earliest)

    # 현재 선택한 요소의 종료 시간보다 큰 시작 시간을 가진 요소들만 남김
    sorted_time_li = [x for x in sorted_time_li if x[0] >= earliest[1]]
    cnt +=1
    
# 결과 출력
print(selected_li )
print(cnt)
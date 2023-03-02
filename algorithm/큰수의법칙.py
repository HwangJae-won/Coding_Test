"""
큰수의 법칙
주어진 수를 M번 더하여 가장 큰 수를 만드는 법칙
특정한 인덱스에 해당되는 수가 연속해서 k번 초과해서 더해질 수 없음
직접 풀어보자 !
1. 큰수데로 정렬 수 첫번째, 두번째큰 수만 뽑아두기 -> 그외의 숫자는 필요없어
2. 젤 큰거 k번 더하고 두번째 큰거 1번 더하는 수열 반복 (젤 큰수가 두개 있으면 그냥 그거 싹 더하면됨)
"""
import time
start = time.time()
n,m,k = map(int, input().split())
arr= list(map(int, input().split()))

arr1= sorted(arr, reverse=True)
n_max = arr1[0] ; n_second =arr1[1]

answer = 0 
while True: 
    for i in range(k):
        if m ==0: #m이 0일 경우는 더할게 없음
            break
        answer += n_max #k번만큼 더하기
        m-=1 #m횟수 감소
    if m ==0: 
        break
    answer += n_second
    m-= 1
end = time.time()
print("time:", end-start)
print(answer)

#------------------------------------
start = time.time()
n,m,k = map(int, input().split())
arr= list(map(int, input().split()))

arr1= sorted(arr, reverse=True)
n_max = arr1[0] ; n_second =arr1[1]

cnt = int(m/(k+1))*k
cnt += m %(k+1)

answer= 0 
answer+= cnt*n_max
answer += m-cnt *n_second
end = time.time()
print("time:", end-start)
print(answer)
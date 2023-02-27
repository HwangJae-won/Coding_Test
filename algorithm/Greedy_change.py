"""
Q. 당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다. 
손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수 구하기 (N은 항상 10의 배수)
"""
import time
def change(n):
    start= time.time()
    cnt = 0
    li =[500,100,50,10]
    for i in li:
        cnt += n // i #몫: 동전 개수
        n %=  i 
    end=time.time()
    print("time:", end-start)
    return cnt

print(change(1260))



"""
11047. 동전0
- 동전은 총 N종류
- 가치의 합을 K로 만들기 
- 필요한 동전 개수의 최소값

=====
각 금액 별로 몇 개있는지 세서 계산하는 방식은 너무 복잡함
가장 큰걸로 확인하고 가능하면 사용 - 아니면 pass
반복문 여러개 쓰는 건 최대한 피하자 
몇개 필요같은 말이 나오면 나눗셈
"""
n,k = map(int, input().split())
coin_li = [int(input()) for _ in range(n)]
coin_li.sort(reverse=True) 
cnt =0 ;  cost = 0 ; 
for coin in coin_li:
    i = (k - cost) // coin #몫 
    cost += coin * i
    cnt += i 
    if cost == k:
        break
print(cnt)
        
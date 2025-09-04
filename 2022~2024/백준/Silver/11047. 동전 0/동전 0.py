n,k = map(int, input().split())
coin_li = [int(input()) for _ in range(n)]

coin_li.sort(reverse=True) 
cnt =0 ;  cost = 0 ; 
for coin in coin_li:
    i = (k - cost) // coin
    cost += coin * i
    cnt += i 
    if cost == k:
        break
print(cnt)
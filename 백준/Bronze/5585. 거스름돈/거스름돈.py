n = int(input())
li = [500,100,50,10,5,1]
cnt =0 
money = 1000-n
for i in li:
    cnt += money // i
    money %=  i 
print(cnt)
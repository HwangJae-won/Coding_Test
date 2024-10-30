n = int(input())
s= input()
cnt = 0
for i in range(n):
    if s[i] != "C":
        cnt+=1
print(n//(cnt+1))

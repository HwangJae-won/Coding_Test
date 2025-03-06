"""
11720 숫자의 합
- n개의 숫자가 공백없이 쓰여짐 
- 숫자를 모두 합해서 출력
"""
n = int(input())
n_s = input()
sum_n =0
for s in n_s:
    sum_n += int(s)
print(sum_n)
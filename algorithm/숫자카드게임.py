"""
Greedy 알고리즘:숫자 카드 게임 
여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
- n*m 형식의 array
- 뽑고자 하는 카드가 포함되어 있는 행 선택-> 선택된 행에서 가장 숫자 낮은 카드 선택
-> 처음 카드 고를 행 선택할 때, 숫자 낮은 카드 뽑을거 고려해서 -> 가장 큰 숫자를 최종적으로 뽑도록 해야함!
"""
n,m = map(int, input().split())
#n*m 만큼의 데이터 입력 받기 -> 각 행별 list로 저장
temp =[]
for i in range(n):
    li = list(map(int, input().split()))
    temp.append(min(li))
print(max(temp))
#----------책 풀이 ----------
n,m = map(int, input().split())
result=0
for i in range(n):
    data = list(map(int, input(),splti()))
    min_value =min(data)
    result = max(result, min_value)
print(result)
                

N = input(str()) #오늘 푼 문제의 개수 : 각각 숫자 list로 넣기 
#숫자의 구성이 같으면서(똑같은 숫자로 이루어짐), 오늘 푼 문제의 개수보다 큰 수 중 가장 작은 수 
#정답이 반드시 있는 경우만 입력값으로 주어짐 -> 예외처리 따로 해줄 필요는 없음 !
from itertools import permutations
per = permutations(list(N), len(list(N)))
word_list= []
for i in per:
    word = int(''.join(i))
    word_list.append(word)
#여기서 이제 N이랑 비교를 해야함 
sort_li = sorted(word_list)
print(sort_li)

for i in range(len(sort_li)):
    if int(N) >= sort_li[i]:
        continue
    else:
        print(sort_li[i])
        break
        
        
    
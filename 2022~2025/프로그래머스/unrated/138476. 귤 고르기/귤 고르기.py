#서로 다른 종류 최소화시키기 :counter 사용해도 될 것 같군
#제일 많은 거부터 k개 소진시킬 때까지 담고 그 때의 종류 수 return하면 되겠당
from collections import Counter
def solution(k, tangerine):
    n = 0
    key_li=[]
    for indx, (key, v) in enumerate(Counter(tangerine).most_common()):
        #key:귤개수 / v:개수
        if n < k: 
            n+= v
            key_li.append(key)
        else:
            pass
    return len(key_li)
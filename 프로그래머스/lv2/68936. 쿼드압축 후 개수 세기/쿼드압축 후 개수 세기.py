from collections import Counter
def quard_check(x, y, arr, now, checked):
    num = arr[x][y]
    
    for i in range(x, x + now):
        for j in range(y, y + now):
            if num != arr[i][j]:
                return 0, 0
    
    for i in range(x, x + now):
        for j in range(y, y + now):
            checked[i][j] = True
    return num, now * now

def solution(arr):
    n, now = len(arr), len(arr)
    checked = [[False] * n for _  in range(n)]
    counter = Counter()
    for a in arr:
        counter += Counter(a)
        
    while now >= 2:
        for i in range(len(arr)):
            for j in range(0, n, now):
                if i % now == 0 and not checked[i][j]:
                    k, v  = quard_check(i, j, arr, now, checked)
                    if v != 0 :
                        counter[k] -= v - 1
            
        now //= 2
    return [counter[0], counter[1]]
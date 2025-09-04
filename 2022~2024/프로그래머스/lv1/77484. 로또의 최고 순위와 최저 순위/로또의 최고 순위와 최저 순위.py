def solution(lottos, win_nums):
    #우선 중복 제거 
    lo_set= set(lottos)
    win_set =set(win_nums)
    #공동된 것 개수 세어주기 
    cnt = len(lo_set & win_set)
    zero = lottos.count(0)
    answer= [7 -max(cnt+zero, 1), 7 -max(cnt, 1)]
    return answer
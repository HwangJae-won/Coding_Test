"""약수 구하기 문제 
약수 : 어떤 수를 나누어 떨어지게 하는 수 (나눠서 0이 되도록 해야함)
"""
def solution(number, limit, power):
    from math import sqrt
    result = []
    for n in range(1, (number + 1)):
        d = set() ; h = []
        for i in range(1, int(sqrt(n)) + 1):
            if (n % i == 0):
                d.add(i)
                d.add(int(n/i))
        result.append(len(list(d)))

    for idx, v in enumerate(result):
            if v > limit:
                result[idx] = power
    return sum(result)


###시간 초과 ㅠ ㅠ ###
# def solution(number, limit, power):
#     d = []
#     for n in range(1, number + 1):
#         cnt = 0
#         for i in range(1, n + 1):
#             if n % i == 0:
#                 cnt += 1
#         d.append(cnt)
    
#     for idx, v in enumerate(d):
#         if v > limit:
#             d[idx] = power
#     return sum(d)
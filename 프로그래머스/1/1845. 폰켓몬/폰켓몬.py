#폰켓몬 종류 번호의 개수 
def solution(nums):
    kind = len(set(nums))
    answer = 0
    if kind <= len(nums)//2:
        return kind
    else:
        return len(nums)//2
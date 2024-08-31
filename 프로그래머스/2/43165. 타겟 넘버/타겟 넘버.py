#BFS 방식
def solution(numbers, target):
    data = [0] 
    for num in numbers:
        res =[]
        for val in data:
            res.append(val+num)
            res.append(val-num)
        data= res
    answer= data.count(target)
    return answer

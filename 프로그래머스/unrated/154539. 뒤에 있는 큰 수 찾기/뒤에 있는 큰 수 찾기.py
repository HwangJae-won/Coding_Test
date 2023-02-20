
def solution(numbers):
    answer = [-1] * len(numbers) #answer을 처음부터 -1로 채우고 큰 수는 대체하기: 예외처리안해도됨
    temp =[]
    for i in range(len(numbers)):
        while temp and numbers[temp[-1]] < numbers[i]:
            answer[temp.pop()] = numbers[i]
        temp.append(i)
    return answer

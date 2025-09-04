def solution(numbers):
    numbers = list(map(str, numbers)) #문자열로 만들기 
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
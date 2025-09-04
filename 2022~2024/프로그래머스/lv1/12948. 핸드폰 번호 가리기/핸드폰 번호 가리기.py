def solution(phone_number):
    answer = ''
    number_len = len(phone_number)
    answer = '*' * (number_len - 4)
    answer += phone_number[-4:]
    return answer
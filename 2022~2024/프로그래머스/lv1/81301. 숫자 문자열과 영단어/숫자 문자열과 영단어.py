def solution(s):
    answer = s
    dict = {0:"zero", 1:"one", 2:"two", 3:"three", 4: "four", 5:"five",
           6:"six", 7:"seven", 8: "eight", 9:"nine"}
    for item in dict.items():
        answer = answer.replace(item[1], str(item[0]) )  #문자열을 숫자로 변경해야함
    return int(answer)
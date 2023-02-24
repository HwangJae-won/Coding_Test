#대소문자 섞여 있으므로 소문자로 변환
#count로 개수 세기 
def solution(s):
    return s.lower().count('p') == s.lower().count('y')
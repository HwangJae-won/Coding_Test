"""
1. 십진법 숫자 이진법으로 변환하기: format 함수 활용 
2. index로 0,1 비교하면서 공백 혹은 #으로 지정하기 
-> replace 를 통해 바꾸기 
???어케하노 
3. 지정한 숫자들 list로 반환하기 

"""
def solution(n, arr1, arr2):
    answer=[]
    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])[2:].zfill(n)
        tmp = tmp.replace('1','#').replace('0',' ')
        answer.append(tmp)
    return answer
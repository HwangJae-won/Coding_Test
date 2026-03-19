def solution(X, Y):
    answer = ''
    for i in range(9,-1,-1) : #공통된 부분을 찾기 위해 0~9개의 숫자로 기준을 잡아서 돌리기 + sort 사용 없이 시간 단축
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))
    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer


## 순열 사용하면 시간 초과
#counter로 중복 있는거만 뽑을시 -> 중복 2개 있는거 탐지 못함.
# li = list(map(int, [k for k in temp if temp.get(k)>1]))
## 집합과 intersaction 활용
# X_no = set(list(X)) ; Y_no = set(list(Y))
# print(X_no & Y_no)
# temp =Counter(list(X) + list(Y))
##for문을 사용하지 않게 노력해보자! 
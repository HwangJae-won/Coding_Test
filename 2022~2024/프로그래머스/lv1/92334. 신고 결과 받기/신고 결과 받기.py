from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    re =list(set(report)) #한 사람이 같은 사람 신고하면 삭제
    user = defaultdict(set) #딕셔너리는 add를 활용하기 어려워 추가하면서 반복문 돌리기 어려웠음
    cnt =defaultdict(int) 
    for i in re:
        reporter=i.split(" ")[0]
        error=i.split(" ")[1]
        user[reporter].add(error)
        cnt[error] +=1
    
    for j in id_list:
        temp =0
        for h in user[j]:
            if cnt[h] >=k:#k번보다 신고 더 많이 당하면 강퇴
                temp+=1
        answer.append(temp)
    return answer

######list는 사용 어려움:dictionary 사용해보자
## 신고자랑 신고당한 사람 분리
#     reporter = []
#     error=[]
#     for i in report:
#         reporter.append(i.split(" ")[0])
#         error.append(i.split(" ")[1])
#         dic = {report:error}
        
#     if id_list[i] ==reporter    
#         error.count
    ## 유저별 신고한 사람 
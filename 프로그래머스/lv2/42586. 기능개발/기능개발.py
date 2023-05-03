def solution(progresses, speeds):
    answer =[]
    #우선 작업 리스트 하나씩 100퍼 만들기 -> 달성하면 cnt 저장하고 방빼
    while progresses:
        cnt =0
        while progresses and progresses[0]>=100:
            cnt+=1
            progresses.pop(0)
            speeds.pop(0)
        progresses = [progresses[i]+speeds[i] for i in range(len(progresses))]

        if cnt:
            answer.append(cnt)
    return answer
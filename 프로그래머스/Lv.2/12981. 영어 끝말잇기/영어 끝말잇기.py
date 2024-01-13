def solution(n, words):
    answer= []
    for i in range(len(words)):
        if len(answer) < 1:
            answer.append(words[i])
        else:
            if answer[-1][-1] == words[i][0] and words[i] not in set(answer):
                answer.append(words[i])
            elif answer[-1][-1] != words[i][0] or words[i] in set(answer):
                return [i%n+1 , i//n + 1]
    return [0,0]
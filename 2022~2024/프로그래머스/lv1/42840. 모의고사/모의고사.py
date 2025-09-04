def solution(answers):
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0] ; result = []
    for idx, ans in enumerate(answers):
        if s1[idx % 5] == ans:
            score[0] += 1
        if s2[idx % 8] == ans:
            score[1] += 1
        if s3[idx % 10] == ans:
            score[2] += 1
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx + 1)
    return result
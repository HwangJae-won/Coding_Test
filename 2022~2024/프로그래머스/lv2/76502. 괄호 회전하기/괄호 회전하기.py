pair = {']':'[', ')': '(', "}":"{"}
def solution(s):
    answer = 0
    for i in range(len(s)):
        letter= s[i:]+s[:i]
        stack =[]
        for char in letter:
            if char in "[({":
                stack.append(char)
            elif stack != [] and pair[char] == stack[-1]:
                stack.pop()
            else:
                break
        else: 
            if stack == []:
                answer+=1
    return answer
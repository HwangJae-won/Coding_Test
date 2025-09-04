#set 사용 시에는 
def solution(arr):
    answer = []
    stack= []
    for n in arr:
        if n not in stack or stack[-1] != n:
            stack.append(n)        
        if n in stack:
            pass

    return stack
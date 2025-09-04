"""
[9012. 괄호]
- ( , ) 로만 구성된 괄호 문자열 
- () : 기본 문자열, VPS라 정의 
- x,y가 VPS면 (x), xy도 모두 VPS
- 주어진 문자열의 VPS 여부 판단하여 YES or NO 출력 

queue로 시도 -> 비어있는 경우의 예외 처리 필요성& remove를 사용하여 연산량 증가 
"""
n = int(input())
for _ in range(n):
    vps = input()
    stack =[]
    is_vps = True
    for s in vps:
        if s=="(":
            stack.append(s)
        elif s== ")":
            if stack:
                stack.pop()
            else:
                is_vps = False
                break
    if is_vps and not stack:
        print("YES")
    else:
        print("NO")
        
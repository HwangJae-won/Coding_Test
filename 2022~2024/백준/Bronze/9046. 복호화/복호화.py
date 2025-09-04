n = int(input())
for _ in range(n):
    s = input().replace(" ", "")
    dic ={}
    for temp in s:
        if temp in dic:
            dic[temp]+=1
        else: 
            dic[temp] = 1
    max_n = max(dic.values())
    max_li = [k for k,v in dic.items() if v ==max_n]
    
    if len(max_li)>1:
        print("?")
    else:
        print(max_li[0])
def solution(arr1, arr2):
    x = len(arr1)
    y = len(arr2[0])
    # arr2_T = list(zip(*arr2)) 
    arr2_T=[list(i) for i in zip(*arr2)]
    answer = [[0]*y for i in range(x)]
    # print(answer)
    for i in range(x) :
        for j in range(y) :  
            answer[i][j] = sum([a*b for a,b in zip(arr1[i],arr2_T[j])])
           
    return answer
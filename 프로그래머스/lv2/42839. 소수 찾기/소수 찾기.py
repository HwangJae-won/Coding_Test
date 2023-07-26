from itertools import permutations
from functools import reduce
def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    myset = set()
    for i in range(1,len(numbers)+1):
        permutation = list(permutations(numbers,i))
        for num in permutation:
            number = int(reduce(lambda x,y : x+y,num))
            if number not in myset and is_prime(number):
                myset.add(number)
                answer +=1
    return answer
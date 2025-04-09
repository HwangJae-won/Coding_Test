#접두어 있는 경우 False / 그렇지 않으면 True
def solution(phone_book):
    #우선 정렬
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
def solution(phone_book):
    phone_book.sort()
    for idx, i in enumerate(phone_book):
        if idx < len(phone_book)-1:
            # if phone_book[idx+1].startswith(i):
            if i == phone_book[idx+1][:len(i)]:
                return False
    return True
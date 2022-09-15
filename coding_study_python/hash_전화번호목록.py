'''
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.
'''

def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    for i in range(len(phone_book)):
        if (i+1 < len(phone_book)) and (len(phone_book[i]) < len(phone_book[i+1])) and (phone_book[i] == phone_book[i+1][:len(phone_book[i])]):
            answer = False

    return answer

# 다른사람 풀이
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
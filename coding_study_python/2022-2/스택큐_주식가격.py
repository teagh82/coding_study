from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        tmp =  prices.popleft()
        cnt = 0
        for i in prices:
            cnt += 1
            if tmp > i:
                break
        
        answer.append(cnt)
    
    
    return answer











# from collections import deque

# def solution(prices):
#     answer = []
#     pricesq = deque(prices)

#     while pricesq:
#         cur = pricesq.popleft()
#         cnt = 0
#         for i in pricesq:
#             cnt += 1
#             if cur > i:
#                 break
#         answer.append(cnt)

#     return answer
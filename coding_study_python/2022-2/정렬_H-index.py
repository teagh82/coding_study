def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort(reverse = True)
    
    for i in range(n):
        cnt = 0
        h = n-i
        
        for j in citations:
            if h <= j:
                cnt += 1
        if cnt >= h:
            return h
        
    return 0







# def solution(citations):
#     answer = 0
    
#     for i in range(len(citations)):
#         h = len(citations) - i
#         cnt_h = len(list(filter(lambda x:x>=h, citations)))
#         cnt_l = len(list(filter(lambda x:x<=h, citations)))
#         if cnt_h >= h and cnt_l <= h: 
#             answer = h
#             break
            
#     return answer
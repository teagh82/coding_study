'''
스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 
서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.
'''

import collections
def solution(clothes):
    answer = 1
    kind = []
    
    for i in clothes:
        kind.append(i[1])
        
    cnt = collections.Counter(kind).most_common()
    
    for i in cnt:
        answer *= (i[1]+1)
        
    return answer -1
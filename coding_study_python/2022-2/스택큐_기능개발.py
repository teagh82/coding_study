import math
import collections

def solution(progresses, speeds):
    answer = []
    days = []
    for idx, i in enumerate(progresses):
        days.append(math.ceil((100-i)/speeds[idx]))
    
    tmp = days[0]
    for idx, i in enumerate(days[1:]):
        if tmp > i:
            days[idx+1] = tmp
        else:
            tmp = i
            
    dic_cnt = dict(collections.Counter(days))
    for i in dic_cnt.values():
        answer.append(i)
    
    return answer










'''

import math

def solution(progresses, speeds):
    answer = []
    day = []
    tmp = 0
    for i in range(len(progresses)):
        day.append(math.ceil((100-progresses[i])/speeds[i]))

        if i > 0 and max(day) == day[i] and day.count(day[i]) == 1:
            answer.append(tmp)
            tmp = 0
        tmp += 1

    if(tmp > 0):
        answer.append(tmp)

    return answer
    
'''
from collections import deque

def solution(priorities, location): 
    answer = 0
    idx_pr = [[[] for i in range(2)] for _ in priorities]
    
    for idx, i in enumerate(priorities):
        idx_pr[idx][0] = i
        idx_pr[idx][1] = idx
    
    idx_pr = deque(idx_pr)
    max_pr = max(priorities)
    
    p_l = -1
    
    while p_l != location:
        tmp = idx_pr.popleft()
        
        if tmp[0] != max_pr:
            idx_pr.append(tmp)
        else:
            p_l = tmp[1]
            answer += 1
            if len(idx_pr) > 0:
                max_pr = max(idx_pr)[0]
            continue
        
    return answer







'''
from collections import deque

def solution(priorities, location):

    answer = []

    q = deque()
    for i in range(len(priorities)):
        q.append((i, priorities[i]))

    while q:
        idx, prop = q.popleft()
        if not q:
            answer.append(idx)
            break
        for i in range(len(q)):
            if q[i][1] > prop:
                q.append((idx, prop))
                break
            else:
                if i == len(q) - 1:
                    answer.append(idx)
                else:
                    continue

    return answer.index(location)+1
    
'''
def solution(queue1, queue2):
    answer = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    finish = (sum1 + sum2) // 2
    
    all_queue = queue1 + queue2
    idx1 = 0
    idx2 = len(queue1)
    
    cnt = 0
    tidx1 = idx1
    tidx2 = idx2
    
    while sum1 != finish:
        cnt += 1
        if idx1 > len(all_queue)-1:
            idx1 -= len(all_queue)
        if idx2 > len(all_queue)-1:
            idx2 -= len(all_queue)
            
        if sum1 > sum2:
            sum1-=all_queue[idx1]
            sum2+=all_queue[idx1]
            idx1 += 1
            answer += 1
        else:
            sum1+=all_queue[idx2]
            sum2-=all_queue[idx2]
            idx2 += 1
            answer += 1
        
        # if cnt > len(queue1) *3:
        #     answer = -1
        #     break
            
        if idx1==idx2 or ((tidx1 == idx1 or tidx2 == idx2) and cnt > len(queue1)*2):
            answer = -1
            break

    
    return answer